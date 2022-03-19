

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
        

        data.forEach(class_ => {
          initial_html +=  '<tr><td class="className">'+class_.thisSession+' | '+class_.className+'</td><td>'+class_.count+'</td></th>';
        });
        
        document.getElementById("classes-table").innerHTML = initial_html;
        classes = document.getElementsByClassName("className")
        length = document.getElementsByClassName("className").length
        
        Array.from(classes).forEach(function (element) {
          console.log(typeof(element.innerHTML))
          element.onclick = () =>{ go_to_class(element.innerHTML);}
        });        
      }
   })
});




function go_to_class(className){    
    window.location.replace("/projectadmin/sessions/class/"+String(className));
}