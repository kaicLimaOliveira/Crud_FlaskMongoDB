$(document).ready(() => {
    $('.btn-clear').on('click', () => {
        $('#firstName').val() == ''
        $('#lastName').val() == ''
    })

    const formError = $('form')

    $('.btn-submit').on('click', () => {
        if ($('#firstName').val() == '' || $('#lastName').val() == '') {
            formError.addClass('validate-error')
            statusSuccess('error', 'Oops...!', 'Seu formulário está incompleto')
        } else {
            $('.btn-submit').submit()
        }
    })

    $('.delete-link').on('click', function () {
        const idx = $(this).val();

        getUrlStatusFormDeleted()

        function getUrlStatusFormDeleted() {
            Swal.fire({
                title: 'Você tem certeza?',
                text: "Você está prestes a excluir esse usuário!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sim, quero excluir!'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '/delete_user/' + idx
                }
            })
        }
    })





    function statusSuccess(icon, title, text) {
        Swal.fire({
            icon: icon,
            title: title,
            text: text
        })
    }
})
