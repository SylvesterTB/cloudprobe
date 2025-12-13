async function loadResults() {
    try {
        const res = await fetch("results.json");
        const data = await res.json();
        renderTable(data);
    } catch (err) {
        console.error("Could not load results.json:", err);
    }
}

function renderTable(results) {
    const tbody = document.getElementById("results-body");
    tbody.innerHTML = "";

    results.forEach(test => {
        const tr = document.createElement("tr");


        const statusClass = test.passed ? "status-pass" : "status-fail";
        const statusText = test.passed ? "PASS" : "FAIL";

        tr.innerHTML = `
            <td>${test.name}</td>
            <td class="${statusClass}">${statusText}</td>
            <td>${test.duration_ms}</td>
            <td>${test.error ? test.error : "None"}</td>
            <td><button class="details-btn">View</button></td>
        `;


        const detailsRow = document.createElement("tr");
        detailsRow.style.display = "none";

        detailsRow.innerHTML = `
            <td colspan="5">
                <div class="details-box">
                    ${JSON.stringify(test.details, null, 2)}
                </div>
            </td>
        `;


        tr.querySelector(".details-btn").onclick = () => {
            detailsRow.style.display =
                detailsRow.style.display === "none" ? "table-row" : "none";
        };

        tbody.appendChild(tr);
        tbody.appendChild(detailsRow);
    });
}

loadResults();
