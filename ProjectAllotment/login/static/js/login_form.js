console.log("hello world");


    let eyeBtn = document.querySelector("#eyebtn");
    let password = document.querySelector("#password");
    console.log(password);
    console.log(eyebtn);
    
    eyeBtn.addEventListener("click", function(e) {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
    });
    
