# Deploy
1) clone repository
2) git checkout dev
3) cp .env.example .env
4) docker network create x-lab-test-task && docker-compose up -d

# Testing
1) docker-compose exec x-lab-test-task-web pytest application/tests/
