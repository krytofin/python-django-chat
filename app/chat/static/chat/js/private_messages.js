let socket = new WebSocket(
    `ws://${document.location.host}/chat/${document.location.pathname.split('/')[2]}/`
);

socket.onopen = () => {
    console.log("Connected");
};



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
    console.log(`You get: ${m.data}`)
    const message_data = JSON.parse(m.data)
    const message_container = document.querySelector(`.message`)
    message_container.innerHTML += `<p>${message_data['message']}</p>`;
}