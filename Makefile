run:
	. .venv/bin/activate; gunicorn -b 0.0.0.0:5000 app:app 

run-dev:
	flask run

clean:
	@find . -name "*.pyc" -exec rm -f '{}' +
	@find . -name "*~" -exec rm -f '{}' +
	@echo "Done!"

create-env:
	  test -d .venv || python3 -m venv .venv
	. .venv/bin/activate; pip install -Ur requirements.txt
	
# docker specific commands
docker-build:
	@docker build -t verloop-fde .

docker-run:
	@docker run -d -p 5000:5000 --name verloop-fde verloop-fde

docker-stop:
	@docker container stop verloop-fde

docker-clean:
	@docker image rm -f verloop-fde