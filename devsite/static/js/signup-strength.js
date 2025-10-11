// static/js/signup-strength.js
(function () {
  function countClasses(s) {
    let c = 0;
    if (/[a-z]/.test(s)) c++;
    if (/[A-Z]/.test(s)) c++;
    if (/\d/.test(s)) c++;
    if (/[^\w\s]/.test(s)) c++; // symbols
    return c;
  }

  // Fallback score if zxcvbn isn't available
  function fallbackScore(pwd) {
    if (!pwd) return 0;
    let score = 0;
    if (pwd.length >= 8) score++;
    if (pwd.length >= 12) score++;
    score += Math.max(0, countClasses(pwd) - 1); // +0..3
    return Math.max(0, Math.min(4, score));
  }

  function ready(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  ready(function () {
    // Try by name first (most reliable with Django forms), then by id, then generic
    const pwd = document.querySelector('input[name="{{ form.password1.html_name }}"]')
             || document.getElementById('{{ form.password1.id_for_label }}')
             || document.querySelector('input[type="password"]');

    const email = document.querySelector('input[name="{{ form.email.html_name }}"]')
               || document.getElementById('{{ form.email.id_for_label }}');

    const meter = document.getElementById('pwd-meter');
    const hint  = document.getElementById('pwd-hint');

    if (!pwd || !meter || !hint) return;

    function update() {
      const pwdVal = pwd.value || '';
      const emailVal = (email && email.value) || '';

      let score = 0;
      let warning = '';
      let suggestions = [];

      if (typeof zxcvbn === 'function') {
        const res = zxcvbn(pwdVal, [emailVal]);
        score = res.score; // 0..4
        warning = res.feedback.warning || '';
        suggestions = res.feedback.suggestions || [];
      } else {
        score = fallbackScore(pwdVal);
      }

      meter.value = score;
      const COLORS = [
        "#c62828", // red
        "#e53935", // bright red
        "#fb8c00", // orange
        "#7cb342", // green
        "#2e7d32"  // dark green
      ];
      document.getElementById('pwd-meter').style.setProperty('--pwd-color', COLORS[score]);

      hint.textContent = warning || suggestions.join(' ') || '';
    }

    ['input', 'change', 'keyup'].forEach(evt => {
      pwd.addEventListener(evt, update);
      if (email) email.addEventListener(evt, update);
    });

    update(); // initial render
  });
})();
