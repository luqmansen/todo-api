
# todo-api

Todo API

## Indices

* [Auth](#auth)

  * [Get Token](#1-get-token)

* [Category](#category)

  * [Create new category](#1-create-new-category)
  * [Get All Category](#2-get-all-category)

* [Note](#note)

  * [Create new notes](#1-create-new-notes)
  * [Delete Notes](#2-delete-notes)
  * [Get Note List](#3-get-note-list)
  * [Partial Update Note](#4-partial-update-note)
  * [Total Update Notes](#5-total-update-notes)

* [User](#user)

  * [Profile](#1-profile)
  * [Register](#2-register)


--------


## Auth
Auth related endpoints



### 1. Get Token



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{server-address}}/auth/token/
```



***Body:***

```js        
{
    "username": "testuser34",
    "password": "test"
}
```



***More example Requests/Responses:***


##### I. Example Request: Get Token (referesh and access)



***Body:***

```js        
{
    "username": "testuser34",
    "password": "test"
}
```



##### I. Example Response: Get Token (referesh and access)
```js
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwNTgyODY5MiwianRpIjoiZGEyMTM5MTEyZjc3NGViZGI2ZWNiN2ZkMDZkYzE2ZGEiLCJ1c2VyX2lkIjo3fQ.i_DHzgeF-oDwwtaS_r2eGrlCv3a5JsyHdFUFJhxaOQk",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA1NzQyMjkyLCJqdGkiOiJjNWE0YzQwYzk3YTM0MTk1YTIxNmQ5MGVjYzU5MThiMiIsInVzZXJfaWQiOjd9.r0EYXgcnHxdyxcO0voC8hWkH7E1tk1Pc1i_Ci1Hfo8I"
}
```


***Status Code:*** 200

<br>



## Category



### 1. Create new category


Create new category for personal user


***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{server-address}}/api/category/
```



***Body:***

```js        
{
    "name": "School"
}
```



***More example Requests/Responses:***


##### I. Example Request: Create new category



***Body:***

```js        
{
    "name": "School"
}
```



##### I. Example Response: Create new category
```js
{
    "id": 5,
    "name": "School"
}
```


***Status Code:*** 201

<br>



### 2. Get All Category



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{server-address}}/api/category/
```



***More example Requests/Responses:***


##### I. Example Request: Get All Category



##### I. Example Response: Get All Category
```js
[
    {
        "id": 1,
        "name": "School"
    },
    {
        "id": 2,
        "name": "Shopping List"
    },
    {
        "id": 3,
        "name": "jackpot"
    },
    {
        "id": 4,
        "name": "School"
    },
    {
        "id": 5,
        "name": "School"
    }
]
```


***Status Code:*** 200

<br>



## Note



### 1. Create new notes



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{server-address}}/api/notes/
```



***Body:***

```js        
{
    "deadline": "2020-11-17 14:04:34",
    "title": "Today's Note",
    "content": "Nothing really matters",
    "category": 1
}
```



***More example Requests/Responses:***


##### I. Example Request: Create new notes



***Body:***

```js        
{
    "deadline": "2020-11-17 14:04:34",
    "title": "Today's Note",
    "content": "Nothing really matters",
    "category": 1
}
```



##### I. Example Response: Create new notes
```js
{
    "id": 2,
    "is_complete": false,
    "created_at": "2020-11-17T14:35:26.082933Z",
    "updated_at": "2020-11-17T14:35:26.083036Z",
    "deadline": "2020-11-17T14:04:34Z",
    "title": "Today's Note",
    "content": "Nothing really matters",
    "category": 1
}
```


***Status Code:*** 201

<br>



### 2. Delete Notes



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: {{server-address}}/api/notes/3/
```



***More example Requests/Responses:***


##### I. Example Request: Delete Notes



***Status Code:*** 204

<br>



### 3. Get Note List



***Endpoint:***

```bash
Method: GET
Type: 
URL: {{server-address}}/api/notes
```



***More example Requests/Responses:***


##### I. Example Request: Get Note List



##### I. Example Response: Get Note List
```js
[
    {
        "id": 2,
        "is_complete": false,
        "created_at": "2020-11-17T14:35:26.082933Z",
        "updated_at": "2020-11-17T14:35:26.083036Z",
        "deadline": "2020-11-17T14:04:34Z",
        "title": "Today's Note",
        "content": "Nothing really matters",
        "category": 1
    }
]
```


***Status Code:*** 200

<br>



### 4. Partial Update Note


Only update specific field of note


***Endpoint:***

```bash
Method: PATCH
Type: RAW
URL: {{server-address}}/api/notes/4/
```



***Body:***

```js        
{
    "content": "Everything matters"
}
```



***More example Requests/Responses:***


##### I. Example Request: Partial Update Note



***Body:***

```js        
{
    "content": "Everything matters"
}
```



##### I. Example Response: Partial Update Note
```js
{
    "id": 2,
    "is_complete": false,
    "created_at": "2020-11-17T14:57:18.526410Z",
    "updated_at": "2020-11-17T14:57:18.526435Z",
    "deadline": "2020-11-17T14:04:34Z",
    "title": "Today's Note",
    "content": "Everything matters",
    "category": 1
}
```


***Status Code:*** 200

<br>



### 5. Total Update Notes


Change all content of a notes


***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: {{server-address}}/api/notes/3/
```



***Body:***

```js        
{
    "deadline": "2020-11-17 14:04:34",
    "title": "Yesterday's Note",
    "content": "Everything really matters",
    "category": 2
}
```



***More example Requests/Responses:***


##### I. Example Request: Total Update Notes



***Body:***

```js        
{
    "deadline": "2020-11-17 14:04:34",
    "title": "Yesterday's Note",
    "content": "Everything really matters",
    "category": 2
}
```



##### I. Example Response: Total Update Notes
```js
{
    "id": 2,
    "is_complete": false,
    "created_at": "2020-11-17T15:00:56.018808Z",
    "updated_at": "2020-11-17T15:00:56.018833Z",
    "deadline": "2020-11-17T14:04:34Z",
    "title": "Yesterday's Note",
    "content": "Everything really matters",
    "category": 2
}
```


***Status Code:*** 200

<br>



## User



### 1. Profile


Get user profile


***Endpoint:***

```bash
Method: GET
Type: 
URL: {{server-address}}/api/user/me/
```



***More example Requests/Responses:***


##### I. Example Request: Profile



##### I. Example Response: Profile
```js
{
    "username": "testuser34",
    "first_name": "test",
    "last_name": "user 4"
}
```


***Status Code:*** 200

<br>



##### II. Example Request: Get User Profile



##### II. Example Response: Get User Profile
```js
{
    "username": "testuser34",
    "first_name": "test",
    "last_name": "user 4"
}
```


***Status Code:*** 200

<br>



### 2. Register


Register new user


***Endpoint:***

```bash
Method: POST
Type: RAW
URL: {{server-address}}/api/user/register/
```



***Body:***

```js        
{
    "username": "testuser34",
    "password": "test",
    "first_name": "test",
    "last_name": "user 4"
}
```



***More example Requests/Responses:***


##### I. Example Request: Create Account Success



***Body:***

```js        
{
    "username": "testuser34",
    "password": "test",
    "first_name": "test",
    "last_name": "user 4"
}
```



##### I. Example Response: Create Account Success
```js
{
    "username": "testuser34",
    "first_name": "test",
    "last_name": "user 4"
}
```


***Status Code:*** 201

<br>



##### II. Example Request: Create Account Duplicate Username



***Body:***

```js        
{
    "username": "testuser",
    "password": "test",
    "first_name": "test",
    "last_name": "user"
}
```



##### II. Example Response: Create Account Duplicate Username
```js
{
    "username": [
        "A user with that username already exists."
    ]
}
```


***Status Code:*** 400

<br>



---
[Back to top](#todo-api)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2020-11-19 09:32:41 by [docgen](https://github.com/thedevsaddam/docgen)
