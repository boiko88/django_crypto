from django.views.generic import TemplateView
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings as conf_settings
import requests


class NewsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)

        # Check if news data is in cache
        cached_news = cache.get('bitcoin_news_article')
        if cached_news:
            context['news_article'] = cached_news
            return context

        api_key = conf_settings.NEWS_API_KEY
        url = f'https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&language=en&apiKey={api_key}'

        try:
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles', [])

            if articles:
                news_article = articles[0]  # Get the latest article
                cache.set('bitcoin_news_article', news_article, timeout=300)  # Cache for 5 minutes
                context['news_article'] = news_article
            else:
                context['news_article'] = None

        except Exception as e:
            print(f'Error fetching Bitcoin news: {e}')
            context['news_article'] = None

        return context
