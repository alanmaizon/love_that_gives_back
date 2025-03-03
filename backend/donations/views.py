from rest_framework import viewsets, status as drf_status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import Donation, Charity
from .serializers import DonationSerializer, CharitySerializer
from .mixins import CsrfExemptMixin
from .utils import CsrfExemptSessionAuthentication
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.db.models import Sum, Count, F, ExpressionWrapper, DecimalField
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decimal import Decimal

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

class DonationViewSet(CsrfExemptMixin, viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]

    @action(detail=True, methods=['patch'], url_path='confirm')
    def confirm_donation(self, request, pk=None):
        donation = self.get_object()
        donation.status = 'confirmed'
        donation.save()
        serializer = self.get_serializer(donation)
        return Response(serializer.data, status=drf_status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'], url_path='fail')
    def fail_donation(self, request, pk=None):
        donation = self.get_object()
        donation.status = 'failed'
        donation.save()
        serializer = self.get_serializer(donation)
        return Response(serializer.data, status=drf_status.HTTP_200_OK)

class CharityViewSet(CsrfExemptMixin, viewsets.ModelViewSet):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer
    authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]

@api_view(['GET'])
def donation_analytics(request):
    confirmed_donations = Donation.objects.filter(status='confirmed')
    total_amount = confirmed_donations.aggregate(total=Sum('amount'))['total'] or 0
    charity_amount = total_amount * Decimal('0.5')
    couple_amount = total_amount * Decimal('0.5')
    donations_count = confirmed_donations.count()
    # Group by charity name and calculate both count and allocated total.
    count_per_charity = confirmed_donations.values('charity__name').annotate(
        count=Count('id'),
        total_allocated=Sum(ExpressionWrapper(F('amount') * Decimal('0.5'), output_field=DecimalField()))
    )
    return Response({
        "total_amount": total_amount,
        "charity_amount": charity_amount,
        "couple_amount": couple_amount,
        "donations_count": donations_count,
        "count_per_charity": list(count_per_charity),
    })