# Set the name of your package
PACKAGE_NAME = drf_queryset_optimization

.PHONY: deploy check-deploy publish clean

deploy:
	@echo "Deploying to PyPI..."
	@python setup.py sdist bdist_wheel

check-deploy:
	@twine check dist/*

publish:
	@twine upload dist/*
	@rm -rf build dist $(PACKAGE_NAME).egg-info

clean:
	@echo "Cleaning up..."
	@rm -rf build dist $(PACKAGE_NAME).egg-info
	@ls -l
