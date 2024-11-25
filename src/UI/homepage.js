function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const main = document.getElementById("main");
    const toggleButton = document.getElementById("toggleSidebarButton");

    // Toggle the 'closed' class on the sidebar
    sidebar.classList.toggle("closed");

    // Adjust the main content margin based on the sidebar state
    if (sidebar.classList.contains("closed")) {
        main.classList.add("sidebar-closed");
        toggleButton.innerHTML = "→"; // Update button text/icon
    } else {
        main.classList.remove("sidebar-closed");
        toggleButton.innerHTML = "←"; // Update button text/icon
    }
}

function toggleStations(line) {
    const stationList = document.getElementById(line);
    if (stationList.style.display === "none" || stationList.style.display === "") {
        stationList.style.display = "block";
    } else {
        stationList.style.display = "none";
    }
}

function updateTime() {
    const timeElement = document.getElementById("live-time");
    const now = new Date();
    const options = {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };
    timeElement.textContent = now.toLocaleTimeString([], options);
}

//THE VARIABLE NAMES IN THIS SECTION WILL NEED TO BE REVISED TO MATCH DB VARS
function fetchStationData(stationName) {
    fetch(`https://run.mocky.io/v3/332c0332-f1e7-4928-a143-d2952dd7760e`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Parse JSON response
        })
        .then(data => {
            // Store the fetched data in localStorage
            localStorage.setItem("stationData", JSON.stringify(data));

            window.location.href = "/station.html";
            // Update the DOM with the fetched data
            document.getElementById("station-name").textContent = data["station-name"];
            document.getElementById("line-name").textContent = data["line-name"];
            document.getElementById("line-direction").textContent = data["line-direction"];
            document.getElementById("delay-info").textContent = data["delayInfo"] || "No Delays";
            document.getElementById("arrival-time").textContent = data["arrival-time"];

            document.getElementById("line-name-2").textContent = data["line-name"];
            document.getElementById("line-direction-2").textContent = data["line-direction-2"];
            document.getElementById("delay-info-2").textContent = data["delayInfo-2"] || "No Delays";
            document.getElementById("arrival-time-2").textContent = data["arrival-time-2"];
        })
        .catch(error => {
            console.error('Error:', error);
            return {
                error: true,
                message: error.message
            };
        });
}


// function testDOMPopulation(event) {
//     event.preventDefault();

//     const mockData = {
//         "station-name": "Howard",
//         "line-name": "Red Line",
//         "line-direction": "Toward Howard",
//         "delayInfo": "No Delays",
//         "arrival-time": 5,
//         "line-direction-2": "Toward 95th",
//         "delayInfo-2": "No Delays",
//         "arrival-time-2": 5
//     };

//     localStorage.setItem("stationData", JSON.stringify(mockData));

//     window.location.href = "/station.html";
// }

updateTime();
setInterval(updateTime, 1000);
