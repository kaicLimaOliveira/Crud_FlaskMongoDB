$(document).ready(() => {
    $('.btn-clear').on('click', () => {
        $('#firstName').val() == ''
        $('#lastName').val() == ''
    })

    const formError = $('form')

    $('.btn-submit').on('click', () => {
        if ($('#firstName').val() == '' || $('#lastName').val() == '') {
            formError.addClass('validate-error')
            getUrlStatusForm('error', 'Oops...!', 'Seu formulário está incompleto')
        } else {
            $('.btn-submit').submit()
        }
    })
})

function getUrlStatusForm(icon, title, text) {
    Swal.fire({
        icon: icon,
        title: title,
        text: text
    })
}