document.getElementById("login-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Отправляем запрос на авторизацию
    const authResponse = await fetch("/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
    });

    if (authResponse.status === 200) {
        document.getElementById("message").textContent = "Login successful!";

        // Запрашиваем данные из базы
        const dataResponse = await fetch("/backend/data");
        if (dataResponse.ok) {
            const data = await dataResponse.json();
            document.getElementById("message").innerHTML = `
                <h3>Database Content:</h3>
                <pre>${JSON.stringify(data, null, 2)}</pre>
                <form id="add-data-form">
                    <h3>Add Data to Database:</h3>
                    <label for="field1">Field1:</label>
                    <input type="text" id="field1" required>
                    <label for="field2">Field2:</label>
                    <input type="text" id="field2" required>
                    <button type="submit">Add Data</button>
                </form>
            `;

            // Добавляем обработчик для формы добавления данных
            document.getElementById("add-data-form").addEventListener("submit", async (event) => {
                event.preventDefault();
                const field1 = document.getElementById("field1").value;
                const field2 = document.getElementById("field2").value;

                const addResponse = await fetch("/backend/data", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ field1, field2 }),
                });

                if (addResponse.ok) {
                    document.getElementById("message").textContent = "Data added successfully!";
                } else {
                    document.getElementById("message").textContent = "Failed to add data!";
                }
            });
        } else {
            document.getElementById("message").textContent = "Failed to fetch data!";
        }
    } else {
        const error = await authResponse.json();
        document.getElementById("message").textContent = error.error || "Login failed!";
    }
});
