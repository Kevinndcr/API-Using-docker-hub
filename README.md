# API-Using-docker-hub
Docker para hacer push

Guia de postman
https://documenter.getpostman.com/view/141107/2sA3QtfBrw

Creando API y dockerfile (Importante estar logueado al notion)
https://file.notion.so/f/f/2264eef4-4879-4d64-8e82-33591c6270e3/286a24c3-9f21-448a-83a3-01f544f35a36/02_-_Install_Docker_environment.txt?id=bb40d47c-9ae2-4308-a79b-db6cc2446109&table=block&spaceId=2264eef4-4879-4d64-8e82-33591c6270e3&expirationTimestamp=1718323200000&signature=p0c06F40z9MYy92g48wCcvXV19EHuPp53yg6U87GNe0&downloadName=02+-+Install+Docker+environment.txt

-- Create image 
docker build -t *usuarioDockerHub*/apidemo01-image:v3 .	

-- Create image tag to use in Docker Hub
docker tag *usuarioDockerHub*/apidemo01-image:v3 *usuarioDockerHub*/apidemo01-image


-- Upload image to Docker Hub
docker push *usuarioDockerHub*/apidemo01-image

	 
-- Create container with image
docker run --name api_demo_01 -p 5001:5001 -d *usuarioDockerHub*/apidemo01-image

