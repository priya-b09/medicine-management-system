function search_medicine() {

    const medicineName = document.getElementById("medicine_name").value.trim();

    if (medicineName === "") {
        return;
    }

    fetch(`http://127.0.0.1:5000/search_medicine?medicine_name=${encodeURIComponent(medicineName)}`)
        .then(response => {

            if (!response.ok) {
                throw new Error("Server Error: " + response.status);
            }

            return response.json();
        })

        .then(data => {


            const tableBody = document.getElementById("medicine_result");
            const resultSection = document.getElementById("resultSection");

           tableBody.innerHTML = "";

            // No medicine found
             if (data.length === 0) {

             resultSection.style.display = "none";
             alert("Medicine not found.");

               return;
             }

            // Show the result section
            resultSection.style.display = "block";

            // Add rows to the table
            data.forEach(medicine => {

                const row = `
                    <tr>
                        <td>${medicine.medicine_id}</td>
                        <td>${medicine.medicine_name}</td>
                        <td>${medicine.company_name}</td>
                        <td>${medicine.category}</td>
                        <td>${medicine.manufacturing_date}</td>
                        <td>${medicine.expiry_date}</td>
                        <td>${medicine.price}</td>
                         <td>${medicine.description}</td>
                        <td>${medicine.quantity}</td>
                        <td>${medicine.batch_no}</td>
                    </tr>
                `;

                tableBody.innerHTML += row;

            });

        })

        .catch(error => {

            console.error("Error:", error);

            document.getElementById("resultSection").style.display = "none";

            alert("Error searching medicine: " + error.message);

        });

}