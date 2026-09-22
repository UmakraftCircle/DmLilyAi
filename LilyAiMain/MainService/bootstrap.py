    if provider is None:
        if settings.groq_api_keys:
            from LilyAiCore.Providers.Groq.client import GroqProvider

            provider = GroqProvider(list(settings.groq_api_keys), settings.groq_base_url, settings.chat_model, pool)
            log.info("Groq provider ready with %d API key(s)", len(settings.groq_api_keys))
        else:
            log.warning("GROQ_API_KEY not set: running with the offline provider")
            provider = OfflineProvider()