# TodoMVC - Backbone.js + Django

## Description

Create a REST API for use with the Backbone.js TodoMVC app.

## Objectives

After completing this assignment, you should be able to:

* Summarize the REST architecture.
* Use Django Rest Framework to create an api

### Deliverables

* A Git repo called todomvc-django containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a Django project

### Requirements  

* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Using the Django REST Framework, build an API with one resource: `todos`.

Your URLs should be nested under `/api/`, and will look like:

* GET `/api/todos/`
* POST `/api/todos/`
* PUT `/api/todos/{id}`
* DELETE `/api/todos/{id}`

The todo resource should have the following fields:

* id
* title - string, required
* completed - boolean, default false
* order - integer, not required, can be null

## Hard Mode

For hard mode, do everything shown above, plus add functional tests for your API.
