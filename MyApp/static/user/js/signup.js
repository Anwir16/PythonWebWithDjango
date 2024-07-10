$("#username").focusout(function (e) {
    e.preventDefault();
    // get the nickname
    var username = $(this).val();
    // GET AJAX request
    $.ajax({
        type: 'GET',
        url: "{% url 'validate_username' %}",
        data: {"username": username},
        success: function (response) {
            // if not valid user, alert the user
            if(!response["valid"]){
                alert("You cannot create a friend with same username");
                var nickName = $("#username");
                nickName.val("")
                nickName.focus()
            }
        },
        error: function (response) {
            console.log(response)
        }
    })
})