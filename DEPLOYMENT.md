# Deploying Afrilott on Coolify

This project is deployed as a **Dockerfile application**. Coolify builds the
repository-owned `Dockerfile`, runs Gunicorn on port `8000`, and serves Django
static files through WhiteNoise.

## Coolify application settings

1. Push this repository to GitHub, GitLab, or another Git provider available to
   your Coolify instance.
2. In Coolify, create a new **Application** from the repository and branch.
3. Choose **Dockerfile** as the build pack.
4. Set **Base Directory** to `/` and **Dockerfile Location** to `Dockerfile`.
5. Set **Ports Exposes** to `8000`.
6. Add the production domain as `https://your-domain.example:8000`. The `:8000`
   informs Coolify which container port to proxy; public HTTPS remains on 443.
7. Set the health-check path to `/healthz/`.

## Runtime environment variables

Set these as runtime variables in Coolify. Do not mark the secret as a build
variable.

```dotenv
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=<generate-a-long-random-secret>
DJANGO_ALLOWED_HOSTS=your-domain.example,www.your-domain.example
DJANGO_CSRF_TRUSTED_ORIGINS=https://your-domain.example,https://www.your-domain.example
DJANGO_SECURE_SSL_REDIRECT=True
```

`DJANGO_ALLOWED_HOSTS` may be omitted when Coolify provides `COOLIFY_FQDN`, but
setting it explicitly is clearer and supports both apex and `www` domains.

Optionally enable HSTS for every subdomain only when every existing subdomain
is served exclusively over HTTPS:

```dotenv
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=True
DJANGO_SECURE_HSTS_PRELOAD=True
```

## DNS and first deployment

Point the domain's A/AAAA record to the Coolify server before deploying. Deploy
from Coolify, inspect the build and application logs, then open the configured
HTTPS domain. Coolify provisions the proxy and TLS certificate for an `https://`
domain.

The current website has no database-backed feature. No database or persistent
volume is required for this phase.
