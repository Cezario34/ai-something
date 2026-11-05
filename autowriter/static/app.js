const fragment = document.querySelector("#fragment");
const charCount = document.querySelector("#char-count");
const checkButton = document.querySelector("#check-button");
const notice = document.querySelector("#notice");

function renderCount() {
  charCount.textContent = `Символов: ${fragment.value.length}`;
}

fragment.addEventListener("input", renderCount);
renderCount();

checkButton.addEventListener("click", async () => {
  notice.hidden = true;
  checkButton.disabled = true;

  try {
    const response = await fetch("/api/check", { method: "POST" });
    if (!response.ok) {
      throw new Error(`status ${response.status}`);
    }
    const data = await response.json();
    notice.textContent = data.message || "Проверка текста пока не реализована.";
  } catch {
    notice.textContent = "Не удалось связаться с сервером.";
  } finally {
    notice.hidden = false;
    checkButton.disabled = false;
  }
});
