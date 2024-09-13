
# **Gender-based Occupation Analysis in Chile: Impact of the COVID-19 Pandemic**

This project presents an in-depth analysis of gender-based occupation differences in Chile, focusing on the effects caused by the COVID-19 pandemic. The study integrates data analysis in **R** and **Python**, utilizing geographical visualizations and maps to illustrate the impact across regions. The work aims to highlight the disparities between male and female employment throughout the country, offering insights into the socioeconomic consequences of the pandemic.

## **Project Structure**

- **R Analysis**: The main analytical portion of this project, conducted in R, examines datasets that detail occupation rates over time. Key insights focus on identifying patterns in occupation across age, gender, and geography.  
    - **Files**: 
      - `Ocupación_Chile_Caso_Estudio/`
      - `R_results/`

- **Python Visualizations**: Geographical maps were created using Python to visually represent the data. The maps display occupation disparities across regions of Chile, providing a clear view of the spatial distribution of these effects.  
    - **Files**:
      - `Dash_Map/`
      - `Graphic_map.ipynb`

- **Geospatial Data**: The project uses shapefiles and GeoJSON files to map out regions in Chile for occupation visualization.  
    - **Files**:
      - `Shape_file/`
      - `Geojson/`

- **Map Results**: The final results of the mapping process are stored in the `Map_results/` folder.

- **Images**: The prints of the charts and map created are stored in the `Prints/` folder.

To explore the code and replicate the analysis:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/Chile-Occupation-Analysis.git
    ```

2. **For Python**: 
   - Install required Python libraries using the `requirements.txt` file.
   - Use **Jupyter Notebook** to open and run `Graphic_map.ipynb`.
     ```bash
     jupyter notebook Graphic_map.ipynb
     ```

3. **For R**:
   - Install the necessary R packages by running:
     ```r
     install.packages("needed_package")
     ```
   - Open and run the R scripts using **RCloud** or **RStudio**.

## **Technologies Used**

- **R**: Data cleaning, analysis, and statistical evaluation.
- **Python**: Visualization and geospatial mapping.
- **GeoJSON** and **Shapefiles**: To map the Chilean regions.

## **Contributing**

Contributions to this project are welcome. Please fork the repository and submit pull requests.
