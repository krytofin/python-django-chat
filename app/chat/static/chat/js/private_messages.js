const socket = new WebSocket(
    `ws://${document.location.host}/chat/${document.location.pathname.split('/')[2]}/`
);

socket.onopen = () => {
    console.log("Connected");
};

const user_id = document.querySelector(`#user_id`).value

const button = document.querySelector(`#send`)
button.addEventListener(`click`, (e)=>{
    e.preventDefault()
    const text_send = document.querySelector(`#text_for_send`).value
    if (text_send){
        socket.send(JSON.stringify({"type": "chat.message", "message": String(text_send)}))
    }
    document.querySelector(`#text_for_send`).value = ''
})

socket.onmessage = (m)=>{
    const message_data = JSON.parse(m.data)
    console.log(message_data.user_uuid)
    console.log(message_data.user, user_id, typeof message_data.user,  typeof user_id);
    
    if (message_data.user_uuid == user_id){
        const message_container = document.querySelector(`.messages`)
        message_container.innerHTML += `<div class="message right">
                    <div class="user"></div>
                    <div class="message_container">
                        ${message_data.message}
                    </div>
                    
                </div>`;
    }
    else {
        const message_container = document.querySelector(`.messages`)
        message_container.innerHTML += `<div class="message">
                    <div class="user">${message_data.username.replace('@', '')}: </div>
                    <div class="message_container">
                        ${message_data.message}
                    </div>
                    
                </div>`;
    }
}