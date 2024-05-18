Welcome to the Coffee Discovery Dashboard project! This interactive dashboard allows users to explore a collection of coffee beans, brewing methods, and tasting notes. Users can embark on a journey of discovery by selecting different paths, such as by manufacturer, brewing method, or country of origin.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Running the App Locally](#running-the-app-locally)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Explore coffee beans by manufacturer, brewing method, or country of origin.
- View detailed information about each bean, including origin, roast level, manufacturer, process, variety, elevation, and more.
- Discover different brewing methods used for each bean.
- Access tasting notes for specific bean and brewing method combinations.
- Interactive and visually appealing dashboard built with Streamlit.

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Streamlit](https://streamlit.io/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/coffee-discovery-dashboard.git
   cd coffee-discovery-dashboard
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

1. Ensure you have MySQL installed. If not, download and install it from [MySQL Downloads](https://dev.mysql.com/downloads/).

2. Create a new database:

   ```sql
   CREATE DATABASE coffee_dashboard;
   ```

3. Use the database:

   ```sql
   USE coffee_dashboard;
   ```

4. Create the necessary tables:

   ```sql
   -- Creating the 'beans' table
   CREATE TABLE beans (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       origin VARCHAR(255),
       roast_level VARCHAR(255),
       manufacturer VARCHAR(255),
       process VARCHAR(255),
       variety VARCHAR(255),
       elevation VARCHAR(255),
       manufacturer_website VARCHAR(255),
       price_per_lb DECIMAL(10, 2)
   );

   -- Creating the 'equipment' table
   CREATE TABLE equipment (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       type VARCHAR(255),
       manufacturer VARCHAR(255)
   );

   -- Creating the 'brewing_details' table
   CREATE TABLE brewing_details (
       id INT AUTO_INCREMENT PRIMARY KEY,
       equipment_id INT,
       bean_id INT,
       grind_size VARCHAR(255),
       brew_time VARCHAR(255),
       temperature VARCHAR(255),
       notes TEXT,
       FOREIGN KEY (equipment_id) REFERENCES equipment (id),
       FOREIGN KEY (bean_id) REFERENCES beans (id)
   );

   -- Creating the 'tasting_notes' table
   CREATE TABLE tasting_notes (
       id INT AUTO_INCREMENT PRIMARY KEY,
       bean_id INT,
       brewing_detail_id INT,
       date DATE,
       aroma VARCHAR(255),
       body VARCHAR(255),
       flavor_profile TEXT,
       rating INT,
       notes TEXT,
       FOREIGN KEY (bean_id) REFERENCES beans (id),
       FOREIGN KEY (brewing_detail_id) REFERENCES brewing_details (id)
   );
   ```

5. Insert sample data if needed for testing:

   ```sql
   -- Sample data insertion
   INSERT INTO beans (name, origin, roast_level, manufacturer, process, variety, elevation, manufacturer_website, price_per_lb)
   VALUES ('Ecuador Hacienda La Papaya Oak Barrel Anaerobic', 'Ecuador', 'Medium', 'ONYX Coffee Lab', 'Anaerobic', 'Typica', '1650 MASL', 'https://onyxcoffeelab.com/products/ecuador-hacienda-la-papaya-oak-barrel-anaerobic?variant=40870424772706', 64.00);
   ```

### Running the App Locally

1. Set up the database configuration using Streamlit's secrets management:

   - Create a `.streamlit` directory in the root of your project:

     ```bash
     mkdir .streamlit
     ```

   - Create a `secrets.toml` file inside the `.streamlit` directory and add your database credentials:

     ```toml
     [db_credentials]
     host = "your_host"
     user = "your_user"
     password = "your_password"
     database = "your_database"
     ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Deployment

To deploy the app to Streamlit's servers:

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub repository.
3. Set up secrets in Streamlit Cloud's settings with your database credentials.
4. Deploy the app and access it through the provided URL.

## Usage

- Select a path to start your coffee discovery journey (by manufacturer, brewing method, or country of origin).
- Explore detailed information about each coffee bean.
- Discover different brewing methods and view tasting notes.
- Enjoy the interactive and visually appealing dashboard.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature-branch\`).
3. Make your changes and commit them (\`git commit -m 'Add new feature'\`).
4. Push to the branch (\`git push origin feature-branch\`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out:

- [jason](mailto:jason@33sticks.com)
- [Project Repository](https://github.com/33sticks/coffee-notebook/)


