function get_classes(session){
    console.log("this runs");
   
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          console.log(this);
        }
    };
    xhttp.open("GET", "/projectadmin/sessions/"+String(session), true);
    xhttp.send();
}

// Get the modal
var modal = document.getElementById("classes");

// Get the button that opens the modal
var btns = document.getElementsByClassName("sessions");

// Get the <span> element that closes the modal
var spans = document.getElementsByClassName("close");

// When the user clicks the button, open the modal 
for (let btn of btns){
    btn.onclick = function() {
    modal.style.display = "block";
    }
}
// When the user clicks on <span> (x), close the modal
for (let span of spans){
    span.onclick = function() {
    modal.style.display = "none";
    }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

$('.sessions').click(function(){
  var id;
  id = $(this).attr("id");
  $.ajax(
  {
      type:"GET",
      url: "/projectadmin/sessions",
      data:{
               curr_session: id
      },
      success: function( data ) 
      {
          console.log(data);
      }
   })
});