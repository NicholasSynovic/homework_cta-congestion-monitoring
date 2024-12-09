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
    const parentNode = document.getElementById("content")

    while (parentNode.firstChild) {
        parentNode.removeChild(parentNode.lastChild)
    }
}

function createRoutes() {
    const parentNodes = document.querySelectorAll(".s-content");

    getAPI("getRoutes")
        .then((routes) => {
            const keys = Object.keys(routes);
            const values = Object.values(routes);

            keys.forEach((key, index) => {
                const routeButton = document.createElement("div");
                routeButton.className = `sidebar-link ${key}-line`;
                routeButton.textContent = values[index];
                routeButton.dataset.routeKey = key;
                routeButton.setAttribute("data-bs-toggle", "collapse");
                routeButton.setAttribute("data-bs-target", `#${key}Stations`);
                routeButton.setAttribute("aria-expanded", "false");
                routeButton.setAttribute("aria-controls", `${key}Stations`);
                routeButton.setAttribute("onclick", `createStops('${key}')`);

                const stationContainer = document.createElement("div");
                stationContainer.id = `${key}Stations`;
                stationContainer.className = "collapse station-container";

                parentNode.appendChild(routeButton);
                parentNode.appendChild(stationContainer);
            });
        })
        .catch((error) => {
            console.error("Error fetching routes:", error);
        });
}

function createStops(element) {
    const targetContainerId = `${route}LineStations`;
    const targetContainer = document.getElementById(targetContainerId);

    if (!targetContainer) {
        console.error(`Target container for route '${route}' not found.`);
        return;
    }

    if (targetContainer.dataset.loaded === "true") {
        console.log(`Stations for route '${route}' are already loaded.`);
        return;
    }

    getAPI(`getStations?route=${route}`)
        .then((stations) => {
            targetContainer.innerHTML = "";

            stations.forEach((station) => {
                const buttonContainer = document.createElement("div");
                buttonContainer.className = "div-container";

                // Create a div for the station
                const stationDiv = document.createElement("div");
                stationDiv.className = "station-item";
                stationDiv.textContent = station["station_name"];
                stationDiv.setAttribute("data-station-name", station["station_name"]);
                stationDiv.setAttribute("route", route);
                stationDiv.setAttribute("onclick", "createTrains(this)");

                // Create station link to the station page
                const link = document.createElement("a");
                link.href = `station.html?station=${station["station_name"]}`;

                buttonContainer.appendChild(stationDiv);
                buttonContainer.appendChild(link);

                targetContainer.appendChild(buttonContainer);
            });
            targetContainer.dataset.loaded = "true";
        })
        .catch((error) => {
            console.error("Error fetching stations:", error);
        });
}

function createTrains(element) {
    const stationName = element.getAttribute("data-station-name");
    const route = element.getAttribute("route")
    const mapID = element.getAttribute("mapID")

    const contentContainer = document.getElementById("content");
    if (!contentContainer) {
        console.error("Parent container with id 'content' not found.");
        return;
    }

    const stationNameElement = contentContainer.querySelector(".station-name");
    if (stationNameElement) {
        stationNameElement.textContent = stationName;
    }

    // updates the title when function is called
    document.title = `${stationName} Station`

    // define and clear content in directions and train listings
    const scheduleGrids = contentContainer.querySelectorAll(".schedule-grid");
    const directionSubtitles = contentContainer.querySelectorAll(".direction-subtitle");

    scheduleGrids.forEach((grid) => (grid.innerHTML = ""));
    directionSubtitles.forEach((subtitle) => (subtitle.textContent = ""));

    let uniqueRuns = new Set();

    getAPI(`getTrains?stationID=${mapID}&route=${route}`)
        .then(
            (trains) => {
                const trainsByDirection = trains.reduce((acc, train) => {
                    const direction = train["destNm"];
                    if (!acc[direction]) acc[direction] = [];
                    acc[direction].push(train);
                    return acc;
                }, {});

                let directionIndex = 0;
            Object.keys(trainsByDirection).forEach((direction) => {
                // >= 2
                if (directionIndex >= directionSubtitles.length) return;

                const subtitle = directionSubtitles[directionIndex];
                const scheduleGrid = scheduleGrids[directionIndex];

                if (!subtitle || !scheduleGrid) return;

                subtitle.textContent = `Toward ${direction}`;

                trainsByDirection[direction].forEach((train) => {
                    const runTime = Math.floor(Date.parse(train["arrT"]) / 1000);
                    const run = train["rn"];

                    if (uniqueRuns.has(run)) return;
                    uniqueRuns.add(run);

                    const trainLine = document.createElement("div");
                    trainLine.className = "train-line";

                    const lineInfo = document.createElement("div");

                    const lineName = document.createElement("span");
                    lineName.className = "line-name";
                    lineName.textContent = `${route} Line`;

                    const delayStatus = document.createElement("span");
                    delayStatus.className = "delay-status";
                    delayStatus.textContent = "On Time";

                    lineInfo.appendChild(lineName);
                    lineInfo.appendChild(delayStatus);

                    const arrivalTimes = document.createElement("span");
                    arrivalTimes.className = "arrival-times";
                    arrivalTimes.textContent = `${Math.max(
                        0,
                        Math.ceil((runTime - currentTime) / 60)
                    )} m`;

                    trainLine.appendChild(lineInfo);
                    trainLine.appendChild(arrivalTimes);

                    scheduleGrid.appendChild(trainLine);
                });

                directionIndex++;
            });
        })
        .catch((error) => {
            console.error("Error fetching train data:", error);
        }
    );
}

function initialize(){
    reset();
    createRoutes();
}

function updateTime() {
    const timeElement = document.getElementById("liveTime");
    const now = new Date();
    const options = {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };
    timeElement.textContent = now.toLocaleTimeString([], options);
}

setInterval(updateLiveTime, 1000);
updateLiveTime();
