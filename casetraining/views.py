from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import hashlib
import json

from wiki.models import Article, ArticleRevision, URLPath

from .models import Casetraining

def index(request):
    casetrainings = Casetraining.objects.order_by('name')
    if not request.user.is_staff:
        casetrainings = casetrainings.filter(approved=True)

    return render(request, "casetraining/index.html", {
        'banner': '/media/original_images/Bogota_IMG_0242-modified.jpg',
        "advanced":  casetrainings.filter(difficulty="advanced"),
        "beginner":  casetrainings.filter(difficulty="beginner"),
        "shortcase": casetrainings.filter(difficulty="shortcase"),
    })

def new(request):
    return render(request, "casetraining/new.html", {
        'banner': '/media/original_images/Bogota_IMG_0242-modified.jpg',
    })

def show(request, case_id):
    if request.user.is_staff:
        case = get_object_or_404(Casetraining, pk=case_id)
    else:
        case = get_object_or_404(Casetraining, pk=case_id, approved=True)

    return render(request, "casetraining/show.html", {
        'banner': '/media/original_images/Bogota_IMG_0242-modified.jpg',
        "case": case,
    })

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

def free_text_mail(request, id):
    case = get_object_or_404(Casetraining, pk=id)
    data = json.loads(request.body)
    email = data.get('email')
    config = data.get('config')
    answers = data.get('answers')

    # return if no answers given
    if len(answers) == 0:
        return HttpResponse(201)

    context = {
        'case': case,
        'site': {
            'root_url': settings.SITE_URL,
        },
        'contact': {'id': id},
        'email': email,
        'questions_and_answers': [
            {'question': q.get('text'), 'answer': a}
            for q, a in zip(config, answers)
        ]
    }

    html_message = render_to_string('casetraining/korrektur-anfrage.html', context)
    plain_message = strip_tags(html_message)

    subject = f"Korrektur-Anfrage: {str(case)}"

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.EMAIL_JURCOACH],
        html_message=html_message,
        fail_silently=False,
    )

    return HttpResponse(201)


def wiki_categories(request):
    modified = Article.objects.order_by('-modified').first().modified
    hash = hashlib.md5(str(modified).encode('utf-8')).hexdigest()
    result = cache.get_or_set("wiki_categories", _wiki_categories_list, timeout=(60 * 60), version=hash)
    return JsonResponse(result, safe=False)

def _wiki_categories_list():
    articles = filter(lambda x: x.other_read, Article.objects.all())
    return list(map(_wiki_article, articles))

def _wiki_article(article):
    return {
        "id": article.id,
        "title": article.current_revision.title,
        "url": article.get_absolute_url(),
    }
