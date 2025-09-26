Anime Review Website
--------------------

  A Django-based web application where users can explore anime details such as title, description, ratings, and images. Anime data is stored in JSON files and dynamically loaded into pages using JavaScript. 
  The project is lightweight, modular, and designed for easy extension.

Features
--------

  -> Anime details (title, description, rating, images) fetched from JSON files
  -> Dynamic anime detail pages using query parameters (e.g., ?id=naruto)
  -> Light and Dark mode toggle with persistence using localStorage
  -> Responsive design with navigation bar and logo
  -> Easily extendable — simply add new anime JSON files and images

Project Structure
-----------------


  myproject/
  
  │── myapp/
  
  │   ├── static/
  
  │   │   ├── myapp/
  
  │   │   │   ├── Data/                # Anime JSON files
  
  │   │   │   ├── images/              # Anime images
  
  │   │   │   ├── js/
  
  │   │   │   │   └── anime-page.js    # Fetch and render anime details
  
  │   │   │   └── css/
  
  │   │   │       └── style.css        # Styling (Light/Dark mode)
  
  │   ├── templates/
  
  │   │   └── anime-page.html          # Anime detail page template
  
  │   └── views.py                     # Django views
  
  │
  
  ├── db.sqlite3
  
  ├── manage.py
  
  └── README.md

Data Source
-----------

  -> Currently, anime data is served from static JSON files located in
     static/myapp/Data/.
  -> The project is also connected to MongoDB, but JSON is the active data source.
  -> Future versions will fetch anime data directly from MongoDB collections.

Getting Started
---------------

  1. Clone the repository:
  
      git clone https://github.com/your-username/anime-review-website.git
      cd anime-review-website
  
  2. Create a virtual environment and install dependencies:
  
      python -m venv env
      source env/bin/activate   # On Linux/Mac
      env\Scripts\activate      # On Windows
  
      pip install -r requirements.txt
  
  3. Run the Django development server:
  
      python manage.py runserver
  
  4. Access the project in your browser:
  
      http://127.0.0.1:8000/anime-page/?id=naruto

Tech Stack
----------

  -> Frontend: HTML, CSS, JavaScript
  -> Backend: Django
  -> Data Storage: JSON files (static)
  -> Styling: Custom CSS with theme toggle

Screenshots
-----------

(screenshots of site here.)

Future Improvements
-------------------

  -> Implement search and filter functionality
  -> Replace JSON with PostgreSQL or MongoDB as the primary data store
  -> Add user authentication (login, reviews, rating system)
  -> Create an anime listing/browsing page

Contributing
------------

  Contributions are welcome. For major changes, please open an issue first to discuss what you would like to implement.

