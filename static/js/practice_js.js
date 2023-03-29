$(document).ready(function () {

    let btnFavouriteList = $(`.btn_favourite`)
    let deleteCommentBtnList = $(".delete_submit")
    let commentText = $(".comment_text")
    let commentSubmit = $(".comment_submit")
    let pictureId = $(".card").data("pictureid")
    const commentBlock = $('#commentBlock')
    let submitButton = $('#id_submit')
    let apiAuthUrl = $('#api_auth_url').val()


    function redirectNext(successUrl){
        window.location.replace(successUrl)
    }


    $(submitButton).click(function authenticateUser(event) {
        let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
        event.preventDefault()
        let username = $('#id_username').val();
        let password = $('#id_password').val();
        let password_confirm = $('#id_password_confirm').val();
        console.log(password);
        console.log(password_confirm);
        console.log(username);
        $.ajax({
            url: $('#id_form').attr('action'),
            method: "POST",
            headers: {"X-CSRFToken": csrfToken},
            data: JSON.stringify({username: username, password: password, password_confirm: password_confirm}),
            success: function (response, status) {
                $.ajax({
                        url: apiAuthUrl,
                        method: "POST",
                        data: {username: username, password: password},
                        success: function (apiAuthResponse, apiAuthStatus,) {
                            localStorage.setItem('apiToken', apiAuthResponse.token);
                            console.log(apiAuthResponse.token);
                            console.log(apiAuthStatus);
                            // location.reload();
                            redirectNext(response.success_url);

                        },
                        error: function (apiAuthResponse, apiAuthStatus) {
                            console.log(apiAuthResponse);
                            console.log(apiAuthStatus);
                        },
                    }
                );
            },
            error: function (response, status) {
                console.log(status);
                console.log(response);
            },
        });
    });


    for (let btnFavourite of btnFavouriteList) {
        $(btnFavourite).click(function toggleFavourite(event) {
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
            event.preventDefault()
            $.ajax({
                url: $(this.parentElement).attr("action"),
                method: 'POST',
                headers: {"X-CSRFToken": csrfToken, "Authorization": 'Token ' + localStorage.getItem('apiToken')},
                data: {picture_id: $(btnFavourite).attr("id")},
                success: function (data, status) {
                    $(btnFavourite).toggleClass("btn-dark")
                    console.log(data);
                    console.log(status);
                    console.log(4)
                },
                error: function (response, status) {
                    console.log(status);
                    console.log(response);
                }
            });
        });
    }


    $(commentSubmit).click(function addComment(event) {
        let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
        event.preventDefault()
        $.ajax({
            url: $(this.parentElement).attr("action"),
            method: 'POST',
            headers: {"X-CSRFToken": csrfToken, "Authorization": 'Token ' + localStorage.getItem('apiToken')},
            data: {"text": commentText.val(), "picture_id": pictureId},
            success: function (data, status) {
                console.log(data)
                console.log(status)
                $('#commentInput').val('')

                commentBlock.prepend(`
                    <div class="card mt-2" id="commentCard-${data.id}">
                        <p class="pt-2 ps-2">${data.author.username}</p>
                        <p><h6 class="ps-2">${data.text}</h6></p>
                        <p class="ps-2">${data.datetime_created}</p>
                        <form>
                        <input type="button" value="delete comment" class=" ms-2 delete_submit btn btn-primary"
                           id="deleteBtnCommentId-${data.id}"
                        </form>
                    </div>
                    `)

                $('#deleteBtnCommentId-' + data.id).click(function deleteComment(event) {
                    event.preventDefault();
                    $.ajax({
                        url: `/api/comments/${data.id}/`,
                        method: 'DELETE',
                        headers: {
                            "X-CSRFToken": csrfToken,
                            "Authorization": 'Token ' + localStorage.getItem('apiToken')
                        },
                        success: function () {
                            $(`#commentCard-${data.id}`).remove()
                        },
                        error: function (response, status) {
                            console.log(status);
                            console.log(response);
                        }
                    });

                })

            },
            error: function (response, status) {
                console.log(status);
                console.log(response);
            }
        });
    })


    for (let deleteCommentBtn of deleteCommentBtnList) {
        $(deleteCommentBtn).click(function deleteComment(event) {
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
            let commentId = $(deleteCommentBtn).data('commentId')
            event.preventDefault()
            $.ajax({
                url: $(this.parentElement).attr("action"),
                method: 'DELETE',
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Authorization": 'Token ' + localStorage.getItem('apiToken')
                },
                // data: {"comment_id": commentId},
                success: function (data, status) {
                    $(`#commentCard-${commentId}`).remove()
                    console.log(data);
                    console.log(status);
                },
                error: function (response, status) {
                    console.log(status);
                    console.log(response);
                }
            });
        })
    }
})
