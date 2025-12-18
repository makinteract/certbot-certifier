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
```

Certificates will be available in:

```bash
/etc/letsencrypt/live/<domain>/
  ├── fullchain.pem
  └── privkey.pem
```

and you can inspect them this way:

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

5. [Optional] Check the certificates were successfully created

List the volumes:

```bash
docker volume ls
```

The certificate should be inside something like `certbot-certifier_certbot-etc`.

```bash
docker run --rm -it -v certbot-certifier_certbot-etc:/data alpine sh
```

From the shell, check the files inside the `data/live` folder.

6. Extracting the certificate from the volume and copying it to /etc/letsencrypt

Assuming the volume with your certificates is `certbot-certifier_certbot-etc`, simply do:

```sh
docker run --rm -v certbot-certifier_certbot-etc:/from -v /etc/letsencrypt:/to alpine sh -c "cp -a /from/* /to/"

sudo chmod -R 755 /etc/letsencrypt
```

7. Set all down

```sh
docker compose down
```
