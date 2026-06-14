import os
import sys
import time
import streamlit as st

# ==========================================
# 1. CUSTOM CSS STYLING OVERRIDES
# ==========================================
def apply_custom_css():
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    /* Global styling overrides */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        background-color: #0B0F19 !important;
        color: #E2E8F0 !important;
    }

    [data-testid="stHeader"] {
        background-color: rgba(11, 15, 25, 0.8) !important;
        backdrop-filter: blur(10px);
    }

    [data-testid="stSidebar"] {
        background-color: #0D1321 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Glassmorphism Container Card */
    .glass-card {
        background: rgba(17, 24, 39, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }

    .glass-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.15);
    }

    /* Small Glass Card for Metrics */
    .metric-card {
        background: rgba(30, 41, 59, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        border-color: rgba(6, 182, 212, 0.4);
    }

    .metric-val {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 2px;
        background: linear-gradient(135deg, #FFF 30%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .metric-val.alert {
        background: linear-gradient(135deg, #FFA07A 30%, #FF4500 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .metric-val.success {
        background: linear-gradient(135deg, #A7F3D0 30%, #059669 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .metric-label {
        font-size: 0.8rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }

    .metric-delta {
        font-size: 0.8rem;
        font-weight: 600;
    }

    .delta-up { color: #10B981; }
    .delta-down { color: #EF4444; }

    /* Custom Title Gradients */
    .title-gradient {
        background: linear-gradient(135deg, #818CF8 0%, #34D399 50%, #60A5FA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 8px;
    }

    .subtitle-text {
        font-size: 1.1rem;
        color: #94A3B8;
        margin-bottom: 24px;
        line-height: 1.6;
    }

    /* Flowchart Node Styling */
    .flow-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 24px;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        margin-bottom: 24px;
    }

    .flow-node {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 10px 16px;
        border-radius: 8px;
        text-align: center;
        font-weight: 600;
        font-size: 0.85rem;
        min-width: 110px;
        position: relative;
    }

    .flow-node.active {
        border-color: #10B981;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.3);
    }

    .flow-node.bottleneck {
        border-color: #EF4444;
        background: rgba(239, 68, 68, 0.15);
        animation: pulse-red 2.0s infinite alternate;
    }

    .flow-arrow {
        color: #475569;
        font-size: 1.2rem;
        font-weight: bold;
    }

    /* Custom Chat Styling */
    .chat-bubble-user {
        background: linear-gradient(135deg, #4F46E5 0%, #3730A3 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 16px 16px 4px 16px;
        margin-bottom: 12px;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.2);
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .chat-bubble-agent {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #E2E8F0;
        padding: 14px 18px;
        border-radius: 16px 16px 16px 4px;
        margin-bottom: 16px;
        max-width: 85%;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .agent-thinking {
        font-family: monospace;
        font-size: 0.8rem;
        color: #6366f1;
        background: rgba(99, 102, 241, 0.08);
        padding: 6px 10px;
        border-radius: 6px;
        margin-bottom: 8px;
        border-left: 2px solid #6366f1;
        display: inline-block;
    }

    .quick-replies {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
        margin-bottom: 16px;
    }

    .quick-reply-btn {
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.3);
        color: #818CF8;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .quick-reply-btn:hover {
        background: rgba(99, 102, 241, 0.25);
        border-color: #818CF8;
        color: white;
    }

    /* Premium Automation Checklist */
    .auto-task {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 16px;
        background: rgba(30, 41, 59, 0.35);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 8px;
        margin-bottom: 8px;
        transition: all 0.2s ease;
    }

    .auto-task.completed {
        border-color: rgba(16, 185, 129, 0.2);
        background: rgba(16, 185, 129, 0.05);
    }

    .auto-task.running {
        border-color: rgba(249, 115, 22, 0.4);
        background: rgba(249, 115, 22, 0.08);
        animation: pulse-orange 1.5s infinite alternate;
    }

    .status-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #64748B;
    }

    .status-dot.completed {
        background-color: #10B981;
        box-shadow: 0 0 8px #10B981;
    }

    .status-dot.running {
        background-color: #F97316;
        box-shadow: 0 0 8px #F97316;
    }

    /* Keyframe Animations */
    @keyframes pulse-red {
        0% { box-shadow: 0 0 4px rgba(239, 68, 68, 0.2); }
        100% { box-shadow: 0 0 16px rgba(239, 68, 68, 0.6); }
    }

    @keyframes pulse-orange {
        0% { box-shadow: 0 0 4px rgba(249, 115, 22, 0.2); }
        100% { box-shadow: 0 0 12px rgba(249, 115, 22, 0.5); }
    }

    /* Streamlit Custom UI Overrides */
    div.stButton > button {
        background: linear-gradient(135deg, #4F46E5 0%, #4338CA 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 14px rgba(79, 70, 229, 0.3) !important;
        width: 100%;
    }

    div.stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5) !important;
        background: linear-gradient(135deg, #6366F1 0%, #4F46E5 100%) !important;
    }

    div.stButton > button:active {
        transform: translateY(1px) !important;
    }

    /* Secondary Button Overrides */
    div.stDownloadButton > button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        transition: all 0.25s ease !important;
        box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3) !important;
        width: 100%;
    }

    div.stDownloadButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(5, 150, 105, 0.5) !important;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
    }

    /* Style the tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(15, 23, 42, 0.4);
        padding: 6px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .stTabs [data-baseweb="tab"] {
        padding: 8px 16px !important;
        border-radius: 8px !important;
        color: #94A3B8 !important;
        font-weight: 500 !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: white !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
    }

    .stTabs [aria-selected="true"] {
        background-color: rgba(99, 102, 241, 0.15) !important;
        color: #818CF8 !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
    }

    /* Info messages style */
    .stAlert {
        background-color: rgba(30, 41, 59, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #E2E8F0 !important;
        border-radius: 12px !important;
    }

    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


# ==========================================
# 2. SCENARIO CONFIGURATION DATA
# ==========================================
SCENARIOS = {
    "supply_chain": {
        "name": "Supply Chain & Manufacturing",
        "tagline": "Augmenting production line scheduling and optimizing logistics disruptions.",
        "avatar": "🏭",
        "nodes": [
            {"name": "Tier-1 Suppliers", "status": ""},
            {"name": "Inbound Logistics", "status": "bottleneck"},
            {"name": "Assembly Line", "status": "active"},
            {"name": "Global Distribution", "status": ""}
        ],
        "metrics": {
            "prod_risk": {
                "label": "Production Line Risk",
                "value": 84,
                "unit": "%",
                "delta": "+38% increase",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 12,
                "improved_delta": "-72% drop",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "buffer_level": {
                "label": "Chip Buffer Stock",
                "value": 2.4,
                "unit": " Days",
                "delta": "-5.8 days",
                "is_delta_up": False,
                "is_alert": True,
                "improved_value": 14.5,
                "improved_delta": "+12.1 days",
                "improved_is_delta_up": True,
                "improved_is_alert": False
            },
            "supplier_delay": {
                "label": "Logistics Transit Time",
                "value": 22.5,
                "unit": " Days",
                "delta": "+14 days delay",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 6.8,
                "improved_delta": "-15.7 days",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "financial_impact": {
                "label": "Projected Downtime Cost",
                "value": 248000,
                "unit": " USD",
                "delta": "+$95k/day risk",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 18500,
                "improved_delta": "-92.5% reduction",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            }
        },
        "diagnosis_logs": [
            "[07:15:02] [SYSTEM] Telemetry Alert: Port of Long Beach logistics queue exceeds threshold. Delay flag raised.",
            "[07:15:05] [AGENT] Fetching Tier-1 supplier logistics invoices. Supplier #402 (Silicon Micro Corp) has 15,000 MCU chips delayed on vessel 'Oceanic Star'.",
            "[07:15:09] [AGENT] Querying active assembly line schedules: SmartTV lines A and C will deplete chip buffer in 2.4 days.",
            "[07:15:12] [AGENT] Bottleneck localized at Inbound Logistics. Performing multi-channel sourcing sweep...",
            "[07:15:15] [SYSTEM] Diagnostic Complete: Found alternative shipment availability in European warehouse (Frankfurt)."
        ],
        "quick_replies": [
            "What is causing the shipping bottleneck?",
            "What are the secondary supplier options?",
            "Run impact simulation of assembly shutdown."
        ],
        "dialogue": {
            "default": "Hello, I am the Supply Chain Orchestrator Agent. I have diagnosed a critical supply bottleneck for our microcontroller units (MCUs) due to port congestion, risking a production line shutdown in 2.4 days. Would you like me to present my root cause diagnosis and recommendations?",
            "What is causing the shipping bottleneck?": {
                "thinking": "Retrieving logistics telemetry... Checking maritime shipping records...",
                "response": "The shipment of 15,000 MCUs (Batch #MC-8829) is aboard the vessel 'Oceanic Star', currently anchored outside the Port of Long Beach with an estimated berthing delay of 14 days. The buffer stock at Assembly Lines A & C is only 2.4 days, meaning we will experience a total stoppage if we do not act immediately."
            },
            "What are the secondary supplier options?": {
                "thinking": "Searching Global Sourcing Network... Filtering by ISO-9001 certifications & shipping times...",
                "response": "I have identified two alternative sourcing channels:\n1. **EuroSilicon (Frankfurt, DE)**: 15,000 units available in stock. Air freight transit is 4 days. Unit price is 15% higher ($4.20 vs $3.65). Total cost delta: +$8,250.\n2. **PacificSemi (Hsinchu, TW)**: 20,000 units available. Shipping transit is 8 days. Unit price is 5% higher. Stoppage risk remains at 35%.\n\nI recommend **EuroSilicon** to eliminate shutdown risk completely. Sourcing from EuroSilicon saves approximately **$229,500** net after factoring in extra shipping costs."
            },
            "Run impact simulation of assembly shutdown.": {
                "thinking": "Calculating hourly downtime penalty rates... Loading labor cost contracts...",
                "response": "If Assembly Lines A & C shut down, the metrics impact will be:\n- Stoppage of 4,200 SmartTV units/day.\n- Idle labor penalties: $45,000/day.\n- Late contract fulfillment penalties with retail partners: $50,000/day.\n- Cumulative 5-day impact: **$475,000 USD** and a severe hit to customer satisfaction indices."
            }
        },
        "recommendations": [
            {
                "title": "Trigger Emergency EuroSilicon Order",
                "description": "Source 15,000 MCU units from EuroSilicon (Frankfurt) via DHL Priority Air Freight.",
                "impact": "Eliminates production halt risk, reduces transit delay by 15.7 days."
            },
            {
                "title": "Reschedule Low-Priority Line Maintenance",
                "description": "Shift Line B scheduled maintenance forward to offset MCU inventory buffer shortage.",
                "impact": "Optimizes idle worker utilization, saving $12,000."
            }
        ],
        "automation_steps": [
            {"title": "Verify Secondary Sourcing Inventory", "detail": "Queried EuroSilicon API. Inventory confirmed: 15,000 MCU units locked.", "duration": 1.2},
            {"title": "Draft ERP Purchase Order", "detail": "Generated PO #EP-99402 in SAP ERP system. Value: $63,000 USD.", "duration": 1.5},
            {"title": "Route Logistics Shipping Dispatch", "detail": "Initiated DHL Air Freight booking with priority custom clearance codes.", "duration": 1.8},
            {"title": "Realign Production Line Schedule", "detail": "Updated Manufacturing Execution System (MES) schedules to shift production window.", "duration": 1.4},
            {"title": "Alert Supply Chain Coordinators", "detail": "Sent automated Slack notification to warehouse managers with tracking code.", "duration": 1.0}
        ],
        "report_template": """# EXECUTIVE BUSINESS IMPACT REPORT
## Supply Chain & Logistics Optimization Loop

**Issue Identified:** Port congestion at Long Beach caused a 14-day logistics delay for MCU shipments, threatening a complete production line shutdown within 2.4 days.

**Agent Sourcing Intervention:**
- Secondary Supplier: EuroSilicon (Frankfurt, DE)
- Quantity Sourced: 15,000 Units
- Shipping Channel: Priority Air Freight

### Business Value Saved
- **Production Risk Reduced:** From **84%** to **12%**
- **Inventory Buffer Secured:** Extended from **2.4 Days** to **14.5 Days**
- **Logistics Lead Time Saved:** Reduced from **22.5 Days** to **6.8 Days**
- **Net Financial Loss Prevented:** **$229,500 USD** (Downtime cost prevented minus freight premium)

### Automation Audit Trail
1. Sourcing inventory locked via API.
2. SAP ERP PO #EP-99402 created and authorized.
3. Priority Air Cargo booking finalized with DHL.
4. MES scheduling modified for line balancing.
5. Supply Chain Slack channels updated.

*Generated by Agentic Value Chain Hub, 2026.*"""
    },

    "healthcare": {
        "name": "Healthcare & Patient Flow",
        "tagline": "Automating discharge planning to resolve emergency department gridlocks.",
        "avatar": "🏥",
        "nodes": [
            {"name": "ER Triage", "status": ""},
            {"name": "Emergency Ward", "status": "bottleneck"},
            {"name": "ICU Beds", "status": "active"},
            {"name": "Discharge / Rehab", "status": ""}
        ],
        "metrics": {
            "er_wait": {
                "label": "ER Wait Time",
                "value": 185,
                "unit": " Mins",
                "delta": "+110m vs target",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 45,
                "improved_delta": "-140m wait reduction",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "bed_util": {
                "label": "Bed Utilization",
                "value": 98.2,
                "unit": "%",
                "delta": "Critical Capacity",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 82.5,
                "improved_delta": "-15.7% buffer created",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "staff_burnout": {
                "label": "Staffing Ratio Index",
                "value": 7.8,
                "unit": " Pts",
                "delta": "Severe Overstretch",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 4.2,
                "improved_delta": "Normal Staffing Ratio",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "divert_cost": {
                "label": "Ambulance Diversion Cost",
                "value": 85000,
                "unit": " USD",
                "delta": "+$22k today",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 0,
                "improved_delta": "-100% cost eliminated",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            }
        },
        "diagnosis_logs": [
            "[07:18:12] [SYSTEM] ER occupancy alerts triggered. Average boarding time exceeds 4 hours.",
            "[07:18:15] [AGENT] Scanning EHR database... 8 stable ICU patients have discharge summaries written but are waiting on coordinator signature.",
            "[07:18:19] [AGENT] Analyzing staffing rosters... Wards 4B and 5A are operating at a 1:8 nurse-to-patient ratio (recommended 1:4).",
            "[07:18:23] [AGENT] Identifying bottleneck: Discharge flow block. Wards cannot intake ER admissions because ICU cannot release patients.",
            "[07:18:26] [SYSTEM] Diagnosis complete: Bed block detected at ICU Discharge."
        ],
        "quick_replies": [
            "Why are discharges delayed in the ICU?",
            "What is the plan to clear the bed block?",
            "Show clinical criteria for discharge candidates."
        ],
        "dialogue": {
            "default": "Hello, I am the Patient Flow & Resource Agent. The Emergency Department is in gridlock, with wait times peaking at 185 minutes and bed occupancy at 98.2%. The root cause is a discharge bed-block in the ICU wards. I have structured a recovery plan. Should we proceed?",
            "Why are discharges delayed in the ICU?": {
                "thinking": "Analyzing EHR metadata... Checking physician signature timestamps...",
                "response": "The delay is administrative. Five patients have been marked medically stable since yesterday afternoon, but they require final senior physician sign-off. The attending physician is currently in back-to-back surgeries. This delays transferring them to the rehabilitation wing, creating a backlog in the ER."
            },
            "What is the plan to clear the bed block?": {
                "thinking": "Optimizing bed assignment heuristics... Matching nursing shift capacities...",
                "response": "My proposed action plan is:\n1. **Automate Signature Route**: Forward EHRs of the 5 stable patients to the on-duty deputy medical director for expedited signature.\n2. **Reallocate Staff**: Temporarily shift 2 float nurses to ER Triage to handle incoming patients, reducing staff stress.\n3. **Coordinate Transport**: Schedule direct patient transport to local rehab facilities for immediate transition.\n\nThis will clear 5 beds in 90 minutes, dropping ER wait times by an estimated **140 minutes** and eliminating the need for ambulance diversion."
            },
            "Show clinical criteria for discharge candidates.": {
                "thinking": "Querying clinical guidelines database (CDC/WHO)... verifying lab vitals...",
                "response": "All 5 identified discharge candidates meet the standard discharge protocol:\n- Normal vitals (HR < 90, Temp < 100.4F, SpO2 > 95% on room air).\n- Completed IV antibiotic courses transitioned to oral equivalents.\n- Confirmed mobility/care plan at the destination rehabilitation unit.\n- Lab reports (WBC, CRP) within normal limits."
            }
        },
        "recommendations": [
            {
                "title": "Expedite ICU Ward Discharges",
                "description": "Trigger electronic routing of medical release forms to the Deputy Medical Director for instant authorization.",
                "impact": "Frees up 5 ICU beds immediately, relieving ER intake stress."
            },
            {
                "title": "Activate Reserve Nurse Staffing",
                "description": "Call in 2 on-call nurse practitioners to assist with lower-acuity ER triage.",
                "impact": "Reduces nurse burnout score from 7.8 to 4.2."
            }
        ],
        "automation_steps": [
            {"title": "Query EHR Discharge Audits", "detail": "Retrieved vitals and clinical summaries for patients #HC-119, #HC-304, #HC-772. All status green.", "duration": 1.4},
            {"title": "Expedite Signatures Via DocuSign", "detail": "Routed digital discharge packets to Deputy Director's mobile portal. Signed and validated.", "duration": 1.6},
            {"title": "Schedule Transit Vans", "detail": "Booked non-emergency medical transit vans for 11:30 AM arrival to clear beds.", "duration": 1.1},
            {"title": "Update Bed Control Systems", "detail": "Logged transfers in Epic EHR, marking 5 beds as 'Available for ER Admit'.", "duration": 1.5},
            {"title": "Send Staff Roster Updates", "detail": "SMS notification sent to float nurses reallocating them to high-pressure wards.", "duration": 0.9}
        ],
        "report_template": """# HEALTHCARE VALUE CHAIN REPORT
## Patient Flow & ER Capacity Management

**Problem Statement:** Critical ER overcrowding with 185-minute average wait times, stemming from a downstream bed block in the ICU where stable patients awaited administrative discharge.

**Agent Intervention Results:**
- **ER Boarding Wait Time:** Reduced from **185 Mins** to **45 Mins**
- **Bed Utilization Rate:** Decreased from **98.2%** to **82.5%** (restoring safety buffer)
- **Staffing Stress Index:** Reduced from **7.8** to **4.2**
- **Ambulance Diversion Cost Saved:** **$85,000 USD** (0 patients diverted to external county hospitals)

### Action Steps Automated
1. EHR audit of stable discharge candidates completed.
2. Clinical summaries approved via priority electronic signatures.
3. Discharge transport scheduled and confirmed.
4. Epic EHR Bed Management synchronized.
5. On-call float nursing rosters adjusted.

*Generated by Healthcare Operations Agent, 2026.*"""
    },

    "banking": {
        "name": "Banking & Risk Operations",
        "tagline": "Accelerating high-value loan processing while maintaining fraud compliance.",
        "avatar": "🏦",
        "nodes": [
            {"name": "Application Intake", "status": ""},
            {"name": "Compliance & Fraud Check", "status": "bottleneck"},
            {"name": "Risk Scoring", "status": "active"},
            {"name": "Loan Disbursement", "status": ""}
        ],
        "metrics": {
            "processing_time": {
                "label": "Turnaround Time (TAT)",
                "value": 5.4,
                "unit": " Days",
                "delta": "+3.4 days delay",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 0.4,
                "improved_delta": "-5 days saved",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "fraud_risk": {
                "label": "Fraud Override Rate",
                "value": 14.2,
                "unit": "%",
                "delta": "+8% manual flag rate",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 2.1,
                "improved_delta": "-12.1% false alerts",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "approval_ratio": {
                "label": "Application Throughput",
                "value": 62,
                "unit": "%",
                "delta": "-18% drop in approvals",
                "is_delta_up": False,
                "is_alert": True,
                "improved_value": 94,
                "improved_delta": "+32% increase",
                "improved_is_delta_up": True,
                "improved_is_alert": False
            },
            "acquisition_cost": {
                "label": "Drop-off Lost Revenue",
                "value": 124000,
                "unit": " USD",
                "delta": "Customer abandonment risk",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 9200,
                "improved_delta": "-92.5% loss reduction",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            }
        },
        "diagnosis_logs": [
            "[07:22:45] [SYSTEM] Alerts triggered: 147 mortgage applications stuck in 'Fraud Pend' status.",
            "[07:22:48] [AGENT] Cross-checking applicants with Secretary of State company registers. Alert commonality identified.",
            "[07:22:52] [AGENT] Findings: Flagged applications originate from employees of 'Avante Biotech'. The company was acquired and renamed 'Avante Health Group'.",
            "[07:22:56] [AGENT] The automated system flagged this employer mismatch as 'Potential Identity Theft/Employment Fraud'.",
            "[07:23:00] [SYSTEM] Diagnosis complete: False-positive alerts generated due to outdated corporate registry database."
        ],
        "quick_replies": [
            "Why is the mortgage processing delayed?",
            "How does the agent resolve the employer mismatch?",
            "What is the revenue risk of keeping these flags?"
        ],
        "dialogue": {
            "default": "Hello, I am the Risk Operations & Underwriting Agent. We have a queue backlog of 147 mortgage applications flagged for fraud. Analysis shows 92% of these are false positives due to a recent corporate renaming event of a major regional employer. I can resolve this issue automatically. Shall we trigger the database override?",
            "Why is the mortgage processing delayed?": {
                "thinking": "Querying compliance engine backlog... Sorting flags by risk scoring...",
                "response": "Mortgage applications are currently averaging 5.4 days to process. The system has automatically halted 147 applications under a high-risk compliance flag. Attending compliance specialists must manually call employers to verify salaries, creating a massive backlog."
            },
            "How does the agent resolve the employer mismatch?": {
                "thinking": "Connecting to SEC EDGAR database... Retrieving company merger records...",
                "response": "I verified via SEC EDGAR and regional state filings that 'Avante Biotech' legally merged into 'Avante Health Group' on May 1st. I have cross-referenced the EIN (Employer Identification Number) of both entities and confirmed they match. By executing a global override rule, we can auto-approve these applications since they meet all credit guidelines (averaging a 745 FICO score)."
            },
            "What is the revenue risk of keeping these flags?": {
                "thinking": "Evaluating competitor processing speeds... Analyzing customer churn history...",
                "response": "Mortgage applicants typically apply to multiple banks. Our models predict that every day a loan is delayed, the customer churn risk increases by 15%. If left in manual review, we stand to lose approximately **$124,000 USD** in interest and origination fee revenues due to customer abandonment."
            }
        },
        "recommendations": [
            {
                "title": "Apply Database EIN Override",
                "description": "Establish a temporary compliance rule mapping 'Avante Biotech' to 'Avante Health Group' in our KYC lookup.",
                "impact": "Unlocks 147 flagged applications immediately, dropping processing time to under 1 day."
            },
            {
                "title": "Trigger Automated Customer Document Upload",
                "description": "Send SMS prompts to affected applicants requesting their most recent W2/paystub containing the new company name.",
                "impact": "Secures an audit trail for compliance auditing."
            }
        ],
        "automation_steps": [
            {"title": "Verify Corporate Registrar Data", "detail": "EIN validation on state registries confirmed. Merger audit document parsed.", "duration": 1.5},
            {"title": "Inject Compliance Database Mapping", "detail": "Inserted rule mapping 'Avante Biotech' to 'Avante Health Group' in fraud registry.", "duration": 1.2},
            {"title": "Automate Underwriting Run", "detail": "Re-ran credit rules engine. 147 loans approved (FICO average 745, DTI 32%).", "duration": 1.8},
            {"title": "Generate Loan Offer Contracts", "detail": "Triggered DocuSign API to build and send loan disclosure packets.", "duration": 1.7},
            {"title": "Update CRM Lead Status", "detail": "Updated Salesforce status to 'Approved - Contract Sent' and alerted brokers.", "duration": 0.9}
        ],
        "report_template": """# RISK & UNDERWRITING AUDIT REPORT
## Automated Loan Processing Override

**Incident Summary:** A merger of 'Avante Biotech' into 'Avante Health Group' triggered a false positive employer mismatch flag, bottlenecking 147 prime mortgage applications.

**Agent Compliance Resolution:**
- Resolved: Corporate registry verification automated.
- Validation: EIN match confirmed via state database.
- Action: Global compliance exception mapping added.

### Financial and Operational Impact
- **Processing Turnaround Time:** Decreased from **5.4 Days** to **0.4 Days** (9.6 hours)
- **False Fraud Alert Rate:** Dropped from **14.2%** to **2.1%**
- **Throughput Approval Ratio:** Increased from **62%** to **94%**
- **Revenue Recovered:** **$114,800 USD** (prevented customer churn losses)

### Compliance Verification Steps
1. State corporate filing retrieved and archived.
2. Compliance exceptions ledger updated (Reference ID: #KYC-2026-994).
3. Auto-underwriting credit parameters re-verified.
4. Disclosures dispatched in compliance with Truth in Lending Act.

*Generated by Banking Compliance Agent, 2026.*"""
    },

    "telecom": {
        "name": "Telecom Network & Churn",
        "tagline": "Dynamic bandwidth optimization and churn mitigation during extreme traffic spikes.",
        "avatar": "📡",
        "nodes": [
            {"name": "Core Network", "status": ""},
            {"name": "Fiber Backhaul", "status": "bottleneck"},
            {"name": "Cellular Tower", "status": "active"},
            {"name": "Subscriber Mobile", "status": ""}
        ],
        "metrics": {
            "drop_rate": {
                "label": "Call/Data Drop Rate",
                "value": 8.9,
                "unit": "%",
                "delta": "+7.4% vs QoS Target",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 0.8,
                "improved_delta": "-91% QoS recovery",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "bandwidth_avail": {
                "label": "Backhaul Capacity",
                "value": 99.1,
                "unit": "% Load",
                "delta": "Congestion Stoppage",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 64.2,
                "improved_delta": "-34.9% traffic headroom",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "churn_risk": {
                "label": "VIP Churn Danger",
                "value": 15.6,
                "unit": "%",
                "delta": "High value users alert",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 1.2,
                "improved_delta": "-92.3% churn reduction",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            },
            "revenue_impact": {
                "label": "SLA Penalties",
                "value": 92000,
                "unit": " USD",
                "delta": "+$12k/hour risk",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 4500,
                "improved_delta": "-95.1% penalty reduction",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            }
        },
        "diagnosis_logs": [
            "[07:25:01] [SYSTEM] Telemetry Warning: Sector 4A (Metropolitan Arena) data drop rate spike detected.",
            "[07:25:04] [AGENT] Reviewing cell tower logs. Dynamic Beamforming is active, but backhaul capacity has hit 99.1% line saturation.",
            "[07:25:08] [AGENT] Checking active subscriber metadata: 420 premium 'VIP Unlimited' plans are experiencing download speeds below 200kbps.",
            "[07:25:12] [AGENT] Identifying congestion cause: High volume video uploading from concert venue.",
            "[07:25:15] [SYSTEM] Diagnosis Complete: Bottleneck localized to Fiber Backhaul Link #FB-202."
        ],
        "quick_replies": [
            "Why is the network drop rate spiking?",
            "What options exist to resolve the fiber backhaul overload?",
            "How can we prevent churn among the VIP subscribers?"
        ],
        "dialogue": {
            "default": "Hello, I am the Telco Operations & Network Agent. Sector 4A at the Arena is experiencing critical cell congestion (99.1% load) during an event, causing connection drops for VIP subscribers. I have designed a dynamic traffic routing and customer retention workflow. Should I initialize?",
            "Why is the network drop rate spiking?": {
                "thinking": "Analyzing packet drops in Sector 4A... Reading radio network controller KPIs...",
                "response": "The drop rate is 8.9% (target is <0.5%). Cell towers are functional, but the localized fiber backhaul link (#FB-202) is saturated. The massive volume of concurrent social media uploads (4K video streaming) is choking the physical link capacity."
            },
            "What options exist to resolve the fiber backhaul overload?": {
                "thinking": "Checking software-defined network (SDN) configurations... Verifying microwave reserve links...",
                "response": "I can execute two actions:\n1. **Route to Microwave Reserve**: Activate the inactive 10Gbps microwave backup link (#MW-88) to offload traffic.\n2. **Apply Traffic Shaping**: Throttle non-critical background updates (OS updates, photo syncs) to 128kbps, preserving bandwidth for calls, texts, and active browsing."
            },
            "How can we prevent churn among the VIP subscribers?": {
                "thinking": "Scanning CRM database for high-risk subscribers... checking promo rules...",
                "response": "We have 420 VIP users in the congested area. I recommend dynamically pushing a 5G Priority Pass to their SIM profiles (elevating QoS queue priority) and sending a localized SMS offering a $10 billing credit for any inconvenience. This drops churn risk from 15.6% to 1.2%."
            }
        },
        "recommendations": [
            {
                "title": "Enable SDN Microwave Backup Routing",
                "description": "Establish software-defined routing protocols to dump 3.5 Gbps of overflow traffic onto the microwave backup network.",
                "impact": "Lowers backhaul load to 64.2% and drops drop rate immediately."
            },
            {
                "title": "Deploy VIP Customer Compensation & Priority Pass",
                "description": "Push SIM card configuration update (Class 1 QCI) to VIP subscribers and dispatch apologies containing bill credits.",
                "impact": "Saves premium contract renewals worth $92,000."
            }
        ],
        "automation_steps": [
            {"title": "Initialize SDN Route Switch", "detail": "Opened port configurations on backhaul routers. Microwave Link #MW-88 online.", "duration": 1.6},
            {"title": "Apply QCI SIM Policy Update", "detail": "Pushed SIM profile overrides to HLR database. 420 VIPs elevated to Priority Queue.", "duration": 1.4},
            {"title": "Deploy Traffic Shaping Rules", "detail": "Enabled Deep Packet Inspection (DPI) policy to throttle cloud updates.", "duration": 1.8},
            {"title": "Trigger CRM Compensation Promo", "detail": "Dispatched SMS promotions offering $10 bill credits to affected subscribers.", "duration": 1.2},
            {"title": "Validate Quality of Service (QoS)", "detail": "Piped latency metrics. Average delay dropped to 22ms. Loss rate under 0.8%.", "duration": 1.0}
        ],
        "report_template": """# TELECOM NETWORK OPTIMIZATION REPORT
## Dynamic Bandwidth & Churn Mitigation

**Incident Description:** Arena event traffic saturated local fiber backhaul #FB-202 (99.1% load), leading to a packet drop rate spike of 8.9% and customer complaints.

**Agent Optimization Solutions:**
- Software-Defined Network: Rerouted traffic to Microwave Link #MW-88.
- Quality of Service (QoS): Elevated QCI levels for 420 VIP subscribers.
- Customer Care: Automated billing compensations.

### Operational Results
- **Network Drop Rate:** Reduced from **8.9%** to **0.8%** (QoS restored)
- **Backhaul Capacity Load:** Reduced from **99.1%** to **64.2%** (headroom created)
- **VIP Churn Danger Index:** Dropped from **15.6%** to **1.2%**
- **Financial Savings (SLA & Retention):** **$87,500 USD** (reduced fines and saved contracts)

### Executed Tasks Audit
1. Microwave backup link connected and synchronized.
2. SIM routing tables in HLR database upgraded.
3. DPI traffic throttling applied on background packet headers.
4. Micro-billing credits dispatched via SMS.
5. Network telemetry verified for latency and jitter.

*Generated by Telecom Network Agent, 2026.*"""
    },

    "energy": {
        "name": "Energy Grid & Storage",
        "tagline": "Dynamic reserve dispatching to maintain grid frequency stability under renewable loss.",
        "avatar": "⚡",
        "nodes": [
            {"name": "Solar / Wind Farms", "status": ""},
            {"name": "Battery Storage", "status": "bottleneck"},
            {"name": "Substations", "status": "active"},
            {"name": "Residential Grid", "status": ""}
        ],
        "metrics": {
            "grid_freq": {
                "label": "Grid Frequency",
                "value": 59.82,
                "unit": " Hz",
                "delta": "-0.18 Hz (Critical)",
                "is_delta_up": False,
                "is_alert": True,
                "improved_value": 59.98,
                "improved_delta": "+0.16 Hz (Stable)",
                "improved_is_delta_up": True,
                "improved_is_alert": False
            },
            "renew_output": {
                "label": "Solar Supply Gap",
                "value": 140,
                "unit": " MW",
                "delta": "-45% vs Forecast",
                "is_delta_up": False,
                "is_alert": True,
                "improved_value": 0,
                "improved_delta": "Gap Closed",
                "improved_is_delta_up": True,
                "improved_is_alert": False
            },
            "battery_reserve": {
                "label": "Battery Buffer Stock",
                "value": 12,
                "unit": " mins",
                "delta": "Rapid Depletion",
                "is_delta_up": False,
                "is_alert": True,
                "improved_value": 90,
                "improved_delta": "Charged via grid dispatch",
                "improved_is_delta_up": True,
                "improved_is_alert": False
            },
            "imbalance_cost": {
                "label": "Frequency Penalties",
                "value": 165000,
                "unit": " USD",
                "delta": "Imbalance penalty alert",
                "is_delta_up": True,
                "is_alert": True,
                "improved_value": 8500,
                "improved_delta": "-94.8% cost saved",
                "improved_is_delta_up": False,
                "improved_is_alert": False
            }
        },
        "diagnosis_logs": [
            "[07:28:12] [SYSTEM] Telemetry Alert: Grid frequency has dropped to 59.82 Hz (Safety threshold is 59.85 Hz).",
            "[07:28:15] [AGENT] Checking renewable output: Sudden cloud cover over Sector 7 Solar Farm caused a 140 MW loss.",
            "[07:28:19] [AGENT] Reviewing storage reserves: Battery storage discharge rate is at 100%, reserves will deplete in 12 minutes.",
            "[07:28:23] [AGENT] Bottleneck localized at Battery Storage. Risk of rolling blackouts or shedding loads in 12 minutes.",
            "[07:28:26] [SYSTEM] Diagnosis Complete: Primary reserves insufficient. Secondary load balancing required."
        ],
        "quick_replies": [
            "What caused the grid frequency drop?",
            "What secondary reserve dispatch options are available?",
            "What is the risk of rolling blackouts if we do not act?"
        ],
        "dialogue": {
            "default": "Hello, I am the Smart Grid Optimization Agent. The grid frequency is critically low (59.82 Hz) due to a sudden 140 MW solar generation loss. Battery storage is depleting rapidly. I have mapped an emergency generation dispatch and demand-response routing. Shall we execute?",
            "What caused the grid frequency drop?": {
                "thinking": "Loading meteorological satellite data... Checking SCADA solar output telemetry...",
                "response": "A localized cloud front moved in 40 minutes faster than forecasted, covering the Sector 7 Solar Arrays. This caused solar output to collapse by 140 MW. The batteries discharged instantly to cover the gap, but they only have 12 minutes of charge remaining at this load rate."
            },
            "What secondary reserve dispatch options are available?": {
                "thinking": "Querying commercial peaker contracts... checking microgrid capacities...",
                "response": "I can execute two recovery steps:\n1. **Dispatch Gas-Peaker Turbines**: Signal the Apex Gas-Peaker Station to start up (takes 6 minutes to sync to grid, supplies 100 MW).\n2. **Activate Demand-Response**: Dispatch commands to 14 enrolled industrial manufacturing plants to temporarily reduce their load by a combined 45 MW (Total: 145 MW supply recovery)."
            },
            "What is the risk of rolling blackouts if we do not act?": {
                "thinking": "Modeling grid load flows... calculating load shedding consequences...",
                "response": "If frequency drops below 59.70 Hz, safety relays will trip automatically to protect substation hardware. This will trigger immediate rolling blackouts in residential Sectors A and B, cutting power to 45,000 households and incurring **$165,000 USD** in frequency imbalance penalties and customer damages."
            }
        },
        "recommendations": [
            {
                "title": "Trigger Gas-Peaker Dispatch",
                "description": "Send automated SCADA startup sequence to the Apex Gas-Peaker facility to inject 100 MW.",
                "impact": "Secures base grid frequency within 6 minutes."
            },
            {
                "title": "Deploy Industrial Demand-Response Program",
                "description": "Send API alerts to enrolled factory HVAC and smelting systems to throttle consumption by 45 MW.",
                "impact": "Frees up grid capacity, preventing load-shedding blackouts."
            }
        ],
        "automation_steps": [
            {"title": "Initiate Gas Turbine SCADA Sync", "detail": "Sent startup command to Apex Peaker. Turbines spinning up, tracking 3,600 RPM.", "duration": 1.8},
            {"title": "Transmit Demand-Response Signals", "detail": "Sent Webhook command to 14 industrial smart meters. 43.8 MW load drop verified.", "duration": 1.2},
            {"title": "Sync Turbine to Grid Phase", "detail": "Synch-check relay confirmed phase match. 100 MW baseline injection online.", "duration": 1.5},
            {"title": "Transition Battery to Charge Mode", "detail": "Relieved battery discharge load, redirecting excess peaker energy to recharge cells.", "duration": 1.4},
            {"title": "Verify Frequency Restoration", "detail": "Queried grid sensors. Frequency stabilized at 59.98 Hz. System secure.", "duration": 1.0}
        ],
        "report_template": """# ENERGY GRID OPERATIONS REPORT
## Emergency Frequency Stabilization Event

**Incident Summary:** Sudden cloud cover over Sector 7 Solar Farm caused a 140 MW generation drop. Grid frequency fell to 59.82 Hz, placing substation hardware at immediate risk of tripping.

**Agent Automation Interventions:**
- Secondary Sourcing: Dispatched Apex Gas-Peaker Turbines (+100 MW).
- Demand-Response: Throttled industrial consumption (-43.8 MW).
- Energy Storage: Secured battery reserves from depleting.

### Operational Performance Metrics
- **Grid Frequency:** Stabilized from **59.82 Hz** to **59.98 Hz** (safe range)
- **Solar Supply Gap:** Closed from **140 MW deficit** to **0 MW deficit**
- **Battery Storage Buffer:** Rebuilt from **12 mins** to **90 mins** (charging active)
- **Grid Imbalance Cost Avoided:** **$156,500 USD** (prevented rolling blackouts)

### SCADA Audit Trail Log
1. Apex gas-peaker start sequence dispatched.
2. Webhooks sent to industrial IoT smart grids.
3. Generator phase-sync relays engaged.
4. Battery state switched from discharge to charge.
5. Grid-frequency metrics locked.

*Generated by Energy Grid Operations Agent, 2026.*"""
    }
}


# ==========================================
# 3. WORKFLOW ENGINE & STATE MACHINE
# ==========================================
def init_session_state(industry):
    """Initializes the session state for a selected industry value chain."""
    if "industry" not in st.session_state or st.session_state.industry != industry:
        st.session_state.industry = industry
        
        # Scenario configurations
        config = SCENARIOS[industry]
        st.session_state.config = config
        
        # Load initial metrics
        st.session_state.metrics = {}
        for k, v in config["metrics"].items():
            st.session_state.metrics[k] = {
                "label": v["label"],
                "value": v["value"],
                "unit": v["unit"],
                "delta": v["delta"],
                "is_delta_up": v["is_delta_up"],
                "is_alert": v["is_alert"]
            }
            
        # Agent status
        st.session_state.workflow_status = "diagnosed" # diagnosed -> running_automation -> completed
        st.session_state.automation_progress = 0.0
        st.session_state.current_step_index = -1
        
        # Chat history
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": config["dialogue"]["default"],
                "thinking": "Value chain monitor triggered. ER/Logistics/Grid anomaly detected. Diagnostic heuristics loading..."
            }
        ]

def handle_user_message(user_text):
    """Processes a user chat message, generating agent response with chain-of-thought."""
    st.session_state.chat_history.append({"role": "user", "content": user_text})
    
    config = st.session_state.config
    dialogue = config["dialogue"]
    
    # Try direct match
    if user_text in dialogue:
        agent_thought = dialogue[user_text]["thinking"]
        agent_resp = dialogue[user_text]["response"]
    else:
        # Keyword heuristic matching
        user_lower = user_text.lower()
        matched = False
        
        for key, value in dialogue.items():
            if key != "default" and any(word in user_lower for word in key.lower().split() if len(word) > 4):
                agent_thought = value["thinking"]
                agent_resp = value["response"]
                matched = True
                break
                
        if not matched:
            if st.session_state.workflow_status == "completed":
                agent_thought = "Workflow completed. Analyzing post-run operational telemetry..."
                agent_resp = f"The agentic workflow has already executed successfully. Critical KPIs have been stabilized. You can review the audit logs in the Automation tab or download the final business report in the Report tab."
            else:
                agent_thought = "Interpreting user query in value chain context..."
                agent_resp = f"I've noted your query regarding '{user_text}'. Based on my diagnostics, we should prioritize addressing the **{config['nodes'][1]['name']}** bottleneck. I highly recommend running the **{config['recommendations'][0]['title']}** by clicking the **Approve & Execute** button in the control console to mitigate the ongoing risk."
                
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": agent_resp,
        "thinking": agent_thought
    })

def run_automation_step():
    """Runs a single step of the automated workflow, updating state."""
    config = st.session_state.config
    steps = config["automation_steps"]
    total_steps = len(steps)
    
    if st.session_state.workflow_status != "running_automation":
        st.session_state.workflow_status = "running_automation"
        st.session_state.current_step_index = 0
        st.session_state.automation_progress = 0.0
        return True

    idx = st.session_state.current_step_index
    if idx < total_steps:
        # Simulate work
        time.sleep(steps[idx]["duration"])
        st.session_state.current_step_index += 1
        st.session_state.automation_progress = (idx + 1) / total_steps
        
        # When all steps complete, transition metrics
        if st.session_state.current_step_index == total_steps:
            st.session_state.workflow_status = "completed"
            
            # Transition metrics to improved state
            for k, v in config["metrics"].items():
                st.session_state.metrics[k] = {
                    "label": v["label"],
                    "value": v["improved_value"],
                    "unit": v["unit"],
                    "delta": v["improved_delta"],
                    "is_delta_up": v["improved_is_delta_up"],
                    "is_alert": v["improved_is_alert"]
                }
            
            # Add completion chat message
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": f"🎉 **Workflow Executed Successfully!** All automation sequence checks have passed. The bottleneck has been cleared and metrics have successfully returned to target limits. You can download the generated impact report in the Report tab.",
                "thinking": "Automation sequence complete. Post-optimization validation checks passed. Generating executive business report."
            })
            
        return True
    return False


# ==========================================
# 4. MAIN RENDERING LOGIC & UI
# ==========================================

# Apply custom styling overrides
apply_custom_css()

# Header Section
st.markdown('<div class="title-gradient">VALUE CHAIN COGNITIVE ORCHESTRATOR</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Harnessing multi-agent workflows to augment diagnostic capacity, automate operations, and accelerate value generation across critical industry sectors.</div>', unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.markdown("### Select Value Chain")
    selected_key = st.selectbox(
        "Active Vertical",
        options=list(SCENARIOS.keys()),
        format_func=lambda k: f"{SCENARIOS[k]['avatar']} {SCENARIOS[k]['name']}"
    )
    
    st.markdown("---")
    
    # Agent status panel
    st.markdown("### Agent Status Console")
    st.markdown(
        """
        <div style="background: rgba(30, 41, 59, 0.4); padding: 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.05);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:0.85rem; font-weight:500;">Orchestrator Agent</span>
                <span style="color:#10B981; font-size:0.75rem;">● ONLINE</span>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:0.85rem; font-weight:500;">Diagnostic Engine</span>
                <span style="color:#10B981; font-size:0.75rem;">● ONLINE</span>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:0.85rem; font-weight:500;">Sourcing/Resource Agent</span>
                <span style="color:#10B981; font-size:0.75rem;">● ONLINE</span>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:0.85rem; font-weight:500;">SCADA/ERP API Bridge</span>
                <span style="color:#10B981; font-size:0.75rem;">● READY</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    st.markdown("### Platform System Context")
    st.markdown(
        """
        - **Engine**: Streamlit Premium Integration
        - **Model Context**: Gemini Cognitive Agent
        - **Mode**: Human-In-The-Loop (HITL)
        - **Version**: v2.4.1-stable
        """
    )
    
    st.markdown("---")
    st.markdown("<p style='font-size:0.75rem; color:#64748B; text-align:center;'>Developer: Antigravity AI Codebase</p>", unsafe_allow_html=True)

# Initialize Session State for the selected industry
init_session_state(selected_key)
config = st.session_state.config
metrics = st.session_state.metrics

# Automation Execution Loop (Forces reruns for step-by-step progress animation)
if st.session_state.workflow_status == "running_automation":
    automation_active = run_automation_step()
    if automation_active:
        time.sleep(0.1) # Small buffer
        st.rerun()

# 1. Flowchart Schematic Visualization
st.markdown("### 📊 Value Chain Topology")
nodes_html = ""
for i, node in enumerate(config["nodes"]):
    status_class = ""
    status_label = ""
    
    # Set status classes dynamically
    if node["status"] == "bottleneck" and st.session_state.workflow_status != "completed":
        status_class = "bottleneck"
        status_label = "<br><span style='font-size:0.7rem; color:#FF4500; font-weight:bold;'>⚠️ BOTTLENECK</span>"
    elif node["status"] == "active" and st.session_state.workflow_status != "completed":
        status_class = "active"
        status_label = "<br><span style='font-size:0.7rem; color:#10B981; font-weight:bold;'>⚡ MONITORING</span>"
    elif st.session_state.workflow_status == "completed":
        status_class = "active"
        status_label = "<br><span style='font-size:0.7rem; color:#10B981; font-weight:bold;'>✓ STABILIZED</span>"
    else:
        status_label = "<br><span style='font-size:0.7rem; color:#64748B;'>● IDLE</span>"
        
    nodes_html += f'<div class="flow-node {status_class}">{node["name"]}{status_label}</div>'
    if i < len(config["nodes"]) - 1:
        nodes_html += '<div class="flow-arrow">➔</div>'

st.markdown(
    f"""
    <div class="flow-container">
        {nodes_html}
    </div>
    """,
    unsafe_allow_html=True
)

# 2. Metrics Grid Section (Formatted premium cards)
st.markdown("### 📈 Value Chain Telemetry")
cols = st.columns(4)

for idx, (key, m) in enumerate(metrics.items()):
    alert_class = "alert" if m["is_alert"] else ("success" if st.session_state.workflow_status == "completed" else "")
    delta_class = "delta-up" if m["is_delta_up"] else "delta-down"
    
    # Format large numeric values nicely (like dollar amounts)
    raw_val = m["value"]
    if isinstance(raw_val, (int, float)) and raw_val > 1000:
        formatted_val = f"${raw_val:,.0f}"
    else:
        formatted_val = f"{raw_val}"
        
    cols[idx].markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{m["label"]}</div>
            <div class="metric-val {alert_class}">{formatted_val}{m["unit"]}</div>
            <div class="metric-delta {delta_class}">{m["delta"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("") # Spacer

# 3. Interactive Console (Split Layout: Chat Left, Control Panel Right)
st.markdown("### 🖥️ Cognitive Command Console")
console_left, console_right = st.columns([1.1, 1.3])

with console_left:
    st.markdown("#### 💬 Intelligent Assistant")
    
    # Chat container box
    chat_box = st.container(height=350, border=True)
    with chat_box:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                thinking_html = ""
                if msg.get("thinking"):
                    thinking_html = f'<div class="agent-thinking">💭 Thought Process: {msg["thinking"]}</div>'
                st.markdown(f'<div class="chat-bubble-agent">{thinking_html}{msg["content"]}</div>', unsafe_allow_html=True)
                
    # Quick replies
    st.markdown("<p style='font-size:0.8rem; font-weight:600; color:#94A3B8; margin-bottom:4px;'>Quick Queries:</p>", unsafe_allow_html=True)
    quick_cols = st.columns(len(config["quick_replies"]))
    for q_idx, reply in enumerate(config["quick_replies"]):
        if quick_cols[q_idx].button(reply, key=f"qr_{q_idx}", use_container_width=True):
            handle_user_message(reply)
            st.rerun()

    # Custom chat input
    user_input = st.chat_input("Ask the agent anything about this bottleneck...")
    if user_input:
        handle_user_message(user_input)
        st.rerun()

with console_right:
    st.markdown("#### ⚙️ Automation & Approvals")
    
    tab_diag, tab_reco, tab_auto, tab_repo = st.tabs([
        "🔍 Root Cause Diagnosis", 
        "💡 Recommendations", 
        "⚡ Approval & Automation", 
        "📝 Business Impact Report"
    ])
    
    with tab_diag:
        st.markdown("**Incident Analysis Report**")
        st.markdown(
            f"The diagnostic engine has isolated an anomaly located in the **{config['nodes'][1]['name']}** stage of the value chain."
        )
        
        # Log Box
        log_box_content = ""
        for log in config["diagnosis_logs"]:
            log_box_content += f"<div style='margin-bottom:6px;'>{log}</div>"
            
        st.markdown(
            f"""
            <div style="background-color:#070B13; color:#06B6D4; font-family:monospace; font-size:0.8rem; padding:16px; border-radius:8px; border:1px solid rgba(255,255,255,0.05); height:200px; overflow-y:auto;">
                {log_box_content}
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with tab_reco:
        st.markdown("**Actionable Agent Directives**")
        
        for r_idx, reco in enumerate(config["recommendations"]):
            st.markdown(
                f"""
                <div style="background: rgba(30, 41, 59, 0.3); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px; margin-bottom: 12px;">
                    <span style="font-size: 0.95rem; font-weight: 600; color:#818CF8;">Directive #{r_idx+1}: {reco['title']}</span>
                    <p style="font-size: 0.85rem; color: #E2E8F0; margin: 4px 0;">{reco['description']}</p>
                    <span style="font-size: 0.8rem; font-weight: 600; color: #34D399;">Projected Impact: {reco['impact']}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    with tab_auto:
        status = st.session_state.workflow_status
        steps = config["automation_steps"]
        curr_idx = st.session_state.current_step_index
        
        if status == "diagnosed":
            st.info("System is awaiting authorization to trigger the automated resolution scripts.")
            
            # Action approval button
            if st.button("✓ AUTHORIZE & EXECUTE ACTION SYSTEM", key="auth_btn"):
                st.session_state.workflow_status = "running_automation"
                st.session_state.current_step_index = 0
                st.session_state.automation_progress = 0.0
                st.rerun()
                
        elif status == "running_automation":
            st.warning("⚠️ EXECUTION IN PROGRESS: Autonomous routing underway. Please do not close this session.")
            st.progress(st.session_state.automation_progress)
            
        elif status == "completed":
            st.success("🎉 EXECUTION COMPLETE: Value chain has been stabilized. Operations returned to target KPIs.")
            if st.button("Reset Simulation Scenario", key="reset_btn"):
                # Clean up session state and re-initialize
                del st.session_state["industry"]
                st.rerun()
                
        # Tasks list visualization
        st.markdown("---")
        st.markdown("**Automation Sequence Checklist:**")
        
        for t_idx, step in enumerate(steps):
            task_status = "pending"
            task_class = ""
            status_dot_class = ""
            icon = "○"
            
            if status == "completed" or t_idx < curr_idx:
                task_status = "completed"
                task_class = "completed"
                status_dot_class = "completed"
                icon = "✓"
            elif status == "running_automation" and t_idx == curr_idx:
                task_status = "running"
                task_class = "running"
                status_dot_class = "running"
                icon = "⚙"
                
            st.markdown(
                f"""
                <div class="auto-task {task_class}">
                    <div class="status-dot {status_dot_class}"></div>
                    <div style="flex-grow: 1;">
                        <span style="font-size:0.85rem; font-weight:600; color:{'#10B981' if task_status == 'completed' else ('#F97316' if task_status == 'running' else '#64748B')};">{step['title']}</span>
                        <p style="font-size:0.75rem; color:#94A3B8; margin:2px 0 0 0;">{step['detail'] if task_status != 'pending' else 'Queue position locked, pending predecessor step.'}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
    with tab_repo:
        if st.session_state.workflow_status != "completed":
            st.info("The Business Impact Report will be generated once the automation sequence completes.")
            st.markdown(
                """
                <div style="text-align:center; padding:40px; color:#64748B;">
                    <span style="font-size:3rem;">🔒</span>
                    <p style="margin-top:12px; font-size:0.85rem;">Report locked. Authorize automation to build metrics analysis.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            # Build and render the report with current timestamp and details
            report_body = config["report_template"]
            st.success("Executive business report compiled successfully.")
            
            report_box = st.container(height=280, border=True)
            with report_box:
                st.markdown(report_body)
                
            # Allow user to download report
            filename = f"Business_Impact_Report_{selected_key}.md"
            st.download_button(
                label="📥 DOWNLOAD EXECUTIVE REPORT (.MD)",
                data=report_body,
                file_name=filename,
                mime="text/markdown"
            )
