Fast API is based on types intro, so we need to use them so that our classes and attibutes can access all of the methods used by the created class. Thats why we use the entities, so that we can organize our code in a way that its useful afterwards.

# REQUESTS: 
When making requests, the function bellow if the `@something` is interpreted in fast api as:  "the function thats in charge of handling requests that go to : "the path "" and using a verb operator. 


example : 

```python 

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```

That @something syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get.

It is the "path operation decorator".

The function bellow the decoratior will be called whenever it receives the request of the specified URL, using the verb operation.

For the requests - Really usefull in the use case part: 
Import FastAPI.
Create an app instance.
Write a path operation decorator using decorators like @app.get("/").
Define a path operation function; for example, def root(): ....
Run the development server using the command fastapi dev.


DTO: Define como os dados entram e saem do banco de dados
Modelo: Define como os dados são salvos.


Mongo db : 
Is a document db 
A document db is composed of field and value pairs. its similar to json objects
It stores documents in collectons, they are analogous as tables in relational db


In pydantic, data validation framework, when we use a underscore _ in a variable, it understands that is private, thus, unmutable


Mongo because its not a relational type, it can have diferent columns in each table, that its in fact, a collection, so thats the big difference.


Repository : 
The repository is used to search, update, delete and save informations in the database, not using 
Basically, the repository, will apply their methods, to get the information about certain object. With that, we can use the loaded data from de db, and use it in the models, just for simplifying it. 


Use case: 
The purpose of the use case is : 
Manage scope
Establish requirements
Outline the ways a user will interact with the system 
Visualize system architecture
Communicate technical requirements to business stakeholders
Risk management

for querering purpouses, we are using the mongoengine db. It makes sense because its whats gonna manage the database and python.

usamos o requirements para acessar o models, que é o banco de dados e pegar as informações que queremos.


In the use case, we inherit the repository from the class that we are making the use case to. Thats wise because than, we can use all methods without imports and all.


## ENTENDER O MOTIVO DE COOKIES



# RODAR:

- env\Scripts\Activate.ps1

-  fastapi dev src/app.py