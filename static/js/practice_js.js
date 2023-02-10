const csrfToken = getCookie('csrftoken')

const btnFavouriteList = $(`.btn_favourite`)


for ( const btnFavourite of btnFavouriteList) {
    $(btnFavourite).click(function toggleFavourite(event) {
    event.preventDefault()
    $.ajax({
        url: $(this.parentElement).attr("action"),
        method: 'POST',
        headers: {"X-CSRFToken": csrfToken},
        data: {picture_id: $(btnFavourite).attr("id")},
        success: function (data, status) {
            $(btnFavourite).toggleClass("btn-dark")
            console.log(data);
            console.log(status);
        },
        error: function (data, response, status) {
            console.log(status);
            console.log(data);
        }
    });
});
};


const commentText = $(".comment_text")
const commentSubmit = $(".comment_submit")
const pictureId = $(".card").data("pictureid")
let detailedUrl = $(".url-detailed").attr("href")
console.log(detailedUrl)


$(commentSubmit).click(function addComment(event){
    event.preventDefault()
    $.ajax({
        url: $(this.parentElement).attr("action"),
        method: 'POST',
        headers: {"X-CSRFToken": csrfToken},
        data: {"text": commentText.val(), picture_id: pictureId},
        success: function (data, status) {
            $(".new_comments").load(detailedUrl);
            console.log(data);
            console.log(status);
        },
        error: function (data, response, status) {
            console.log(status);
            console.log(data);
        }
    });
})

