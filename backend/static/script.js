async function compileSystem() {

    const prompt = document.getElementById("prompt").value;
    const resultDiv = document.getElementById("result");

    if (!prompt.trim()) {
        resultDiv.innerHTML = "<p>Please enter a prompt.</p>";
        return;
    }

    resultDiv.innerHTML = "<p>Compiling...</p>";

    try {

        const response = await fetch("/compile", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                prompt: prompt
            })
        });

        if (!response.ok) {
            throw new Error(`Server Error: ${response.status}`);
        }

        const data = await response.json();

        resultDiv.innerHTML = `
            <div class="card">
                <h2>Generated Application Specification</h2>
                <pre>${JSON.stringify(data, null, 2)}</pre>
            </div>
        `;

    } catch (error) {

        resultDiv.innerHTML = `
            <div class="card">
                <h2>Error</h2>
                <pre>${error.message}</pre>
            </div>
        `;

        console.error(error);
    }
}