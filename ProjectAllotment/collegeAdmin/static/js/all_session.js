// function get_classes(session){
//     console.log("this runs");
   
//     var xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//           console.log(this);
//         }
//     };
//     xhttp.open("GET", "/projectadmin/sessions/"+String(session), true);
//     xhttp.send();
// }

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
    modal.innerHTML = '<!-- Modal content --><div class="modal-content"><div class="cross" ><span class="close">&times;</span></div><table id="classes-table"><tr><th>Class</th><th>No of Students</th></tr></table>';
    }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    modal.innerHTML = '<!-- Modal content --><div class="modal-content"><div class="cross" ><span class="close">&times;</span></div><table id="classes-table"><tr><th>Class</th><th>No of Students</th></tr></table>';
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
        let initial_html = document.getElementById("classes-table");
        initial_html = initial_html.innerHTML
        console.log(initial_html);
        console.log("Before parse \n",data);
        data = JSON.parse(data);
        console.log("after parse \n",data);
        console.log(data.lenght);
        // for (let i=0; i<data.lenght; i++){
        //   initial_html = initial_html+ "<tr><td>"+data[i].className+"</td><td>"+data[i].count+"</td></th>";
        // }

        data.forEach(class_ => {
          initial_html +=  "<tr><td>"+class_.className+"</td><td>"+class_.count+"</td></th>";
        });
        console.log(initial_html);
        document.getElementById("classes-table").innerHTML = initial_html;
        console.log((data[0]).className );
        console.log((data[0]).count );
        console.log((data[1]).className );
        console.log((data[1]).count);
      }
   })
});