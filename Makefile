.PHONY: build up down logs restart clean jupyter

# Build all Docker images
build:
	docker compose build

# Start all services
up:
	docker compose up -d

# Start all services with build
up-build:
	docker compose up -d --build

# Stop all services
down:
	docker compose down

# View logs for all services
logs:
	docker compose logs -f

# View logs for a specific service
logs-%:
	docker compose logs -f $*

# Restart all services
restart:
	docker compose restart

# Remove all containers, images, and volumes
clean:
	docker compose down --rmi all --volumes --remove-orphans

# Run only the Jupyter notebook server
jupyter:
	docker compose up -d jupyter

# Run only the Streamlit apps
apps:
	docker compose up -d call-log-analysis covid-data-analysis bank-deposit-analysis

# Check service health
status:
	docker compose ps
