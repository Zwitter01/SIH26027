# 🏆 FINAL SIH PRESENTATION SCRIPT — TEAM CODEX (SIH26027)

> **Flow of Presentation:**
> 1. **Ujjawal Yadav:** Greet judges + SIH Problem Statement (SIH26027) + Solution overview + Handover to Tech Team
> 2. **Kvish (You):** Complete Backend explanation (Python, FastAPI, OR-Tools CP-SAT, 4-Factor Scorer, Shadow Blocking)
> 3. **Abhinav:** Frontend explanation (React + Vite, Tailwind CSS, D3.js Stringline Marey chart)
> 4. **Kvish (You):** Transition dialogue ("Now we are going to show how our website works...")
> 5. **Live Demo:** Gaurav (VS Code & servers setup ready) + **Kvish conducts the full live walkthrough**
> 6. **Sakshi:** Impact, Benefits & Feasibility
> 7. **Nandini:** References, Audit data & Closing Q&A invitation

---

---

## 🎬 ACT 1: GREETING & PROBLEM STATEMENT

### 🎤 Speaker 1: UJJAWAL YADAV (Time: ~45-50 seconds)

> **[Slide 1 & Slide 2 on Screen]**

**Ujjawal:**
> *"Respected judges and panel members, a very good morning/afternoon to all of you. We are **Team CODEX**, presenting our solution for Problem Statement **SIH26027** under the Ministry of Railways:*
>
> ***'AI-Powered Automatic Block Planning to Maximize Asset Availability for Train Operations on Indian Railways.'***
>
> *Indian Railways is the 4th largest rail network in the world, running over 13,000 passenger and freight trains daily. But maintenance planning today is heavily manual, fragmented, and paper-based.*
>
> *Three core departments work in complete silos:*
> - *Civil Engineering manages tracks via **TMS**,*
> - *Electrical department manages OHE power lines via **TDMS**, and*
> - *Signalling & Telecom operates via **SMMS**.*
>
> *They coordinate through manual phone calls and registers. The alarming result? According to official **CAG Audit Reports**, **30% to 35% of sanctioned maintenance blocks go underutilized or cancelled**, while corridor availability drops down to 91%.*
>
> *To solve this critical bottleneck, our team has built an intelligent, end-to-end automated platform that combines multi-departmental demands and optimizes corridor maintenance with mathematical zero-collision safety.*
>
> *Now, I would like to invite our Tech Lead, **Kvish**, to explain our technical architecture and backend optimization engine."*

---

---

## ⚙️ ACT 2: TECHNICAL ARCHITECTURE & TECH STACK

### 🎤 Speaker 2: KVISH (YOU) — Complete Backend Explanation (Time: ~75-90 seconds)

> **[Slide 4: Technical Approach / System Architecture on Screen]**

**Kvish (You):**
> *"Thank you, Ujjawal. Respected judges, let me walk you through our backend architecture and the core engine that powers this system.*
>
> *When designing the backend, we had two critical requirements:*
> 1. *It must process complex multi-variable scheduling in **sub-second time**, and*
> 2. *It must guarantee **100% railway safety with zero conflicts**.*
>
> ### 1. Why Python & FastAPI?
> *We chose **Python** because it has the industry-standard ecosystem for operations research and optimization algorithms. On top of Python, we built our microservices using **FastAPI**.*
> *Why FastAPI instead of Django or Flask? Because FastAPI is built on ASGI and `asyncio`, allowing asynchronous, non-blocking I/O. When hundreds of station controllers query corridor schedules simultaneously, FastAPI handles concurrent requests with sub-5 millisecond latency. Plus, it gives us automatic schema validation via **Pydantic** and auto-generated OpenAPI documentation.*
>
> ### 2. Database Architecture (SQLite & PostgreSQL / pgAdmin 4):
> *For our data layer, we designed a clean relational schema using **SQLAlchemy ORM**.*
> *In our local development and prototype, we use **SQLite with Write-Ahead Logging (WAL mode)**, enabling high-concurrency zero-lock reads.*
> *For production deployment, our system connects directly to **PostgreSQL managed via pgAdmin 4**. Because we use SQLAlchemy ORM, switching between SQLite and PostgreSQL requires zero code changes — just updating the connection string.*
>
> ### 3. Why Google OR-Tools CP-SAT instead of Machine Learning? (⭐ MOST IMPORTANT)
> *Judges often ask: 'Why not use Deep Learning or Neural Networks?'*
> *The answer is simple: **In railway operations, safety cannot be probabilistic.** A machine learning model might be 95% accurate, but that remaining 5% error could schedule a passenger train and a track renewal machine on the same track at the same time — which is fatal.*
> *Instead, we implemented **Google OR-Tools CP-SAT (Constraint Programming with Boolean Satisfiability)**. We model train paths and maintenance windows as `IntervalVar` objects and enforce hard mathematical constraints using `AddNoOverlap()`. This gives a **mathematical guarantee of ZERO collision** solved in less than **0.06 seconds** for a 131-kilometer corridor.*
>
> ### 4. Our Two Core Innovations:
> - *First, the **4-Factor AI Priority Scorer**: Every incoming maintenance request is mathematically scored across 4 dynamic parameters:*
>   - *Urgency (40%)*
>   - *Safety Impact (30%)*
>   - *Overdue Days (20%), and*
>   - *Section Speed Class (10%).*
> - *Second, **Shadow Block Co-Scheduling**: If the Civil department books a track section for tamping, our algorithm scans whether Traction (OHE) or Signalling also have pending maintenance within that same 10-kilometer section. If yes, it bundles them into a **single coordinated Mega Block** during the night window (01:00 to 05:00 AM).*
> *The track is closed **once instead of three times**, saving up to 40% cumulative track downtime!*
>
> *Now, my teammate **Abhinav** will explain our frontend architecture and visual interface."*

---

---

### 🎤 Speaker 3: ABHINAV — Frontend Explanation (Time: ~35-45 seconds)

> **[Still on Slide 4 / pointing to Frontend section]**

**Abhinav:**
> *"Thank you, Kvish. Respected judges, railway section controllers work in high-stress, real-time environments. They cannot navigate cluttered spreadsheets or complex forms.*
>
> *Our frontend is built using **React with Vite and TypeScript** for ultra-fast, type-safe rendering and hot-reloading.*
>
> *For the design system, we utilized **Tailwind CSS**, allowing us to create a high-contrast, clean dark and light interface that conforms to modern operational dashboards.*
>
> *The highlight of our frontend is the **Interactive Stringline (Marey) Diagram powered by D3.js**.*
> *For over a century, Indian Railways controllers have used paper stringline charts where the X-axis represents 24 hours of time, the Y-axis represents corridor kilometer distance, and diagonal lines represent train trajectories.*
> *We digitized this using D3.js vector graphics. Whenever Kvish's optimization engine runs, D3 dynamically renders maintenance block corridors as shaded safe zones and plots train lines around them in real-time, with hover tooltips and instant conflict alerts.*
>
> *Now, I hand it back to Kvish to present our live working prototype."*

---

---

## 💻 ACT 3: LIVE DEMO TRANSITION & EXECUTION

### 🎤 Speaker 2: KVISH (YOU) — Transition Speech

**Kvish (You):**
> *"Thank you, Abhinav.*
>
> ***Now, we are going to show you how our system works in real-time.***
> *My teammate **Gaurav** has the complete development environment and servers running live on our system."*

---

### 🖥️ LIVE DEMO WALKTHROUGH BY KVISH (YOU) + GAURAV (Time: ~60-75 seconds)

> *(Gaurav is managing the screen / switching windows, Kvish speaks with authority and points at the screen)*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LIVE DEMO STEP-BY-STEP ACTIONS                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Step 1: Show VS Code Project Structure (10 seconds)
*(Screen shows VS Code)*

**Kvish (You):**
> *"As you can see on the screen in VS Code, our project is organized cleanly:*
> - *In the `backend/` directory, we have `main.py` containing our FastAPI microservice endpoints and `database.py` with SQLAlchemy models.*
> - *In the `frontend/` directory, we have our React and Vite application with TypeScript and D3 charting modules.*
> - *In the terminal, our FastAPI server is live on `http://127.0.0.1:8000` and our frontend dev server is running on `http://localhost:5173`."*

---

#### Step 2: Show pgAdmin 4 / Database (10 seconds)
*(Gaurav briefly switches to pgAdmin 4 or shows `railway_planner.db`)*

**Kvish (You):**
> *"Here in our database layer, we maintain the tables for incoming maintenance requests from TMS, TDMS, and SMMS, along with train timetables from COA and the resulting optimized schedules."*

---

#### Step 3: Open Dashboard & Explain Corridor Baseline (20 seconds)
*(Gaurav switches to Chrome browser at `http://127.0.0.1:8000`)*

**Kvish (You):**
> *"This is our live operational dashboard. We are demonstrating this on our pilot testbed:*
> ***The New Delhi (NDLS) to Aligarh Junction (ALJN) mainline corridor — 131.2 kilometers of high-density track.***
>
> *Before optimization, look at our baseline KPI cards:*
> - *Corridor Availability is sitting at **91.2%**,*
> - *We have 10 unscheduled maintenance requests from Civil, Electrical, and Signal teams,*
> - *Multiple departments have overlapping demands on the same physical track sections."*

---

#### Step 4: Click "Run AI Optimizer" & Show Results (25 seconds)
*(Gaurav clicks the blue/green **"Run AI Optimizer"** button on screen)*

**Kvish (You):**
> *"Now watch as we trigger the optimization engine.*
>
> *(Button clicked — results load instantly)*
>
> *In just **0.058 seconds** — less than 60 milliseconds:*
> 1. *The CP-SAT solver scheduled all 10 maintenance requests with **ZERO train conflicts**.*
> 2. *Look at the top KPI card: **Corridor Availability jumped from 91.2% to 96.6% — a net gain of +5.4%!***
> 3. *And right here: **4 Coordinated Shadow Blocks were automatically created**, bundling Civil track tamping with OHE power blocks in the same night window (01:00 AM to 04:30 AM).*
> 4. *The system also auto-generated the statutory **Form 351 Joint Disconnection Notice**, ready for the Section Controller's digital sign-off.*
>
> *Now, I invite **Sakshi** to present our project's impact and operational feasibility."*

---

---

## 📈 ACT 4: IMPACT, BENEFITS & FEASIBILITY

### 🎤 Speaker 4: SAKSHI (Time: ~40-45 seconds)

> **[Slide 5: Feasibility & Viability on Screen]**

**Sakshi:**
> *"Thank you, Kvish. Respected judges, our solution delivers measurable, high-impact benefits for Indian Railways:*
>
> ### 1. Quantifiable Operational Gains:
> - ***+5.4% Corridor Availability Gain:** On high-density freight and passenger corridors like Delhi-Howrah, even a 1% increase in availability translates to dozens of additional freight train paths and crores in freight revenue.*
> - ***Zero Bottlenecks:** Manual planning that takes 3 to 5 days of inter-departmental meetings is now executed in **under 0.06 seconds**.*
> - ***Elimination of Underutilized Blocks:** By auto-scheduling shadow blocks, we directly target the 30-35% block cancellation rate flagged by CAG audit reports.*
>
> ### 2. Non-Invasive Feasibility:
> - *Our system requires **no expensive hardware replacements**. It connects via lightweight REST APIs to CRIS's existing TMS, TDMS, SMMS, and COA servers.*
> - *It strictly adheres to **G&SR (General & Subsidiary Rules)** safety buffers (enforcing a mandatory 15-minute headway buffer).*
> - *And it is horizontally scalable across all 68 divisions and 17 Zonal Railways.*
>
> *Now, **Nandini** will conclude our presentation with our research benchmarks."*

---

---

## 📚 ACT 5: RESEARCH, REFERENCES & CONCLUSION

### 🎤 Speaker 5: NANDINI (Time: ~30-40 seconds)

> **[Slide 6: Research, References & Comparative Analysis on Screen]**

**Nandini:**
> *"Thank you, Sakshi. Respected judges, our design is grounded in extensive research and real railway operational data:*
>
> - *We benchmarked against the **Indian Railways Permanent Way Manual (IRPWM)**, **Indian Railways OHE Maintenance Manuals**, and the **CAG Report on Punctuality and Maintenance Utilization**.*
> - *In our comparative analysis against existing systems like CRIS TMS and legacy manual registers, our solution is the **only one offering multi-departmental co-scheduling, automated Form 351 compliance, and mathematical conflict-free guarantees**.*
>
> *To summarize: Team CODEX has transformed railway maintenance planning from reactive, manual paperwork into a proactive, intelligent, sub-second optimization engine.*
>
> *Thank you very much for your time. We are now eagerly open to your questions."*

---

---

## 🧠 KVISH'S QUICK CHEAT-SHEET (Tech Keywords to Remember on Stage)

| Question / Concept | Exactly What to Say |
|---|---|
| **Why not Machine Learning?** | *"ML is probabilistic (e.g. 95% accurate). In railway safety, 5% error means collisions. Google OR-Tools CP-SAT provides a **mathematical guarantee of 100% zero collision**."* |
| **What is Shadow Blocking?** | *"Civil, Traction, and Signal pending works in the same 10-km section are bundled into a single night mega-block (01:00-05:00). Track shuts once instead of three times."* |
| **Why FastAPI?** | *"Asynchronous ASGI architecture, handles concurrent controller requests with sub-5ms latency, Pydantic type validation, and auto Swagger docs."* |
| **Why SQLite & pgAdmin/PostgreSQL?** | *"SQLite with WAL mode for rapid zero-config local prototyping; production-ready PostgreSQL managed via pgAdmin 4 with instant migration via SQLAlchemy ORM."* |
| **Why D3.js?** | *"Digitizes the century-old Stringline (Marey) time-distance diagram with interactive SVG vectors and real-time updates."* |
| **What is Form 351?** | *"Indian Railways' statutory Joint Disconnection Notice / Permit-to-Work authorization."* |

---

# 🚀 ALL THE BEST TEAM CODEX! 🏆
