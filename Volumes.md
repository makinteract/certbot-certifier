# Manually extracting certificates from Volume

1. Check the certificates were successfully created

List the volumes:

```bash
docker volume ls
```

The certificate should be inside something like `certbot-certifier_certbot-etc`.

```bash
docker run --rm -it -v certbot-certifier_certbot-etc:/data alpine sh
```

From the shell, check the files inside the `data/live` folder.

2. Extracting the certificate from the volume and copying it to /etc/letsencrypt

Assuming the volume with your certificates is `certbot-certifier_certbot-etc`, simply do:

```sh
docker run --rm -v certbot-certifier_certbot-etc:/from -v /etc/letsencrypt:/to alpine sh -c "cp -a /from/* /to/"

sudo chmod -R 755 /etc/letsencrypt
```
