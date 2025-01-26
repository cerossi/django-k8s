# Take Aways
1. Setup django apps using environment variables.
    - Define the env variables in the **.env** file
    ```
    DEBUG=1
    DJANGO_SUPERUSER_USERNAME=admin
    ``` 
    - Load the environemnt variables from the .env file in **manage.py**
    ````python
    import dotenv

    def main():
        [...]

    if __name__ == '__main__':
        dotenv.read_dotenv()
        main()

    ````
    - Get the environment variables value using the os module in **settings.py**
    ````python
    import os
    from pathlib import Path

    [...]

    DEBUG = str(os.environ.get("DEBUG")) == "1"
    ````
1. Use docker compose to build complex containers. See docker-compose.yaml
1. Automatically setup kubeconfig.yaml as environment variable through the VS Code workspace setting
    ````json
    {
        "folders": [
            {
                "path": "."
            }
        ],
        "settings": {
            "terminal.integrated.env.osx": {
                "KUBECONFIG": "${workspaceFolder}/.kube/kubeconfig.yaml"
            }
        }
    }
    ````

1. Generated strong random passwords using python
    ```` shell
    python -c "import secrets;print(secrets.token_urlsafe(32))"

    or

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ````
