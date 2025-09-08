## How activate python venv

```sh
python -m venv <environmentName>
<environtmentName>\Scripts\activate
```

or 

Then select in [Visual Studio Code]:

`>Python select interpreter <environmentName>` 

Close and reopen a terminal in [Visual Studio Code]. The virtual environtment will be activated.

Finally install the modules:

   ```sh
   <environtmentName>pip install fastapi uvicorn motor
   ```
   
[//]: # (These are reference links used in the body this note)

   [Visual Studio Code]: <https://code.visualstudio.com/>