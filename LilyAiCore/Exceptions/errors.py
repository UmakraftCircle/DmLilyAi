class LilyAiError(Exception):
    """Base class for every LilyAi error."""


class ConfigError(LilyAiError):
    pass


class ProviderError(LilyAiError):
    pass


class RateLimitError(ProviderError):
    def __init__(self, message: str = "Rate limited", retry_after: float | None = None):
        super().__init__(message)
        self.retry_after = retry_after


class ToolError(LilyAiError):
    pass


class ToolValidationError(ToolError):
    pass


class WebError(LilyAiError):
    pass
