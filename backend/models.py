from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Request(Base): # <-- UPGRADED: Replaces InputData!
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    request_type = Column(String, nullable=False) # 'TRAIN' or 'MAINTENANCE'
    name = Column(String, nullable=False)          # Train Name OR Maintenance Task Description (e.g., "Track Defect 402")
    start_time = Column(DateTime, default=datetime.utcnow) # When the request needs to happen
    end_time = Column(DateTime, nullable=True)       # For maintenance blocks (if known)
    
    # --- NEW FIELDS FOR PRIORITY/IMPACT (TMS/SMMS/TDMS Integration) ---
    criticality = Column(String, default='MEDIUM') # HIGH, MEDIUM, LOW
    urgency = Column(String, default='MEDIUM')     # HIGH, MEDIUM, LOW
    impact_score = Column(Float, default=0.0)      # Calculated impact (e.g., 1.0 for critical track failure)

class OptimizedPlan(Base): # This represents the *scheduled* version of a Request
    __tablename__ = "optimized_plans"
    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("requests.id")) 
    plan_name = Column(String, nullable=False)
    optimization_score = Column(Float, default=0.0) # Percentage utilization (of total requests)
    generated_at = Column(DateTime, default=datetime.utcnow())
    # --- NEW FIELDS FOR VISUALIZATION ---
    start_time = Column(DateTime, nullable=True) 
    end_time = Column(DateTime, nullable=True)
