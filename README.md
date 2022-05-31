# Installation
1. Install docker
2. Install git
3. `git clone https://github.com/AlexeyKutsenko/PortfoliosDB.git`
4. `docker-compose up`
5. Create superuser `docker-compose exec web python manage.py createsuperuser`
6. Collect static files `docker-compose exec web python manage.py collectstatic`

# To Do
1. Parse `http://www.lazyportfolioetf.com/`
2. Migrate correlation tool to the django admin
