# Docker test

Docker compose project including postgresql and python containers.<br>Postgresql container includes database, python container includes python script, which connects to database and executes queries.

## Installation

Install [docker](https://docs.docker.com/engine/install/ubuntu/) using script on ubuntu.

```bash
# download script
curl -fsSL https://get.docker.com -o get-docker.sh

# run script
sudo sh get-docker.sh
```

The library already includes docker compose.

## Usage

```bash
# build docker compose from yaml
docker compose build .

# run containers via docker compose in detached mode
docker compose up -d
```
