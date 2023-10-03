SHELL := /bin/bash

serve:
	uvicorn app:application --host 0.0.0.0 --reload
