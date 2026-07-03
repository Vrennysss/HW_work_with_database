#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    import os, sys
    import django
    from django.conf import settings

    if __name__ == "__main__":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
        django.setup()

        db = settings.DATABASES['default']
        for key in ['HOST', 'PORT', 'NAME', 'USER', 'PASSWORD']:
            val = db.get(key)
            print(f"{key}: repr={repr(val)}, type={type(val)}")

        # Проверяем также известную переменную DATABASE_URL
        db_url = os.environ.get('DATABASE_URL')
        if db_url:
            print(f"DATABASE_URL: repr={repr(db_url)}, type={type(db_url)}")

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
    execute_from_command_line(sys.argv)
