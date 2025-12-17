# Certbot HTTP-01 with Docker (Python Webroot)

## Requirements

- Docker
- Docker Compose
- Public DNS A record pointing to this machine
- Port 80 open

## Setup

1. Clone this repository on a machine

```bash
git clone https://github.com/makinteract/certbot-certifier
```

2. Create `.env`:

```env
CERTBOT_EMAIL=you@example.com
CERTBOT_DOMAIN=example.com
```

3. Start services:

```bash
docker compose up --build certbot
Certificates will be available in:
```

Certificates appear here

```bash
/etc/letsencrypt/live/<domain>/
  ├── fullchain.pem
  └── privkey.pem
```

and you can inspect them this way

```bash
docker volume inspect certbot-etc
```

Renewal (⚠️ important)

HTTP-01 renewals will fail unless:

- DNS still points to this machine
- Port 80 is still open
- The web container is running

4. Renewal

```bash
docker compose run certbot renew
```
