from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in salon_appointment/__init__.py
from salon_appointment import __version__ as version

setup(
	name="salon_appointment",
	version=version,
	description="Application for booking appointment",
	author="Aerele",
	author_email="rethikmaheswaran@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
