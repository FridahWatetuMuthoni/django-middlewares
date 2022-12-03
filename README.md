# django-middlewares

## Middleware Meaning and Description

Middleware is  framework of hooks into Django's request/ response processing.It is a light, low-level plugin system globally altering django's input and output

Client => HTTP Request => Web Server => URL match =>View Processing Database => Template
Template => URL match =>View processing => Database

Client =>Webserver=> Middleware=> View processing=> Database=>Template
Template => Viewprocessing=>middleware=>client
Examples of middlewares:
    1. Security middleware
    2. Session middleware
    3.common middleware
We can create middlewares that respond to request or before responses

During requests the middleware go from top to bottom
During response the middlewares go from bottom to top
