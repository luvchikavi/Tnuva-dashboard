import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ------------------------------------------------------------------------------
# Adjust working directory to script's location (so relative paths work properly).
# ------------------------------------------------------------------------------
os.chdir(os.path.dirname(__file__))

# ------------------------------------------------------------------------------
# Set Streamlit page configuration
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Tnuva Environmental Decision Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------------------
# Pale vanilla styling using HTML/CSS (optional)
# ------------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Pale Vanilla Background for main and sidebar */
    .main {
        background-color: #f9f4ef;
    }
    .css-1lcbmhc { 
        background-color: #f9f4ef; 
    }
    /* Default font */
    .block-container {
        font-family: "Helvetica", sans-serif;
    }
    /* Headings color */
    h1, h2, h3, h4, h5, h6 {
        color: #513c2c;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Helper / Cached functions
# ------------------------------------------------------------------------------
@st.cache_data
def load_tnuva_data(file_path: str) -> pd.DataFrame:
    """
    Load Tnuva's expanded Scope 1, 2, and 3 data from a CSV file.
    If file is not found, returns a sample set.
    """
    if not os.path.isfile(file_path):
        # Return sample data if file does not exist
        st.warning(f"File not found: {file_path}. Using sample data instead.")
        sample_df = pd.DataFrame({
            "Business Unit": ["Dairy", "Meat", "Plant-Based", "Beverages", "Snacks"],
            "Scope 1 Emissions (MT CO2e)": [10000, 8000, 5000, 6000, 4000],
            "Scope 2 Emissions (MT CO2e)": [3000, 2500, 1500, 1800, 1200],
            "Scope 3 Emissions (MT CO2e)": [50000, 45000, 30000, 35000, 20000],
            "Electricity Consumption (MWh)": [20000, 15000, 10000, 12000, 8000],
            "Fuels Consumption (Liters)": [50000, 60000, 20000, 30000, 25000],
            "Direct Emissions (MT CO2e)": [5000, 3000, 2500, 2800, 2000],
            "Indirect Emissions (MT CO2e)": [7000, 4000, 2800, 3200, 2200],
            "Supply Chain Emissions (MT CO2e)": [35000, 30000, 20000, 25000, 15000]
        })
        return sample_df

    # Load the real data
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error reading file: {e}. Using sample data instead.")
        sample_df = pd.DataFrame({
            "Business Unit": ["Dairy", "Meat", "Plant-Based", "Beverages", "Snacks"],
            "Scope 1 Emissions (MT CO2e)": [10000, 8000, 5000, 6000, 4000],
            "Scope 2 Emissions (MT CO2e)": [3000, 2500, 1500, 1800, 1200],
            "Scope 3 Emissions (MT CO2e)": [50000, 45000, 30000, 35000, 20000],
            "Electricity Consumption (MWh)": [20000, 15000, 10000, 12000, 8000],
            "Fuels Consumption (Liters)": [50000, 60000, 20000, 30000, 25000],
            "Direct Emissions (MT CO2e)": [5000, 3000, 2500, 2800, 2000],
            "Indirect Emissions (MT CO2e)": [7000, 4000, 2800, 3200, 2200],
            "Supply Chain Emissions (MT CO2e)": [35000, 30000, 20000, 25000, 15000]
        })
        return sample_df
def page_footer():
    """
    Displays a simple footer at the bottom of each page/tab.
    """
    st.markdown("---")
    st.write("**Powered by Oporto-Carbon | Designed by Dr. Avi Luvchik**")
    st.write("@All rights reserved - 2025")

# ------------------------------------------------------------------------------
# Landing Page
# ------------------------------------------------------------------------------
if "start" not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    # Attempt to load logos on landing
    col_logo1, col_logo2 = st.columns([0.2, 0.2])
    with col_logo1:
        try:
            st.image("assests/tnuva_logo.png", width=150)
        except FileNotFoundError:
            st.warning("Tnuva logo not found in 'assests/tnuva_logo.png'.")

    with col_logo2:
        try:
            st.image("assests/oporto_logo.png", width=150)
        except FileNotFoundError:
            st.warning("Oporto logo not found in 'assests/oporto_logo.png'.")

    st.title("Welcome to Tnuva's Environmental Decision Dashboard")

    # Load data once here to check if file is missing
    csv_data_path = "tnuva_scope_data.csv"
    data_df = load_tnuva_data(csv_data_path)
    if data_df.shape[0] > 0 and "Dairy" not in data_df["Business Unit"].values:
        # This is a naive check for sample data vs. real data
        st.caption("Real Tnuva data loaded successfully!")
    else:
        st.caption("File not found: 'tnuva_scope_data.csv'. Using sample data instead.")

    st.markdown(
        """
        ### About CLEAR Dashboard
        CLEAR (Compliance, Lifecycle Emissions Analysis, and Reporting) is a cutting-edge decision-making tool designed
        to help industries streamline their sustainability and compliance strategies.
        
        It provides an integrated platform for:
        - **Analyzing environmental impacts**
        - **Estimating financial costs**, including carbon taxes
        - **Ensuring regulatory compliance** with frameworks like CBAM, REACH, and more.
        - **Model Simultaion** for better decision making and reliable results. 

        By connecting to the most up-to-date Life Cycle Assessment (LCA) and regulatory databases, CLEAR ensures users always
        work with the latest and most accurate information.

        ---

        About Dr. Avi Luvchik  
        Avi is an internationally recognized expert in sustainability and environmental compliance. With over 
        20 years of experience, he has advised top organizations across various industries. His expertise spans life cycle 
        assessments, emissions reduction, and corporate sustainability strategies. Dr. Luvchik is the founder of CLEAR and 
        continues to innovate solutions to tackle global environmental challenges.
        """
    )

    # Footer and Button Section
    st.write("---")
    if st.button("Let's Get Started"):
        st.session_state.start = True

    st.markdown(
        """
        **Powered by Oporto-Carbon | Designed by Dr. Avi Luvchik**  
        @All rights reserved - 2025
        """,
        unsafe_allow_html=True
    )
    st.stop()
# ------------------------------------------------------------------------------
# Load data for other pages
# ------------------------------------------------------------------------------
csv_data_path = "tnuva_scope_data.csv"
tnuva_data = load_tnuva_data(csv_data_path)

# ------------------------------------------------------------------------------
# Sidebar Navigation
# ------------------------------------------------------------------------------
st.sidebar.header("Navigation")
selected_tab = st.sidebar.radio(
    "Select a tab (all lower-case):",
    [
        "environmental analysis",
        "regulatory tracker",
        "model simulation",
        "audit assurance",
        "data collection"
    ]
)
# ------------------------------------------------------------------------------
####-Tab 1 environmental analysis#####
# ------------------------------------------------------------------------------
if selected_tab == "environmental analysis":
    # Header with logos
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.subheader("Scope 1, 2, and 3 Emissions Overview")
    with col2:
        try:
            st.image("assests/oporto_logo.png", width=200)  # Display Oporto logo
        except FileNotFoundError:
            st.warning("Oporto logo not found in 'assests/oporto_logo.png'.")

    st.write("Below is Tnuva’s expanded emissions data, including electricity, fuels, and other details.")

    # Create a total row as a DataFrame
    total_row = pd.DataFrame({
        "Business Unit": ["TOTAL"],
        "Scope 1 Emissions (MT CO2e)": [tnuva_data["Scope 1 Emissions (MT CO2e)"].sum()],
        "Scope 2 Emissions (MT CO2e)": [tnuva_data["Scope 2 Emissions (MT CO2e)"].sum()],
        "Scope 3 Emissions (MT CO2e)": [tnuva_data["Scope 3 Emissions (MT CO2e)"].sum()],
        "Electricity Consumption (MWh)": [tnuva_data["Electricity Consumption (MWh)"].sum()],
        "Fuels Consumption (Liters)": [tnuva_data["Fuels Consumption (Liters)"].sum()],
        "Direct Emissions (MT CO2e)": [tnuva_data["Direct Emissions (MT CO2e)"].sum()],
        "Indirect Emissions (MT CO2e)": [tnuva_data["Indirect Emissions (MT CO2e)"].sum()],
        "Supply Chain Emissions (MT CO2e)": [tnuva_data["Supply Chain Emissions (MT CO2e)"].sum()],
    })

    # Append the total row to the main DataFrame using pd.concat()
    analysis_df = pd.concat([tnuva_data, total_row], ignore_index=True)

    # Display the updated DataFrame
    st.dataframe(analysis_df)

    # -----------------------------------
    # Pie chart of total emissions by Scope 1, 2, 3 (using the total row)
    # -----------------------------------
    total_scope1 = total_row["Scope 1 Emissions (MT CO2e)"].iloc[0]
    total_scope2 = total_row["Scope 2 Emissions (MT CO2e)"].iloc[0]
    total_scope3 = total_row["Scope 3 Emissions (MT CO2e)"].iloc[0]

    pie_df = pd.DataFrame({
        "Scope": ["Scope 1", "Scope 2", "Scope 3"],
        "Emissions (MT CO2e)": [total_scope1, total_scope2, total_scope3]
    })

    st.write("### Total Emissions Distribution")
    pie_chart = px.pie(
        pie_df,
        names="Scope",
        values="Emissions (MT CO2e)",
        title="Total Emissions by Scope"
    )
    st.plotly_chart(pie_chart, use_container_width=True)

    # -----------------------------------
    # Emission Intensity Metrics
    # -----------------------------------
    st.write("### Emission Intensity Metrics")
    tnuva_data["Scope 1 Intensity (MT CO2e/MWh)"] = tnuva_data["Scope 1 Emissions (MT CO2e)"] / tnuva_data["Electricity Consumption (MWh)"]
    tnuva_data["Scope 2 Intensity (MT CO2e/MWh)"] = tnuva_data["Scope 2 Emissions (MT CO2e)"] / tnuva_data["Electricity Consumption (MWh)"]

    st.dataframe(tnuva_data[["Business Unit", "Scope 1 Intensity (MT CO2e/MWh)", "Scope 2 Intensity (MT CO2e/MWh)"]])

    # -----------------------------------
    # Hotspots Bar Chart
    # -----------------------------------
    st.write("### Emission Hotspots by Business Unit")
    hotspots_chart = px.bar(
        tnuva_data,
        x="Business Unit",
        y=["Scope 1 Emissions (MT CO2e)", "Scope 2 Emissions (MT CO2e)", "Scope 3 Emissions (MT CO2e)"],
        title="Emission Hotspots by Business Unit",
        labels={"value": "Emissions (MT CO2e)", "variable": "Scope"},
        barmode="group"
    )
    st.plotly_chart(hotspots_chart, use_container_width=True)

    page_footer()
# ------------------------------------------------------------------------------
####-Tab 2 regulatory tracker#####
# ------------------------------------------------------------------------------
if selected_tab == "regulatory tracker":
    # Add the Oporto Carbon logo at the top-right corner
    col1, col2 = st.columns([0.8, 0.2])  # Adjust column width ratios as needed
    with col2:
        try:
            st.image("assests/oporto_logo.png", width=200)  # Adjust the width for logo size
        except FileNotFoundError:
            st.warning("Oporto logo not found in 'assests/oporto_logo.png'.")
    st.subheader("Regulations and Compliance")

    
    # -----------------------------------
    # 1. Regulatory Summary Table
    # -----------------------------------
    st.write("### Regulatory Summary")
    regulations_data = pd.DataFrame({
        "Regulation Name": [
            "CBAM (Carbon Border Adjustment Mechanism)",
            "ISO 14001 Certification",
            "GHG Protocol Verification",
            "EU Carbon Reporting",
            "Local Water Use Regulation"
        ],
        "Description": [
            "Imposes a carbon tax on imported goods based on their embedded emissions.",
            "Certification for environmental management systems.",
            "Ensures comprehensive GHG accounting and reporting.",
            "Mandates detailed carbon reporting for goods exported to the EU.",
            "Limits industrial water use based on local laws."
        ],
        "Status": [
            "In Compliance", "Renewal Due", "Completed", "Pending Submission", "In Progress"
        ],
        "Compliance Deadline": [
            "2025-12-31", "2024-06-30", "2023-12-15", "2024-10-01", "2025-03-31"
        ]
    })
    st.dataframe(regulations_data)

    # -----------------------------------
    # 2. Task Manager
    # -----------------------------------
    st.write("### Task Manager")
    if "tasks" not in st.session_state:
        st.session_state.tasks = [
            {"Task": "Prepare CBAM submission", "Regulation": "CBAM", "Status": "Not Started", "Due Date": "2024-10-01"},
            {"Task": "Schedule ISO 14001 audit", "Regulation": "ISO 14001", "Status": "In Progress", "Due Date": "2024-06-30"},
            {"Task": "Verify GHG report", "Regulation": "GHG Protocol", "Status": "Completed", "Due Date": "2023-12-15"}
        ]

    # Display existing tasks
    task_df = pd.DataFrame(st.session_state.tasks)
    st.write("#### Current Tasks")
    st.dataframe(task_df)

    # Add a new task
    with st.expander("Add a New Task"):
        task_name = st.text_input("Task Name")
        regulation = st.selectbox("Associated Regulation", regulations_data["Regulation Name"])
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
        due_date = st.date_input("Due Date")
        if st.button("Add Task"):
            new_task = {"Task": task_name, "Regulation": regulation, "Status": status, "Due Date": str(due_date)}
            st.session_state.tasks.append(new_task)
            st.success("Task added successfully!")

    # Delete tasks
    with st.expander("Delete a Task"):
        delete_task_name = st.selectbox("Select Task to Delete", [t["Task"] for t in st.session_state.tasks])
        if st.button("Delete Task"):
            st.session_state.tasks = [t for t in st.session_state.tasks if t["Task"] != delete_task_name]
            st.success("Task deleted successfully!")

    # -----------------------------------
    # 3. Upcoming Deadlines
    # -----------------------------------
    st.write("### Upcoming Deadlines")
    deadlines = pd.DataFrame({
        "Regulation Name": regulations_data["Regulation Name"],
        "Compliance Deadline": pd.to_datetime(regulations_data["Compliance Deadline"]),
        "Status": regulations_data["Status"]
    })

    # Filter deadlines within the next 6 months
    upcoming_deadlines = deadlines[deadlines["Compliance Deadline"] <= pd.Timestamp.now() + pd.DateOffset(months=6)]
    if not upcoming_deadlines.empty:
        st.write("#### Deadlines in the Next 6 Months")
        st.dataframe(upcoming_deadlines)
    else:
        st.write("No deadlines in the next 6 months.")

    # -----------------------------------
    # 4. Gantt Chart for Compliance Tracker
    # -----------------------------------
    st.write("### Compliance Timeline (Gantt Chart)")
    deadlines_for_gantt = regulations_data[["Regulation Name", "Compliance Deadline", "Status"]]
    deadlines_for_gantt["Start"] = pd.Timestamp.now()
    deadlines_for_gantt["End"] = pd.to_datetime(deadlines_for_gantt["Compliance Deadline"])
    deadlines_for_gantt["Status"] = deadlines_for_gantt["Status"].replace(
        {"Completed": "green", "In Compliance": "blue", "Pending Submission": "orange", "Renewal Due": "yellow", "In Progress": "purple"}
    )

    fig_gantt = px.timeline(
        deadlines_for_gantt,
        x_start="Start",
        x_end="End",
        y="Regulation Name",
        color="Status",
        title="Regulation Compliance Timeline",
        labels={"Status": "Compliance Status"},
        color_discrete_map={
            "green": "green",
            "blue": "blue",
            "orange": "orange",
            "yellow": "yellow",
            "purple": "purple"
        }
    )
    fig_gantt.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig_gantt, use_container_width=True)

    # -----------------------------------
    # 5. Decision Tool for Compliance
    # -----------------------------------
    st.write("### Decision Tool for Compliance Prioritization")
    regulation_to_review = st.selectbox(
        "Select a Regulation to Prioritize:",
        regulations_data["Regulation Name"]
    )
    selected_regulation = regulations_data[regulations_data["Regulation Name"] == regulation_to_review]
    if not selected_regulation.empty:
        st.write(f"#### Regulation: {regulation_to_review}")
        st.write(f"**Description**: {selected_regulation['Description'].iloc[0]}")
        st.write(f"**Status**: {selected_regulation['Status'].iloc[0]}")
        st.write(f"**Compliance Deadline**: {selected_regulation['Compliance Deadline'].iloc[0]}")
        if pd.to_datetime(selected_regulation["Compliance Deadline"].iloc[0]) <= pd.Timestamp.now() + pd.DateOffset(months=1):
            st.warning("This regulation has an urgent deadline within the next month!")
        elif selected_regulation["Status"].iloc[0] in ["Pending Submission", "Renewal Due"]:
            st.info("This regulation requires immediate attention due to pending compliance actions.")
        else:
            st.success("This regulation is currently in compliance.")

    page_footer()
# ------------------------------------------------------------------------------
####-Tab 3 model simulation#####
# ------------------------------------------------------------------------------
elif selected_tab == "model simulation":
    # Add the Oporto Carbon logo at the top-right corner
    col1, col2 = st.columns([0.8, 0.2])  # Adjust column width ratios as needed
    with col2:
        try:
            st.image("assests/oporto_logo.png", width=200)  # Adjust the width for logo size
        except FileNotFoundError:
            st.warning("Oporto logo not found in 'assests/oporto_logo.png'.")

    st.subheader("Scenario Modeling")

    # -----------------------------------
    # 1. Scenario Input
    # -----------------------------------
    st.write("### Define Your Scenarios")
    st.markdown(
        "Use the sliders and dropdowns below to define different scenarios and explore their impacts."
    )
    col1, col2 = st.columns(2)

    # Scenario 1 Inputs
    with col1:
        st.write("#### Scenario 1")
        carbon_tax_s1 = st.slider("Carbon Tax ($/ton CO2e) - Scenario 1", 0, 150, 50, step=10, key="s1_tax")
        renewable_energy_s1 = st.slider("Renewable Energy Mix (%) - Scenario 1", 0, 100, 50, step=10, key="s1_renewable")
        efficiency_gain_s1 = st.slider("Efficiency Improvement (%) - Scenario 1", 0, 30, 10, step=1, key="s1_efficiency")

    # Scenario 2 Inputs
    with col2:
        st.write("#### Scenario 2")
        carbon_tax_s2 = st.slider("Carbon Tax ($/ton CO2e) - Scenario 2", 0, 150, 25, step=10, key="s2_tax")
        renewable_energy_s2 = st.slider("Renewable Energy Mix (%) - Scenario 2", 0, 100, 75, step=10, key="s2_renewable")
        efficiency_gain_s2 = st.slider("Efficiency Improvement (%) - Scenario 2", 0, 30, 20, step=1, key="s2_efficiency")

    # -----------------------------------
    # 2. Scenario Comparison
    # -----------------------------------
    st.write("### Scenario Results")

    def calculate_scenario(df, tax, renewable, efficiency):
        """Helper function to calculate emissions and costs for a scenario."""
        scenario_df = df.copy()
        scenario_df["Adjusted Scope 1"] = scenario_df["Scope 1 Emissions (MT CO2e)"] * (1 - efficiency / 100)
        scenario_df["Adjusted Scope 2"] = scenario_df["Scope 2 Emissions (MT CO2e)"] * (1 - renewable / 100)
        scenario_df["Adjusted Scope 3"] = scenario_df["Scope 3 Emissions (MT CO2e)"]  # No change in this example
        scenario_df["Total Adjusted Emissions"] = (
            scenario_df["Adjusted Scope 1"] + scenario_df["Adjusted Scope 2"] + scenario_df["Adjusted Scope 3"]
        )
        scenario_df["Carbon Tax Cost"] = scenario_df["Total Adjusted Emissions"] * tax
        return scenario_df

    # Calculate results for both scenarios
    results_s1 = calculate_scenario(tnuva_data, carbon_tax_s1, renewable_energy_s1, efficiency_gain_s1)
    results_s2 = calculate_scenario(tnuva_data, carbon_tax_s2, renewable_energy_s2, efficiency_gain_s2)

    # Display results side by side
    st.write("#### Scenario 1 Results")
    st.dataframe(results_s1[["Business Unit", "Total Adjusted Emissions", "Carbon Tax Cost"]])

    st.write("#### Scenario 2 Results")
    st.dataframe(results_s2[["Business Unit", "Total Adjusted Emissions", "Carbon Tax Cost"]])

    # -----------------------------------
    # 3. Financial Impact Analysis
    # -----------------------------------
    st.write("### Financial Impact Analysis")

    # Total Costs for each scenario
    total_cost_s1 = results_s1["Carbon Tax Cost"].sum()
    total_cost_s2 = results_s2["Carbon Tax Cost"].sum()

    st.metric(label="Total Cost (Scenario 1)", value=f"${total_cost_s1:,.0f}")
    st.metric(label="Total Cost (Scenario 2)", value=f"${total_cost_s2:,.0f}", delta=f"${total_cost_s2 - total_cost_s1:,.0f}")

    # -----------------------------------
    # 4. Carbon Reduction vs ROI
    # -----------------------------------
    st.write("### Carbon Reduction vs ROI")
    projects_data = pd.DataFrame({
        "Project": ["Solar Installation", "Energy Efficiency", "Waste-to-Energy", "Supply Chain Optimization"],
        "Carbon Reduction (MT CO2e)": [15000, 8000, 10000, 12000],
        "Cost (USD)": [200000, 50000, 120000, 75000],
        "ROI (%)": [15, 20, 10, 18]
    })
    st.dataframe(projects_data)

    project_chart = px.scatter(
        projects_data,
        x="Carbon Reduction (MT CO2e)",
        y="ROI (%)",
        size="Cost (USD)",
        color="Project",
        hover_data=["Cost (USD)"],
        title="Carbon Reduction vs ROI"
    )
    st.plotly_chart(project_chart, use_container_width=True)

    # -----------------------------------
    # 5. Dynamic Recommendations
    # -----------------------------------
    st.write("### Recommendations")

    if total_cost_s1 < total_cost_s2:
        st.success(f"Scenario 1 is more cost-effective with a total cost of ${total_cost_s1:,.0f}.")
        st.info("Consider increasing efficiency improvements to further reduce emissions.")
    else:
        st.success(f"Scenario 2 is more cost-effective with a total cost of ${total_cost_s2:,.0f}.")
        st.info("Consider adopting a higher renewable energy mix to reduce Scope 2 emissions.")

    # -----------------------------------
    # 6. Export Results
    # -----------------------------------
    st.write("### Export Scenario Results")
    export_option = st.radio("Choose a scenario to export:", ["Scenario 1", "Scenario 2"])

    if export_option == "Scenario 1":
        export_df = results_s1
    else:
        export_df = results_s2

    export_csv = export_df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=export_csv,
        file_name=f"{export_option}_results.csv",
        mime="text/csv",
    )

    page_footer()
# ------------------------------------------------------------------------------
####-Tab 4 audit assurance#####
# ------------------------------------------------------------------------------
elif selected_tab == "audit assurance":

    # Add the Oporto Carbon logo at the top-right corner
    col1, col2 = st.columns([0.8, 0.2])  # Adjust column width ratios as needed
    with col2:
        try:
            st.image("assests/oporto_logo.png", width=200)  # Adjust the width for logo size
        except FileNotFoundError:
            st.warning("Oporto logo not found in 'assests/oporto_logo.png'.")

    st.subheader("Audit & Assurance")
    st.write("Overview of internal and external audits, plus verification of Tnuva’s environmental data.")
    


    st.write("""
    - **Next Internal Audit**: May 2025  
    - **External Certification**: ISO 14001 (Renewal due Q2 2026)  
    - **GHG Protocol Verification**: Completed Q4 2024  
    """)

    uploaded_file = st.file_uploader("Upload your recent audit report (PDF)", type=["pdf"])
    if uploaded_file:
        st.success("File uploaded successfully!")

    page_footer()

# ------------------------------------------------------------------------------
####-Tab 5 data collection#####
# ------------------------------------------------------------------------------
elif selected_tab == "data collection":

    # Add the Oporto Carbon logo at the top-right corner
    col1, col2 = st.columns([0.8, 0.2])  # Adjust column width ratios as needed
    with col2:
        try:
            st.image("assests/oporto_logo.png", width=200)  # Adjust the width for logo size
        except FileNotFoundError:
            st.warning("Oporto logo not found in 'assests/oporto_logo.png'.")

    st.subheader("Data Collection & Management")
    st.write("Gather new environmental data, update existing datasets, or integrate with external data sources.")
    


    new_data_file = st.file_uploader("Upload new Tnuva emissions data (CSV)", type=["csv"])
    if new_data_file:
        df_new = pd.read_csv(new_data_file)
        st.write("Preview of new data:")
        st.dataframe(df_new)
        st.success("Data uploaded successfully.")

    st.write("**Manual Entry Form**")
    business_unit = st.text_input("Business Unit")
    scope1_val = st.number_input("Scope 1 (MT CO2e)", min_value=0, value=0, step=100)
    scope2_val = st.number_input("Scope 2 (MT CO2e)", min_value=0, value=0, step=100)
    scope3_val = st.number_input("Scope 3 (MT CO2e)", min_value=0, value=0, step=100)

    if st.button("Add Entry"):
        st.success(f"Added entry for {business_unit} | S1={scope1_val} | S2={scope2_val} | S3={scope3_val}")
        # In a real app, you'd append to a DataFrame or database here

    page_footer()