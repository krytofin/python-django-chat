console.log(`ws://${document.location.origin}/chat/${document.location.pathname.split('/')[2]}/a`)
let socket = new WebSocket(`ws://${document.location.origin}/chat/${document.location.pathname.split('/')[2]}/`);
socket.onopen = () =>{
    console.log("Connected")
}