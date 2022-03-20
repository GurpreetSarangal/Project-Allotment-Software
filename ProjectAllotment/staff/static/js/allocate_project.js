var x, i, j, l, ll, selElmnt, a, b, c;
/* Look for any elements with the class "project-title-div": */
x = document.getElementsByClassName("project-title-div");
l = x.length;
for (i = 0; i < l; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  ll = selElmnt.length;
  /* For each element, create a new DIV that will act as the selected item: */
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /* For each element, create a new DIV that will contain the option list: */
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < ll; j++) {
    /* For each option in the original select element,
    create a new DIV that will act as an option item: */
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function(e) {
        /* When an item is clicked, update the original select box,
        and the selected item: */
        var y, i, k, s, h, sl, yl;
        s = this.parentNode.parentNode.getElementsByTagName("select")[0];
        sl = s.length;
        h = this.parentNode.previousSibling;
        for (i = 0; i < sl; i++) {
          if (s.options[i].innerHTML == this.innerHTML) {
            s.selectedIndex = i;
            h.innerHTML = this.innerHTML;
            y = this.parentNode.getElementsByClassName("same-as-selected");
            yl = y.length;
            for (k = 0; k < yl; k++) {
              y[k].removeAttribute("class");
            }
            this.setAttribute("class", "same-as-selected");
            break;
            }
        }
        h.click();
        put_details(this.innerHTML);
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function(e) {
    /* When the select box is clicked, close any other select boxes,
    and open/close the current select box: */
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}

function closeAllSelect(elmnt) {
  /* A function that will close all select boxes in the document,
  except the current select box: */
  var x, y, i, xl, yl, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  xl = x.length;
  yl = y.length;
  for (i = 0; i < yl; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < xl; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}

function put_details(project_title){
    console.log("this is inside function ",project_title)
    const projects = JSON.parse(document.getElementById('projects').innerText);
    console.log(projects)
    Array.from(projects).forEach(function(proj) {
        
        console.log("this is inside for each ",proj)
        if(proj.title == project_title){
            var lang = document.forms["allocate"]["lang"];
            console.log(lang)
            lang.setAttribute("value", proj.language);
            document.getElementById("tech").value = proj.tech;
            
        }
    });
}

// $('.sessions').click(function(){
//     var id;
//     id = $(this).attr("id");
//     $.ajax(
//     {
//         type:"GET",
//         url: "/projectadmin/sessions",
//         data:{
//                  curr_session: id
//         },
//         success: function( data ) 
//         {
//           let initial_html = document.getElementById("classes-table");
//           initial_html = initial_html.innerHTML
//           console.log(initial_html);
//           console.log("Before parse \n",data);
//           data = JSON.parse(data);
//           console.log("after parse \n",data);
//           console.log(data.lenght);
          
  
//           data.forEach(class_ => {
//             initial_html +=  '<tr><td class="className">'+class_.thisSession+' | '+class_.className+'</td><td>'+class_.count+'</td></th>';
//           });
          
//           document.getElementById("classes-table").innerHTML = initial_html;
//           classes = document.getElementsByClassName("className")
//           length = document.getElementsByClassName("className").length
          
//           Array.from(classes).forEach(function (element) {
//             console.log(typeof(element.innerHTML))
//             element.onclick = () =>{ go_to_class(element.innerHTML);}
//           });        
//         }
//      })
//   });

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);
const projects = JSON.parse(document.getElementById('projects').innerText)
console.log(projects)