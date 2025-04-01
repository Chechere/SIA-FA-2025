
function onClickSelectName() {
	closeAlert();

	const name = document.getElementById("userName").value;
	const alerta = document.getElementById("alertError");

	fetch("../api/registerUser?user=" + name, { method: 'POST' })
	.then(response => {
		if(!response.ok) {
			alerta.firstElementChild.innerText = "¡Error! Nombre de usuario no válido"
			alerta.classList.add("mostrar");
		} else {
			window.location.href="./espera"
		}
	})
	.catch(error => {
		alerta.firstElementChild.innerText = "Hay problemas con los servidores..."
		alerta.classList.add("mostrar");
	});
}

function closeAlert() {
		document.getElementById("alertError").classList.remove("mostrar");
}
