Purpose of the script
  This script downloads, processes, and visualizes global population density on an interactive 3D globe using Plotly. It first checks for and downloads a world countries shapefile from Natural Earth if it is not already available, then extracts and loads the data using GeoPandas. 
  The script calculates each country's area and population density, applying a log transformation to handle extreme variations. The data is then converted into GeoJSON format for compatibility with Plotly. Finally, it generates a rotatable, interactive 3D globe where countries are color-coded based on their population density, providing an engaging and intuitive way to explore global demographic patterns.


Steps followed
1. A new directory was created in my repository with a file named "globe.py."
2. Manually installed all the required packages using "pip install."
3. Generated a full requirements file(all_requirements.txt) and used pipreqs to determine the minimal required dependencies.
4. Removed all installed packages to simulate a clean environment
5. Reinstalled from requirement.txt(the minimal required dependencies).
6. Verified script works
7. Analyzed dependencies with pipdeptree


Output of pipdeptree
<img width="1198" alt="image" src="https://github.com/user-attachments/assets/9147d308-278e-4a59-8f75-e3f9e98b0d55" />
