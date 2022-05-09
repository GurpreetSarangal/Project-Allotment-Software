$(document).ready(function() {
    
    // $('#submit').click((event)=>{
    //     event.preventDefault()
    // });

    $("#login-form").validate({
        rules:{
            username: {
                required: true,
            },
            password: {
                required: true,
            }
        },
        messages: {
            username: "Username is required",
            password: "Password is required",
            
        },
        submitHandler: function(form){
            form.submit();
        }
    });
});