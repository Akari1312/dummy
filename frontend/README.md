# Insecure Frontend

This directory contains a simple HTML/JS frontend designed to interact with the Flask backend and include common client-side vulnerabilities.

## Features & Vulnerabilities

- **Reflected XSS**: `index.html` reads a `name` query parameter and inserts it into the DOM without sanitization.
- **Insecure API key storage**: the script places a fake key into `localStorage`.
- **Unsafe `eval` use**: `app.js` exposes a `runSnippet` function that evaluates arbitrary code.
- **Global state**: `globalState` object is accessible globally (bad practice).

To use, serve the `frontend` folder (e.g. with `python -m http.server`) and point it at the backend endpoints.
