import React, { useState, useEffect } from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";

// Language Learning Tracker - Single file React component
// Tailwind CSS assumed available in host project.
// Recharts assumed available for charts.

export default function LanguageLearningTracker() {
  // Overview
  const [overview, setOverview] = useState(() => {
    const saved = localStorage.getItem("ll_overview");
    return saved ? JSON.parse(saved) : {
      language: "Spanish",
      reason: "Travel & career",
      currentLevel: "A1",
      targetLevel: "B2",
      startDate: new Date().toISOString().slice(0,10),
      goalDate: "",
    };
  });

  // Daily tracker entries
  const [entries, setEntries] = useState(() => {
    const saved = localStorage.getItem("ll_entries");
    return saved ? JSON.parse(saved) : [];
  });

  // Weekly goals
  const [goals, setGoals] = useState(() => {
    const saved = localStorage.getItem("ll_goals");
    return saved ? JSON.parse(saved) : [];
  });

  // Vocabulary
  const [vocab, setVocab] = useState(() => {
    const saved = localStorage.getItem("ll_vocab");
    return saved ? JSON.parse(saved) : [];
  });

  // Speaking practice log
  const [speaks, setSpeaks] = useState(() => {
    const saved = localStorage.getItem("ll_speaks");
    return saved ? JSON.parse(saved) : [];
  });

  // Temp form states
  const [dailyForm, setDailyForm] = useState({ date: new Date().toISOString().slice(0,10), topic: "", minutes: 30, newWords: 0, type: "Listening", notes: "" });
  const [vForm, setVForm] = useState({ word: "", meaning: "", example: "", reviewDate: "" });
  const [goalForm, setGoalForm] = useState({ week: "", focus: "Vocabulary", targetHours: 3 });
  const [sForm, setSForm] = useState({ date: new Date().toISOString().slice(0,10), topic: "", duration: 10, rating: 6, notes: "" });

  // Persist to localStorage
  useEffect(() => { localStorage.setItem("ll_overview", JSON.stringify(overview)); }, [overview]);
  useEffect(() => { localStorage.setItem("ll_entries", JSON.stringify(entries)); }, [entries]);
  useEffect(() => { localStorage.setItem("ll_goals", JSON.stringify(goals)); }, [goals]);
  useEffect(() => { localStorage.setItem("ll_vocab", JSON.stringify(vocab)); }, [vocab]);
  useEffect(() => { localStorage.setItem("ll_speaks", JSON.stringify(speaks)); }, [speaks]);

  // Add handlers
  function addDaily(e){
    e?.preventDefault();
    const item = { ...dailyForm, minutes: Number(dailyForm.minutes), newWords: Number(dailyForm.newWords), id: Date.now() };
    setEntries(prev => [item, ...prev]);
    setDailyForm({ ...dailyForm, topic: "", minutes: 30, newWords: 0, notes: "" });
  }

  function addVocab(e){ e?.preventDefault(); const item={...vForm,id:Date.now()}; setVocab(prev=>[item,...prev]); setVForm({word:"",meaning:"",example:"",reviewDate:""}); }
  function addGoal(e){ e?.preventDefault(); const item={...goalForm,id:Date.now(),actualHours:0}; setGoals(prev=>[item,...prev]); setGoalForm({week:"",focus:"Vocabulary",targetHours:3}); }
  function addSpeak(e){ e?.preventDefault(); const item={...sForm,id:Date.now()}; setSpeaks(prev=>[item,...prev]); setSForm({date:new Date().toISOString().slice(0,10),topic:"",duration:10,rating:6,notes:""}); }

  function removeItem(listSetter, id){ listSetter(prev => prev.filter(x => x.id !== id)); }

  // Export & import
  function exportCSV(){
    const csvParts = [
      ["Date,Topic,Minutes,NewWords,Type,Notes"],
      ...entries.map(e => `${e.date},"${e.topic}",${e.minutes},${e.newWords},${e.type},"${(e.notes||"").replace(/"/g,'""')}"`)
    ];
    const blob = new Blob([csvParts.join("\n")], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = `language_entries_${overview.language || 'lang'}.csv`; a.click(); URL.revokeObjectURL(url);
  }

  function clearAll(){ if(window.confirm('Clear all tracker data? This cannot be undone.')){ localStorage.clear(); setEntries([]); setGoals([]); setVocab([]); setSpeaks([]); setOverview({language:'',reason:'',currentLevel:'',targetLevel:'',startDate:'',goalDate:''}); } }

  // Derived metrics for chart: last 14 days minutes per day
  function deriveChartData(){
    const map = {};
    const days = 14;
    for(let i=0;i<days;i++){ const d = new Date(); d.setDate(d.getDate() - (days-1 - i)); const key = d.toISOString().slice(0,10); map[key]=0; }
    entries.forEach(e => { if(map.hasOwnProperty(e.date)) map[e.date] += Number(e.minutes || 0); });
    return Object.keys(map).map(k => ({ date: k, minutes: map[k] }));
  }

  const chartData = deriveChartData();

  return (
    <div className="p-4 max-w-6xl mx-auto">
      <header className="mb-6">
        <h1 className="text-3xl font-semibold">Language Learning Tracker</h1>
        <p className="text-sm text-slate-500 mt-1">A compact web tracker — works offline (localStorage). Built with React + Tailwind + Recharts.</p>
      </header>

      <section className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div className="col-span-1 md:col-span-2 bg-white shadow rounded p-4">
          <h2 className="font-semibold mb-2">Overview</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <input className="border p-2 rounded" placeholder="Language" value={overview.language} onChange={e=>setOverview({...overview, language:e.target.value})} />
            <input className="border p-2 rounded" placeholder="Reason" value={overview.reason} onChange={e=>setOverview({...overview, reason:e.target.value})} />
            <input className="border p-2 rounded" placeholder="Current Level" value={overview.currentLevel} onChange={e=>setOverview({...overview, currentLevel:e.target.value})} />
            <input className="border p-2 rounded" placeholder="Target Level" value={overview.targetLevel} onChange={e=>setOverview({...overview, targetLevel:e.target.value})} />
            <label className="text-xs text-slate-500">Start Date</label>
            <input type="date" className="border p-2 rounded" value={overview.startDate} onChange={e=>setOverview({...overview, startDate:e.target.value})} />
            <label className="text-xs text-slate-500">Goal Date</label>
            <input type="date" className="border p-2 rounded" value={overview.goalDate} onChange={e=>setOverview({...overview, goalDate:e.target.value})} />
          </div>
          <div className="mt-3 text-sm text-slate-600">Quick actions: <button className="ml-2 px-2 py-1 bg-slate-100 rounded" onClick={exportCSV}>Export Entries CSV</button> <button className="ml-2 px-2 py-1 bg-red-50 text-red-600 rounded" onClick={clearAll}>Clear All</button></div>
        </div>

        <div className="bg-white shadow rounded p-4">
          <h2 className="font-semibold mb-2">14-day Trend</h2>
          <div style={{ height: 180 }}>
            <ResponsiveContainer>
              <LineChart data={chartData} margin={{ top: 10, right: 10, left: -10, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" tickFormatter={(d)=>d.slice(5)} />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="minutes" stroke="#8884d8" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-6">
        <div className="bg-white shadow rounded p-4">
          <h3 className="font-semibold mb-2">Add Daily Practice</h3>
          <form onSubmit={addDaily} className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            <input type="date" className="border p-2 rounded" value={dailyForm.date} onChange={e=>setDailyForm({...dailyForm,date:e.target.value})} />
            <select className="border p-2 rounded" value={dailyForm.type} onChange={e=>setDailyForm({...dailyForm,type:e.target.value})}>
              <option>Listening</option>
              <option>Reading</option>
              <option>Writing</option>
              <option>Speaking</option>
            </select>
            <input className="border p-2 rounded col-span-1 sm:col-span-2" placeholder="Topic" value={dailyForm.topic} onChange={e=>setDailyForm({...dailyForm,topic:e.target.value})} />
            <input type="number" min={1} className="border p-2 rounded" value={dailyForm.minutes} onChange={e=>setDailyForm({...dailyForm,minutes:e.target.value})} />
            <input type="number" min={0} className="border p-2 rounded" value={dailyForm.newWords} onChange={e=>setDailyForm({...dailyForm,newWords:e.target.value})} />
            <textarea className="border p-2 rounded col-span-1 sm:col-span-2" placeholder="Notes" value={dailyForm.notes} onChange={e=>setDailyForm({...dailyForm,notes:e.target.value})} />
            <div className="col-span-2 flex gap-2 justify-end">
              <button type="submit" className="px-4 py-2 bg-indigo-600 text-white rounded">Add</button>
            </div>
          </form>

          <div className="mt-4">
            <h4 className="font-medium">Recent Entries</h4>
            <div className="overflow-x-auto mt-2">
              <table className="w-full text-sm">
                <thead className="text-left text-slate-500"><tr><th>Date</th><th>Topic</th><th>Min</th><th>New</th><th>Type</th><th></th></tr></thead>
                <tbody>
                  {entries.slice(0,8).map(e=> (
                    <tr key={e.id} className="border-t"><td>{e.date}</td><td>{e.topic}</td><td>{e.minutes}</td><td>{e.newWords}</td><td>{e.type}</td><td><button className="text-xs text-red-500" onClick={()=>removeItem(setEntries,e.id)}>Delete</button></td></tr>
                  ))}
                  {entries.length===0 && <tr><td colSpan={6} className="text-slate-400 py-2">No entries yet — add one above.</td></tr>}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div className="bg-white shadow rounded p-4">
          <h3 className="font-semibold mb-2">Vocabulary</h3>
          <form onSubmit={addVocab} className="grid grid-cols-1 gap-2">
            <input className="border p-2 rounded" placeholder="Word" value={vForm.word} onChange={e=>setVForm({...vForm,word:e.target.value})} />
            <input className="border p-2 rounded" placeholder="Meaning" value={vForm.meaning} onChange={e=>setVForm({...vForm,meaning:e.target.value})} />
            <input className="border p-2 rounded" placeholder="Example sentence" value={vForm.example} onChange={e=>setVForm({...vForm,example:e.target.value})} />
            <input type="date" className="border p-2 rounded" value={vForm.reviewDate} onChange={e=>setVForm({...vForm,reviewDate:e.target.value})} />
            <div className="flex justify-end"><button className="px-4 py-2 bg-emerald-600 text-white rounded">Add Word</button></div>
          </form>

          <div className="mt-4 overflow-y-auto max-h-64">
            <ul className="space-y-2 text-sm">
              {vocab.map(v=> (
                <li key={v.id} className="p-2 border rounded flex justify-between items-start">
                  <div>
                    <div className="font-medium">{v.word} <span className="text-slate-400 text-xs">{v.meaning}</span></div>
                    <div className="text-xs text-slate-600">{v.example}</div>
                    {v.reviewDate && <div className="text-xs text-amber-600">Review: {v.reviewDate}</div>}
                  </div>
                  <div className="text-right"><button className="text-xs text-red-500" onClick={()=>removeItem(setVocab,v.id)}>Remove</button></div>
                </li>
              ))}
              {vocab.length===0 && <li className="text-slate-400">No vocab yet — add words above.</li>}
            </ul>
          </div>
        </div>
      </section>

      <section className="grid grid-cols-1 lg:grid-cols-2 gap-4 mb-6">
        <div className="bg-white shadow rounded p-4">
          <h3 className="font-semibold mb-2">Weekly Goals</h3>
          <form onSubmit={addGoal} className="grid grid-cols-1 sm:grid-cols-3 gap-2">
            <input className="border p-2 rounded" placeholder="Week label (e.g. 2025-W49)" value={goalForm.week} onChange={e=>setGoalForm({...goalForm,week:e.target.value})} />
            <select className="border p-2 rounded" value={goalForm.focus} onChange={e=>setGoalForm({...goalForm,focus:e.target.value})}><option>Vocabulary</option><option>Speaking</option><option>Grammar</option><option>Listening</option></select>
            <input type="number" min={1} className="border p-2 rounded" value={goalForm.targetHours} onChange={e=>setGoalForm({...goalForm,targetHours:e.target.value})} />
            <div className="col-span-3 flex justify-end"><button className="px-4 py-2 bg-indigo-600 text-white rounded">Add Goal</button></div>
          </form>

          <div className="mt-4 text-sm">
            {goals.length===0 && <div className="text-slate-400">No goals yet.</div>}
            <ul className="space-y-2">
              {goals.map(g=> (
                <li key={g.id} className="p-2 border rounded flex justify-between items-center">
                  <div>
                    <div className="font-medium">{g.week || '—'} <span className="text-slate-500">{g.focus}</span></div>
                    <div className="text-xs">Target: {g.targetHours} hrs — Actual: {g.actualHours || 0} hrs</div>
                  </div>
                  <div className="flex items-center gap-2">
                    <button className="text-xs text-red-500" onClick={()=>removeItem(setGoals,g.id)}>Delete</button>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="bg-white shadow rounded p-4">
          <h3 className="font-semibold mb-2">Speaking Practice</h3>
          <form onSubmit={addSpeak} className="grid grid-cols-1 gap-2">
            <input type="date" className="border p-2 rounded" value={sForm.date} onChange={e=>setSForm({...sForm,date:e.target.value})} />
            <input className="border p-2 rounded" placeholder="Topic" value={sForm.topic} onChange={e=>setSForm({...sForm,topic:e.target.value})} />
            <div className="grid grid-cols-3 gap-2">
              <input type="number" min={1} className="border p-2 rounded" value={sForm.duration} onChange={e=>setSForm({...sForm,duration:e.target.value})} />
              <input type="number" min={1} max={10} className="border p-2 rounded" value={sForm.rating} onChange={e=>setSForm({...sForm,rating:e.target.value})} />
              <div />
            </div>
            <textarea className="border p-2 rounded" placeholder="Notes" value={sForm.notes} onChange={e=>setSForm({...sForm,notes:e.target.value})} />
            <div className="flex justify-end"><button className="px-4 py-2 bg-emerald-600 text-white rounded">Log</button></div>
          </form>

          <div className="mt-4 overflow-y-auto max-h-64">
            <ul className="space-y-2 text-sm">
              {speaks.map(s=> (
                <li key={s.id} className="p-2 border rounded flex justify-between items-start">
                  <div>
                    <div className="font-medium">{s.date} — {s.topic}</div>
                    <div className="text-xs">{s.duration} min • Rating: {s.rating}/10</div>
                    <div className="text-xs text-slate-600">{s.notes}</div>
                  </div>
                  <div><button className="text-xs text-red-500" onClick={()=>removeItem(setSpeaks,s.id)}>Remove</button></div>
                </li>
              ))}
              {speaks.length===0 && <li className="text-slate-400">No speaking logs yet.</li>}
            </ul>
          </div>
        </div>
      </section>

      <footer className="text-sm text-slate-500 py-6">Tip: this app stores data locally in your browser. Use the Export button to back up. If you want, I can convert this into a deployable HTML/CSS/JS bundle or a Google Sheets template.</footer>
    </div>
  );
}
