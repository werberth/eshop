## Eshop Project

Project example from the book [Django By Example by Antonio Melé (Copyright © 2015 Packt Publishing)](https://www.packtpub.com/web-development/django-example) using Celery to launching asynchronous tasks.

![Eshop](http://image.ibb.co/maPf6b/Captura_de_tela_2018_01_06_02_01_55.png)

### Installation

```
git clone git@github.com:werberth/eshop.git eshop
cd eshop
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Running

Open 3 Terminal windows, and run the following commands:

- ``` python manage.py runserver ```
- ``` celery -A eshop worker -l info ``` 
- ``` celery -A eshop flower ```
