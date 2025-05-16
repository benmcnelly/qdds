# qdds

> Quick Django Dev Server — start your local Django project with your IP exposed for LAN testing.

<p align="center">
  <a href="https://pypi.org/project/qdds/"><img src="https://badge.fury.io/py/qdds.svg" alt="PyPI version"></a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <a href="https://github.com/benmcnelly/qdds/issues"><img src="https://img.shields.io/github/issues/benmcnelly/qdds.svg" alt="GitHub issues"></a>
  <a href="https://pyup.io/repos/github/benmcnelly/qdds/"><img src="https://pyup.io/repos/github/benmcnelly/qdds/shield.svg" alt="Updates"></a>
  <a href="https://www.youtube.com/watch?v=EIyixC9NsLI"><img src="https://img.shields.io/badge/badger-approved-ff69b4.svg" alt="badger approved"></a>
</p>

---

## 🚀 What is qdds?

**qdds** (`devserver`) is a small CLI tool that runs your Django project's dev server using your local network IP, making it accessible to other devices on your Wi-Fi. Great for testing on mobile or with a team.

By default, it runs on **port 80**, so other devices on your network can just enter your IP address (like `http://192.168.1.50`) without needing a port number. 🔥

If that fails due to permissions or port binding restrictions, you can pass `--safe` to fall back to Django's default port 8000.

---

## 🛠 Installation

```bash
pip install qdds
```

---

## 📦 Usage

Inside your Django project folder (where `manage.py` lives):

```bash
devserver
```

This runs:

```bash
python manage.py runserver 0.0.0.0:80
```

That means devices on your Wi-Fi can hit `http://<your-ip>` with no port required.

If you get a permission error or want to play it safe:

```bash
devserver --safe
```

This runs it on port 8000, just like Django normally would.

---

## 🔧 Options

- `--safe` — Run on port 8000 instead of 80 (for systems that restrict port binding).
- `--regular` — Skip IP detection and just run on localhost (Django default behavior).

---

## 🧪 Development

Clone and install in editable mode:

```bash
git clone https://github.com/benmcnelly/qdds.git
cd qdds
pip install -e .
```

Run tests:

```bash
pytest
```

---

## 💬 Why qdds?

Sometimes you just want to fire up Django on your LAN, show a teammate something on their phone, or test a layout in mobile Safari without thinking. qdds makes that effortless.

---

## 📝 License

MIT © Ben McNelly
