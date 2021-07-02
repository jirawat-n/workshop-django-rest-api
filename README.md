# REST-API
## Project setup
- `cd api_workshop`
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt1

## Start Develop
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

## init data

- `python manage.py loaddata fixdata/product.json`
- `python manage.py loaddata fixdata/product_image.json`
- `python manage.py loaddata fixdata/user.json`
- `python manage.py loaddata fixdata/cart.json`
- `python manage.py loaddata fixdata/category.json`
- `python manage.py loaddata fixdata/invoice.json`
- `python manage.py loaddata fixdata/invoice_item.json`
