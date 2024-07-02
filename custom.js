document.addEventListener("DOMContentLoaded", function() {
    const todos = document.querySelectorAll('.admonition-todo .admonition-title');
    todos.forEach(function(todo) {
        if (todo.textContent.trim() === 'Todo') {
            todo.textContent = 'Exercise';
        }
    });
});
