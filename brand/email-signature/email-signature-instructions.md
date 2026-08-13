# Ascend Lettings — Email Signature Instructions

This folder contains a professional, email-safe HTML signature (`email-signature.html`).

## Before you start

1. Open `email-signature.html` in a text editor (or a web browser to preview).
2. Replace the two placeholders:
   - `[Your Name]` → your full name
   - `[Your Title]` → your job title (e.g. *Lettings Manager*)
3. Replace the compliance placeholders once you have your numbers:
   - `[ICO REGISTRATION NUMBER]`
   - `[PRS NUMBER]`
4. Save the file.

> **Tip:** Everything you need to paste sits between the `<!-- SIGNATURE START -->` and `<!-- SIGNATURE END -->` comments.

---

## Gmail

1. Open Gmail → click the **gear icon** (top right) → **See all settings**.
2. On the **General** tab, scroll to **Signature**.
3. Click **Create new**, give it a name (e.g. *Ascend*).
4. Open `email-signature.html` in a web browser, select the rendered signature (from the name down to the compliance line), and copy it (**Ctrl/Cmd + C**).
5. Paste (**Ctrl/Cmd + V**) into the Gmail signature box.
6. Set **Signature defaults** to use it for new emails and replies.
7. Scroll down and click **Save Changes**.

> Gmail does not always keep inline SVG logos. If the logo does not appear, upload a PNG version of the logo (`brand/logo/`) using the image button in the signature editor, or use the **Insert image** option.

---

## Outlook (Desktop — Windows)

1. **File** → **Options** → **Mail** → **Signatures…**
2. Click **New**, name it *Ascend*.
3. Open `email-signature.html` in a web browser, select and copy the rendered signature.
4. Paste into the edit box.
5. Choose it under **New messages** and **Replies/forwards**.
6. Click **OK**.

## Outlook on the web (outlook.com / Microsoft 365)

1. **Settings** (gear) → **Mail** → **Compose and reply**.
2. Under **Email signature**, paste the copied rendered signature.
3. Tick **Automatically include my signature** as required.
4. Click **Save**.

---

## Apple Mail (macOS)

1. **Mail** → **Settings…** (or **Preferences**) → **Signatures**.
2. Select the account on the left, then click **+** to add a signature.
3. Untick **Always match my default message font**.
4. Open `email-signature.html` in Safari, select and copy the rendered signature, then paste it into the signature box.
5. Drag the new signature onto your account and set it as the default under **Choose Signature**.

> If Apple Mail flattens the layout, the safest approach is to keep the signature simple or use a PNG logo from `brand/logo/`.

---

## Notes on email compatibility

- The signature uses **table-based layout with inline styles** for maximum compatibility.
- The logo is an **inline SVG**. Some email clients (notably some versions of Gmail and Outlook) strip SVG. If the logo does not display, replace the `<svg>…</svg>` block with an `<img>` tag pointing to a hosted PNG, for example:
  ```html
  <img src="https://transforms.ascendproperties.com/production/images/Ascend-Living-Intro.png?w=1256&h=836&fm=webp&auto=compress&fit=crop&dm=1752145140&s=ffe329b6cdfcc7d1edf7f3a2363e611b" width="72" height="72" alt="Ascend Lettings">
  ```
- Fonts fall back to Arial/Georgia where Inter/Playfair Display are unavailable — this is expected and correct behaviour for email.
