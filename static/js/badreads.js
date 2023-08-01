var updateShelf = document.getElementsByClassName("update-shelf")

for (var i=0; i<updateShelf.length; i++) {
    updateShelf[i].addEventListener("click", function(){
        var bookID = this.dataset.product
        var action = this.dataset.action
        console.log("bookID", bookID, "action", action)

        updateUserShelves(bookID, action)
    })
}

function updateUserShelves(bookID, action) {
    console.log("button clicked, processing...")

    let url = "/add_to_shelf/"

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body:JSON.stringify({'bookID':bookID, 'action':action})
    })
    .then((response) => {
        console.log("success", response)
        return response.json();
    })
    .then((data) => {
        console.log(data)
        // location.reload()
    });
}



var postMsgBtn = document.getElementById("group-message")

if (postMsgBtn) {
    postMsgBtn.addEventListener("click", function(){
        console.log("button clicked")
        var groupID = this.dataset.group
        let messageInput = document.getElementById("group-message-input");
        if (messageInput) {
            let msg = document.getElementById("group-message-input").value
            console.log(groupID, msg)
            postMessage(groupID, msg)
        }
    })
}

function postMessage(groupID, msg) {
    console.log("Success, posting msg")
    let url = "/add_message/"

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({"groupID": groupID, "msg": msg})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log(data)
        location.reload()
    })
}

var postReview = document.getElementsByClassName("review-message")

for (var i=0; i<postReview.length; i++) {
    postReview[i].addEventListener("click", function(){
        var bookID = this.dataset.book
        let reviewinput = document.getElementById("review-body");
        if (reviewinput) {
            let review = document.getElementById("review-body").value
            addBookReview(bookID, review)
        }
        // console.log("bookID", bookID, "review", review)

    })
}

function addBookReview(bookID, review) {
    console.log("Success, adding review")

    let url = "/add_review/"

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body:JSON.stringify({"bookID": bookID, "review": review})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log(data)
        location.reload()
    })
}


var submitForm = document.getElementById("create-article")

if (submitForm) {
    submitForm.addEventListener("click", async function(){
        console.log("button clicked, processing..")
        var url = "/create-article/"
        var imageInput = document.getElementById("ns-image-input")
        let headline = document.getElementById("headline-input").value
        let running_head = tinymce.get("editor").getContent()
        let body = tinymce.get("editor1").getContent()
        const image = imageInput.files[0];
        console.log("headline", headline, "running_head", running_head, "body", body, "image", image)
        const formData = new FormData()
        formData.append('image', image)
        formData.append('headline', headline)
        formData.append('running_head', running_head)
        formData.append("body", body)

        await fetch(url, {
            method: "POST",
            headers: {
                // "Content-Type": "multipart/form-data",
                "X-CSRFToken": csrftoken
            },
            body: formData
            })
            .then((response) => {
                console.log("API working",response)
                return response
            })
            .then((data) => {
                console.log(data)
                alert("Article Uploaded")
            })
            .catch((error) => {
                // console.error(error)
                alert("Error uploading file")
            })
    })
}

var friendRequestBtn = document.getElementsByClassName("friendRequestBtn")

if (friendRequestBtn) {
    for (var i=0; i<friendRequestBtn.length; i++) {
        friendRequestBtn[i].addEventListener("click", function() {
            console.log("button pressed, processing friend request")
            var requestID = this.dataset.request
            var action = this.dataset.action
            console.log(requestID, action)

            processFriendRequest(requestID, action)
        })
    }
}

function processFriendRequest(requestID, action) {
    let url = "/accept-friend-request/"

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body:JSON.stringify({"requestID": requestID, "action": action})
    })
    .then((response) => {
        console.log(response)
        return response.json()
    })
    .then((data) => {
        console.log(data)
        alert("Friend Request Accepted")
        location.reload()
    })
}
