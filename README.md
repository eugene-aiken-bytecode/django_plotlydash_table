##Looker DataTable Dashboard

### Purpose:

-   Looker is a powerful BI tool and data modeling engine that allows users to model data directly from their data warehouse and visualize it in reports and dashboards.

-   One drawback of Looker is it has a limit of only being able to display 5000 rows of data at any one time. This is fine in many cases because when creating a visualization, Looker is aggregating the rows to create the visualizations.

-   But in the case of someone wanting a table visualization that displays more than 5000 rows, they will have to download the data to a .csv file and view it that way. This I feel ruins the entire dashboarding experience that makes Looker so great to use. But fear not, I have a solution.

### The Solution:

-   Looker has an API that will allow many scripting languages to connect to your Looker instance and execute a query based on having the query slug from the explore or the actual query ID itself. This will return the query from the explore you have constructed in Looker in a format such as a .csv or a JSON file.

-   So utilizing the Python scripting language, the Django web application framework, and a DataTable visualization from Plotly Dash, I am going to construct a web application that will be containerized in a Docker file and hosted on Google App Engine.

-   When the user inputs the query slug for their desired query, the application will return a rendered Data Table with the data from their query and provided a better dashboard experience than one would get by parsing a .csv file

##This project is still under construction. Please check back for updates!
