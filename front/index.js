function onClickSelectName() {
	closeAlert();

	name = document.getElementById("userName").value;

	if(!nameChecker(name)) {
		document.getElementById("alertError").classList.add("mostrar");
	} else {
		fetch("/api")
		.then(response => response.json())
		.then(data => console.log(data["message"]))
		.catch(error => console.error("Error:", error));
		//window.location.href = "/desarrollador";
	}
}

function nameChecker(name) {
	if(!name) {
		return false;
	}

	return true;
}

function closeAlert() {
		document.getElementById("alertError").classList.remove("mostrar");
}
