async function getStations() {
    const url = "http://127.0.0.1:8001/getStations";
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


function createRouteButton() {
    const parentNode = document.getElementById("route-buttons")

    getStations().then(
        (stations) => {
            for (let i = 0; i < stations.length; i++)  {
                const buttonContainer = document.createElement("div")
                buttonContainer.className = "div-container"

                const btn = document.createElement("button")
                btn.innerHTML = "Hello World"
                btn.type = "submit"

                buttonContainer.appendChild(btn)
                parentNode.appendChild(buttonContainer)
            }

        }
    )
}
