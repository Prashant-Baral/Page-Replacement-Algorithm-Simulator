function simulate() {
    let pages = document.getElementById("pages").value.split(",").map(Number);
    let frames = parseInt(document.getElementById("frames").value);

    fetch("/simulate", { // Use relative URL
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pages: pages, frames: frames })
    })
        .then(response => response.json())
        .then(data => {
            let memoryStates = data.states.map(state => `[${state.join(", ")}]`).join(", ");
            document.getElementById("result").innerText =
                `Page Faults: ${data.faults}\nMemory States: ${memoryStates}`;
        })
        .catch(error => console.error("Error:", error));
}
