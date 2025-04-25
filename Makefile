# Makefile for managing legacy-bot and ai-brain
.PHONY: up down build rebuild logs restart ps health dev

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

rebuild:
	docker-compose down
	docker-compose build
	docker-compose up

logs:
	docker-compose logs -f

restart:
	docker-compose down
	docker-compose up

ps:
	docker-compose ps


health:
	@echo "Checking legacy-bot (port 5000)..."
	@until curl --silent --fail http://localhost:5000/health; do \
		echo "Waiting for legacy-bot..."; \
		sleep 2; \
	done
	@echo "✔ legacy-bot is up!"
	@echo ""

	@echo "Checking ai-brain (port 8000)..."
	@until curl --silent --fail http://localhost:8000/health; do \
		echo "Waiting for ai-brain..."; \
		sleep 2; \
	done
	@echo "✔ ai-brain is up!"

	@echo "Opening Swaggers UI in your browser..."
	@$(MAKE) open

# Health but I write it wrong almost every time
h:
	$(MAKE) health

open:
	vivaldi --new-tab http://localhost:5000/apidocs
	vivaldi --new-tab http://localhost:8000/apidocs

dev:
	@$(MAKE) up &
	@$(MAKE) h
