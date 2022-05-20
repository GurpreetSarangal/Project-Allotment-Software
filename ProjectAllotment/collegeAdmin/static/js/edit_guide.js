$(document).ready(function() {
    
    // $('#submit').click((event)=>{
    //     event.preventDefault()
    // });

    $("#edit-guide-form").validate({
        rules:{
            guide_name: {
                required: true,
            },
            mobile1: {
                required: true,
                minlength: 10,
                maxlength: 10,
            },
            mobile2: {
                
                minlength: 10,
                maxlength: 10,
            },

            email: {
                required: true,
                email: true
            }
        },
        messages: {
            guide_name: "Name of Guide is required",
            mobile1:{
                // required: "Mobile number is required",
                minlength: "Invalid Mobile Number",
                maxlength: "Invalid Mobile Number",
            },
            mobile2:{
                // required: "Mobile number is required",
                minlength: "Invalid Mobile Number",
                maxlength: "Invalid Mobile Number",
            },
            email:{
                required: "Email is required",
                email: "Invalid Email ID",
            }
            
        },
        submitHandler: function(form){
            form.submit();
        }
    });
});