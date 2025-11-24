#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_crud.settings')
    try:
        import importlib
        # Import at runtime to avoid static analysis/import-resolution errors in editors/environments
        django_management = importlib.import_module('django.core.management')
        execute_from_command_line = django_management.execute_from_command_line  # type: ignore
    except ImportError:
        # If Django isn't available, provide a clear message and exit when executed.
        def execute_from_command_line(argv):
            sys.stderr.write(
                "Django is not installed in this environment. Install Django or activate your virtualenv.\n"
            )
            sys.exit(1)
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
