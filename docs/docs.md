
# todo-api

Todo API

## Indices

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

  * [profile](#1-profile)


--------


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
URL: {{server-address}}/api/notes/2/
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
URL: {{server-address}}/api/notes/2/
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
URL: {{server-address}}/api/notes/2/
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



### 1. profile


Get user profile


***Endpoint:***

```bash
Method: GET
Type: 
URL: http://0.0.0.0:9999/api/user/
```



---
[Back to top](#todo-api)
> Made with &#9829; by [thedevsaddam](https://github.com/thedevsaddam) | Generated at: 2020-11-17 22:02:55 by [docgen](https://github.com/thedevsaddam/docgen)
