# Django Project README

## Installation

### Prerequisites

- Python 3.9+
- Django 3.x or 4.x
- Virtualenv

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/CapitanGrant/django_pet.git
    cd django_pet
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```
