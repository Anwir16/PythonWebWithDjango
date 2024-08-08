
document.addEventListener('DOMContentLoaded', function () {
    function handleGuess(guess) {
        $.ajax({
            type: 'POST',
            url: playRoundUrl,
            data: {
                'guess': guess,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (response) {
                console.log(response.result);
                console.log(response.player_card);
                $('#player-card').attr('src', "/static/game/img/" + response.player_card + ".png");
                $('#house-card').attr('src', "/static/game/img/" + response.house_card + ".png");
                $('#profile-point').text(response.player_points);
                $('.reward-point h4').first().text("Your reward point: " + response.reward_point);
                // Update result
                if (response.result) {
                    if (response.result === 'Game over'){
                        // Clear previous result
                    $('.reward-point .result').remove();
                    // Append new result
                    $('.reward-point').append("<h4 class='result'>" + response.result + "</h4>");
                    $('#guess-buttons').hide();
                    $('#action-buttons').show();
                    $('#continue').hide();
                    } else{
                        // Clear previous result
                    $('.reward-point .result').remove();
                    // Append new result
                    $('.reward-point').append("<h4 class='result'>" + response.result + "</h4>");
                    $('#guess-buttons').hide();
                    $('#action-buttons').show();
                    }
                } else {
                    // Remove the result if it's not provided in the response
                    $('.reward-point .result').remove();
                    $('#guess-buttons').show();
                    $('#action-buttons').hide();
                }
            },
            error: function (response) {
                console.log(response);
            }
        });
    }

    function handleAction(action) {
        $.ajax({
            type: 'POST',
            url: playRoundUrl,
            data: {
                'action': action,
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (response) {
                console.log(response.result);
                console.log(response.player_card);
                $('#player-card').attr('src', "/static/game/img/" + response.player_card + ".png");
                $('#house-card').attr('src', "/static/game/img/" + response.house_card + ".png");
                $('#profile-point').attr('span', response.player_point);
                $('.reward-point h4').first().text("Your reward point: " + response.reward_point);
                // Update result
                if (response.result) {
                    // Clear previous result
                    $('.reward-point .result').remove();
                    // Append new result
                    $('.reward-point').append("<h4 class='result'>" + response.result + "</h4>");
                    $('#guess-buttons').hide();
                    $('#action-buttons').show();
                } else {
                    // Remove the result if it's not provided in the response
                    $('.reward-point .result').remove();
                    $('#guess-buttons').show();
                    $('#action-buttons').hide();
                }
            },
            error: function (response) {
                console.log(response);
            }
        });
    }

    $('#less').click(function () {
        handleGuess('less');
    });

    $('#greater').click(function () {
        handleGuess('greater');
    });

    $('#continue').click(function () {
        handleAction('Continue');
    });

    $('#stop').click(function () {
        if (confirm('Do you want to exit?')) {
            handleAction('Stop');
            window.location.href = '/';
        }
    });


    console.log("result: ", result)
    if (result) {
        $('.result').remove();
        // Append new result
        $('.reward-point').append("<h4 class='result'>" + result + "</h4>");
        $('#guess-buttons').hide();
        $('#action-buttons').show();
    } else {
        $('#guess-buttons').show();
        $('#action-buttons').hide();
    }
});
