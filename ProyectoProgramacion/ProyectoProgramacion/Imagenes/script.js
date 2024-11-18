document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('usuario').value;
    const contrasena = document.getElementById('contrasena').value;

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, contrasena })
        });

        const data = await response.json();

        if (data.success) {
            localStorage.setItem('userEmail', data.email);
            window.location.href = 'inicio.html';
        } else {
            alert(data.message);
        }
    } catch (error) {
        console.error('Error en el inicio de sesión:', error);
        alert('Ocurrió un error al iniciar sesión');
    }
});
