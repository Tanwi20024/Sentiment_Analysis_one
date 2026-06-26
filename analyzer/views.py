
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from textblob import TextBlob
import json

# In-memory history store
analysis_history = []

def home(request):
    return render(request, 'analyzer/index.html', {'history': analysis_history[-5:][::-1]})

@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '').strip()
        except:
            text = request.POST.get('text', '').strip()

        if not text:
            return JsonResponse({'error': 'No text provided'}, status=400)

        blob = TextBlob(text)
        polarity    = round(blob.sentiment.polarity, 4)
        subjectivity = round(blob.sentiment.subjectivity, 4)

        if polarity > 0.1:
            sentiment = 'Positive'
            emoji     = '😊'
            color     = '#10b981'
        elif polarity < -0.1:
            sentiment = 'Negative'
            emoji     = '😞'
            color     = '#ef4444'
        else:
            sentiment = 'Neutral'
            emoji     = '😐'
            color     = '#f59e0b'

        # Polarity percentage (0-100)
        polarity_pct    = round((polarity + 1) / 2 * 100, 1)
        subjectivity_pct = round(subjectivity * 100, 1)

        # Word & sentence count
        words     = len(text.split())
        sentences = len(blob.sentences)

        result = {
            'text': text,
            'sentiment': sentiment,
            'emoji': emoji,
            'color': color,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'polarity_pct': polarity_pct,
            'subjectivity_pct': subjectivity_pct,
            'words': words,
            'sentences': sentences,
        }

        # Save to history
        analysis_history.append(result)
        if len(analysis_history) > 20:
            analysis_history.pop(0)

        return JsonResponse(result)

    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def history(request):
    return JsonResponse({'history': analysis_history[-10:][::-1]})
