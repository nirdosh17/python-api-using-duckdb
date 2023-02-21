build:
	pip3 install -r requirements.txt

run: build
	python3 server.py

docker.build:
	./build_image.sh

docker.run:
	docker run --rm -it --name python-api -p 8080:8080 python-api:latest
