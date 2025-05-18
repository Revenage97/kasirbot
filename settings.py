# … import, BASE_DIR, INSTING_APPS, dll …

LOGIN_URL = '/'                   # kalau belum login, redirect ke /
LOGIN_REDIRECT_URL = '/dashboard/'  # setelah login sukses, ke /dashboard/
LOGOUT_REDIRECT_URL = '/'         # setelah logout, kembali ke /

# TEMPLATES setting harus ada root templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],   # ⬅ pastikan ini
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # … default …
                'django.contrib.auth.context_processors.auth',
                # … dst …
            ],
        },
    },
]
