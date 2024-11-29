## Setup Instructions

### Prerequisites

Before starting the application, make sure you have the necessary Python packages listed in `requirements.txt`. You can install these dependencies using `pip`.

### Installation and Running the Server

1. **Install Required Packages**  
   Use the following command to install all necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI Server**  
   Run the server using Uvicorn with the following command:
   ```bash
   uvicorn main:app --reload
   ```

## Triggering the Scraper

Once the server is running, you can trigger the web scraper through a web browser by visiting the URL:

```
http://127.0.0.1:8000/scrape?token=atlys-mohit-fixed-token&limit=5&use_proxy=false
```

### URL Parameters

- **`token`**: Hard coded token value `atlys-mohit-fixed-token` is requeired. For simplicity to access from browser, token has to be added as query param only not in headers-Authentication.
- **`limit`**: Specifies the number of pages to be fetched. It can be any integer.
- **`use_proxy`**: A boolean parameter. If set to `true`, requests will be routed through a proxy server (note that free proxies may be slow).

Both parameters can be used simultaneously to adjust the scraper's behavior according to your needs. This aligns with the "condition 1 of the task."

## Application Behavior

### Debug Mode

The application's behavior differs based on whether it is operating in debug mode:

- **DEBUG = true**:
  - **Notifications**: No notifications will be triggered.
  - **Data Storage**: Scraped data will not be saved in the database but will be written to a local JSON file named `products.json`.

- **DEBUG = false**:
  - **Notifications**: Both WhatsApp and email notifications will be triggered if valid credentials are provided.
  - **Data Storage**: Products will be saved into an SQLite database by default. If configurations for other supported databases (PostgreSQL, MySQL, MariaDB, Oracle) are present in the environment variables, they will be used instead.
