<?php
/**
 * Ascend Lettings — website enquiry form handler.
 * Receives POST submissions from the landlord, tenant, contact and rental
 * valuation forms and emails them to the business inbox below.
 * Requires a PHP-enabled host (GoDaddy cPanel supports this by default).
 */
declare(strict_types=1);

$to = "info@ascendlettings.co.uk";
$siteName = "Ascend Lettings";

function is_ajax(): bool
{
    return isset($_SERVER['HTTP_X_REQUESTED_WITH'])
        && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest';
}

function respond(bool $ok, string $message): void
{
    if (is_ajax()) {
        header('Content-Type: application/json');
        http_response_code($ok ? 200 : 400);
        echo json_encode(['ok' => $ok, 'message' => $message]);
        exit;
    }

    $referer = $_SERVER['HTTP_REFERER'] ?? 'index.html';
    $separator = strpos($referer, '?') === false ? '?' : '&';
    header('Location: ' . $referer . $separator . ($ok ? 'sent=1' : 'sent=0'));
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    respond(false, 'Invalid request method.');
}

// Honeypot: a hidden field real visitors never fill in. If it has a value,
// silently pretend success so the bot moves on without an email being sent.
if (!empty($_POST['website'])) {
    respond(true, 'Thank you.');
}

$formType = trim((string)($_POST['form_type'] ?? 'Website Enquiry'));
$name = trim((string)($_POST['name'] ?? ''));
$email = trim((string)($_POST['email'] ?? ''));

if ($name === '' || $email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    respond(false, 'Please provide a valid name and email address.');
}

$excludedFields = ['form_type', 'website'];
$lines = [];
foreach ($_POST as $key => $value) {
    if (in_array($key, $excludedFields, true)) {
        continue;
    }
    if (is_array($value)) {
        $value = implode(', ', $value);
    }
    $label = ucwords(str_replace('_', ' ', (string)$key));
    $lines[] = $label . ': ' . trim((string)$value);
}

$subject = 'New ' . $formType . ' - ' . $siteName . ' Website';
$body = "You have a new enquiry from the {$siteName} website.\n\n"
    . "Form: {$formType}\n"
    . str_repeat('-', 40) . "\n"
    . implode("\n", $lines) . "\n"
    . str_repeat('-', 40) . "\n"
    . 'Submitted: ' . date('d/m/Y H:i') . "\n";

// Strip header-injection characters from anything going into email headers.
$safeName = str_replace(["\r", "\n"], '', $name);
$safeEmail = str_replace(["\r", "\n"], '', $email);

$headers = "From: {$siteName} Website <no-reply@ascendlettings.co.uk>\r\n"
    . "Reply-To: {$safeName} <{$safeEmail}>\r\n"
    . "Content-Type: text/plain; charset=UTF-8\r\n";

$sent = mail($to, $subject, $body, $headers);

respond(
    $sent,
    $sent
        ? 'Thank you - your enquiry has been sent.'
        : 'Sorry, something went wrong sending your enquiry. Please call or WhatsApp us instead.'
);
