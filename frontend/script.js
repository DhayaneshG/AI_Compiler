async function compileSystem() {

    const prompt =
        document.getElementById("prompt").value;

    const resultDiv =
        document.getElementById("result");

    resultDiv.innerHTML =
        "<p>Compiling...</p>";

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/compile",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    prompt: prompt
                })
            }
        );

        const data =
            await response.json();

        resultDiv.innerHTML = `

        <div class="card">
            <h2>Intent</h2>
            <pre>${JSON.stringify(data.intent, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>Design</h2>
            <pre>${JSON.stringify(data.design, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>UI Schema</h2>
            <pre>${JSON.stringify(data.ui_schema, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>Database Schema</h2>
            <pre>${JSON.stringify(data.db_schema, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>API Schema</h2>
            <pre>${JSON.stringify(data.api_schema, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>Auth Schema</h2>
            <pre>${JSON.stringify(data.auth_schema, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>Validation</h2>
            <pre>${JSON.stringify(data.validation, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>Repair</h2>
            <pre>${JSON.stringify(data.repair, null, 2)}</pre>
        </div>

        <div class="card">
            <h2>Metrics</h2>
            <pre>${JSON.stringify(data.metrics, null, 2)}</pre>
        </div>
        `;

    } catch (error) {

        resultDiv.innerHTML =
            "<p>Error while compiling.</p>";

        console.error(error);
    }
}