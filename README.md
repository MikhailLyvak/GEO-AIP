# DRF-GEO_API
There is a GEO srevice, where you can create/update/delete or see some geo places.

### Docs: /api/doc/swagger/


## 🎥 Video PRESENTATION ->   [Click me!](https://youtu.be/6RyPXR9MXGg)


## 💼 Installing using GIT
```python
Download code with this commands:
    git clone https://github.com/MikhailLyvak/DRF-Library.git
    cd PY-GEO-API

Create file named .env    :
    Fill this file with data from .env.example u can just do copy-paste )

Than use docker ( Should be already installed!!! )

    sudo docker compose up     <-- For Linux
    docker-compose up --build  <-- For Windows

Do to telegram channel to check how bot works:
   ===== https://t.me/test_api_geo =====
```


# 🤟 To get access to work with api do next steps
```python
create user via /user/register/
get access token via /user/token/
```

# 📈 How to user ModHeader
```python
# ModHeader should be already installed
1. + MOD --> Request header
2. Put correct credentials
    2.1. Name --> Authorization
    2.2. Value --> Bearer < Your token >
```

# 📜 Some project Features
- JWT authenticated
- Admin panel /admin/
- Documentation is located at /doc/swagger/
- CRUD GEO-places
- Telegram bot notifications
- Approving places by admins
- Simple user can`t see unapproved places
