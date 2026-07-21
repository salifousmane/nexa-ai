"use client";

import {useState} from "react";

export default function ChatBox(){

const [message,setMessage]=useState("");

return (
<div>

<h2>Nexa Mentor</h2>

<input
value={message}
onChange={(e)=>setMessage(e.target.value)}
placeholder="Posez votre question"
/>

<button>
Envoyer
</button>

</div>
)

}