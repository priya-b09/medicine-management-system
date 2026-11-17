function delete_medicine() {

    const medicineName = document.getElementById("medicine_name").value;

    let medicine = {
        medicine_name: medicineName
    };

  //  fetch("/delete_medicine", {
     fetch("http://127.0.0.1:5000/delete_medicine", {
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