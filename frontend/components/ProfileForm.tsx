"use client";

import {useState} from "react";

export default function ProfileForm(){

const [goal,setGoal]=useState("");

return (
<div>
<h2>Votre objectif</h2>

<input
value={goal}
onChange={(e)=>setGoal(e.target.value)}
placeholder="Ex: apprendre Python"
/>

<button>
Analyser mon profil
</button>

</div>
)

}