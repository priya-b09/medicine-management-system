function save_medicine(){
    const medicineName = document.getElementById("medicine_name").value;
    const companyName = document.getElementById("company_name").value;
    const category = document.getElementById("category").value;


const mfgDate = document.getElementById("mfg_date").value;
alert(mfg_date);
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
    fetch("/save_medicine", {
  //fetch("http://127.0.0.1:8000/save_medicine", {
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



