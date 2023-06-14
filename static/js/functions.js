

$( document ).ready(function() {
    /**
    Send a notification
    */
    $("#send_notification").click(function(){
        url = 'http://localhost:9009/api/notification'
        category_id = $("#category_id").val()
        message = $("#message").val()

        if(category_id==0){
            alert("Select a category!");
            return 0;
        }
        if(message==''){
            alert("Message is needed!");
            return 0;
        }



        $.ajax({
          type: "POST",
          url: url+'?category_id='+category_id+'&message='+message,
          success: function(){
            alert('Notification sent!');
            window.location.replace("http://localhost:9009/messages");
          },
          dataType: 'json'
        });

    });

    /**
    Create a new category
    */
    $("#create_category").click(function(){
        url = 'http://localhost:9009/api/category'
        category_name = $("#category_name").val()
        if(category_name==""){
            alert("Category name is needed!");
            return 0;
        }



        $.ajax({
          type: "POST",
          url: url,
          data: JSON.stringify({'name': category_name}),
          success: function(){
            alert('category was created!');
            window.location.replace("http://localhost:9009/categories");
          },
          contentType:"application/json; charset=utf-8",
          dataType:"json",
        });

    });


})


