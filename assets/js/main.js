/* =============================================================
   Ascend Lettings — Global JavaScript
   ============================================================= */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initStickyHeader();
    initMobileMenu();
    initSmoothScroll();
    initFaqAccordion();
    initFormValidation();
    initCookieBanner();
    initScrollReveal();
    initWhatsAppFloat();
    initActiveNav();
    initLogoCarousels();
  });

  /* ---------- Sticky header: transparent -> solid ---------- */
  function initStickyHeader() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    var toggle = function () {
      if (window.scrollY > 40) header.classList.add('solid');
      else header.classList.remove('solid');
    };
    toggle();
    window.addEventListener('scroll', toggle, { passive: true });
  }

  /* ---------- Mobile hamburger menu ---------- */
  function initMobileMenu() {
    var burger = document.querySelector('.hamburger');
    var nav = document.querySelector('.mobile-nav');
    var overlay = document.querySelector('.nav-overlay');
    if (!burger || !nav) return;

    var close = function () {
      burger.classList.remove('open');
      nav.classList.remove('open');
      if (overlay) overlay.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };
    var open = function () {
      burger.classList.add('open');
      nav.classList.add('open');
      if (overlay) overlay.classList.add('open');
      burger.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    };

    burger.addEventListener('click', function () {
      if (nav.classList.contains('open')) close(); else open();
    });
    if (overlay) overlay.addEventListener('click', close);
    nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  }

  /* ---------- Smooth scroll for on-page anchors ---------- */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener('click', function (e) {
        var id = link.getAttribute('href');
        if (id === '#' || id.length < 2) return;
        var target = document.querySelector(id);
        if (!target) return;
        e.preventDefault();
        var offset = 90;
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      });
    });
  }

  /* ---------- FAQ accordion ---------- */
  function initFaqAccordion() {
    document.querySelectorAll('.faq-item').forEach(function (item) {
      var q = item.querySelector('.faq-question');
      var a = item.querySelector('.faq-answer');
      if (!q || !a) return;
      q.setAttribute('aria-expanded', 'false');
      q.addEventListener('click', function () {
        var isOpen = item.classList.contains('open');
        // close siblings within the same list
        var list = item.closest('.faq-list') || document;
        list.querySelectorAll('.faq-item.open').forEach(function (other) {
          if (other !== item) {
            other.classList.remove('open');
            var oa = other.querySelector('.faq-answer');
            var oq = other.querySelector('.faq-question');
            if (oa) oa.style.maxHeight = null;
            if (oq) oq.setAttribute('aria-expanded', 'false');
          }
        });
        if (isOpen) {
          item.classList.remove('open');
          a.style.maxHeight = null;
          q.setAttribute('aria-expanded', 'false');
        } else {
          item.classList.add('open');
          a.style.maxHeight = a.scrollHeight + 'px';
          q.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }

  /* ---------- Form validation (client-side) ---------- */
  function initFormValidation() {
    var forms = document.querySelectorAll('form[data-validate]');
    forms.forEach(function (form) {
      form.setAttribute('novalidate', 'novalidate');

      var validateField = function (field) {
        var group = field.closest('.form-group');
        if (!group) return true;
        var value = (field.value || '').trim();
        var valid = true;
        var type = field.getAttribute('type');
        var isRequired = field.hasAttribute('required');

        if (isRequired && !value) valid = false;
        else if (value && type === 'email') valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
        else if (value && type === 'tel') valid = /^[0-9+()\-\s]{7,}$/.test(value);

        group.classList.toggle('error', !valid);
        field.classList.toggle('invalid', !valid);
        return valid;
      };

      form.querySelectorAll('input, select, textarea').forEach(function (field) {
        field.addEventListener('blur', function () { validateField(field); });
        field.addEventListener('input', function () {
          if (field.closest('.form-group').classList.contains('error')) validateField(field);
        });
      });

      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var allValid = true;
        var firstInvalid = null;
        form.querySelectorAll('input, select, textarea').forEach(function (field) {
          if (field.type === 'hidden' || field.type === 'submit') return;
          if (!validateField(field)) {
            allValid = false;
            if (!firstInvalid) firstInvalid = field;
          }
        });
        if (!allValid) {
          if (firstInvalid) firstInvalid.focus();
          return;
        }

        var success = form.querySelector('.form-success');
        var error = form.querySelector('.form-error');
        var submitBtn = form.querySelector('button[type="submit"]');
        if (error) error.classList.remove('show');
        if (submitBtn) {
          submitBtn.dataset.originalText = submitBtn.dataset.originalText || submitBtn.textContent;
          submitBtn.disabled = true;
          submitBtn.textContent = 'Sending…';
        }

        var showError = function (message) {
          if (error) {
            error.textContent = message;
            error.classList.add('show');
            error.setAttribute('role', 'alert');
            error.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        };

        fetch(form.getAttribute('action') || 'mail-handler.php', {
          method: 'POST',
          body: new FormData(form),
          headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
          .then(function (res) {
            return res.json().catch(function () { return { ok: res.ok }; });
          })
          .then(function (data) {
            if (data && data.ok) {
              if (success) {
                success.classList.add('show');
                success.setAttribute('role', 'status');
                success.scrollIntoView({ behavior: 'smooth', block: 'center' });
              }
              form.reset();
            } else {
              showError((data && data.message) || 'Sorry, something went wrong. Please call or WhatsApp us instead.');
            }
          })
          .catch(function () {
            showError('Sorry, something went wrong sending your enquiry. Please check your connection and try again, or call/WhatsApp us instead.');
          })
          .finally(function () {
            if (submitBtn) {
              submitBtn.disabled = false;
              submitBtn.textContent = submitBtn.dataset.originalText;
            }
          });
      });
    });
  }

  /* ---------- Cookie consent banner ---------- */
  function initCookieBanner() {
    var banner = document.querySelector('.cookie-banner');
    if (!banner) return;
    var KEY = 'ascend_cookie_consent';
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (e) {}
    if (!stored) {
      setTimeout(function () { banner.classList.add('show'); }, 900);
    }
    var set = function (val) {
      try { localStorage.setItem(KEY, val); } catch (e) {}
      banner.classList.remove('show');
    };
    var accept = banner.querySelector('[data-cookie="accept"]');
    var reject = banner.querySelector('[data-cookie="reject"]');
    if (accept) accept.addEventListener('click', function () { set('accepted'); });
    if (reject) reject.addEventListener('click', function () { set('rejected'); });
  }

  /* ---------- Scroll reveal via IntersectionObserver ---------- */
  function initScrollReveal() {
    var els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    if (!('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('visible'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  /* ---------- WhatsApp float show/hide on scroll (mobile-friendly) ---------- */
  function initWhatsAppFloat() {
    var btn = document.querySelector('.whatsapp-float');
    if (!btn) return;
    var lastY = window.scrollY;
    window.addEventListener('scroll', function () {
      var y = window.scrollY;
      // hide when scrolling up quickly near top, always show after 200px
      if (y > 200) btn.style.opacity = '1';
      lastY = y;
    }, { passive: true });
  }

  /* ---------- Logo carousel: rotates groups of logos ---------- */
  function initLogoCarousels() {
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    document.querySelectorAll('[data-logo-carousel]').forEach(function (carousel) {
      var track = carousel.querySelector('[data-track]');
      if (!track) return;
      var slides = Array.prototype.slice.call(track.children);
      var dots = Array.prototype.slice.call(carousel.querySelectorAll('[data-dot]'));
      if (slides.length < 2) return;
      var index = 0;
      var timer = null;

      var goTo = function (i) {
        index = (i + slides.length) % slides.length;
        track.style.transform = 'translateX(-' + (index * 100) + '%)';
        dots.forEach(function (dot, di) {
          var active = di === index;
          dot.classList.toggle('is-active', active);
          dot.setAttribute('aria-selected', active ? 'true' : 'false');
        });
      };

      var start = function () {
        if (reduceMotion) return;
        stop();
        timer = setInterval(function () { goTo(index + 1); }, 3500);
      };
      var stop = function () { if (timer) { clearInterval(timer); timer = null; } };

      dots.forEach(function (dot) {
        dot.addEventListener('click', function () {
          goTo(parseInt(dot.getAttribute('data-dot'), 10));
          start();
        });
      });

      carousel.addEventListener('mouseenter', stop);
      carousel.addEventListener('mouseleave', start);
      carousel.addEventListener('focusin', stop);
      carousel.addEventListener('focusout', start);

      goTo(0);
      start();
    });
  }

  /* ---------- Active nav link highlighting ---------- */
  function initActiveNav() {
    var path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.main-nav a, .mobile-nav a').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href) return;
      var file = href.split('/').pop().split('#')[0];
      if (file === path || (path === 'index.html' && (href === 'index.html' || href === './' || href === '/'))) {
        a.classList.add('active');
      }
    });
  }
})();
