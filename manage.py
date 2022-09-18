#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
'''
 18개의 적용되지 않은 migration들이 있다는 문구가 보인다. 
 admin, auth, contenttypes, sessions 앱들과 관련된 내용이고 
 이것을 적용하려면 python manage.py migrate 를 실행해야 한다고 나와 있다. 
 admin, auth, contenttypes, sessions 앱들은 장고 프로젝트 생성시 기본적으로 설치되는 앱들이다.


시작 명령어!
mysite
python manage.py runserver


'''
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
