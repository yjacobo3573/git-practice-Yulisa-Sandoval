# **Global Population Density Visualization Script**

## **Purpose of the Script**
This script downloads, processes, and visualizes global population density on an interactive 3D globe using Plotly. It follows these key steps:

- Checks for and downloads a world countries shapefile from Natural Earth if it is not already available.
- Extracts and loads geographic data using GeoPandas.
- Calculates each country's area and population density, applying a log transformation to handle extreme variations.
- Converts the processed data into GeoJSON format for compatibility with Plotly.
- Generates a rotatable, interactive 3D globe where countries are color-coded based on population density.
  
This visualization provides an engaging and intuitive way to explore global demographic patterns.


---

## **Steps followed**
1. A new directory was created in my repository with a file named "globe.py."
2. Manually installed all the required packages using "pip install."
3. Generated a full requirements file(all_requirements.txt) and used pipreqs to determine the minimal required dependencies.
4. Removed all installed packages to simulate a clean environment
5. Reinstalled from requirement.txt(the minimal required dependencies).
6. Verified script works
7. Analyzed dependencies with pipdeptree

---

## **Output of pipdeptree**
<img width="1198" alt="image" src="https://github.com/user-attachments/assets/9147d308-278e-4a59-8f75-e3f9e98b0d55" />

---

## **Observations or issues**
Throughout this assignment, I encountered several challenges, particularly with getting the "pipreqs . --force" command to work. I later discovered that I hadn't properly set up my virtual environment, causing the terminal to reference the wrong directory. Many of the issues I faced stemmed from my lack of experience, but I'm grateful that this assignment helped me strengthen my understanding in this area.
