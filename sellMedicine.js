function sell_medicine() {

    const medicineName = document.getElementById("medicine_name").value;
    const quantity = document.getElementById("quantity").value;

    let medicine = {
        medicine_name: medicineName,
        quantity: quantity
    };

    console.log(medicine);

    fetch("http://127.0.0.1:5000/sell_medicine", {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(medicine)
    })

    .then(response => response.text())

    .then(result => {
        alert(result);
    })

    .catch(error => {
        console.log(error);
        alert("Error selling medicine: " + error);
    });
}
