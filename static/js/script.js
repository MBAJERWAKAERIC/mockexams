// script.js

document.addEventListener('DOMContentLoaded', () => {
    console.log("Script loaded successfully");

    // Example: You can later use this for button events
    const buttons = document.querySelectorAll(".btn");
    buttons.forEach(button => {
        button.addEventListener('click', (e) => {
            console.log(`Button clicked: ${button.textContent.trim()}`);
        });
    });
});
