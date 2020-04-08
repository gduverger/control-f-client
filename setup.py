import setuptools

with open('README.md', 'r') as fh:
	readme = fh.read()

setuptools.setup(
	name='ctrlf-python',
	version='0.1.2',
	author='Georges Duverger',
	author_email='georges.duverger@gmail.com',
	description='CTRL+F Python client',
	long_description=readme,
	long_description_content_type='text/markdown',
	url='https://github.com/gduverger/ctrlf-python',
	license='MIT',
	packages=['ctrlf'],
	# install_requires=[],
	python_requires='>=3',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Intended Audience :: Developers',
		'Natural Language :: English'
	],
)
