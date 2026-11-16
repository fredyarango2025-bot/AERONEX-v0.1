import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================
# CONFIG
# =========================

st.set_page_config(
    page_title="AERONEX",
    page_icon="✈️",
    layout="wide"
)

# =========================
# STYLES
# =========================

st.markdown("""
<style>

.main {
    background-color:#f7f9fc;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 6px rgba(0,0,0,0.10);
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3{
    color:#0C2340;
}

.success-badge{
    background:#23A55A;
    color:white;
    padding:5px 12px;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================

initiatives = pd.DataFrame([
    ["CAPEX-001","Primary Radar Runway 16","APPROVED",2500000],
    ["CAPEX-002","Terminal Expansion Phase 1","EXECUTION",12000000],
    ["CAPEX-003","Runway Lighting Upgrade","COMMITTEE",3500000],
    ["CAPEX-004","Security Screening Modernization","APPROVED",4200000],
    ["CAPEX-005","Baggage Handling Upgrade","EXECUTION",6800000],
])

initiatives.columns = [
    "Code",
    "Initiative",
    "Status",
    "Budget"
]

contracts = pd.DataFrame([
    ["CTR-001","INDRA","ACTIVE",2300000],
    ["CTR-002","THALES","ACTIVE",6000000],
    ["CTR-003","SIEMENS","DRAFT",1500000]
])

contracts.columns = [
    "Contract",
    "Vendor",
    "Status",
    "Amount"
]

risks = pd.DataFrame([
    ["Import Delay",4,5],
    ["Permit Approval Delay",3,4],
    ["Supplier Shortage",5,3],
    ["Weather Impact",2,2]
])

risks.columns = [
    "Risk",
    "Probability",
    "Impact"
]

actions = pd.DataFrame([
    ["Weekly Logistics Review","PMO","OPEN"],
    ["Supplier Escalation","Procurement","OPEN"],
    ["Airport Authority Follow-up","Engineering","DONE"]
])

actions.columns = [
    "Action",
    "Owner",
    "Status"
]

assets = pd.DataFrame([
    ["AST-001","Primary Radar Thales X200","READY FOR RECOGNITION",2300000],
    ["AST-002","Runway Lighting System","RECOGNIZED",1800000],
    ["AST-003","Security Scanner","IDENTIFIED",900000]
])

assets.columns = [
    "Asset Code",
    "Asset",
    "Status",
    "Value"
]

# =========================
# SIDEBAR
# =========================

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/0/0f/Airplane_silhouette.png",
    width=100
)

st.sidebar.title("AERONEX™")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Initiatives",
        "Contracts",
        "Risks",
        "Actions",
        "Assets",
        "Recognition Engine"
    ]
)

# =========================
# DASHBOARD
# =========================

if page == "Dashboard":

    st.title("✈️ AERONEX")

    st.subheader(
        "Airport Capital Governance Platform"
    )

    st.markdown("---")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Portfolio CAPEX",
        "USD 48.5M"
    )

    c2.metric(
        "Initiatives",
        "12"
    )

    c3.metric(
        "Assets",
        "34"
    )

    c4.metric(
        "Recognized",
        "29"
    )

    st.markdown("## KPI Dashboard")

    k1,k2,k3 = st.columns(3)

    k1.metric(
        "CRI",
        "85%"
    )

    k2.metric(
        "GBI",
        "6%"
    )

    k3.metric(
        "REI",
        "22"
    )

    st.markdown("---")

    left,right = st.columns(2)

    with left:

        portfolio = pd.DataFrame({
            "Area":[
                "Airside",
                "Terminal",
                "Security",
                "CNS"
            ],
            "Value":[42,31,17,10]
        })

        fig = px.pie(
            portfolio,
            values="Value",
            names="Area",
            hole=.55,
            title="CAPEX Portfolio Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        status = pd.DataFrame({
            "Status":[
                "Draft",
                "Committee",
                "Approved",
                "Execution",
                "Capitalized"
            ],
            "Count":[2,3,4,2,1]
        })

        fig = px.bar(
            status,
            x="Status",
            y="Count",
            title="Initiative Status"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================
# INITIATIVES
# =========================

elif page == "Initiatives":

    st.title("Governance")

    st.subheader(
        "CAPEX Portfolio"
    )

    st.dataframe(
        initiatives,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Selected Initiative"
    )

    st.success(
        "Primary Radar Runway 16 - APPROVED"
    )

    st.write("Sponsor: Air Navigation Services")
    st.write("Owner: Capital Projects Office")
    st.write("Approved Budget: USD 2,500,000")

# =========================
# CONTRACTS
# =========================

elif page == "Contracts":

    st.title("Procurement")

    st.dataframe(
        contracts,
        use_container_width=True
    )

# =========================
# RISKS
# =========================

elif page == "Risks":

    st.title("Risk Management")

    st.dataframe(
        risks,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=risks["Probability"],
            y=risks["Impact"],
            mode='markers+text',
            text=risks["Risk"],
            textposition='top center',
            marker=dict(
                size=25,
                color="red"
            )
        )
    )

    fig.update_layout(
        title="Risk Heat Map",
        xaxis_title="Probability",
        yaxis_title="Impact",
        xaxis=dict(range=[0,6]),
        yaxis=dict(range=[0,6])
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================
# ACTIONS
# =========================

elif page == "Actions":

    st.title("Actions")

    st.dataframe(
        actions,
        use_container_width=True
    )

# =========================
# ASSETS
# =========================

elif page == "Assets":

    st.title("Assets")

    st.dataframe(
        assets,
        use_container_width=True
    )

# =========================
# RECOGNITION ENGINE
# =========================

elif page == "Recognition Engine":

    st.title("⭐ Asset Recognition Engine")

    st.markdown("---")

    st.subheader(
        "Asset"
    )

    st.info(
        "Primary Radar Thales X200"
    )

    st.markdown("### Recognition Checklist")

    t = st.checkbox(
        "Technical Acceptance",
        value=True
    )

    f = st.checkbox(
        "Financial Acceptance",
        value=True
    )

    a = st.checkbox(
        "As-Built Documentation",
        value=True
    )

    c = st.checkbox(
        "Commissioning Certificate",
        value=True
    )

    d = st.checkbox(
        "Final Documentation",
        value=True
    )

    st.markdown("---")

    st.subheader(
        "Validation Engine"
    )

    st.success("✅ Initiative Approved")
    st.success("✅ Active Contract")
    st.success("✅ No Critical Blockers")

    ready = all([
        t,
        f,
        a,
        c,
        d
    ])

    if ready:

        st.success(
            "✅ Checklist Completed"
        )

        if st.button(
            "Recognize Asset",
            use_container_width=True
        ):
            st.balloons()

            st.success(
                """
                Asset Recognized Successfully

                Status: RECOGNIZED

                Recognition Date:
                20-Jun-2027
                """
            )

    else:

        st.error(
            "Checklist incomplete"
        )

# =========================
# FOOTER
# =========================

st.sidebar.markdown("---")
st.sidebar.caption("AERONEX™ v0.2 Demo")
st.sidebar.caption("Airport Capital Governance Platform")
