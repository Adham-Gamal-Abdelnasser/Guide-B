
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SignUpSerializer
import re
from datetime import date


@api_view(['POST'])
def register(request):
    data = request.data

    
    phone_pattern = r'^(010|011|012|015)\d{8}$'
    if not re.match(phone_pattern, data.get('phone', '')):
        return Response({"error": "Phone number must be 11 digits and start with 010, 011, 012, or 015."}, status=status.HTTP_400_BAD_REQUEST)

    
    if not re.match(r'^\d{14}$', data.get('national_id', '')):
        return Response({"error": "The national number must be exactly 14 digits."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        birth_date = date.fromisoformat(data.get('birth_date', ''))
        if birth_date >= date.today():
            return Response({"error": "Birth date cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({"error": "Invalid birth date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    user = SignUpSerializer(data=data)

    if user.is_valid():
        if not CustomUser.objects.filter(username=data['email']).exists():
            user = CustomUser.objects.create(
                full_name=data['full_name'],
                phone=data['phone'],
                email=data['email'],
                username=data['email'],
                address=data['address'],
                national_id=data['national_id'],
                password=make_password(data['password']),
                birth_date=data['birth_date'],
                profile_image=data['profile_image'],
                medical_report=data['medical_report'],
                national_id_image=data['national_id_image'],
                form_2_gond=data['form_2_gond'],
                form_6_7_gond=data['form_6_7_gond'],
                payment_receipt=data['payment_receipt'],
                high_school_certificate=data['high_school_certificate'],
                final_nomination_card=data['final_nomination_card'],
            )
            return Response(
                {'details': 'Registered successfully!'},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {'error': 'This user already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
