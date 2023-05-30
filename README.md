# DRF-GEO_API
There is a GEO srevice, where you can create/update/delete or see some geo places.

### Docs: /api/doc/swagger/


## 🎥 Video PRESENTATION ->   [Click me!](https://youtu.be/6RyPXR9MXGg)


## 💼 Installing using GIT
```python
git clone https://github.com/MikhailLyvak/DRF-Library.git
cd PY-GEO-API

Than use docker ( Should be already installed!!! )
sudo docker compose up     <-- For Linux
docker-compose up --build  <-- For Windows        

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
