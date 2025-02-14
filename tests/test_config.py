class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # In-memory DB for testing
    SECRET_KEY = "test_secret_key"
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing forms
