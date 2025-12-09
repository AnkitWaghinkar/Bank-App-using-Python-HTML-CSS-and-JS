function sendData(url) {
    const amount = document.getElementById("amount").value;

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: "amount=" + amount
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("result").innerHTML = data;
    });
}

function checkBalance() {
    fetch("/balance")
    .then(res => res.text())
    .then(data => {
        document.getElementById("result").innerHTML = data;
    });
}

function loadTransactions() {
    fetch("/transaction")
    .then(res => res.text())
    .then(data => {
        document.getElementById("result").innerHTML = data;
    });
}
