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

// THE VARIABLE NAMES IN THIS SECTION WILL NEED TO BE REVISED TO MATCH DB VARS
function fetchStationData(stationName) {
    return fetch(`mongo_db=${stationName}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Return the parsed JSON object
        })
        .catch(error => {
            console.error('Error:', error);
            return {
                error: true,
                message: error.message
            }; // Return an error object
        });
}

updateTime();
setInterval(updateTime, 1000);
