// Prevent forms to submit more than once
let forms = document.getElementById('form');
if (forms) {
    forms.addEventListener('submit', function () {
        $('#submit-button').attr('disabled', true);
    });
}
