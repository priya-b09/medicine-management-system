function delete_medicine() {

    alert("Checking Delete");

    const medicineName = document.getElementById("medicine_name").value;

    alert("Medicine Name is " + medicineName);

    let medicine = {
        medicine_name: medicineName
    };

    fetch("/delete_medicine", {
        method: "DELETE",
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
        alert("Error deleting data " + error);
    });

    alert("Finished");
}