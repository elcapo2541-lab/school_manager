# School Manager (TP 1 → TP 4)

## Lancer le projet (PowerShell, Windows)
```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations students teachers
python manage.py migrate
python manage.py seed_demo          # 6 étudiants + 3 enseignants fictifs (facultatif)
python manage.py createsuperuser    # pour /admin/
python manage.py runserver
```

## Pages
| Adresse | Rôle |
|---|---|
| `/` | accueil (chiffres réels) |
| `/students/` | liste + recherche `?q=` |
| `/students/new/` | inscrire (GET formulaire / POST enregistre) |
| `/students/<id>/` | fiche |
| `/students/<id>/edit/` | modifier |
| `/students/<id>/delete/` | confirmer puis supprimer (POST) |
| `/students/classe/L1/` | filtre par classe |
| `/teachers/`, `/teachers/new/` | liste, ajout enseignant |

## Tests manuels du TP 4 (critères de réussite)
1. Enregistrer un formulaire vide -> "Veuillez renseigner ce champ".
2. Email déjà utilisé -> "Un objet Student avec ce champ Email existe déjà."
3. Téléphone `77-12` -> erreur ; `77 123 45 67` -> OK, stocké `771234567`.
4. Inscription -> redirection vers la fiche + bandeau vert (disparaît au F5).
5. Modifier -> formulaire pré-rempli, pas de doublon.
6. Supprimer -> page de confirmation, puis suppression en POST.

## Commits Git conseillés
```
git init
git add . ; git commit -m "feat: add StudentForm and create view"
git add . ; git commit -m "feat: add validation, messages and form styles"
git add . ; git commit -m "feat: add student update and delete views"
git add . ; git commit -m "feat: add teacher create view"
```
(Si tout est déjà fait : un seul commit. `db.sqlite3` et `venv/` sont dans `.gitignore`.)

## Réponses aux questions du TP (à reformuler avec vos mots)
1. **GET** : lire/chercher (données dans l'adresse, sans danger au F5). **POST** : créer/modifier/supprimer (données dans le corps de la requête).
2. **`{% csrf_token %}`** : jeton qui prouve que le formulaire vient bien de notre site ; s'il manque -> erreur 403.
3. **Form** : champs décrits à la main. **ModelForm** : construit automatiquement depuis un Model (champs, types, `unique=True`) et sait faire `save()`.
4. **`is_valid()`** lance les vérifications (True/False) ; **`cleaned_data`** contient les valeurs validées ; **`errors`** les messages d'erreur par champ.
5. **`redirect()`** après succès : évite de renvoyer le POST si on recharge la page (motif POST/Redirect/GET).
6. Même ModelForm : sans `instance` -> création ; avec `instance=student` -> pré-rempli et `save()` met à jour.
7. Suppression en **POST** après confirmation : un lien = GET, qui ne doit jamais modifier la base ; et la suppression est définitive.
8. Règle perso : méthode `clean_<champ>()` dans le formulaire, qui lève `forms.ValidationError` ou renvoie la valeur nettoyée.
9. **Question pro** (réserver aux enseignants connectés) : authentification Django + `@login_required` (ou `LoginRequiredMixin`) et permissions (`@permission_required`) sur les vues create/update/delete.
