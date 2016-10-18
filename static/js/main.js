$(function(){

    $('.panell').click(function(){
        $('#the_post').toggle('slow');
    });

	      $('#post-form').on('submit', function(event){
            event.preventDefault();
            console.log("form submitted!")
            create_post();
      })

    function create_post() {
        console.log("create post is working!") // sanity check
        $.ajax({
            url : "new/", // the endpoint
            type : "POST", // http method
            data : { task_name: $('#post-text').val(),
                    start_date: $('#start_date').val(),
                    end_date: $('#end_date').val(),
                    status:  $('select[name="status"] option:selected').text(),
                    'csrfmiddlewaretoken': csrftoken }, // data sent with the post request
            // handle a successful response
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                $('#start_date').val('');
                $('#end_date').val('');
                console.log(json); // log the returned json to the console
                $("#add-task").append("<tr>" + "<td>" + json.task_name + "</td><td>" + json.start_date + "</td><td>" + json.end_date + "</td><td>" + json.status + "</td>" + "<td></td></tr>")
                
                console.log("success");
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
    
    
    function edit_post() {
    	console.log("creat post is working!")
    	$.ajax({
    		url: "edit/",
    		type: "POST",
    		
    	})
    }
    
    
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