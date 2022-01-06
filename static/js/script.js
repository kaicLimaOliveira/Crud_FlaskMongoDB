$(document).ready(() => {
    $('.btn-clear').on('click', () => {
        $('#firstName').val() == ''
        $('#lastName').val() == ''
    })

    $('.btn-submit').on('click', (event) => {
        event.preventDefault()

        if ($('#firstName').val() == '' || $('#lastName').val() == '') {
            alert('Não há nada no formulario para enviar')
        } else {
            $('.btn-submit').submit()
        }
    })
})
