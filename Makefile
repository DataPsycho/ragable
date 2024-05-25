docker_build:
	docker build -t ragable:latest .

docker_run:
	docker run -p 7860:7860 ragable:latest