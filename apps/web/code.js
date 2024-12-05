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
                const values = Object.values(routes)
                const keys = Object.keys(routes)

                for (let idx = 0; idx < values.length; idx++)  {
                    const buttonContainer = document.createElement("div")
                    buttonContainer.className = "div-container"

                    const btn = document.createElement("button")
                    btn.id = keys[idx]
                    btn.type = "submit"
                    btn.innerHTML = values[idx]
                    btn.setAttribute("onclick", "createRouteStops(this)")

                    buttonContainer.appendChild(btn)
                    parentNode.appendChild(buttonContainer)
            }

        }
    )
}

function reset() {
    const parentNode = document.getElementById("route-buttons")

    while (parentNode.firstChild) {
        parentNode.removeChild(parentNode.lastChild)
    }

    createRouteButtons()
}

function createRouteStops(element) {
    const parentNode = document.getElementById("route-buttons")

    while (parentNode.firstChild) {
        parentNode.removeChild(parentNode.lastChild)
    }

    getAPI(`getSpecificStation?stationID=${element.id}`)
        .then(
            (stations) => {
                for (let idx = 0; idx < stations.length; idx++) {
                    const buttonContainer = document.createElement("div")
                    buttonContainer.className = "div-container"

                    const btn = document.createElement("button")
                    btn.id = stations[idx]["stop_id"]
                    btn.type = "submit"
                    btn.innerHTML = stations[idx]["station_name"]
                    btn.setAttribute("onclick", "createRouteStops(this)")

                    buttonContainer.appendChild(btn)
                    parentNode.appendChild(buttonContainer)
                }
            }
        )
}
