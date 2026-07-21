# Nexa AI — Vue d'ensemble de l'architecture

## Objectif

Nexa AI est une plateforme intelligente destinée à aider les utilisateurs à identifier les compétences nécessaires à leur évolution.

L'architecture est organisée en trois grandes couches :

1. Interface utilisateur.
2. API backend.
3. Intelligence artificielle.

---

## Architecture générale

Utilisateur

↓

Frontend Next.js

↓

API FastAPI

↓

Services métier

↓

OpenAI GPT

↓

Base de données

---

## Principes techniques

- séparation frontend/backend ;
- modularité ;
- évolutivité ;
- sécurité ;
- personnalisation.