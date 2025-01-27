- Build and push docker image:
    ```shel
    # Login
    docker login registry.digitalocean.com

    # Build
    docker build -t registry.digitalocean.com/cerossi-k8s/django-k8s-web:latest -f web/Dockerfile web

    # Push
    docker push registry.digitalocean.com/cerossi-k8s/django-k8s-web --all-tags
    ```