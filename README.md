# Deploy
Clone repository
```sh
git clone https://github.com/i-korolkevich/x-lab-test-task.git
```
Set up environment
```sh
cp .env.example .env
```
Create network and run application
```sh
docker network create x-lab-test-task && docker-compose up -d
```
# Testing
```sh
docker-compose exec x-lab-test-task-web pytest application/tests/
```