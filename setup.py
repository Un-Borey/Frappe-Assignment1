from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in online_course_management/__init__.py
from online_course_management import __version__ as version

setup(
	name="online_course_management",
	version=version,
	description="Online Course Management System",
	author="rey",
	author_email="rey@flexiblesolution.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
