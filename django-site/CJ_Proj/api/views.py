from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.utils import timezone
from .models import Manga, PretAnimInt
from .serializers import PretAnimIntSerializer

@api_view(['POST'])
def reserver_manga(request, manga_id):
    user = request.user
    
    # Vérification si l'utilisateur est badgeur
    if not user.badgeur:
        return Response({'error': 'Vous devez être badgeur pour réserver un manga.'}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        # Récupération du manga à réserver
        manga = Manga.objects.get(id=manga_id)
    except Manga.DoesNotExist:
        return Response({'error': 'Le manga demandé n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)

    # Vérification si le manga est déjà prêté
    if manga.etat_pret_livre:
        return Response({'error': 'Le manga est déjà prêté.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Création d'une réservation
    pret = PretAnimInt(
        user=user,
        livre=manga,
        date_debut_livre=timezone.now(),
        date_fin_livre=timezone.now() + timezone.timedelta(days=7)  # Durée de prêt de 7 jours par défaut
    )
    pret.save()

    # Mise à jour de l'état du manga pour indiquer qu'il est prêté
    manga.etat_pret_livre = True
    manga.save()

    # Sérialisation de la réservation
    serializer = PretAnimIntSerializer(pret)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)
