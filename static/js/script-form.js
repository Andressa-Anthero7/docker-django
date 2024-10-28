
$(document).ready(function(){
    $(document).on('keyup','#nome, #whatsapp', function(){
        nome_digitado = $("#nome").val();
        whatsapp_digitado = $("#whatsapp").val();
        if(nome_digitado.length >= 3 && whatsapp_digitado.length >= 10){
            $("#aceito-termos").removeAttr('disabled');
        }
        if(whatsapp_digitado.length == 3){
            //alert('maior que 2 digitos')
            whatsapp_digitado = '(' + whatsapp_digitado.slice(0, 2) + ') ' + whatsapp_digitado.slice(2);
            $("#whatsapp").val(whatsapp_digitado);
        }
    })

    $(document).on('click','#aceito-termos',function(){
       $("#btn-enviar").removeAttr('disabled');
    })
})




