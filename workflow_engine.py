import time
import streamlit as st

try:
    from valchain_utils.scenarios import SCENARIOS
except ImportError:
    from utils.scenarios import SCENARIOS

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
            # General fallback responses depending on state
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
