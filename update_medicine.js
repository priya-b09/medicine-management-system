function update_medicine(){
    const medicineName = document.getElementById("medicine_name").value;
    const companyName = document.getElementById("company_name").value;
    const category = document.getElementById("category").value;
    const mfgDate = document.getElementById("mfg_date").value;
    const expDate = document.getElementById("exp_date").value;
    const price = document.getElementById("price").value;
    const description = document.getElementById("description").value;
    const quantity = document.getElementById("quantity").value;
    const batchNo = document.getElementById("batch_no").value;
    let medicine = {
        medicine_name: medicineName,
        company_name: companyName,
        category: category,
        mfg_date: mfgDate,
        exp_date: expDate,
        price: price,
        description: description,
        quantity: quantity,
        batch_no: batchNo
    };
    console.log(medicine);
  //  fetch("/update_medicine", {
  fetch("http://127.0.0.1:5000/update_medicine", {
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
        alert("Error saving data"+error);
    });
    
}



