import LearningPath from "@/components/LearningPath";
import DiagnosticCard from "@/components/DiagnosticCard";

export default function Dashboard(){

return (
<main style={{padding:"40px"}}>

<h1>Tableau de bord Nexa AI</h1>

<p>
Suivez votre progression et votre parcours personnalisé.
</p>

<DiagnosticCard />

<LearningPath />

</main>
)

}
