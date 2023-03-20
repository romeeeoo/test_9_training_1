$(document).ready(function () {
    console.log(2)
    let btnFavouriteList = $(`.btn_favourite`)
    let deleteCommentBtnList = $(".delete_submit")
    let commentText = $(".comment_text")
    let commentSubmit = $(".comment_submit")
    let pictureId = $(".card").data("pictureid")
    let detailedUrl = $(".url-detailed").attr("href")
    const commentBlock = $('#commentBlock')
    console.log(3)


    for (let btnFavourite of btnFavouriteList) {
        $(btnFavourite).click(function toggleFavourite(event) {
            let csrfToken = $("input[name='csrfmiddlewaretoken']").attr("value")
            event.preventDefault()
            $.ajax({
                url: $(this.parentElement).attr("action"),
                method: 'post',
                headers: {"X-CSRFToken": csrfToken},
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
            method: 'post',
            headers: {"X-CSRFToken": csrfToken},
            data: {"text": commentText.val(), "picture_id": pictureId},
            success: function (data, status) {
                console.log(data)
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
                        headers: {"X-CSRFToken": csrfToken},
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
            console.log(`this is ${commentId}`)
            event.preventDefault()
            $.ajax({
                url: $(this.parentElement).attr("action"),
                method: 'DELETE',
                headers: {"X-CSRFToken": csrfToken},
                data: {"comment_id": commentId},
                success: function (data, status) {
                    console.log(data);
                    console.log(status);
                    console.log(6);
                    console.log(8);
                },
                error: function (response, status) {
                    console.log(status);
                    console.log(response);
                }
            });
        })

    }
    console.log(9)
})
