function search_medicine() {

    alert("Checking Search");
     const medicineName = document.getElementById("medicine_name").value;

    alert("Medicine Name is " + medicineName);
    let medicine = {
    medicine_name: medicineName
};
    fetch("/search_medicine", {
  //fetch("http://127.0.0.1:8000/search_medicine", {
        method: "POST",
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
        alert("Error saving data"+error);
    });
    alert("finished")
}

