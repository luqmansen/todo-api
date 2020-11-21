# chems-todo-api
This is chems's todo API. Chems wants to be organized.

## Live Demo
https://api-todo-srv.herokuapp.com/

## Requirements
- Python 3.8+ (3.6+ might work, but idk, never tested)
- Docker compose
- Make (if you want to use the Makefile, else run the command manually)


## Development Setup
1. Create .env files in project's root directory
    ```
    SECRET_KEY=<ur secret stuff>
    CLEARDB_DATABASE_URL='mysql://root:password@0.0.0.0:3306/db' # setup your own creds
    ENV=DEV
    ```
2. Run! 
    ```
    make db 
    make migrate
    make dev
    ```

## Docs
- Read the [Swagger](http://api-todo-srv.herokuapp.com/swagger/) here
- or [Redoc](http://api-todo-srv.herokuapp.com/redoc/) here
- or [Github docs](docs/docs.md) here (perhaps outdated)
- or [Postman docs](https://documenter.getpostman.com/view/8693382/TVeqe7eP) here (perhaps outdated)