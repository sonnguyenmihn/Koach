from rest_framework.decorators import api_view
from django.http import JsonResponse
from .utils.translating import translating_sign_language

@api_view(['POST'])
def translate(request):
    "API endpoint that simulate sign language translation"
    
    #get the input text from the request
    input_text = request.data.get('text')
    
    #validate input
    if not input_text:
        return JsonResponse(
            {"error": "input text not found"},
            status=400
        )
        
    translated_text = translating_sign_language(input_text)
    return JsonResponse(
        {"message": "Translation successful", "translated_text": translated_text},
        status = 200
    )