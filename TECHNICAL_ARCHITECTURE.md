# Nexa AI — Technical Architecture

Version : MVP V1  
Projet : OpenAI Build Week

---

# 1. Objectif technique

Construire une application web intelligente permettant à un utilisateur de :

1. créer son profil d’évolution ;
2. recevoir une analyse personnalisée grâce à l’IA ;
3. obtenir un parcours de développement de compétences ;
4. discuter avec un mentor IA ;
5. suivre sa progression.

L’architecture doit être :
- simple ;
- évolutive ;
- sécurisée ;
- adaptée à un MVP.

---

# 2. Architecture générale
Utilisateur
↓
Frontend Web
↓
API Backend
↓
Services métier
↓
Base de données + Services IA

---

# 3. Stack technique

## Frontend

Technologies :

- Next.js
- React
- TypeScript
- Tailwind CSS

Responsabilités :

- interface utilisateur ;
- formulaires ;
- affichage des rapports ;
- dashboard ;
- interface conversationnelle.

---

## Backend

Technologies :

- Python
- FastAPI

Responsabilités :

- API REST ;
- authentification ;
- logique métier ;
- communication avec OpenAI ;
- gestion des utilisateurs.

---

## Base de données

Technologie :

- PostgreSQL

Stockage :

- utilisateurs ;
- profils ;
- diagnostics ;
- parcours ;
- progression ;
- historique IA.

---

# 4. Structure du projet
nexa-ai/
├── frontend/ │ │   ├── app/ │   ├── components/ │   ├── services/ │   └── styles/ │ ├── backend/ │ │   ├── main.py │   ├── models/ │   ├── routes/ │   ├── services/ │   └── database/ │ ├── ai/ │ │   ├── prompts/ │   ├── agents/ │   └── memory/ │ ├── docs/ │ └── README.md

---

# 5. Modules principaux

## Module utilisateur

Fonctions :

- inscription ;
- connexion ;
- gestion du profil.

---

## Module profil intelligent

Données collectées :

- situation ;
- domaine ;
- objectif ;
- niveau ;
- disponibilité ;
- compétences actuelles.

---

## Module diagnostic IA

Entrée :

Profil utilisateur.

Traitement :

Analyse par OpenAI.

Sortie :

- résumé du profil ;
- forces ;
- lacunes ;
- compétences recommandées ;
- priorités.

---

## Module parcours personnalisé

Génère :

- objectif ;
- étapes ;
- durée ;
- ressources ;
- exercices.

---

## Module mentor IA

Assistant conversationnel avec contexte :

- profil utilisateur ;
- diagnostic ;
- parcours ;
- progression.

---

## Module progression

Suivi :

- compétences acquises ;
- tâches terminées ;
- évolution.

---

# 6. Architecture IA

## Agent principal

Nom :

Nexa Agent

Rôle :

Conseiller intelligent d’évolution.

---

## Entrées IA

Exemple :

```json
{
"domaine":"Finance",
"objectif":"évolution professionnelle",
"niveau":"débutant"
}
Sorties attendues
Format JSON structuré :
{
"analyse":"",
"forces":[],
"competences_prioritaires":[],
"plan":[]
}
7. Mémoire utilisateur
Deux types :
Mémoire longue durée
Informations stables :
préférences ;
objectifs ;
domaine.
Mémoire de session
Informations temporaires :
discussion actuelle ;
problème rencontré ;
étape en cours.
8. Sécurité
Principes :
ne jamais stocker de clés API dans le code ;
utiliser des variables d’environnement ;
protéger les données utilisateurs ;
valider les entrées ;
gérer les erreurs API.
9. Déploiement prévu
MVP :
Frontend :
Vercel
Backend :
Render / Railway / Replit
Base :
PostgreSQL cloud
10. Contraintes MVP
Priorités :
Fonctionnalité réelle.
Qualité de l’expérience IA.
Simplicité.
Code maintenable.
Ne pas ajouter :
fonctionnalités sociales ;
marketplace ;
complexité inutile.
11. Évolution future
Possibilités :
analyse de CV ;
connexion aux plateformes d’emploi ;
recommandations en temps réel ;
application mobile ;
certifications ;
agents IA spécialisés.
