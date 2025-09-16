console.log(`ws://${document.location.host}/chat/${document.location.pathname.split('/')[2]}/`);

let socket = new WebSocket(
    `ws://${document.location.host}/chat/${document.location.pathname.split('/')[2]}/`
);

socket.onopen = () => {
    console.log("Connected");
};



const button = document.querySelector(`#send`)
button.addEventListener(`click`, (e)=>{
    e.preventDefault()
    socket.send(JSON.stringify({"type": "chat.message", "message": "a"}))
})

socket.onmessage = (m)=>{
    console.log(m.data)
}