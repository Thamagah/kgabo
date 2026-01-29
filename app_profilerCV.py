import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(page_title="Kgabo Humphrey Thamaga - CV", page_icon="📄", layout="wide")

# Title and Header
st.title("Kgabo Humphrey Thamaga")
st.subheader("Geospatial & Earth Observation Expert | Researcher")

# Contact Information
st.markdown('<h3 style="color: #000000;">Contact Information</h3>', unsafe_allow_html=True)
#st.markdown("### Contact Information")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Email:** thamakh@unisa.ac.za")  
with col2:
    st.write("**Phone:** +27 78 408 0205")  
with col3:
    st.write("**Location:** Gauteng, South Africa")  

# Professional Summary
st.markdown('<h3 style="color: #000000;">Professional Summary</h3>', unsafe_allow_html=True)
#st.markdown("### Professional Summary")
st.write("""
Passionate geospatial technologist.
""")

# Education
st.markdown('<h3 style="color: #000000;">Education</h3>', unsafe_allow_html=True)
#st.markdown("### Education")
st.write("""
- **Doctor of Philosophy in Environmental & Water Science**  
  University of the Western Cape, (2019 - 2021)  
  Thesis: Impacts of land use land cover change on wetland productivity and hydrological systems in the Limpopo Transboundary River Basin, South Africa. 

- **Master of Science in Geography**  
  University of Limpopo, (2018)  
  Thesis: emote sensing of the spatio-temporal distribution of invasive water hyacinth (Eicchornia crassipes) in the Greater Letaba River system in Tzaneen, South Africa.  

- **Bachelor of Science in Environmental & Resource Studies**  
  University of Limpopo (2013 - 2016)  
  Modules:Human geography, Environmental management, GIS & Remote sensing, Applied Ecology, Economic geography, Statistics, Demography, Cartography, Natural resources management, Tourism, Sustainable resource development (water-energy-food nexus), Waste management.
  **Honours project**: GIS-based groundwater quality assessment in Polokwane local municipality, Limpopo Province of South Africa

""")

# Professional Experience
st.markdown('<h3 style="color: #000000;">Professional experience</h3>', unsafe_allow_html=True)
#st.markdown("### Professional Experience")
st.write("""

- **University of South Africa | Geographical information Systems S. Lecturer | 01 May 2025**
- **University of Fort Hare | GIS & Remote Sensing Lecturer | 01 January 2023 to 30 April 2025**
- **ENVIRO AI | Environmental Management Officer | 01 November 2021 to 31 November 2022**
- **EPF Tech Hub | Geospatial analyst and researcher | 01 July 2019 to 31 October 2021**
- **Kumari Solutions | Waste Management Officer (Intern) | 01 January 2019 - 30 June 2019**
- **University of Limpopo | GIS & Remote Sensing Lecturer (Assistant) | 01 July 2018 – 31 December 2018**


""")

# Skills
st.markdown('<h3 style="color: #000000;">Skills</h3>', unsafe_allow_html=True)
#st.markdown("### Skills")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    - Cloud computing - python
    - Machine Learning Applications
    - Geospatial analysis
    - Modelling and Simulations
    """)
with col2:
    st.write("""
    - Data analysis (Big data - Geospatial data)
    - UAV data processing
    - Research skills
    """)

# Certifications and Achievements
st.markdown('<h3 style="color: #000000;">Certification and Achievements</h3>', unsafe_allow_html=True)
#st.markdown("### Certifications")
st.write("""
- Certified UAV
- Certified Synthetic Apperture Radar

""")

# Grants
st.markdown("### Grants")
st.write("""
- The development and application of a SuperCeasar model for hydro-geomorphic modelling to support reliable prediction of flooding and subsequent erosion. Water Research Commission (WRC). R 2 495 000 [2025 – 2027]
- Predictive Modeling of Water Availability Dynamics in Southern Africa: A Data-Driven Approach for Sustainable Water Resource Management. Water Research Commission (WRC). R 1 500 000.00. [2025 – 2027]
- Integrating Innovative Nature based solutions for resilient Aquatic Ecosystems [INNAQUE]. RASMUS-EDU-2025-CBHE-STRAND-2. Erasmus +. Amount: € 88,598.00 (R 1 815 491,51) [2025 – 2027]. 
- Bathymetric of reservoirs in Southern Africa. NRF. R2 200 000.00. [2023 – 2026]
- Evaluation of remote sensing as a multidisciplinary approach for wetland monitoring, Eastern Cape. NRF Thuthuka. Amount: R 260 000.00. [2024 – 2026].
- Monitoring the spatio-temporal dynamics of wetland ecosystems using remotely sensed datasets in semi-arid regions. Govan Mbeki Research and Development Centre. Amount: R 120 000.00 [2023 - 2024].
- Exploring aquatic weed coexistence using multi-source satellite data for informed aquatic weed management for inland waterbodies. [EXPO-AQUA], EO Africa and Facility. Amount: € 23 000.00. (R 481 101.93) [2023 – 2024].
- Towards daily maps of water hyacinth cover: exploiting synergies between Sentinel-2 and 3. EO Africa and Facility. Amount: € 24 700.00 (R 516 661.64) [2022 – 2023].
- MAPinAQUA - MAPping, monitoring, and assessment of invasive AQUAtic plants in Europe and Africa for a better understanding of ecosystem (dis)services. Collaborating countries: France, Romania, Finland, Poland, Portugal, and South Africa. [2024 – 2029] (outcomes pending)

""")

# Languages
st.markdown('<h3 style="color: #000000;">Languages</h3>', unsafe_allow_html=True)
#st.markdown("### Languages")
st.write("""
- English: Fluent
- Sepedi: Fluent
- Other Language: Proficient
""")

# Publications
st.markdown('<h3 style="color: #000000;">Publications</h3>', unsafe_allow_html=True)
#st.markdown("### Publications")
st.write("""
- Tshanga, M., Ncube, L. & Thamaga, K.H. (2026). Geological mapping of copper deposits in the Democratic Republic of Congo through Remote Sensing data and machine learning. Remote Sensing.
- Kgapiyana, B.C., Mndela, M. & Thamaga, K.H. (2025). Shrub invasion drives herbaceous vegetation degradation in semi-arid rangelands of the Eastern Cape Province of South Africa. 
- Matsane W., Mothapo, C.M., Dhau, I. & Thamaga, K.H. (2025). Modelling the Potential Distribution of African Wormwood (Artemisia afra) using Machine Learning algorithm-based approach (MaxEnt) in Sekhukhune District, South Africa. Ecology and Evolution. https://doi.org/10.1002/ece3.71866. 
- Mani, A.; Badola, R., Kumari, M., Mishra, V.N., Thamaga, K.H., Hasher, F.F.B., Zhran, M. (2025). Watershed Prioritization with Respect to Flood Susceptibility in the Indian Himalayan Region (IHR) Using Geospatial Techniques for Sustainable Water Resource Management. Water, 17:2039. https://doi.org/10.3390/w17132039. 
- Adesola, G.O., Gwavava, O., Pharoe, B.K., Baiyegunhi, C., Thamaga, K.H., Muavhi, N. (2025). Appraising the Accuracy of GIS-Based Bivariate Statistical Model for Groundwater Potential Mapping in South Africa. Heliyon, https://doi.org/10.1016/j.heliyon.2025.e43411. 
- Thamaga, K.H., Dube, T., Shoko, C. & Mndela M. (2024). Modeling wetland vegetation diversity and aboveground productivity using Sentinel-2 MSI data in South Africa. Journal of Environmental Management. MN: JEMA-D-24-09118. [Manuscript under-review].
- Ndou, N., Nontongana, N., Thamaga, K.H. & Afuye, G.A. (2024). Uncertainty Evaluation and Compensation for Reservoir’s Bathymetric Patterns Predicted with Radial Basis Function Approaches Based on Conventionally Acquired Water Depth Data. Water, 16, 3052. https://doi.org/10.3390/w16213052. 
- Slayi, M., Zhou, L. & Thamaga, K.H. (2024). Land Degradation in Southern Africa: Restoration Strategies, Grazing Management, and Livelihoods. Agriculture, 14, 1849. https://doi.org/10.3390/ agriculture14101849.  
- Slayi, M., Zhou, L., Thamaga, K.H. & Nyambo, P. (2024). The Role of Social Inclusion in Restoring Communal Rangelands in Southern Africa: A Systematic Review of Approaches, Challenges, and Outcomes. Land, 13, 1521. https://doi.org/10.3390/land13091521. 
- Afuye, A.A., Kalumba, A.M., Owalabi, S.T., Thamaga, K.H., Ndou, N., Sibandze, P. & Orimoloye, I.R. (2024). Analyzing spatiotemporal variations and dynamics of vegetation over Amathole district municipality in South Africa. Environment, Development and Sustainability, https://doi.org/10.1007/s10668-024-05221-0.  
- Thamaga, K.H., Gom, S., Adesola, G.O., Ndou, N., Muavhi, N., Mndela, M. Sibandze, P., Abdo, H.G., Maphanga, T., Afuye, G.A., Madonsela, B.S. & Almohamad, H. (2024). Integration of Geospatial Based Algorithms for Groundwater Potential Characterization in Keiskamma Catchment of South Africa. Groundwater for Sustainable Development 26 (2024) 101262. https://doi.org/10.1016/j.gsd.2024.101262.  
- Maphanga T., Dube, T., Shoko, C., Sibanda M. & Thamaga, K.H. (2023). Understanding the spatio-temporal distribution of bush encroachment in (un)protected savanna rangelands, South Africa. Geocarto International, 39:1, 2366515, e: https://doi.org/10.1080/10106049.2024.2366515.   
- Afuye, G.A., Nduku, L., Kalumba, A.M., Santos, C.A.G., Orimoloye, I.R., Ojeh, V.N., Thamaga, K.H., Sibandze, P. (2023). Global Trend Assessment of Land Use and Land Cover Changes: A Systematic Approach to Future Research Development and Planning. Journal of King Saud University – Science, 36: 103262. https://doi.org/10.1016/j.jksus.2024.103262. 
- Mashao, F.M., Thaba, S.J., Muyambo, N.P., Tjale, C.R., Zwane, P.S.M., Munjonji, L., Nkuna, D., Ayisi, K.K., & Thamaga, K.H. (2024). Exploring laboratory-based spectroscopy for estimating NPK content in the hutton soils of Syferkuil Farmlands, South Africa, Geocarto International, 39:1, 2339289, https://doi.org/10.1080/10106049.2024.2339289.  
- Madonsela, B.S., Maphanga, T., Malakane, K.C., Phungela, T.T., Gqomfa, B., Grangxabe, S., Thamaga, K.H., Hajji, L., Lekata, S., Karmaoui, A. & Mbonane, T.P. (2024). The Influence of Outdoor Exposure Concentrations on Indoor Air Quality in Rudimentary Designed Household Structures: Mpumalanga Province, South Africa. Pollution, 10 (1), 466-480. https://doi.org/10.22059/POLL.2023.365069.2064. 
- Gbenga, O.A., Thamaga, K.H., Gwavava, O. & Pharoe, K. (2023). Groundwater Potential Zones Assessment Using Geospatial Models in Semi-Arid Areas of South Africa Land. 12, 1877. https://doi.org/10.3390/land12101877. 
- Madonsela, B.S., Maphanga, T., Malakane, K., Phungela, T., Gqomfa, B., Grangxabe, S., Thamaga, K.H., Lekata, S., Hajji, L., Karmaoui, A. & Mbonane, T. (2023). The influence of outdoor exposure concentrations on indoor air quality in rudimentary designed household structures: Mpumalanga Province, South Africa. Pollution. https://doi.org/10.22059/POLL.2023.365069.2064.    
- Mndela, M., Thamaga, K.H. & Gusha, B. (2023). A global perspective of functional trait responses of graminoids to seasonality of fire. Plants, https://doi.org/10.3390/fire6090329. 
- Ndou, N., Thamaga, K.H., Mndela, Y. & Nyamugama, A. (2023). Radiometric compensation for occluded crops imaged using high spatial resolution Unmanned Aerial Vehicle system. Agriculture.13(8):1598. https://doi.org/10.3390/agriculture13081598. 
- Grangxabe, X.S., Madonsela, B.S., Maphanga, T., Gqomfa, B., Phungela, T.T., van Bilson, J., Malakane, K.C., Thamaga, K.H. & Angwenyi, D. (2023). The escalation of informal settlement and the high levels of illegal dumping post-apartheid: a systematic review. Challenges. 14: 38. https://doi.org/10.3390/challe14030038.  
- Mndela, M., Moss, S., Gusha, B., Thamaga, K.H., Afuye, G.A.; Abdo, H.G.; Almohamad, H. (2023). Functional Trait Responses of C4 Bunchgrasses to Fire Return Intervals in the Semi-Arid Savanna of South Africa. Diversity, 15(12), 1201. https://doi.org/10.3390/d15121201. 
- Thamaga, K.H., Dube, T. & Shoko, C. (2022). Evaluating the impact of land use and land cover change on unprotected wetland ecosystems in the arid-tropical areas of South Africa using the Landsat dataset and Support Vector Machine. Geocarto International, 1-21. https://doi.org/10.1080/10106049.2022.2034986.
- Thamaga K.H., Dube, T. & Shoko, C. (2021). Advances in satellite remote sensing of the wetland ecosystems in Sub-Saharan Africa. Geocarto International, 1-19. https://doi.org/10.1080/10106049.2021.1926552. 
- Muavhi, N., Thamaga, K.H. & Mutoti, M.I. (2021). Mapping groundwater potential using Relative Frequency Ratio, Analytical Hierarchy Process, and their Hybrid Models: Case of Nzhelele-Makhado Area in South Africa. Geocarto international, https://doi.org/10.1080/10106049.2021.1936212.
- Dzurume, T., Dube, T., Thamaga, K.H., Shoko, C. & Mazvimavi, D. (2021). Use of multispectral satellite data to assess impacts of land management practices on wetlands in the Limpopo Transfrontier River Basin, South Africa. South African Geographical Journal. https://doi.org/10.1080/03736245.2021.1941220. 
- Thamaga K.H. & Dube T. (2019). Understanding the seasonal mapping of invasive water hyacinth (Eichhornia crassipes) in the Greater Letaba River system using Sentinel-2 satellite data. GIScience and Remote Sensing, 56(8):1355-1377. https://doi.org/10.1080/15481603.2019.1646988.
- Thamaga K.H & Dube T. (2018a). Remote sensing of invasive water hyacinth (Eichhornia crassipes): A review on applications and challenges. Remote Sensing Applications: Society and Environment, 10:36-46. https://doi.org/10.1016/j.rsase.2018.02.005.
- Thamaga K.H & Dube T. (2018b). Testing two methods for mapping water hyacinth (Eichhornia crassipes) in the Greater Letaba river system, South Africa: Discrimination and mapping potential of the polar-orbiting Sentinel-2 MSI and Landsat 8 OLI sensors. International Journal of Remote Sensing, 39(22):8401-8059. https://doi.org/10.1080/01431161.2018.1479796.

""")

# Interests
st.markdown('<h3 style="color: #000000;">Interests</h3>', unsafe_allow_html=True)
#st.markdown("### Interests")
st.write("""
- Geospatial Big Data Analytics
- Hydrological Modeling and Water Resource management
- Cloud Computing and Geospatial Artificial Intelligence (Geo-AI)
- Synthetic Aperture Radar (SAR) Applications
- Land Use Land Cover Analysis and Future Prediction
- Disaster Risk Management
- Drone technology and Geospatial intelligence

""")

# Footer
st.markdown("---")
st.write("© 2026 Kgabo Humphrey Thamaga. hkgaboreba@gmail.com")