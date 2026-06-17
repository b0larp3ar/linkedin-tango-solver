const button = document.getElementById("solve");

button.addEventListener("click", () => {

    console.log("button clicked");

    chrome.tabs.query(
        {
            active: true,
            currentWindow: true
        },

        ([tab]) => {

            console.log("tab id:", tab.id);

            chrome.tabs.sendMessage(
                tab.id,
                { action: "solve" }
            )
            .then(() => {
                console.log("message sent");
            })
            .catch(err => {
                console.error(err);
            });

        }

    );

});
