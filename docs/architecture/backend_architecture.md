# Nexa AI — Architecture Backend

## Technologie

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

---

## Organisation

backend/

app/

- routes : endpoints API
- services : logique métier
- models : données SQL
- schemas : validation des données

---

## Responsabilités

Le backend gère :

- utilisateurs ;
- profils ;
- diagnostics ;
- parcours ;
- conversations IA.

---

## API principales

/users

Gestion des utilisateurs.

 /diagnostic

Création du diagnostic IA.

 /paths

Génération du parcours.

 /chat

Interaction avec Nexa Mentor.