$(function(){

    $('.new_project').click(function(){
		$('.add_newproject').toggle('slow');
		$('.shadow').toggle('slow');

	});
    $('.glyphicon').click(function(){
		$('.add_newproject').toggle('slow');
		$('.shadow').toggle('slow');

	});

	      $('.post-form').on('submit', function(event){
            event.preventDefault();
            console.log("form submitted!")
            create_post();
            
      })
      
/*      $('a').click(function(){
    	  go_to_task();

	});*/

/*    function refresh_post(){
        $.ajax({
            url: "/projects/1/",
            data : { project_name: $('#post-text').val(),
                    start_date: $('#start_date').val(),
                    end_date: $('#end_date').val(),
                    'csrfmiddlewaretoken': csrftoken },
            success: function(data){
                $('.project_container').html(data);
                
            }
        })
    }*/


    function create_post() {
        console.log("create post is working!") // sanity check
        $.ajax({
            url : "new/", // the endpoint
            type : "POST", // http method
            data : { project_name: $('#post-text').val(),
                    start_date: $('#start_date').val(),
                    end_date: $('#end_date').val(),
                    'csrfmiddlewaretoken': csrftoken }, // data sent with the post request
            // handle a successful response
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                $('#start_date').val('');
                $('#end_date').val('');
                console.log(json); // log the returned json to the console
                /*$("#project_append").append( "<p>" + json.task_name + json.start_date + json.end_date + "</p>")*/
                $(".column").load("/projects/" + json.user_id + " #project_append");
                $('.add_newproject').hide('slow');
        		$('.shadow').hide('slow');
                console.log("success");
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
    
/*    
    function go_to_task(){
    	$.ajax({
    		url:"tasks/task/29",
    		type: "POST",
    		success : function(json) {
                console.log(json);
                location.reload();
                console.log("success");
            },
    	})
    };*/
    
    
    
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

})