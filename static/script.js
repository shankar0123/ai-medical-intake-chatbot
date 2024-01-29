function sendMessage() {
    var input = document.getElementById("userInput");
    var message = input.value;
    input.value = '';

    if (message) {
        addToChatbox('You', message);
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({message: message}),
        })
        .then(response => response.json())
        .then(data => addToChatbox('Bot', data.message));
    }
}

function addToChatbox(sender, message) {
    var chatbox = document.getElementById("chatbox");
    var newMessage = document.createElement("div");
    newMessage.textContent = sender + ": " + message;
    chatbox.appendChild(newMessage);
    chatbox.scrollTop = chatbox.scrollHeight;
}
