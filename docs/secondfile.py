<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>📝 To-Do List</title>
  <style>
    /* CSS Styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: linear-gradient(135deg, #74ebd5, #9face6);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .container {
      background: white;
      padding: 30px;
      border-radius: 15px;
      width: 100%;
      max-width: 400px;
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }

    .input-group {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
    }

    input[type="text"] {
      flex: 1;
      padding: 10px;
      border-radius: 8px;
      border: 1px solid #ccc;
      font-size: 16px;
    }

    button {
      padding: 10px 16px;
      border: none;
      border-radius: 8px;
      background-color: #4caf50;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #45a049;
    }

    ul {
      list-style: none;
    }

    li {
      background-color: #f4f4f4;
      padding: 12px;
      margin-bottom: 10px;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: default;
      user-select: none;
      transition: background-color 0.3s ease;
    }

    li.done {
      text-decoration: line-through;
      color: gray;
      background-color: #d0d0d0;
    }

    li span {
      flex-grow: 1;
    }

    li button {
      background: none;
      border: none;
      color: red;
      font-size: 18px;
      cursor: pointer;
      padding-left: 15px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📝 To-Do List</h1>
    <div class="input-group">
      <input type="text" id="taskInput" placeholder="Enter a task..." />
      <button id="addBtn">Add</button>
    </div>
    <ul id="taskList"></ul>
  </div>

  <script>
    // JavaScript code
    const taskList = document.getElementById("taskList");
    const taskInput = document.getElementById("taskInput");
    const addBtn = document.getElementById("addBtn");

    // Load saved tasks from localStorage when page loads
    window.onload = () => {
      const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
      savedTasks.forEach(task => renderTask(task.text, task.done));
    };

    addBtn.addEventListener("click", addTask);
    taskInput.addEventListener("keypress", function(e) {
      if (e.key === "Enter") {
        addTask();
      }
    });

    function addTask() {
      const text = taskInput.value.trim();
      if (text === "") {
        alert("Please enter a task.");
        return;
      }
      renderTask(text);
      saveTasks();
      taskInput.value = "";
      taskInput.focus();
    }

    function renderTask(text, done = false) {
      const li = document.createElement("li");
      if (done) li.classList.add("done");

      const span = document.createElement("span");
      span.textContent = text;

      // Toggle done on click
      span.addEventListener("click", () => {
        li.classList.toggle("done");
        saveTasks();
      });

      const btn = document.createElement("button");
      btn.textContent = "✖";
      btn.title = "Delete task";
      btn.addEventListener("click", () => {
        li.remove();
        saveTasks();
      });

      li.appendChild(span);
      li.appendChild(btn);
      taskList.appendChild(li);
    }

    function saveTasks() {
      const tasks = [];
      taskList.querySelectorAll("li").forEach(li => {
        tasks.push({
          text: li.querySelector("span").textContent,
          done: li.classList.contains("done")
        });
      });
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }
  </script>
</body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>📝 To-Do List</title>
  <style>
    /* CSS Styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: linear-gradient(135deg, #74ebd5, #9face6);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .container {
      background: white;
      padding: 30px;
      border-radius: 15px;
      width: 100%;
      max-width: 400px;
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }

    .input-group {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
    }

    input[type="text"] {
      flex: 1;
      padding: 10px;
      border-radius: 8px;
      border: 1px solid #ccc;
      font-size: 16px;
    }

    button {
      padding: 10px 16px;
      border: none;
      border-radius: 8px;
      background-color: #4caf50;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #45a049;
    }

    ul {
      list-style: none;
    }

    li {
      background-color: #f4f4f4;
      padding: 12px;
      margin-bottom: 10px;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: default;
      user-select: none;
      transition: background-color 0.3s ease;
    }

    li.done {
      text-decoration: line-through;
      color: gray;
      background-color: #d0d0d0;
    }

    li span {
      flex-grow: 1;
    }

    li button {
      background: none;
      border: none;
      color: red;
      font-size: 18px;
      cursor: pointer;
      padding-left: 15px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📝 To-Do List</h1>
    <div class="input-group">
      <input type="text" id="taskInput" placeholder="Enter a task..." />
      <button id="addBtn">Add</button>
    </div>
    <ul id="taskList"></ul>
  </div>

  <script>
    // JavaScript code
    const taskList = document.getElementById("taskList");
    const taskInput = document.getElementById("taskInput");
    const addBtn = document.getElementById("addBtn");

    // Load saved tasks from localStorage when page loads
    window.onload = () => {
      const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
      savedTasks.forEach(task => renderTask(task.text, task.done));
    };

    addBtn.addEventListener("click", addTask);
    taskInput.addEventListener("keypress", function(e) {
      if (e.key === "Enter") {
        addTask();
      }
    });

    function addTask() {
      const text = taskInput.value.trim();
      if (text === "") {
        alert("Please enter a task.");
        return;
      }
      renderTask(text);
      saveTasks();
      taskInput.value = "";
      taskInput.focus();
    }

    function renderTask(text, done = false) {
      const li = document.createElement("li");
      if (done) li.classList.add("done");

      const span = document.createElement("span");
      span.textContent = text;

      // Toggle done on click
      span.addEventListener("click", () => {
        li.classList.toggle("done");
        saveTasks();
      });

      const btn = document.createElement("button");
      btn.textContent = "✖";
      btn.title = "Delete task";
      btn.addEventListener("click", () => {
        li.remove();
        saveTasks();
      });

      li.appendChild(span);
      li.appendChild(btn);
      taskList.appendChild(li);
    }

    function saveTasks() {
      const tasks = [];
      taskList.querySelectorAll("li").forEach(li => {
        tasks.push({
          text: li.querySelector("span").textContent,
          done: li.classList.contains("done")
        });
      });
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }
  </script>
</body>
</html>


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>📝 To-Do List</title>
  <style>
    /* CSS Styles */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: linear-gradient(135deg, #74ebd5, #9face6);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .container {
      background: white;
      padding: 30px;
      border-radius: 15px;
      width: 100%;
      max-width: 400px;
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }

    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }

    .input-group {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
    }

    input[type="text"] {
      flex: 1;
      padding: 10px;
      border-radius: 8px;
      border: 1px solid #ccc;
      font-size: 16px;
    }

    button {
      padding: 10px 16px;
      border: none;
      border-radius: 8px;
      background-color: #4caf50;
      color: white;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #45a049;
    }

    ul {
      list-style: none;
    }

    li {
      background-color: #f4f4f4;
      padding: 12px;
      margin-bottom: 10px;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: default;
      user-select: none;
      transition: background-color 0.3s ease;
    }

    li.done {
      text-decoration: line-through;
      color: gray;
      background-color: #d0d0d0;
    }

    li span {
      flex-grow: 1;
    }

    li button {
      background: none;
      border: none;
      color: red;
      font-size: 18px;
      cursor: pointer;
      padding-left: 15px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>📝 To-Do List</h1>
    <div class="input-group">
      <input type="text" id="taskInput" placeholder="Enter a task..." />
      <button id="addBtn">Add</button>
    </div>
    <ul id="taskList"></ul>
  </div>

  <script>
    // JavaScript code
    const taskList = document.getElementById("taskList");
    const taskInput = document.getElementById("taskInput");
    const addBtn = document.getElementById("addBtn");

    // Load saved tasks from localStorage when page loads
    window.onload = () => {
      const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
      savedTasks.forEach(task => renderTask(task.text, task.done));
    };

    addBtn.addEventListener("click", addTask);
    taskInput.addEventListener("keypress", function(e) {
      if (e.key === "Enter") {
        addTask();
      }
    });

    function addTask() {
      const text = taskInput.value.trim();
      if (text === "") {
        alert("Please enter a task.");
        return;
      }
      renderTask(text);
      saveTasks();
      taskInput.value = "";
      taskInput.focus();
    }

    function renderTask(text, done = false) {
      const li = document.createElement("li");
      if (done) li.classList.add("done");

      const span = document.createElement("span");
      span.textContent = text;

      // Toggle done on click
      span.addEventListener("click", () => {
        li.classList.toggle("done");
        saveTasks();
      });

      const btn = document.createElement("button");
      btn.textContent = "✖";
      btn.title = "Delete task";
      btn.addEventListener("click", () => {
        li.remove();
        saveTasks();
      });

      li.appendChild(span);
      li.appendChild(btn);
      taskList.appendChild(li);
    }

    function saveTasks() {
      const tasks = [];
      taskList.querySelectorAll("li").forEach(li => {
        tasks.push({
          text: li.querySelector("span").textContent,
          done: li.classList.contains("done")
        });
      });
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }
  </script>
</body>
</html>
