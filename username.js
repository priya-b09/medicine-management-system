function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username =="admin" && password =="123") {
        window.location.href = "admin.html";
    } 
    else if(username =="worker" && password =="1234") {
        window.location.href = "worker.html";
    }
    else {
        alert ("wrong username or password");
    }
}