from django.core.management.base import BaseCommand

from students.models import Student
from teachers.models import Teacher

STUDENTS = [
    ("Awa", "Diop", "awa.diop@ecole.sn", "L1", True),
    ("Moussa", "Fall", "moussa.fall@ecole.sn", "L2", True),
    ("Fatou", "Ndiaye", "fatou.ndiaye@ecole.sn", "L1", False),
    ("Ibrahima", "Sow", "ibrahima.sow@ecole.sn", "L3", True),
    ("Mariama", "Ba", "mariama.ba@ecole.sn", "L2", True),
    ("Ousmane", "Cissé", "ousmane.cisse@ecole.sn", "L3", True),
]
TEACHERS = [
    ("Mamadou", "Ba", "mamadou.ba@ecole.sn", "Mathématiques"),
    ("Aïssatou", "Sy", "aissatou.sy@ecole.sn", "Informatique"),
    ("Cheikh", "Diallo", "cheikh.diallo@ecole.sn", "Anglais"),
]


class Command(BaseCommand):
    help = "Ajoute des étudiants et enseignants fictifs (idempotent)."

    def handle(self, *args, **options):
        for first, last, email, classe, active in STUDENTS:
            Student.objects.get_or_create(
                email=email,
                defaults=dict(first_name=first, last_name=last,
                              classe=classe, active=active),
            )
        for first, last, email, subject in TEACHERS:
            Teacher.objects.get_or_create(
                email=email,
                defaults=dict(first_name=first, last_name=last, subject=subject),
            )
        self.stdout.write(self.style.SUCCESS("Données de démonstration ajoutées."))
