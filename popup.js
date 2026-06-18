const button = document.getElementById("solve");

button.addEventListener("click", () => {
    chrome.tabs.query(
        {
            active: true,
            currentWindow: true             // get the active tab
        },

        ([tab]) => {
            chrome.tabs.sendMessage(
                tab.id,
                { action: "solve" }         // send message to its console(main.js will be listening)
            )
        }
    );
});
