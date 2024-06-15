// Define variables to store current number and previous number
let currentNumber = "";
let previousNumber = "";
let operator = "";

// Function to clear the screen
function clearScreen() {
    currentNumber = "";
    previousNumber = "";
    operator = "";
    document.querySelector(".screen").textContent = "0";
}

// Function to handle backspace
function backspace() {
    currentNumber = currentNumber.slice(0, -1);
    document.querySelector(".screen").textContent = currentNumber;
}

// Function to append numbers to the screen
function appendNumber(number) {
    currentNumber += number;
    document.querySelector(".screen").textContent = currentNumber;
}

// Function to append operators
function appendOperator(op) {
    operator = op;
    previousNumber = currentNumber;
    currentNumber = "";
}

// Function to perform the calculation
function calculate() {
    let result = 0;
    let a = parseFloat(previousNumber);
    let b = parseFloat(currentNumber);

    if (operator === "+") {
        result = a + b;
    } else if (operator === "-") {
        result = a - b;
    } else if (operator === "*") {
        result = a * b;
    } else if (operator === "/") {
        if (b === 0) {
            alert("Error: Division by zero!");
            return;
        }
        result = a / b;
    }

    currentNumber = result.toString();
    previousNumber = "";
    operator = "";
    document.querySelector(".screen").textContent = currentNumber;
}