console.log("Inventory Dashboard JS loaded");

document.addEventListener("DOMContentLoaded", function () {

    // -------------------------
    // ELEMENTS (SAFE)
    // -------------------------
    const searchBox = document.getElementById("searchBox");
    const resultsDiv = document.getElementById("results");
    const productDetailsDiv = document.getElementById("productDetails");
    const chartCanvas = document.getElementById("chart");

    // Safety checks (prevents silent crashes)
    if (!searchBox || !resultsDiv || !productDetailsDiv || !chartCanvas) {
        console.error("One or more DOM elements are missing!");
        return;
    }

    // -------------------------
    // KPI STATS
    // -------------------------
    fetch("/stats")
        .then(res => res.json())
        .then(data => {

            document.getElementById("totalProducts").innerText =
                `Products: ${data.total_products}`;

            document.getElementById("totalInventory").innerText =
                `Inventory: ${data.total_inventory_records}`;

            document.getElementById("totalSales").innerText =
                `Sales: ${data.total_sales_records}`;
        })
        .catch(err => console.error("Stats error:", err));


    // -------------------------
    // LOW STOCK CHART
    // -------------------------
    fetch("/low-stock")
        .then(res => res.json())
        .then(data => {

            const labels = data.map(item => item.product_name);
            const values = data.map(item => item.stock_quantity);

            new Chart(chartCanvas.getContext("2d"), {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Low Stock Products",
                        data: values
                    }]
                }
            });

        })
        .catch(err => console.error("Chart error:", err));


    // -------------------------
    // SEARCH PRODUCTS
    // -------------------------
    searchBox.addEventListener("input", function () {

        const query = this.value.trim();

        if (query.length === 0) {
            resultsDiv.innerHTML = "";
            productDetailsDiv.innerHTML = "";
            return;
        }

        fetch(`/products/search?name=${encodeURIComponent(query)}`)
            .then(res => res.json())
            .then(data => {

                resultsDiv.innerHTML = "";

                if (!Array.isArray(data)) {
                    console.error("Search API did not return array:", data);
                    return;
                }

                data.forEach(product => {

                    const item = document.createElement("div");

                    item.innerHTML = `
                        <strong>${product.product_name}</strong><br>
                        £${product.unit_price}
                    `;

                    item.style.padding = "8px";
                    item.style.borderBottom = "1px solid #ddd";
                    item.style.cursor = "pointer";
                    item.style.background = "#fff";

                    // hover effect
                    item.addEventListener("mouseenter", () => {
                        item.style.background = "#f2f2f2";
                    });

                    item.addEventListener("mouseleave", () => {
                        item.style.background = "#fff";
                    });

                    // CLICK EVENT
                    item.addEventListener("click", () => {

                        console.log("CLICKED:", product.product_name);

                        productDetailsDiv.innerHTML = `
                            <div class="product-card">
                                <h3>${product.product_name}</h3>
                                <p><strong>Price:</strong> £${product.unit_price}</p>
                            </div>
                        `;
                    });

                    resultsDiv.appendChild(item);
                });
            })
            .catch(err => console.error("Search error:", err));
    });

});