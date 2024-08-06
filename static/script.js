function updateTaskCounter() {
  const totalTasks = document.querySelectorAll("ul li").length;
  const completedTasks = document.querySelectorAll(
    'input[type="checkbox"]:checked'
  ).length;
  document.getElementById(
    "task-counter"
  ).innerText = `${completedTasks} out of ${totalTasks} tasks finished`;
}

document.addEventListener("DOMContentLoaded", (event) => {
  updateTaskCounter();
});

document
  .querySelectorAll('.task-form input[type="checkbox"]')
  .forEach((checkbox) => {
    checkbox.addEventListener("change", updateTaskCounter);
  });
