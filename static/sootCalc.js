document.getElementById("calc2").onclick = function() {calculateSoot()};

async function calculateSoot() {

const payload = {"Absorbance" : document.getElementById("Absorbance").value}
console.log(payload)
const response = await fetch("/calculateSoot", {
    method: 'POST',
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
});

const result = await response.json();
document.getElementById("Soot").value = result.percentage;
}
