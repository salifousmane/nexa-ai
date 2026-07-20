# Nexa AI — MVP Development Tasks

Version : MVP V1  
Projet : OpenAI Build Week

---

# Objectif

Construire une première version fonctionnelle de Nexa AI permettant à un utilisateur de :

1. créer son profil ;
2. obtenir un diagnostic personnalisé grâce à l’IA ;
3. recevoir un parcours d’évolution ;
4. discuter avec un mentor IA ;
5. suivre sa progression.

---

# Phase 0 — Préparation du projet

## Objectif

Mettre en place une base de développement propre.

Tâches :

- créer le dépôt Git ;
- configurer l’environnement ;
- définir la structure frontend/backend ;
- configurer les variables d’environnement ;
- préparer la documentation.

Critères de validation :

- le projet démarre correctement ;
- l’architecture est claire ;
- les dépendances sont installées.

---

# Phase 1 — Création du frontend

## Objectif

Créer l’interface utilisateur.

Tâches :

Créer :

- page d’accueil ;
- système de navigation ;
- composants réutilisables ;
- design responsive.

Pages :

- Landing page ;
- Profil utilisateur ;
- Diagnostic ;
- Rapport Nexa ;
- Parcours ;
- Dashboard ;
- Mentor IA.

Critères :

- interface fonctionnelle ;
- navigation fluide ;
- design cohérent.

---

# Phase 2 — Gestion du profil utilisateur

## Objectif

Permettre à l’utilisateur de fournir les informations nécessaires à l’analyse IA.

Créer :

- formulaire utilisateur ;
- validation des données ;
- stockage en base.

Données :

- situation ;
- domaine ;
- objectif ;
- niveau ;
- disponibilité ;
- compétences actuelles.

Critères :

- les données sont enregistrées ;
- elles peuvent être récupérées par l’API.

---

# Phase 3 — Backend API

## Objectif

Créer le serveur backend.

Tâches :

Créer :

- API utilisateur ;
- API profil ;
- connexion base de données ;
- gestion des erreurs.

Endpoints prévus :
POST /users
POST /profile
GET /profile/{id}
POST /diagnostic
POST /path
POST /chat

Critères :

- API accessible ;
- réponses JSON correctes ;
- documentation disponible.

---

# Phase 4 — Intégration IA

## Objectif

Connecter Nexa AI à OpenAI.

Créer les services :

- analyse profil ;
- génération diagnostic ;
- création parcours ;
- mentor conversationnel.

---

## Diagnostic IA

Entrée :

Profil utilisateur.

Sortie :

- résumé ;
- forces ;
- compétences prioritaires ;
- recommandations.

---

## Génération parcours

Sortie :

- objectif ;
- étapes ;
- durée ;
- actions.

---

## Mentor IA

Contexte utilisé :

- profil ;
- diagnostic ;
- parcours.

Critères :

- réponses personnalisées ;
- cohérence avec l’utilisateur.

---

# Phase 5 — Base de données

## Objectif

Créer le stockage permanent.

Tables :

## User

Informations compte.

---

## Profile

Informations personnelles et professionnelles.

---

## Diagnostic

Résultats générés par l’IA.

---

## LearningPath

Parcours créé.

---

## Progress

Suivi utilisateur.

---

# Phase 6 — Dashboard utilisateur

## Objectif

Créer une vue de progression.

Afficher :

- profil ;
- compétences ;
- progression ;
- prochaines actions.

Critères :

- informations claires ;
- expérience utilisateur simple.

---

# Phase 7 — Tests et amélioration

Tester :

- inscription ;
- création profil ;
- génération IA ;
- sauvegarde données ;
- chat IA.

Corriger :

- erreurs ;
- problèmes d’interface ;
- problèmes de performance.

---

# Phase 8 — Préparation démonstration jury

Créer :

- scénario utilisateur ;
- présentation ;
- captures d’écran ;
- vidéo démonstration.

Scénario :

Un étudiant utilise Nexa AI pour découvrir les compétences nécessaires à son avenir.

Démonstration :

1. Création profil.
2. Analyse IA.
3. Rapport d’évolution.
4. Création parcours.
5. Discussion avec mentor IA.

---

# Critères finaux du MVP

Le projet doit permettre :

✅ Profil utilisateur fonctionnel  
✅ Diagnostic IA personnalisé  
✅ Parcours généré automatiquement  
✅ Mentor IA contextuel  
✅ Dashboard de progression  
✅ Démonstration claire de la valeur du produit

---

# Priorité absolue

La qualité de l’expérience utilisateur et la personnalisation IA sont plus importantes que le nombre de fonctionnalités.
