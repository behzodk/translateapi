from django.shortcuts import render
from googletrans import Translator
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.


def translate(request):
    text = request.GET.get('text')
    from_lang = request.GET.get('from')
    to_lang = request.GET.get('to')
    actual_lang = Translator().detect(text).lang
    if from_lang == 'auto' or from_lang == None or from_lang == 'auto-detect':
        from_lang = actual_lang
    if text is None:
        return HttpResponse('No text provided', status=400)
    return JsonResponse({
        'creators':{
            'name': 'Behzod Musurmonqulov',
            'email': 'behzodmusurmonqulov@gmail.com',
            'website': 'www.ischools.uz'
        },
        'input':{
            'text': text,
            'from': from_lang,
            'to': to_lang,
            'length': len(text)
        },
        'output':{
            'status': '200',
            'actual_lang': actual_lang,
            'translated': Translator().translate(text, src=from_lang, dest=to_lang).text,
            'pronunciation': Translator().translate(text, src=from_lang, dest=to_lang).pronunciation            
        }
        })
