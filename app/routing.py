import os
import pkgutil
import logging
from importlib import import_module
from fastapi import APIRouter


# Initialize main router
main_router = APIRouter()

# Get project dir
project_dir = os.path.dirname(__file__)

# Get API routers
for (_, pkg_name, _) in pkgutil.iter_modules([f'{project_dir}/api']):

    print(pkg_name)

    prev_modules = []
    for module in os.listdir(f'{project_dir}/api/{pkg_name}'):
        if module.startswith('__'):  # ignore __init__.py and __pycache__
            continue

        module = module.split(".")[0]  # remove extension .py/.pyc

        if module in prev_modules:
            continue

        # Get api module
        api = import_module(
            f'.{pkg_name}.{module}', package='app.api')

        # Add api router to main router
        main_router.include_router(api.router)

        prev_modules.append(module)

        logging.info(f'Register "{module}" api')
