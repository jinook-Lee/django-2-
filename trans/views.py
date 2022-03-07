from django.shortcuts import render
from googletrans import Translator
import googletrans

# Create your views here.
def index(request):
    d = {"ko" :"korean"}
    for i in googletrans.LANGUAGES:
        d[i] = googletrans.LANGUAGES[i]
    
    context = { "ndict" : d }
    if request.method == "POST":
        text = request.POST.get("bf")
        fr = request.POST.get("fr")
        to = request.POST.get("to")
        translator = Translator()
        if text:
            inter = translator.translate(text, src=fr, dest=to)
            context.update({
                "bf" : text,
                "fr" : fr,
                "to" : to,
                "af" : inter.text
            })
    return render(request, "trans/index.html", context)

