# uba_denylist_app
This repo hosts solution that sends list of IOCs (IP, Domain) from Splunk to UBA via intermediate Web Server. 

# Alert Action


# IOCbin Web Server

# Deploy Web Server(Production)

```
git clone https://github.com/splunk/uba_denylist_app.git

cd uba_denylist_app

docker-compose up
```

---

# For developer

## Install (first time)

```
pip install poetry

cd IOCbin

poetry install
```

## Run

```
cd IOCbin

poetry run iocbin
```

## Run at specific port

```
poetry run iocbin -p <PORT_NUM>
```


## Run in docker
```
cd IOCbin

docker build . -t iocbin-server

docker run -p 5000:5000 iocbin-server
```


