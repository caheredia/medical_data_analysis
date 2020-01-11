test:
	python -m pytest tests/
notebook:
	jupyter nbconvert --to notebook --execute --inplace data_exploration.ipynb
