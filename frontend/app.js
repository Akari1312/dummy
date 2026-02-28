// This file is intentionally insecure to demonstrate frontend vulnerabilities

// Example of executing user input via eval (dangerous!)
function runSnippet(code) {
    // an attacker could inject arbitrary JS here
    eval(code);
}

// Hook for console testing
window.runSnippet = runSnippet;

// Ugly global variable
var globalState = { user: null };
