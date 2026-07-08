import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="\U0001f43e", layout="centered")
st.title("\U0001f43e PawPal+")
st.markdown("A smart pet care scheduler that sorts, filters, and detects conflicts.")

st.divider()

# ── Section 1: Owner & Pet setup ──────────────────────────────────────────────
st.subheader("1. Owner & Pet Info")

owner_name = st.text_input("Owner name", value="Frank")
pet_name   = st.text_input("Pet name",   value="Biscuit")
species    = st.selectbox("Species", ["dog", "cat", "other"])
breed      = st.text_input("Breed (optional)", value="")

if st.button("Set Owner & Pet"):
    owner = Owner(owner_name)
    pet   = Pet(pet_name, species, breed)
    owner.add_pet(pet)
    st.session_state.owner = owner
    st.session_state.pet   = pet
    st.success(f"Owner: {owner_name} | Pet: {pet_name} ({species})")

if "owner" not in st.session_state:
    st.info("Fill in owner and pet info above, then click Set Owner & Pet.")
    st.stop()

owner = st.session_state.owner
pet   = st.session_state.pet

st.divider()

# ── Section 2: Add tasks ──────────────────────────────────────────────────────
st.subheader("2. Add a Task")

col1, col2 = st.columns(2)
with col1:
    task_title = st.text_input("Task name", value="Morning walk")
    task_time  = st.text_input("Time (HH:MM)", value="08:00")
    duration   = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=30)
with col2:
    priority  = st.selectbox("Priority",  ["low", "medium", "high"], index=2)
    frequency = st.selectbox("Frequency", ["daily", "weekly", "none"])

if st.button("Add Task"):
    task = Task(task_title, task_time, int(duration), priority, frequency)
    pet.add_task(task)
    st.success(f"Added: {task_title} at {task_time}")

current_tasks = pet.get_tasks()
if current_tasks:
    st.markdown(f"**Current tasks for {pet.name}:**")
    for t in current_tasks:
        status = "done" if t.is_complete else "todo"
        st.markdown(f"- `{t.time}` — {t.description} ({t.duration} min) [{t.priority}] ({status})")
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# ── Section 3: Generate schedule ──────────────────────────────────────────────
st.subheader("3. Generate Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(owner)
    all_tasks = scheduler.get_todays_schedule()

    if not all_tasks:
        st.warning("No tasks to schedule. Add some tasks first.")
    else:
        sorted_tasks = scheduler.sort_by_time(all_tasks)
        conflict_msg = scheduler.check_conflicts(all_tasks)

        st.markdown("### Today's Schedule (sorted by time)")
        for t in sorted_tasks:
            st.markdown(f"- `{t.time}` — {t.description} ({t.duration} min) [{t.priority}]")

        st.divider()
        if "No conflicts" in conflict_msg:
            st.success(conflict_msg)
        else:
            st.warning(conflict_msg)

        st.divider()
        st.markdown("### High-Priority Tasks Only")
        high = scheduler.filter_tasks(all_tasks, priority="high")
        if high:
            for t in scheduler.sort_by_time(high):
                st.markdown(f"- `{t.time}` — {t.description} ({t.duration} min)")
        else:
            st.info("No high-priority tasks found.")
