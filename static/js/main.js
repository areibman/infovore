// This script contains the JavaScript code for handling user interactions and API calls

document.addEventListener("DOMContentLoaded", function () {
  const queryForm = document.getElementById("query-form");
  const userInput = document.getElementById("user-input");
  const queryResult = document.getElementById("query-result");

  queryForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    const input = userInput.value.trim();
    if (input.length === 0) {
      alert("Please enter a query.");
      return;
    }

    const response = await fetch("/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input: input }),
    });

    if (response.ok) {
      const data = await response.json();
      queryResult.textContent = JSON.stringify(data.response, null, 2);
    } else {
      alert("An error occurred. Please try again.");
    }
  });
});
