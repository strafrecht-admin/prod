from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from core.views import exams
from profiles.views import login

from wagtailpolls.views.vote import vote
from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls
from birdsong.urls import urlpatterns as birdsong_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/autocomplete/', include(autocomplete_admin_urls)),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('search/', include('pages.urls')),

    path('jurcoach/klausurendatenbank/', exams, name='exams'),

    path('notifications/', include('django_nyt.urls')),

    path('feedback/', include('feedback.urls')),
    path('accounts/login/', login, name='login'),

    path('profile/', include('profiles.urls')),
    path('flashcards/', include('flashcards.urls')),
    path('quiz/', include('quiz.urls')),
    path('run/', include('core.urls')),
    path('lehre/', include('core.urls')),

    path('mail/', include(birdsong_urls)),
    path('', include('pwa.urls')),

    path('chat/', include('chat.urls')),
    path('comments/', include('django_comments_xtd.urls')),

    re_path(r'^vote/(?P<poll_pk>.*)/$', vote, name='wagtailpolls_vote'),

    path('wiki/', include('wiki.urls')),
    path('', include(wagtail_urls)),
    path('avatar/', include('avatar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if True and settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
