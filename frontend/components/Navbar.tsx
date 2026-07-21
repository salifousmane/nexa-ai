export default function Navbar() {
  return (
    <nav style={{padding:"20px",display:"flex",justifyContent:"space-between"}}>
      <h2>Nexa AI</h2>

      <div>
        <a href="/">Accueil</a>{" "}
        <a href="/diagnostic">Diagnostic</a>{" "}
        <a href="/mentor">Mentor</a>
      </div>
    </nav>
  );
        }
