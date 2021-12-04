#!/usr/bin/env bash

case $1 in
    docker)
        case $2 in
            up)
                docker-compose up -d
            ;;
            start)
                docker-compose start
            ;;
            stop)
                docker-compose stop
            ;;
            restart)
                docker-compose stop
                docker-compose start
            ;;
            create)
                docker-compose down
                docker-compose build
                docker-compose up -d --force-recreate
            ;;
            stats)
                docker ps -q | xargs  docker stats --no-stream
            ;;
        esac
    ;;
    log)
        docker-compose logs -f server
    ;;
    ssh)
        docker-compose exec app /bin/bash
    esac
    