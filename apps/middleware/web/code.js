async function getAPI(endpoint) {
    // Access a REST API on port 8001
    const url = `http://127.0.0.1:8001/${endpoint}`;

    console.log(url)

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        console.log(json)

        return json
    } catch (error) {
        console.error(error.message);
    }
}

function reset() {
    // Remove all buttons on the screen except the `Home` button
    const parentNode = document.getElementById("route-buttons")

    while (parentNode.firstChild) {
        parentNode.removeChild(parentNode.lastChild)
    }
}

function createRoutes() {
    // Create route (Red, Orange, Yellow, etc.) buttons
    reset()
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
                    btn.type = "submit"
                    btn.innerHTML = values[idx]
                    btn.setAttribute("onclick", "createStops(this)")
                    btn.setAttribute("route", keys[idx])

                    buttonContainer.appendChild(btn)
                    parentNode.appendChild(buttonContainer)
            }
        }
    )
}

function createStops(element) {
    // Create stop (Howard, Loyola, etc.)
    reset()
    const parentNode = document.getElementById("route-buttons")
    const route = element.getAttribute("route")

    getAPI(`getStations?route=${route}`)
        .then(
            (stations) => {
                for (let idx = 0; idx < stations.length; idx++) {
                    const buttonContainer = document.createElement("div")
                    buttonContainer.className = "div-container"

                    const btn = document.createElement("button")
                    btn.type = "submit"
                    btn.innerHTML = stations[idx]["station_name"]
                    btn.setAttribute("mapID", stations[idx]["map_id"])
                    btn.setAttribute("route", route)
                    btn.setAttribute("onclick", "createTrains(this)")

                    buttonContainer.appendChild(btn)
                    parentNode.appendChild(buttonContainer)
                }
            }
        )
}

function createTrains(element) {
    // Create content of when Trains will arrive
    reset()

    const currentTime = Math.ceil(Date.now() / 1000)
    const parentNode = document.getElementById("route-buttons")
    const route = element.getAttribute("route")
    const mapID = element.getAttribute("mapID")

    let uniqueRuns = new Set([])

    getAPI(`getTrains?stationID=${mapID}&route=${route}`)
        .then(
            (trains) => {
                for (let idx = 0; idx < trains.length; idx++) {
                    const infoContainer = document.createElement("div")
                    infoContainer.className = "div-container"

                    const runTime = Date.parse(trains[idx]["arrT"])/1000
                    const run = trains[idx]["rn"]

                    console.log(runTime, currentTime)

                    // if (runTime < currentTime) {
                    //     continue
                    // }

                    if (uniqueRuns.has(run)) {
                        continue
                    }

                    uniqueRuns.add(run)

                    const content1 = document.createElement("button")
                    content1.innerHTML = run
                    infoContainer.appendChild(content1)
                    // btn.id = stations[idx]["stop_id"]
                    // btn.type = "submit"
                    // btn.setAttribute("onclick", "createRouteStops(this)")

                    // buttonContainer.appendChild(btn)
                    parentNode.appendChild(infoContainer)
                }
            }
        )
}
