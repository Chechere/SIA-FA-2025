maxspeedchanged(document.getElementById("controlvelocidadmax").value);

function maxspeedchanged(value) {
	let label = document.getElementById("velocidadmaxlabel");
	label.innerText = "Máxima Velocidad Coche (Actual: " + value + "%):"
}

function nuevaPartida() {
	console.log("TODO: Hacer nueva partida");
}

function iniciarCarrera() {
	console.log("TODO: Iniciar nueva carrera");
}
