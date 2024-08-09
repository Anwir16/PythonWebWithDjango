$(document).ready(function () {
    $("#username").focusout(function (e) {
        e.preventDefault();
        // get the nickname
        var username = $(this).val();
        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: validateUsernameUrl,
            data: { "username": username },
            success: function (response) {
                // if not valid user, alert the user
                if (!response["valid"]) {
                    alert("Username already exist.");
                    var nickName = $("#username");
                    nickName.val("")
                    nickName.focus()
                }
            },
            error: function (response) {
                console.log(response)
            }
        });
    });
});