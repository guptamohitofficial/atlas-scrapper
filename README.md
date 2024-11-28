Run pip -r requirements.txt
Run uvicorn main:app --reload

After running the server use the given url in browser to trigger scrapper : `http://127.0.0.1:8000/scrape?token=atlys-mohit-fixed-token&limit=5&use_proxy=false`

`limit` can be any integer representing numbner of pages to be fetched
`use_proxy` is `true` then proxy request will use (free proxy is very slow)
both of these params can work otgether stating `condition 1 of the task`

If application is running in DEBUG = true mode then no notifications will be release, count will only be logged as info and no data will be saved in db but will be saved in products.json file.

If application is running in DEBUG = false, whatsapp and email notifications will be triggered if correct credentails are provided and products will be saved into sqlite db by default if other support DBs (postgresql, mysql, mariaDB, oracle) configs are not given in environment vars
