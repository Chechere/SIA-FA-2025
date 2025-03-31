const urlParams = new URLSearchParams(window.location.search);
const raceId = urlParams.get('raceId');

fetch('../api/checkRaceId?raceId=' + raceId)
.then(response => {
	if(!response.ok) {
		window.location.href="..";
	}
});

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
			document.getElementById("registerContent").style.display = "none";
			const waitingContent = document.getElementById("waitingContent");

			waitingContent.removeAttribute("style");
			waitingContent.appendChild(document.getElementById("imgIEEELogo"));

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
