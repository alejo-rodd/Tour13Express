const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');
const cerrarSesion = document.getElementById('cerrarSesion');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

cerrarSesion.addEventListener("click", function() {
    window.location.href = "{% url 'salir' %}";
});

function RedirectToFormRegisterEmp(){
    window.location.href = '/FormRegisterEmp';
}