import setuptools

with open('README.md', 'r') as fh:
	readme = fh.read()

setuptools.setup(
	name='control-f',
	version='0.1.5',
	author='Georges Duverger',
	author_email='georges.duverger@gmail.com',
	description='Control-F Python client',
	long_description=readme,
	long_description_content_type='text/markdown',
	url='https://github.com/gduverger/control-f-client',
	license='MIT',
	packages=['control_f'],
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
