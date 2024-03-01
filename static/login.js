document.getElementById("login").onclick = function() {authenticate()};

async function authenticate() {

if (document.getElementById("username").value == ""){
    document.getElementById("loginStatus").innerText = "Please enter a valid username!"
    document.getElementById("loginStatus").style.color = "red"
    return
}
if (document.getElementById("password").value == ""){
    document.getElementById("loginStatus").innerText = "Please enter a password!"
    document.getElementById("loginStatus").style.color = "red"
    return
}
const payload = {
    "username" : document.getElementById("username").value,
    "password" : document.getElementById("password").value
}

const response = await fetch("/authenticate", {
    method: 'POST',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
});

const result = await response.json();
    if (result.status) {
        document.getElementById("loginStatus").innerText = "Login Successful"
        document.getElementById("loginStatus").style.color = "green"
    } else {
        document.getElementById("loginStatus").innerText = "Login Failed"
        document.getElementById("loginStatus").style.color = "red"
    }
}