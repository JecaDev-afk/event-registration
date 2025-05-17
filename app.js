const api = "https://event-registration-xbwm.onrender.com";

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showMessage(message, type = 'success') {
  const box = document.getElementById("message");
  box.textContent = message;
  box.className = `message ${type} show`;

  setTimeout(() => {
    box.classList.remove('show');
    setTimeout(() => {
      box.textContent = '';
      box.className = 'message';
    }, 300);
  }, 4000);
}

// ------------------ Перемикач форм ------------------
const regForm = document.getElementById('regForm');
const delForm = document.getElementById('delForm');
const switchToRegister = document.getElementById('switchToRegister');
const switchToDelete = document.getElementById('switchToDelete');
const formTitle = document.getElementById('formTitle');

switchToRegister.addEventListener('click', () => {
  regForm.classList.remove('hidden');
  delForm.classList.add('hidden');
  switchToRegister.classList.add('active');
  switchToDelete.classList.remove('active');
  formTitle.textContent = "Реєстрація на захід";
});

switchToDelete.addEventListener('click', () => {
  regForm.classList.add('hidden');
  delForm.classList.remove('hidden');
  switchToRegister.classList.remove('active');
  switchToDelete.classList.add('active');
  formTitle.textContent = "Видалення користувача";
});

// ------------------ Реєстрація ------------------

regForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const payload = Object.fromEntries(formData.entries());

  if (!isValidEmail(payload.email)) {
    showMessage("Невірний формат email", 'error');
    return;
  }

  if (payload.password.length < 8) {
    showMessage("Пароль має містити щонайменше 8 символів", 'error');
    return;
  }

  try {
    const res = await fetch(`${api}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();

    if (!res.ok) {
      showMessage(data.detail || 'Помилка реєстрації', 'error');
      return;
    }

    showMessage("Успішно зареєстровано: " + data.name, 'success');
    e.target.reset();

  } catch (err) {
    showMessage("Помилка з'єднання з сервером", 'error');
  }
});

// ------------------ Видалення за email ------------------

delForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = e.target.email.value;

  if (!isValidEmail(email)) {
    showMessage("Невірний формат email", 'error');
    return;
  }

  try {
    const res = await fetch(`${api}/users/email/${encodeURIComponent(email)}`, {
      method: 'DELETE'
    });

    const data = await res.json();

    if (!res.ok) {
      showMessage(data.detail || 'Помилка видалення', 'error');
      return;
    }

    showMessage(data.message || 'Користувача видалено', 'success');
    e.target.reset();

  } catch (err) {
    showMessage("Помилка сервера при видаленні", 'error');
  }
});

// ------------------ Цитата ------------------

async function getQuote() {
  try {
    const res = await fetch(`${api}/quote`);
    const data = await res.json();
    document.getElementById("quote").textContent = data.quote;
  } catch (err) {
    document.getElementById("quote").textContent = "⚠️ Не вдалося отримати цитату";
  }
}
так
