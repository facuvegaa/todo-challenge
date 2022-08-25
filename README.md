# Invera ToDo-List Challenge (Python/Django Jr-SSr)
Technical test for Python Developer job.


## Run Locally

Clone the project.
```bash
git clone https://github.com/facuvegaa/todo-challenge.git
```

Go to the project directory.
```bash
cd todo-challenge/todo_app
```

Build images from the application and database.
```bash
docker-compose build
```

Run the generated images.
```bash
docker-compose up
```

CTRL+C to stop and run the migrations.
```bash
docker-compose run web python manage.py migrate
```

Run the tests.
```bash
docker-compose run web python manage.py test
```

Run the generated images again.
```bash
docker-compose up
```


## API Reference


#### Register a User

```http
  POST localhost:8000/user/register/
```

| Parameters | Type     |Example| Description                |
| :-------- | :------- | :------- | :------------------------- |
| `username` | `string` | "Facu" | **Required** |
| `name` | `string` | "Facundo" | **Required** |
| `email` | `sring` | "facu@test.com" | **Required** |
| `password` | `sring` | "123456" | **Required** |

Returns info of the new user.
```JSON
{
    "id": 1,
    "name": "Facundo",
    "email": "facu@test.com",
    "username": "Facu"
}
```

#### Log In with an existing user

```http
  POST localhost:8000/user/login/
```

| Parameters | Type     |Example| Description                |
| :-------- | :------- | :------- | :------------------------- |
| `email` | `sring` | "facu@test.com" | **Required** |
| `password` | `sring` | "123456" | **Required** |


Returns a JWT (located on the cookies) wich is necessary to access to access protected endpoints.

#### Log uot with a user

```http
  POST localhost:8000/user/logout/
```
Delte the JWT cookie 

#### Create a task

```http
  POST localhost:8000/create_task/
```

| Parameters | Type     |Example| Description                |
| :-------- | :------- | :------- | :------------------------- |
| `body` | `sring` | "test task" | **Required** |

Returns a response with information about the new task.
```JSON
{
    "id": 1,
    "body": "test task",
    "completed": false,
    "created_at": "2022-08-25T15:07:15.859535Z",
    "updated_at": "2022-08-25T15:07:15.859552Z",
    "user": 1
}
``` 

#### Get all tasks

```http
  GET localhost:8000/get_all_tasks/
```
Return all the existing tasks regardless of the user who created them.

#### Get a task by search

```http
  GET localhost:8000/get_task/$search={whatever}
```
Return all the existing tasks that match with the search (only with this fields: "body", "created_at", "updated_at" ).

#### Delete a task

```http
  DELETE localhost:8000/delete_task/{id}
```
Delete a task by id (only the user who created it can delete it).

#### Update a game

```http
  POST localhost:8000/update_task/{id}
```

| Parameters | Type     |Example| Description                |
| :-------- | :------- | :------- | :------------------------- |
| `body` | `string` | "updated task" | **Required**(actually only one of the two fields is required) |
| `completed` | `boolean` | "True" | **Required** (actually only one of the two fields is required)|

Update the task by id (only the user who created it can update it).
```JSON
{
    "id": 1,
    "body": "update task",
    "completed": true,
    "created_at": "2022-08-25T15:07:15.859535Z",
    "updated_at": "2022-08-25T15:16:04.672685Z",
    "user": 1
}
```

## Tech Stack

**Language:**
- Python

**Database:**
- PostgresSQL

**Others:**
- Docker Compose

  
## Author

- [@FacundoVega](https://github.com/facuvegaa)