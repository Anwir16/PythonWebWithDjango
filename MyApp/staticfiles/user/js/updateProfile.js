$(document).ready(function () {
    $("#id_email").focusout(function (e) {
        e.preventDefault();
        // get the nickname
        var id_email = $("#id_email").val();
        // GET AJAX request
        var url = validateEmailUrl.replace('%40', '@');
        $.ajax({
            type: 'GET',
            url: url,
            data: { "id_email": id_email },
            success: function (response) {
                // if not valid user, alert the user
                if (!response["valid"]) {
                    alert("Email already exists. Please use another email!");
                    var nickName = $("#id_email");
                    nickName.val("")
                    nickName.focus()
                }
            },
            error: function (response) {
                console.log(response)
            }
        });
    });
    $("#id_first_name").focusout(function (e) {
        e.preventDefault();
        // get the nickname
        var id_first_name = $(this).val();
        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: validateFirstNameUrl,
            data: { "id_first_name": id_first_name },
            success: function (response) {
                // if not valid user, alert the user
                if (!response["valid"]) {
                    alert("First name must contain at least 1 character and cannot be a special character");
                    var nickName = $("#id_first_name");
                    nickName.val("")
                    nickName.focus()
                }
            },
            error: function (response) {
                console.log(response)
            }
        });
    });
    $("#id_last_name").focusout(function (e) {
        e.preventDefault();
        // get the nickname
        var id_last_name = $(this).val();
        // GET AJAX request
        $.ajax({
            type: 'GET',
            url: validateLastNameUrl,
            data: { "id_last_name": id_last_name },
            success: function (response) {
                // if not valid user, alert the user
                if (!response["valid"]) {
                    alert("Last name must contain at least 1 character and cannot be a special character!");
                    var nickName = $("#id_last_name");
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