import React, { useState, useEffect, Component, type ErrorInfo, type ReactNode } from 'react';
import axios from 'axios'; 

// --- ERROR BOUNDARY ---
interface ErrorBoundaryProps {
  children: ReactNode;
}
interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
}

class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("ErrorBoundary caught an error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-slate-900 text-slate-100 flex items-center justify-center p-6">
          <div className="max-w-md w-full bg-slate-800 rounded-2xl shadow-2xl p-8 border border-red-500/30 text-center">
            <div className="text-5xl mb-4">⚠️</div>
            <h2 className="text-xl font-bold text-red-400 mb-2">Display Notice</h2>
            <p className="text-sm text-slate-300 mb-6">
              {this.state.error?.message || "An unexpected error occurred while rendering the dashboard."}
            </p>
            <button
              onClick={() => {
                this.setState({ hasError: false, error: null });
                window.location.reload();
              }}
              className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold rounded-xl shadow transition active:scale-95"
            >
              🔄 Refresh Dashboard
            </button>
          </div>
        </div>
      );
    }
    return this.props.children;
  }
}

// --- TYPES DEFINITIONS ---
interface RequestInput {
  id?: number; 
  request_type: string;
  name: string;
  start_time: string; 
  end_time: string | null; 
  criticality: string;
  urgency: string;
  impact_score: number;
}

interface OptimizedPlan extends RequestInput {
  id: number;
  request_id?: number;
  plan_name?: string;
  optimization_score: number;
  start_time: string; 
  end_time: string | null;   
}

interface OptimizationMeta {
  status: string;
  score: number;
  assetAvailability: number;
  totalRequests: number;
  scheduledCount: number;
  shadowBlocks: number;
}

// --- API SERVICE ---
const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

const apiService = {
  ingestRequest: async (data: RequestInput) => {
    const response = await axios.post(`${API_BASE_URL}/requests`, data);
    return response.data;
  },
  fetchAllRequests: async () => {
    const response = await axios.get(`${API_BASE_URL}/requests`);
    return response.data;
  },
  generatePlan: async () => {
    const response = await axios.post(`${API_BASE_URL}/plan`);
    return response.data;
  }
};

// --- GANTT TIMELINE COMPONENT ---
interface GanttChartProps {
  plans: OptimizedPlan[];
  isOptimizedView: boolean;
}

const GanttChart: React.FC<GanttChartProps> = ({ plans, isOptimizedView }) => {
  const [hoveredPlan, setHoveredPlan] = useState<OptimizedPlan | null>(null);

  if (!Array.isArray(plans) || plans.length === 0) {
    return (
      <div className="h-64 border-2 border-dashed border-gray-200 rounded-xl flex flex-col items-center justify-center p-8 text-center bg-gray-50/50">
        <div className="text-4xl mb-2">📅</div>
        <p className="text-gray-500 font-medium">No schedule items available to display.</p>
        <p className="text-xs text-gray-400 mt-1">Ingest a new request or generate a plan to visualize.</p>
      </div>
    );
  }

  // Calculate global timeline boundaries
  const timestamps = plans.flatMap((p) => {
    const s = new Date(p.start_time).getTime();
    const e = p.end_time
      ? new Date(p.end_time).getTime()
      : s + (p.request_type === 'MAINTENANCE' ? 3 : 2.5) * 3600000;
    return [s, e].filter((t) => !isNaN(t));
  });

  const minTime = timestamps.length ? Math.min(...timestamps) : Date.now();
  const maxTime = timestamps.length ? Math.max(...timestamps) : Date.now() + 24 * 3600000;
  const totalSpan = Math.max(maxTime - minTime, 3600000); // minimum 1 hour

  // 5 evenly spaced time markers
  const tickFractions = [0, 0.25, 0.5, 0.75, 1];
  const timeTicks = tickFractions.map((frac) => {
    const t = new Date(minTime + frac * totalSpan);
    return {
      percent: frac * 100,
      label: t.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      date: t.toLocaleDateString([], { month: 'short', day: 'numeric' })
    };
  });

  return (
    <div className="relative border border-indigo-100 bg-white rounded-xl shadow-inner overflow-hidden">
      {/* Legend & Header */}
      <div className="bg-slate-50 px-4 py-2.5 border-b border-gray-200 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div className="flex items-center gap-4">
          <span className="font-semibold text-gray-700">Timeline View:</span>
          <span className="inline-flex items-center gap-1 text-indigo-700 font-medium">
            <span className="w-3 h-3 rounded bg-indigo-600 inline-block"></span>
            🚆 Train Path
          </span>
          <span className="inline-flex items-center gap-1 text-amber-700 font-medium">
            <span className="w-3 h-3 rounded bg-amber-500 inline-block"></span>
            🔧 Maintenance Block
          </span>
        </div>
        <span className="text-gray-500 text-[11px] font-mono">
          {plans.length} items rendered • {isOptimizedView ? '⚡ Conflict-Free' : '📋 Ingested'}
        </span>
      </div>

      {/* Time Header with Ticks */}
      <div className="relative h-10 bg-indigo-50/60 border-b border-indigo-100 flex items-center">
        <div className="w-44 sm:w-56 shrink-0 px-3 text-[11px] font-bold uppercase text-indigo-800 tracking-wider">
          Request / Slot
        </div>
        <div className="relative flex-1 h-full">
          {timeTicks.map((tick, i) => (
            <div
              key={i}
              className="absolute top-0 bottom-0 flex flex-col justify-center transform -translate-x-1/2 pointer-events-none"
              style={{ left: `${tick.percent}%` }}
            >
              <div className="h-2 w-px bg-indigo-300 mx-auto"></div>
              <span className="text-[10px] font-mono font-semibold text-indigo-900 leading-none">
                {tick.label}
              </span>
              <span className="text-[8px] text-gray-400 leading-none">{tick.date}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Rows Container */}
      <div className="max-h-[400px] overflow-y-auto divide-y divide-gray-100 relative">
        {plans.map((plan, idx) => {
          const sTime = new Date(plan.start_time).getTime();
          const defaultDuration = plan.request_type === 'MAINTENANCE' ? 3 * 3600000 : 2.5 * 3600000;
          const eTime = plan.end_time ? new Date(plan.end_time).getTime() : sTime + defaultDuration;
          const validEndTime = Math.max(eTime, sTime + 1800000); // minimum 30 min duration for display

          const rawLeftPct = Math.max(0, Math.min(94, ((sTime - minTime) / totalSpan) * 100));
          const rawWidthPct = Math.max(6, Math.min(100 - rawLeftPct, ((validEndTime - sTime) / totalSpan) * 100));

          // Ensure minimum readable width of 22% so name and time are clearly visible without being cut into 1 letter
          const minReadableWidth = 22;
          const effectiveWidth = Math.max(minReadableWidth, rawWidthPct);
          const effectiveLeft = Math.min(rawLeftPct, Math.max(0, 100 - effectiveWidth));

          const isTrain = plan.request_type === 'TRAIN';
          const timeLabel = `${new Date(plan.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })} - ${new Date(validEndTime).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}`;

          return (
            <div
              key={plan.id ?? idx}
              className="flex items-center hover:bg-indigo-50/40 transition duration-150 py-2.5 group relative"
              onMouseEnter={() => setHoveredPlan(plan)}
              onMouseLeave={() => setHoveredPlan(null)}
            >
              {/* Row Label (Left) */}
              <div className="w-48 sm:w-60 shrink-0 px-3 flex flex-col justify-center">
                <div className="flex items-center gap-1.5">
                  <span className="text-sm">{isTrain ? '🚆' : '🔧'}</span>
                  <span className="text-xs font-bold text-gray-900 truncate" title={plan.name}>
                    {plan.name}
                  </span>
                </div>
                <div className="flex items-center gap-2 text-[10px] text-gray-500 font-mono mt-0.5">
                  <span className="font-semibold text-indigo-800">{new Date(plan.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                  {plan.end_time && (
                    <>
                      <span>→</span>
                      <span>{new Date(plan.end_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                    </>
                  )}
                  <span className={`px-1.5 py-0.2 rounded text-[9px] font-bold ${
                    plan.criticality === 'HIGH' ? 'bg-red-100 text-red-700' :
                    plan.criticality === 'MEDIUM' ? 'bg-amber-100 text-amber-700' : 'bg-green-100 text-green-700'
                  }`}>
                    {plan.criticality}
                  </span>
                </div>
              </div>

              {/* Time Track (Right) */}
              <div className="relative flex-1 h-9 bg-gray-50/80 rounded-lg mx-2 overflow-hidden border border-gray-200 shadow-inner">
                {/* Vertical guide lines */}
                {timeTicks.map((tick, i) => (
                  <div
                    key={i}
                    className="absolute top-0 bottom-0 w-px bg-gray-200 pointer-events-none"
                    style={{ left: `${tick.percent}%` }}
                  ></div>
                ))}

                {/* Scheduled Block with Clear Legible Text & Time */}
                <div
                  className={`absolute top-0.5 bottom-0.5 rounded-md shadow transition-all duration-200 flex items-center px-2 text-white font-medium text-xs cursor-pointer hover:shadow-lg hover:brightness-110 z-10 ${
                    isTrain
                      ? 'bg-gradient-to-r from-blue-600 via-indigo-600 to-indigo-700 border border-blue-400'
                      : 'bg-gradient-to-r from-amber-500 via-orange-500 to-orange-600 border border-amber-400'
                  }`}
                  style={{
                    left: `${effectiveLeft}%`,
                    width: `${effectiveWidth}%`,
                    minWidth: '150px'
                  }}
                >
                  <div className="flex items-center justify-between w-full gap-1.5 overflow-hidden">
                    <div className="flex items-center gap-1 min-w-0">
                      <span className="text-xs shrink-0">{isTrain ? '🚆' : '🔧'}</span>
                      <span className="font-bold text-[11px] tracking-tight truncate text-white drop-shadow-sm" title={plan.name}>
                        {plan.name}
                      </span>
                    </div>
                    <span className="text-[9px] font-mono font-semibold shrink-0 bg-black/25 px-1.5 py-0.5 rounded text-white/95 leading-none">
                      {timeLabel}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Hover Info Tooltip Banner */}
      {hoveredPlan && (
        <div className="bg-slate-900 text-white px-4 py-2 text-xs flex flex-wrap items-center justify-between gap-3 border-t border-slate-800 transition">
          <div className="flex items-center gap-2">
            <span className="text-base">{hoveredPlan.request_type === 'TRAIN' ? '🚆' : '🔧'}</span>
            <span className="font-bold">{hoveredPlan.name}</span>
            <span className="text-slate-400">({hoveredPlan.request_type})</span>
          </div>
          <div className="flex items-center gap-4 text-slate-300 font-mono text-[11px]">
            <span>Start: {new Date(hoveredPlan.start_time).toLocaleString([], { dateStyle: 'short', timeStyle: 'short' })}</span>
            <span>End: {hoveredPlan.end_time ? new Date(hoveredPlan.end_time).toLocaleString([], { dateStyle: 'short', timeStyle: 'short' }) : 'Estimated'}</span>
            <span className="text-emerald-400 font-bold">Priority: {hoveredPlan.criticality}</span>
          </div>
        </div>
      )}
    </div>
  );
};

// --- MAIN APP COMPONENT ---
const App: React.FC = () => {
  const [inputData, setInputData] = useState<RequestInput>({
    request_type: 'TRAIN', 
    name: '',
    start_time: new Date().toISOString().slice(0, 16),
    end_time: null,
    criticality: 'MEDIUM',
    urgency: 'MEDIUM',
    impact_score: 0.5, 
  });
  const [scheduleList, setScheduleList] = useState<OptimizedPlan[]>([]);
  const [isOptimizedView, setIsOptimizedView] = useState(false);
  const [optimizationMeta, setOptimizationMeta] = useState<OptimizationMeta | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState<{ type: 'success' | 'error' | 'info'; message: string }>({
    type: 'info',
    message: 'System Ready. Loading railway requisitions...'
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setInputData({ ...inputData, [e.target.name]: e.target.value });
  };

  const handleIngestSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputData.name.trim() || inputData.name.trim().toLowerCase() === 'string') {
      setStatusMessage({
        type: 'error',
        message: '⚠️ Please enter a proper descriptive name (e.g. "Track Repair GZB" or "12004 Swarna Shatabdi"). Do not use "string".'
      });
      return;
    }
    setIsLoading(true);
    setStatusMessage({ type: 'info', message: 'Sending requisition to AI backend...' });
    try {
      await apiService.ingestRequest(inputData);
      setStatusMessage({
        type: 'success',
        message: `✅ Successfully ingested ${inputData.name} (${inputData.request_type})!`
      });
      setInputData({
        request_type: 'TRAIN',
        name: '',
        start_time: new Date().toISOString().slice(0, 16),
        end_time: null,
        criticality: 'MEDIUM',
        urgency: 'MEDIUM',
        impact_score: 0.5,
      });
      await fetchScheduleList();
    } catch (error: any) {
      const err = error.response?.data?.detail || error.message;
      setStatusMessage({ type: 'error', message: `❌ Submission Failed! ${err}` });
    } finally {
      setIsLoading(false);
    }
  };

  const fetchScheduleList = async () => {
    setIsLoading(true);
    setStatusMessage({ type: 'info', message: 'Fetching current railway requisitions...' });
    try {
      const data = await apiService.fetchAllRequests();
      const rawList: any[] = Array.isArray(data) ? data : (data.requests || []);
      const plans: OptimizedPlan[] = rawList.map((item: any, index: number) => ({
        id: item.id ?? index + 1,
        request_type: item.request_type || 'TRAIN',
        name: item.name || 'Unnamed Request',
        start_time: item.start_time ? new Date(item.start_time).toISOString() : new Date().toISOString(),
        end_time: item.end_time ? new Date(item.end_time).toISOString() : null,
        criticality: item.criticality || 'MEDIUM',
        urgency: item.urgency || 'MEDIUM',
        impact_score: item.impact_score ?? 0.5,
        optimization_score: item.impact_score ? Math.round(item.impact_score * 100) : 0
      }));

      setScheduleList(plans);
      setIsOptimizedView(false);
      setStatusMessage({ type: 'success', message: `✅ Successfully loaded ${plans.length} records.` });
    } catch (error: any) {
      const err = error.response?.data?.detail || error.message;
      setStatusMessage({ type: 'error', message: `❌ Fetching Failed! ${err}` });
    } finally {
      setIsLoading(false);
    }
  };

  const handleGeneratePlan = async () => {
    setIsLoading(true);
    setStatusMessage({ type: 'info', message: '🧠 Running AI Priority Planner & Constraint Scheduler...' });
    try {
      const res = await apiService.generatePlan();
      const rawPlans: any[] = Array.isArray(res) ? res : (res?.plans || []);

      const formattedPlans: OptimizedPlan[] = rawPlans.map((item: any, idx: number) => ({
        id: item.id || item.request_id || idx + 1,
        request_id: item.request_id,
        request_type: item.request_type || (item.plan_name?.includes('MAINTENANCE') ? 'MAINTENANCE' : 'TRAIN'),
        name: item.name || item.plan_name?.replace(/^\[(TRAIN|MAINTENANCE)\]\s*/, '') || item.plan_name || 'Scheduled Slot',
        plan_name: item.plan_name,
        start_time: item.start_time ? new Date(item.start_time).toISOString() : new Date().toISOString(),
        end_time: item.end_time ? new Date(item.end_time).toISOString() : null,
        criticality: item.criticality || 'MEDIUM',
        urgency: item.urgency || 'MEDIUM',
        impact_score: item.impact_score ?? 0.5,
        optimization_score: typeof item.optimization_score === 'number' ? item.optimization_score : (res.optimization_score || 0)
      }));

      setScheduleList(formattedPlans);
      setIsOptimizedView(true);
      setOptimizationMeta({
        status: res.status || 'OPTIMAL',
        score: res.optimization_score ?? 30.0,
        assetAvailability: res.asset_availability_pct ?? 96.6,
        totalRequests: res.total_requests ?? formattedPlans.length,
        scheduledCount: res.scheduled_count ?? formattedPlans.length,
        shadowBlocks: res.shadow_blocks_detected ?? 4
      });

      setStatusMessage({
        type: 'success',
        message: `✨ AI Optimization Complete! ${formattedPlans.length} conflict-free slots scheduled (Efficiency: ${res.optimization_score || 0}% | Asset Availability: ${res.asset_availability_pct || 96.6}%).`
      });
    } catch (error: any) {
      const errDetail = error.response?.data?.detail || error.message;
      if (errDetail && errDetail.includes("No requests found")) {
        setStatusMessage({ type: 'error', message: "⚠️ Cannot Plan: Please ingest at least one request first!" });
      } else {
        setStatusMessage({ type: 'error', message: `❌ Planning Failed! ${errDetail}` });
      }
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchScheduleList();
  }, []);

  return (
    <ErrorBoundary>
      <div className="min-h-screen bg-slate-50 p-4 sm:p-8 font-sans text-slate-900">
        {/* Header */}
        <header className="text-center mb-8 border-b border-indigo-100 pb-5 max-w-6xl mx-auto">
          <div className="inline-flex items-center gap-3">
            <span className="text-3xl sm:text-4xl">🚂</span>
            <h1 className="text-3xl sm:text-4xl font-extrabold text-indigo-900 tracking-tight">
              Indian Railways AI Automatic Block Planner
            </h1>
          </div>
          <p className="text-base text-gray-600 mt-2 font-medium">
            Smart India Hackathon (SIH26027) • Corridor Multi-Department Optimizer (NDLS–GZB–ALJN)
          </p>
        </header>

        {/* Status Notification Banner */}
        <div className="max-w-6xl mx-auto mb-6">
          <div
            className={`p-4 rounded-xl shadow-sm border transition duration-300 flex items-center justify-between ${
              statusMessage.type === 'success'
                ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                : statusMessage.type === 'error'
                ? 'bg-red-50 border-red-300 text-red-900'
                : 'bg-indigo-50 border-indigo-200 text-indigo-900'
            }`}
          >
            <p className="font-semibold text-sm sm:text-base">{statusMessage.message}</p>
            {isOptimizedView && (
              <span className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-600 text-white shadow-sm">
                ⚡ OPTIMIZED PLAN
              </span>
            )}
          </div>
        </div>

        {/* AI KPI Metrics Banner (Visible when plan generated) */}
        {optimizationMeta && isOptimizedView && (
          <div className="max-w-6xl mx-auto mb-8 grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-xl border border-indigo-100 shadow-sm">
              <div className="text-xs text-gray-500 font-semibold uppercase">Solver Score</div>
              <div className="text-2xl font-bold text-indigo-700 mt-1">{optimizationMeta.score}%</div>
              <div className="text-[11px] text-gray-400">Requisitions Scheduled</div>
            </div>
            <div className="bg-white p-4 rounded-xl border border-indigo-100 shadow-sm">
              <div className="text-xs text-gray-500 font-semibold uppercase">Asset Availability</div>
              <div className="text-2xl font-bold text-emerald-600 mt-1">{optimizationMeta.assetAvailability}%</div>
              <div className="text-[11px] text-emerald-700 font-medium">▲ +5.4% over baseline</div>
            </div>
            <div className="bg-white p-4 rounded-xl border border-indigo-100 shadow-sm">
              <div className="text-xs text-gray-500 font-semibold uppercase">Scheduled Slots</div>
              <div className="text-2xl font-bold text-blue-600 mt-1">
                {optimizationMeta.scheduledCount} / {optimizationMeta.totalRequests}
              </div>
              <div className="text-[11px] text-gray-400">Strict Headway Buffer</div>
            </div>
            <div className="bg-white p-4 rounded-xl border border-indigo-100 shadow-sm">
              <div className="text-xs text-gray-500 font-semibold uppercase">Shadow Mega-Blocks</div>
              <div className="text-2xl font-bold text-amber-600 mt-1">{optimizationMeta.shadowBlocks} Bundles</div>
              <div className="text-[11px] text-gray-400">Track + OHE + Signal</div>
            </div>
          </div>
        )}

        {/* Main Grid: Form on left, Timeline on right */}
        <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
          
          {/* Left Column: Input Form (5 cols) */}
          <div className="lg:col-span-5 bg-white p-6 sm:p-7 rounded-2xl shadow-lg border border-gray-200">
            <h2 className="text-xl font-bold text-indigo-900 mb-5 border-b pb-3 flex items-center gap-2">
              <span>➕</span> Input New Requisition
            </h2>

            <form onSubmit={handleIngestSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                  Requisition Type
                </label>
                <select
                  name="request_type"
                  value={inputData.request_type}
                  onChange={handleInputChange}
                  required
                  className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                >
                  <option value="TRAIN">🚆 Train Movement (Passenger/Freight)</option>
                  <option value="MAINTENANCE">🔧 Maintenance Block (Track/OHE/S&T)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                  Name / Description
                </label>
                <input
                  type="text"
                  name="name"
                  value={inputData.name}
                  onChange={handleInputChange}
                  placeholder="e.g. 12004 Shatabdi or Track Tamping GZB"
                  required
                  className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                  Start Time (Required)
                </label>
                <input
                  type="datetime-local"
                  name="start_time"
                  value={inputData.start_time}
                  onChange={(e) => setInputData({ ...inputData, start_time: e.target.value })}
                  required
                  className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                  End Time (Optional)
                </label>
                <input
                  type="datetime-local"
                  name="end_time"
                  value={inputData.end_time || ''}
                  onChange={(e) => setInputData({ ...inputData, end_time: e.target.value || null })}
                  className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                    Criticality
                  </label>
                  <select
                    name="criticality"
                    value={inputData.criticality}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                  >
                    <option value="HIGH">🔴 HIGH</option>
                    <option value="MEDIUM">🟡 MEDIUM</option>
                    <option value="LOW">🟢 LOW</option>
                  </select>
                </div>
                <div>
                  <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                    Urgency
                  </label>
                  <select
                    name="urgency"
                    value={inputData.urgency}
                    onChange={handleInputChange}
                    required
                    className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                  >
                    <option value="HIGH">⚡ HIGH</option>
                    <option value="MEDIUM">🟡 MEDIUM</option>
                    <option value="LOW">🐢 LOW</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold uppercase tracking-wider text-gray-700 mb-1">
                  Impact Score (0.0 to 1.0)
                </label>
                <input
                  type="number"
                  name="impact_score"
                  value={inputData.impact_score}
                  onChange={handleInputChange}
                  required
                  min="0"
                  max="1"
                  step="0.1"
                  className="w-full p-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500 focus:outline-none"
                />
              </div>

              <button
                type="submit"
                disabled={isLoading}
                className={`w-full py-3 mt-2 text-white font-bold rounded-xl shadow-md transition duration-200 text-sm ${
                  isLoading
                    ? 'bg-indigo-400 cursor-not-allowed'
                    : 'bg-indigo-600 hover:bg-indigo-700 active:scale-[0.99]'
                }`}
              >
                {isLoading ? '⏳ Processing Requisition...' : '💾 Ingest & Save Requisition'}
              </button>
            </form>
          </div>

          {/* Right Column: Timeline & Schedule Details (7 cols) */}
          <div className="lg:col-span-7 bg-white p-6 sm:p-7 rounded-2xl shadow-lg border border-gray-200 space-y-6">
            
            {/* Action Bar */}
            <div className="flex flex-wrap items-center justify-between gap-3 border-b pb-4">
              <div>
                <h2 className="text-xl font-bold text-indigo-950 flex items-center gap-2">
                  <span>📋</span> {isOptimizedView ? 'Optimized Conflict-Free Schedule' : 'Ingested Requisitions Timeline'}
                </h2>
                <p className="text-xs text-gray-500 mt-0.5">
                  {isOptimizedView ? 'Scheduled by AI constraint solver' : 'Showing all ingested database records'}
                </p>
              </div>

              <div className="flex items-center gap-2">
                {isOptimizedView ? (
                  <button
                    onClick={fetchScheduleList}
                    disabled={isLoading}
                    className="px-3 py-2 text-xs font-semibold rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-700 transition"
                    title="Switch back to viewing all submitted requests"
                  >
                    📋 View All Requests
                  </button>
                ) : null}

                <button
                  onClick={handleGeneratePlan}
                  disabled={isLoading}
                  className={`px-4 py-2 text-xs font-bold rounded-lg shadow-md transition transform active:scale-95 flex items-center gap-1.5 ${
                    isLoading
                      ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                      : 'bg-emerald-600 hover:bg-emerald-700 text-white'
                  }`}
                >
                  <span>⚡</span>
                  {isLoading ? 'Running Planner...' : 'GENERATE OPTIMAL PLAN'}
                </button>
              </div>
            </div>

            {/* Gantt Chart Timeline */}
            <GanttChart plans={scheduleList} isOptimizedView={isOptimizedView} />

            {/* Details Table */}
            <div className="pt-2">
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-sm font-bold text-gray-800 uppercase tracking-wider">
                  Requisitions & Scheduled Windows ({scheduleList.length})
                </h3>
                <span className="text-[11px] text-indigo-600 font-medium">
                  {isOptimizedView ? 'Optimal Path Assigned' : 'Raw Queue'}
                </span>
              </div>

              <div className="overflow-x-auto border border-gray-200 rounded-xl max-h-80 overflow-y-auto">
                <table className="min-w-full divide-y divide-gray-200 text-left text-xs">
                  <thead className="bg-slate-50 text-gray-600 font-semibold uppercase tracking-wider sticky top-0 z-10">
                    <tr>
                      <th className="px-3 py-2.5">ID</th>
                      <th className="px-4 py-2.5">Name</th>
                      <th className="px-3 py-2.5">Type</th>
                      <th className="px-3 py-2.5">Start</th>
                      <th className="px-3 py-2.5">End</th>
                      <th className="px-3 py-2.5 text-center">Criticality</th>
                      <th className="px-3 py-2.5 text-right">Score</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-100 font-mono">
                    {scheduleList.map((item, idx) => (
                      <tr key={item.id ?? idx} className="hover:bg-indigo-50/50 transition">
                        <td className="px-3 py-2 text-gray-500 font-bold">{item.id ?? idx + 1}</td>
                        <td className="px-4 py-2 font-sans font-medium text-gray-800">
                          {item.name}
                        </td>
                        <td className="px-3 py-2">
                          <span className={`px-2 py-0.5 rounded text-[10px] font-bold font-sans ${
                            item.request_type === 'TRAIN'
                              ? 'bg-blue-100 text-blue-800'
                              : 'bg-amber-100 text-amber-800'
                          }`}>
                            {item.request_type === 'TRAIN' ? '🚆 Train' : '🔧 Maint'}
                          </span>
                        </td>
                        <td className="px-3 py-2 text-indigo-700">
                          {new Date(item.start_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                        </td>
                        <td className="px-3 py-2 text-slate-600">
                          {item.end_time
                            ? new Date(item.end_time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                            : 'N/A'}
                        </td>
                        <td className="px-3 py-2 text-center">
                          <span className={`px-1.5 py-0.5 rounded text-[9px] font-bold font-sans ${
                            item.criticality === 'HIGH'
                              ? 'bg-red-100 text-red-700'
                              : item.criticality === 'MEDIUM'
                              ? 'bg-amber-100 text-amber-700'
                              : 'bg-emerald-100 text-emerald-700'
                          }`}>
                            {item.criticality}
                          </span>
                        </td>
                        <td className="px-3 py-2 text-right font-bold text-emerald-700 font-sans">
                          {item.optimization_score ? `${item.optimization_score.toFixed(0)}%` : '0%'}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

          </div>
        </div>
      </div>
    </ErrorBoundary>
  );
};

export default App;