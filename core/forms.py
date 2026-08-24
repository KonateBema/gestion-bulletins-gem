from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import (
    Etudiant,
    Classe,
    Matiere,
    Note,
    AffectationMatiere
)

# =========================
# USER REGISTER FORM
# =========================
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# =========================
# CLASSE FORM
# =========================
class ClasseFormHHH(forms.ModelForm):
    class Meta:
        model = Classe
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": "form-control"
            })

class ClasseForm(forms.ModelForm):

    class Meta:
        model = Classe
        fields = [
            'nom',
            'filiere_bts',  # ✅ ici
            'niveau',
            'salle'
        ]

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'filiere_bts': forms.Select(attrs={'class': 'form-select'}),
            'niveau': forms.Select(attrs={'class': 'form-select'}),
            'salle': forms.Select(attrs={'class': 'form-select'}),
        }
# =========================
# MATIERE FORM
# =========================
from django import forms
from .models import Matiere, GrandeUnite


class MatiereForm(forms.ModelForm):

    class Meta:
        model = Matiere

        fields = [
            "code",
            "libelle",
            "coefficient",
            "volume_horaire",
            "filiere_bts",
            "grande_unite",
            "categorie",
            "professeur",
        ]

        widgets = {

            "code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex : MAT001",
            }),

            "libelle": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nom de la matière",
            }),

            "coefficient": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 1,
            }),

            "volume_horaire": forms.NumberInput(attrs={
                "class": "form-control",
                "min": 0,
            }),

            "filiere_bts": forms.Select(attrs={
                "class": "form-select",
            }),

            "grande_unite": forms.Select(attrs={
                "class": "form-select",
            }),

            "categorie": forms.Select(attrs={
                "class": "form-select",
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["grande_unite"].queryset = GrandeUnite.objects.select_related(
            "filiere_bts"
        ).order_by(
            "filiere_bts",
            "ordre"
        )

        self.fields["grande_unite"].required = False

        self.fields["grande_unite"].empty_label = (
            "— Sélectionner une grande unité —"
        )

# =========================
# ETUDIANT FORM
# =========================
class EtudiantFormOOO(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = [
            "matricule",
            "nom",
            "prenoms",
            "date_naissance",
            "lieu_naissance",
            "sexe",
            "telephone",
            "email",
            "classe",
            'filiere_bts',
        ]
from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):

    class Meta:
        model = Etudiant

        fields = [
            'matricule',
            'identifiant_permanent',  # 👈 juste après matricule
            'nom',
            'prenoms',
            'date_naissance',
            'lieu_naissance',
            'sexe',
            'telephone',
            'email',
            'classe',
            'filiere_bts',
        ]

        widgets = {

            'matricule': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : MAT20250001'
            }),

            'identifiant_permanent': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex : IP20250001'
            }),

            'nom': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'prenoms': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'date_naissance': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'lieu_naissance': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'sexe': forms.Select(attrs={
                'class': 'form-select'
            }),

            'telephone': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'classe': forms.Select(attrs={
                'class': 'form-select'
            }),

            'filiere_bts': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
# =========================
# AFFECTATION FORM
# =========================
class AffectationForm(forms.ModelForm):
    class Meta:
        model = AffectationMatiere
        fields = "__all__"


# =========================
# NOTE FORM
# =========================
from django import forms
from .models import Note

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note

        fields = [
            "etudiant",
            "matiere",
            "devoir",
            "examen",
            "cc",
            "semestre",
        ]

        widgets = {

            "etudiant": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "matiere": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "devoir": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Note devoir"
                }
            ),

            "examen": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Note examen"
                }
            ),

            "cc": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Note CC"
                }
            ),

            "semestre": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
        }