const projects = JSON.parse(document.getElementById('projects').textContent);
console.table(projects)

if(document.readyState){
    projects.forEach(project => {
        // console.table(project)
        $("#editproject"+String(project.id)).click(function() {
            console.log(project)
            fillModal(project);
            $("#editModal").modal("toggle");
        });

        $("#delete"+String(project.id)).click( function() {
            $("#to-be-deleted").val(project.id);
            $("#deleteModal").modal("toggle");
        });
    });
    
}



function fillModal(project){
    $("#project-id2").val(project.id);
    $("#projectTitle2").val(project.name);
    $("#langUsed2").val(project.lang);
    $("#otherTechUsed2").val (project.tech);
}

