# CGObot

This awesome bot cites quotes of CGO when it is pinged.

## Requirements

This app can be deployed using Docker. To build the Docker image, run the following command:

```bash
docker build --tag cgobot .
```

Then to lauch the simulation, run:

```bash
docker run -it --restart unless-stopped --env-file .env -v $PWD:/bot --name container-cgobot cgobot
```
