async function getAPI(endpoint) {
    const url = `http://127.0.0.1:8001/${endpoint}`;

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        return json
    } catch (error) {
        console.error(error.message);
    }
}


function createRouteButtons() {
    const parentNode = document.getElementById("route-buttons")

    getAPI("getRoutes")
        .then(
        (routes) => {
            const names = Object.values(routes)

            for (let i = 0; i < names.length; i++)  {
                const buttonContainer = document.createElement("div")
                buttonContainer.className = "div-container"

                const btn = document.createElement("button")
                btn.innerHTML = names[i]
                btn.type = "submit"

                buttonContainer.appendChild(btn)
                parentNode.appendChild(buttonContainer)
            }

        }
    )
}
