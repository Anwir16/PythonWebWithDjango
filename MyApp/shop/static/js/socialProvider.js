
document.addEventListener('DOMContentLoaded', (event) => {
        const buttons = document.querySelectorAll('.social-login__icon');
        const form = document.getElementById('social-login-form');

        buttons.forEach(button => {
                button.addEventListener('click', (event) => {
                        event.preventDefault();
                        const provider = event.target.getAttribute('data-provider');
                        form.action = `{% provider_login_url 'provider="dummy"' %}`.replace('dummy', provider);
                        form.submit();
                });
        });
});