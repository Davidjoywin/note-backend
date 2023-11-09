# Note Backend app

## Install all required libraries for the app

```
    pip3 install -r requirement.txt
```

## To Setup and run server on localhost

```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
```
        or
    For linux User only. Run the following from the root direction.
```
    ./app-setup
```

## Create a discord webhook
step 1
    Create a discord channel

step 2
    Go to 'server setting' under 'app' click on 'integrations'

step 3
    click on 'create webhook'

## Create a credential.json file
    Create in the root folder and paste the following json object into the file
    using the generated webhook url

```
{
    "webhook_url": "https://discord.com/api/webhooks/*/*"
    
}
```
