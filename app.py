import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Music Theory Pro", layout="wide")

HTML_APP = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Music Theory Pro</title>
<style>
  :root {
    --bg: #0f172a;
    --panel: #111827;
    --panel-2: #1f2937;
    --line: #334155;
    --text: #e5e7eb;
    --muted: #94a3b8;
    --accent: #38bdf8;
    --accent-2: #f59e0b;
    --success: #22c55e;
    --danger: #ef4444;
    --wood-1: #5b3a29;
    --wood-2: #7a4d33;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
    color: var(--text);
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    min-height: 100vh;
  }
  .app {
    max-width: 1400px;
    margin: 0 auto;
    padding: 16px;
  }

  /* ── Header ── */
  .hero {
    padding: 18px 22px;
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 20px;
    background: radial-gradient(circle at top left, rgba(56,189,248,0.16), transparent 30%), rgba(15,23,42,0.95);
    box-shadow: 0 16px 32px rgba(2,6,23,0.3);
    margin-bottom: 14px;
  }
  .hero h1 { font-size: 2rem; line-height: 1.1; margin-bottom: 4px; }
  .hero p { color: var(--muted); font-size: 0.92rem; }

  /* ── Tab Bar ── */
  .tab-bar {
    display: flex;
    gap: 4px;
    background: rgba(15,23,42,0.8);
    border: 1px solid rgba(148,163,184,0.15);
    border-radius: 16px;
    padding: 5px;
    margin-bottom: 14px;
    overflow-x: auto;
  }
  .tab-btn {
    flex: 1;
    min-width: 120px;
    padding: 10px 14px;
    border: none;
    border-radius: 12px;
    background: transparent;
    color: var(--muted);
    font: 600 0.88rem/1.3 inherit;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
  }
  .tab-btn:hover { background: rgba(56,189,248,0.08); color: var(--text); }
  .tab-btn.active {
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(56,189,248,0.08));
    color: var(--accent);
    box-shadow: 0 2px 8px rgba(56,189,248,0.15);
  }
  .tab-content { display: none; }
  .tab-content.active { display: block; }

  /* ── Shared Card ── */
  .card {
    background: rgba(15,23,42,0.86);
    border: 1px solid rgba(148,163,184,0.18);
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 12px 24px rgba(2,6,23,0.2);
    margin-bottom: 14px;
  }
  .card h2 { font-size: 1.2rem; margin-bottom: 10px; }
  .card h3 { font-size: 1.05rem; margin-bottom: 8px; color: var(--accent); }

  /* ── Buttons ── */
  .btn {
    border: 0; border-radius: 12px; padding: 10px 16px;
    cursor: pointer; transition: all 0.15s; color: white; font-weight: 600; font-size: 0.85rem;
  }
  .btn:active { transform: scale(0.97); }
  .btn.primary { background: linear-gradient(135deg, #2563eb, #1d4ed8); }
  .btn.primary:hover { background: linear-gradient(135deg, #3b82f6, #2563eb); }
  .btn.secondary { background: linear-gradient(135deg, #6366f1, #4f46e5); }
  .btn.success { background: linear-gradient(135deg, #16a34a, #15803d); }
  .btn.ghost { background: rgba(148,163,184,0.12); color: var(--muted); }
  .btn.ghost:hover { background: rgba(148,163,184,0.2); color: var(--text); }
  .btn.amber { background: linear-gradient(135deg, #d97706, #b45309); }
  .btn.small { padding: 6px 12px; font-size: 0.8rem; border-radius: 8px; }

  select {
    padding: 10px 12px; border-radius: 12px;
    border: 1px solid var(--line); background: rgba(15,23,42,0.9);
    color: var(--text); font: inherit; font-size: 0.9rem;
  }

  /* ── Chip ── */
  .chip {
    display: inline-block; padding: 4px 12px;
    border-radius: 20px; font-weight: 700; font-size: 0.9rem;
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(99,102,241,0.2));
    color: var(--accent);
  }

  /* ── Toolbar (Chord Lab) ── */
  .toolbar {
    display: flex; flex-wrap: wrap; gap: 10px;
    align-items: end; margin-bottom: 14px;
  }
  .toolbar .field { display: flex; flex-direction: column; gap: 4px; }
  .toolbar .field label { font-size: 0.8rem; color: var(--muted); }
  .toolbar select { min-width: 110px; }
  .browser-summary {
    display: flex; flex-wrap: wrap; align-items: center; gap: 10px;
    font-size: 0.85rem; color: var(--muted); padding: 8px 0;
  }

  /* ── Grid (2-col) ── */
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 14px; }
  @media (max-width: 900px) { .grid { grid-template-columns: 1fr; } }

  .section-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
  .section-head h2 { margin: 0; }
  .mini-actions { display: flex; gap: 6px; }
  .mini-btn {
    padding: 5px 10px; border-radius: 8px; border: 1px solid var(--line);
    background: transparent; color: var(--muted); cursor: pointer; font-size: 0.78rem;
    transition: all 0.15s;
  }
  .mini-btn:hover { background: rgba(56,189,248,0.1); color: var(--text); }

  .status { font-size: 0.82rem; color: var(--muted); margin-bottom: 8px; }

  /* ── Piano ── */
  .piano-shell { position: relative; height: 160px; margin: 10px 0; overflow-x: auto; }
  .piano { position: relative; width: 630px; height: 150px; }
  .white-key {
    position: absolute; width: 42px; height: 150px;
    background: linear-gradient(180deg, #f8fafc, #e2e8f0);
    border: 1px solid #94a3b8; border-radius: 0 0 6px 6px;
    cursor: pointer; display: flex; align-items: flex-end; justify-content: center;
    padding-bottom: 8px; font-size: 0.7rem; color: #475569;
    transition: background 0.1s;
  }
  .white-key:hover { background: linear-gradient(180deg, #e0f2fe, #bae6fd); }
  .white-key.active { background: linear-gradient(180deg, #38bdf8, #0ea5e9); color: white; }
  .white-key.scale-highlight {
    background: linear-gradient(180deg, #a78bfa, #7c3aed); color: white;
  }
  .white-key.scale-root {
    background: linear-gradient(180deg, #f59e0b, #d97706); color: white;
  }
  .black-key {
    position: absolute; width: 28px; height: 95px;
    background: linear-gradient(180deg, #1e293b, #0f172a);
    border: 1px solid #0f172a; border-radius: 0 0 4px 4px;
    cursor: pointer; z-index: 2; display: flex; align-items: flex-end;
    justify-content: center; padding-bottom: 6px; font-size: 0.6rem; color: #64748b;
    transition: background 0.1s;
  }
  .black-key:hover { background: linear-gradient(180deg, #334155, #1e293b); }
  .black-key.active { background: linear-gradient(180deg, #0ea5e9, #0284c7); color: white; }
  .black-key.scale-highlight {
    background: linear-gradient(180deg, #7c3aed, #6d28d9); color: white;
  }
  .black-key.scale-root {
    background: linear-gradient(180deg, #d97706, #b45309); color: white;
  }

  /* ── Guitar Fretboard ── */
  .fretboard-wrap { overflow-x: auto; margin: 10px 0; }
  .fretboard { display: grid; grid-template-rows: repeat(7, auto); gap: 0; min-width: 700px; }
  .fret-row { display: grid; grid-template-columns: 36px repeat(13, 1fr); }
  .fret-header { font-size: 0.7rem; color: var(--muted); text-align: center; }
  .string-label { font-size: 0.75rem; font-weight: 700; color: var(--accent-2); display: flex; align-items: center; }
  .string-cell {
    height: 28px; border-right: 1px solid var(--line);
    border-bottom: 1px solid rgba(148,163,184,0.08);
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; position: relative;
    background: linear-gradient(90deg, var(--wood-1), var(--wood-2));
  }
  .string-cell::after {
    content: ""; position: absolute; top: 50%; left: 0; right: 0;
    height: 2px; background: rgba(200,180,140,0.5); transform: translateY(-50%);
  }
  .open-cell { background: rgba(15,23,42,0.6); }
  .open-cell::after { display: none; }
  .marker {
    width: 20px; height: 20px; border-radius: 50%; z-index: 1;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.65rem; color: transparent;
  }
  .string-cell.active .marker {
    background: var(--accent); color: white; box-shadow: 0 0 8px rgba(56,189,248,0.5);
  }
  .string-cell.scale-dot .marker {
    background: rgba(124,58,237,0.85); color: white; box-shadow: 0 0 6px rgba(124,58,237,0.4);
  }
  .string-cell.scale-root-dot .marker {
    background: rgba(245,158,11,0.9); color: white; box-shadow: 0 0 6px rgba(245,158,11,0.5);
  }

  .legend {
    display: flex; gap: 16px; font-size: 0.75rem; color: var(--muted); margin: 6px 0;
  }
  .legend-dot {
    display: inline-block; width: 10px; height: 10px; border-radius: 50%;
    background: var(--accent); margin-right: 4px; vertical-align: middle;
  }
  .legend-key {
    display: inline-block; width: 14px; height: 10px; border-radius: 2px;
    background: var(--accent); margin-right: 4px; vertical-align: middle;
  }

  /* ── Detected Chords ── */
  .detected { margin-top: 8px; }
  .detected-title { font-size: 0.8rem; color: var(--muted); margin-bottom: 4px; }
  .detected-empty { font-size: 0.8rem; color: var(--muted); font-style: italic; }
  .detected-list { display: flex; flex-wrap: wrap; gap: 6px; }
  .detected-item {
    padding: 5px 12px; border-radius: 20px; border: 1px solid var(--line);
    background: rgba(56,189,248,0.08); color: var(--accent);
    cursor: pointer; font-size: 0.8rem; font-weight: 600;
    transition: all 0.15s;
  }
  .detected-item:hover { background: rgba(56,189,248,0.2); }

  /* ── Supported Chords Grid ── */
  .support-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 6px; font-size: 0.8rem;
  }
  .support-grid div {
    padding: 5px 8px; border-radius: 8px;
    background: rgba(148,163,184,0.06); text-align: center;
  }

  /* ── Scale Explorer ── */
  .scale-controls {
    display: flex; flex-wrap: wrap; gap: 10px; align-items: end; margin-bottom: 14px;
  }
  .scale-info-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 10px; margin-bottom: 14px;
  }
  .info-box {
    padding: 12px; border-radius: 12px;
    background: rgba(148,163,184,0.06); border: 1px solid rgba(148,163,184,0.1);
  }
  .info-box .label { font-size: 0.75rem; color: var(--muted); margin-bottom: 4px; }
  .info-box .value { font-size: 0.95rem; font-weight: 600; }
  .diatonic-chords {
    display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px;
  }
  .diatonic-chord {
    padding: 8px 14px; border-radius: 10px; text-align: center;
    background: rgba(148,163,184,0.08); border: 1px solid rgba(148,163,184,0.12);
    cursor: pointer; transition: all 0.15s;
  }
  .diatonic-chord:hover { background: rgba(56,189,248,0.15); }
  .diatonic-chord .degree { font-size: 0.72rem; color: var(--muted); }
  .diatonic-chord .chord-name { font-size: 0.9rem; font-weight: 700; color: var(--text); }

  /* ── Chord Theory ── */
  .theory-nav {
    display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px;
  }
  .theory-nav-btn {
    padding: 7px 14px; border-radius: 10px; border: 1px solid var(--line);
    background: transparent; color: var(--muted); cursor: pointer;
    font-size: 0.82rem; font-weight: 600; transition: all 0.15s;
  }
  .theory-nav-btn:hover { background: rgba(56,189,248,0.08); color: var(--text); }
  .theory-nav-btn.active { background: rgba(56,189,248,0.15); color: var(--accent); border-color: var(--accent); }
  .theory-section { display: none; }
  .theory-section.active { display: block; }
  .theory-text { font-size: 0.9rem; line-height: 1.7; color: var(--text); margin-bottom: 12px; }
  .theory-text strong { color: var(--accent); }
  .interval-table {
    width: 100%; border-collapse: collapse; font-size: 0.85rem; margin: 12px 0;
  }
  .interval-table th {
    text-align: left; padding: 8px 12px; background: rgba(148,163,184,0.08);
    color: var(--muted); font-weight: 600; border-bottom: 1px solid var(--line);
  }
  .interval-table td {
    padding: 8px 12px; border-bottom: 1px solid rgba(148,163,184,0.06);
  }
  .interval-table tr:hover td { background: rgba(56,189,248,0.04); }
  .play-interval-btn {
    padding: 3px 10px; border-radius: 6px; border: none;
    background: rgba(56,189,248,0.15); color: var(--accent);
    cursor: pointer; font-size: 0.78rem; transition: all 0.15s;
  }
  .play-interval-btn:hover { background: rgba(56,189,248,0.3); }
  .formula-display {
    display: flex; flex-wrap: wrap; gap: 6px; margin: 10px 0;
  }
  .formula-display .interval-chip {
    padding: 5px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 600;
    background: rgba(124,58,237,0.15); color: #a78bfa;
  }

  /* ── Chord Progressions ── */
  .prog-controls {
    display: flex; flex-wrap: wrap; gap: 10px; align-items: end; margin-bottom: 14px;
  }
  .prog-list { display: flex; flex-direction: column; gap: 12px; }
  .prog-item {
    padding: 14px; border-radius: 14px;
    background: rgba(148,163,184,0.05); border: 1px solid rgba(148,163,184,0.1);
    transition: all 0.15s;
  }
  .prog-item:hover { border-color: rgba(56,189,248,0.3); }
  .prog-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
  .prog-name { font-weight: 700; font-size: 0.95rem; }
  .prog-roman { font-size: 1rem; font-weight: 700; color: var(--accent); margin-bottom: 4px; letter-spacing: 1px; }
  .prog-chords {
    display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0;
  }
  .prog-chord-chip {
    padding: 6px 14px; border-radius: 10px; font-weight: 700; font-size: 0.88rem;
    background: rgba(56,189,248,0.1); color: var(--accent); border: 1px solid rgba(56,189,248,0.2);
    cursor: pointer; transition: all 0.15s;
  }
  .prog-chord-chip:hover { background: rgba(56,189,248,0.2); }
  .prog-chord-chip.playing { background: var(--accent); color: #0f172a; }
  .prog-desc { font-size: 0.82rem; color: var(--muted); line-height: 1.5; margin-top: 6px; }
  .tempo-control { display: flex; align-items: center; gap: 8px; }
  .tempo-control input[type="range"] { width: 100px; }
  .tempo-control span { font-size: 0.8rem; color: var(--muted); min-width: 55px; }

  /* ── Circle of Fifths ── */
  .circle-container {
    display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; align-items: flex-start;
  }
  .circle-svg-wrap { flex: 0 0 auto; }
  .circle-info { flex: 1; min-width: 280px; }
  .circle-info .info-box { margin-bottom: 10px; }
  .key-chords-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
    gap: 6px; margin-top: 8px;
  }
  .key-chord-item {
    padding: 8px; border-radius: 8px; text-align: center;
    background: rgba(148,163,184,0.06); border: 1px solid rgba(148,163,184,0.1);
    cursor: pointer; transition: all 0.15s;
  }
  .key-chord-item:hover { background: rgba(56,189,248,0.12); }
  .key-chord-item .deg { font-size: 0.7rem; color: var(--muted); }
  .key-chord-item .name { font-size: 0.85rem; font-weight: 700; }

  /* ── Tooltip ── */
  .tooltip-wrap { position: relative; display: inline-block; }
  .tooltip-content {
    display: none; position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%);
    padding: 8px 12px; border-radius: 10px; background: #1e293b; border: 1px solid var(--line);
    color: var(--text); font-size: 0.78rem; white-space: nowrap; z-index: 100;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3); margin-bottom: 6px;
  }
  .tooltip-wrap:hover .tooltip-content { display: block; }

  /* ── Color Legend ── */
  .color-legend {
    display: flex; flex-wrap: wrap; gap: 16px; padding: 10px 14px;
    background: rgba(148,163,184,0.05); border-radius: 12px;
    font-size: 0.82rem; color: var(--muted); margin-bottom: 12px;
    border: 1px solid rgba(148,163,184,0.08);
  }
  .color-legend-item { display: flex; align-items: center; gap: 6px; }
  .color-swatch {
    width: 18px; height: 12px; border-radius: 3px; flex-shrink: 0;
  }

  /* ── Collapsible Guide ── */
  .guide-toggle {
    padding: 8px 16px; border-radius: 10px; border: 1px solid rgba(56,189,248,0.3);
    background: rgba(56,189,248,0.08); color: var(--accent);
    cursor: pointer; font-size: 0.84rem; font-weight: 600;
    transition: all 0.15s; margin-bottom: 12px;
  }
  .guide-toggle:hover { background: rgba(56,189,248,0.15); }
  .guide-panel {
    display: none; padding: 16px; border-radius: 14px;
    background: rgba(15,23,42,0.9); border: 1px solid rgba(148,163,184,0.15);
    margin-bottom: 14px; line-height: 1.7; font-size: 0.88rem;
  }
  .guide-panel.open { display: block; }
  .guide-panel h4 { color: var(--accent); margin: 12px 0 6px; font-size: 0.95rem; }
  .guide-panel h4:first-child { margin-top: 0; }
  .guide-panel p { margin-bottom: 8px; }
  .guide-panel code {
    background: rgba(56,189,248,0.1); padding: 1px 6px; border-radius: 4px;
    color: var(--accent); font-size: 0.85rem;
  }
  .guide-panel ul { margin: 4px 0 8px 20px; }
  .guide-panel li { margin-bottom: 4px; }

  /* ── Staff Notation ── */
  .staff-container {
    overflow-x: auto; margin: 10px 0; padding: 10px;
    background: rgba(255,255,255,0.03); border-radius: 12px;
    border: 1px solid rgba(148,163,184,0.08);
  }

  /* ── Scale History/Theory Panel ── */
  .scale-history {
    padding: 16px; border-radius: 14px;
    background: rgba(148,163,184,0.04); border: 1px solid rgba(148,163,184,0.1);
    margin-bottom: 14px;
  }
  .scale-history h3 { color: var(--accent); margin-bottom: 8px; font-size: 1rem; }
  .scale-history p { font-size: 0.88rem; line-height: 1.7; margin-bottom: 8px; color: var(--text); }
  .scale-history .highlight { color: var(--accent-2); font-weight: 600; }
  .scale-history .tag {
    display: inline-block; padding: 3px 10px; border-radius: 6px;
    background: rgba(56,189,248,0.1); color: var(--accent);
    font-size: 0.78rem; font-weight: 600; margin-right: 6px; margin-bottom: 4px;
  }
</style>
</head>
<body>
<div class="app">
  <div class="hero">
    <h1>Music Theory Pro</h1>
    <p>Interactive chord lab, scales, theory, progressions &amp; circle of fifths</p>
  </div>

  <div class="tab-bar">
    <button class="tab-btn active" data-tab="chordlab">Chord Lab</button>
    <button class="tab-btn" data-tab="scales">Scale Explorer</button>
    <button class="tab-btn" data-tab="theory">Chord Theory</button>
    <button class="tab-btn" data-tab="progressions">Progressions</button>
    <button class="tab-btn" data-tab="circle">Circle of Fifths</button>
  </div>

  <!-- ═══════════════ TAB 1: CHORD LAB ═══════════════ -->
  <div class="tab-content active" id="tab-chordlab">
    <div class="card toolbar">
      <div class="field">
        <label for="rootSelect">Chord root</label>
        <select id="rootSelect"></select>
      </div>
      <div class="field">
        <label for="qualitySelect">Chord quality</label>
        <select id="qualitySelect"></select>
      </div>
      <button class="btn primary" id="loadPianoBtn">Piano</button>
      <button class="btn primary" id="loadGuitarBtn">Guitar</button>
      <button class="btn secondary" id="loadBothBtn">Both</button>
      <button class="btn success" id="playBrowserBtn">Play</button>
      <button class="btn ghost" id="clearAllBtn">Clear</button>
      <div class="browser-summary">
        <span class="chip" id="browserName">C major</span>
        <span>Notes: <strong id="browserNotes">C, E, G</strong></span>
        <span id="chordTooltip" style="font-size:0.82rem;color:var(--accent-2);"></span>
      </div>
    </div>

    <div class="grid">
      <section class="card">
        <div class="section-head">
          <h2>Piano</h2>
          <div class="mini-actions">
            <button class="mini-btn" id="playPianoBtn">Play selected</button>
            <button class="mini-btn" id="clearPianoBtn">Clear</button>
          </div>
        </div>
        <div class="status" id="pianoStatus">Selected notes: none</div>
        <div class="piano-shell"><div class="piano" id="piano"></div></div>
        <div class="detected" id="pianoDetected"></div>
      </section>

      <section class="card">
        <div class="section-head">
          <h2>Guitar</h2>
          <div class="mini-actions">
            <button class="mini-btn" id="strumGuitarBtn">Strum</button>
            <button class="mini-btn" id="clearGuitarBtn">Clear</button>
          </div>
        </div>
        <div class="status" id="guitarStatus">Selected notes: none</div>
        <div class="fretboard-wrap"><div class="fretboard" id="fretboard"></div></div>
        <div class="legend">
          <span><span class="legend-dot"></span> active fret</span>
          <span><span class="legend-key"></span> active piano key</span>
        </div>
        <div class="detected" id="guitarDetected"></div>
      </section>
    </div>

    <section class="card">
      <h3>Supported chord qualities</h3>
      <div class="support-grid" id="supportedChords"></div>
    </section>
  </div>

  <!-- ═══════════════ TAB 2: SCALE EXPLORER ═══════════════ -->
  <div class="tab-content" id="tab-scales">
    <div class="card">
      <div class="scale-controls">
        <div class="field">
          <label for="scaleRootSelect">Root note</label>
          <select id="scaleRootSelect"></select>
        </div>
        <div class="field">
          <label for="scaleCategorySelect">Category</label>
          <select id="scaleCategorySelect"></select>
        </div>
        <div class="field">
          <label for="scaleTypeSelect">Scale</label>
          <select id="scaleTypeSelect"></select>
        </div>
        <button class="btn primary" id="playScaleUpBtn">Play ascending</button>
        <button class="btn secondary" id="playScaleDownBtn">Play descending</button>
        <button class="btn ghost" id="clearScaleBtn">Clear</button>
      </div>
    </div>

    <button class="guide-toggle" id="guideToggle">How to read this page</button>
    <div class="guide-panel" id="guidePanel">
      <h4>Formula (W, H, 3H)</h4>
      <p><code>W</code> = <strong>Whole step</strong> (2 semitones) — skip one key. E.g. C → D.<br>
      <code>H</code> = <strong>Half step</strong> (1 semitone) — the very next key. E.g. E → F, or C → C#.<br>
      <code>3H</code> = <strong>3 half steps</strong> (a minor 3rd jump). E.g. C → Eb.</p>
      <p>The formula tells you how to build the scale step by step from the root note. For example, <code>W-W-H-W-W-W-H</code> (Major scale) means: start on root, go up a whole step, whole, half, whole, whole, whole, half.</p>

      <h4>Degrees (1, b2, b3, #4, etc.)</h4>
      <p>Degrees compare each note to the <strong>major scale</strong> as reference:</p>
      <ul>
        <li><strong>No symbol</strong> (1, 2, 3, 4, 5, 6, 7) = same as major scale</li>
        <li><strong>b (flat/bemolle)</strong> = lowered by one half step from major (e.g. b3 = minor 3rd)</li>
        <li><strong># (sharp/diesis)</strong> = raised by one half step from major (e.g. #4 = augmented 4th)</li>
      </ul>
      <p>So <code>1 – b2 – b3 – 4 – 5 – b6 – b7</code> (Phrygian) means: the 2nd, 3rd, 6th, and 7th degrees are all one semitone lower than in a major scale.</p>

      <h4>Intervals (P1, m2, M3, P5, etc.)</h4>
      <p>Intervals are the standard music theory names for the distance from the root:</p>
      <ul>
        <li><strong>P</strong> = Perfect (P1, P4, P5, P8) — the most consonant, stable intervals</li>
        <li><strong>M</strong> = Major (M2, M3, M6, M7) — the "bright" version of an interval</li>
        <li><strong>m</strong> = minor (m2, m3, m6, m7) — the "dark" version, one semitone smaller than Major</li>
        <li><strong>TT</strong> = Tritone — exactly 6 semitones, the most unstable interval</li>
      </ul>
      <p>Formula, degrees, and intervals express the <strong>same information in three different ways</strong>: step-by-step directions, comparison to major, and standard distance names.</p>

      <h4>Colors on piano and guitar</h4>
      <div class="color-legend" style="margin-top:4px;">
        <div class="color-legend-item"><div class="color-swatch" style="background:linear-gradient(135deg,#f59e0b,#d97706)"></div> <strong>Orange</strong> = Root note (tonic)</div>
        <div class="color-legend-item"><div class="color-swatch" style="background:linear-gradient(135deg,#a78bfa,#7c3aed)"></div> <strong>Purple</strong> = Other scale notes</div>
        <div class="color-legend-item"><div class="color-swatch" style="background:linear-gradient(135deg,#e2e8f0,#cbd5e1)"></div> <strong>White/Uncolored</strong> = Not in the scale</div>
      </div>
    </div>

    <div class="color-legend" id="scaleLegend">
      <div class="color-legend-item"><div class="color-swatch" style="background:linear-gradient(135deg,#f59e0b,#d97706)"></div> Root note</div>
      <div class="color-legend-item"><div class="color-swatch" style="background:linear-gradient(135deg,#a78bfa,#7c3aed)"></div> Scale note</div>
      <div class="color-legend-item"><div class="color-swatch" style="background:linear-gradient(135deg,#e2e8f0,#cbd5e1)"></div> Not in scale</div>
    </div>

    <div class="scale-info-grid" id="scaleInfoGrid"></div>

    <div id="scaleHistoryPanel"></div>

    <section class="card">
      <h2>Staff Notation</h2>
      <div class="staff-container" id="staffContainer"></div>
    </section>

    <div class="grid">
      <section class="card">
        <h2>Piano</h2>
        <div class="piano-shell"><div class="piano" id="scalePiano"></div></div>
      </section>
      <section class="card">
        <h2>Guitar Fretboard</h2>
        <div class="fretboard-wrap"><div class="fretboard" id="scaleFretboard"></div></div>
      </section>
    </div>

    <section class="card">
      <h3>Chords in this scale</h3>
      <p style="font-size:0.82rem;color:var(--muted);margin-bottom:8px;">Diatonic triads and 7th chords built on each scale degree. Click to hear.</p>
      <div id="diatonicChordsContainer"></div>
    </section>
  </div>

  <!-- ═══════════════ TAB 3: CHORD THEORY ═══════════════ -->
  <div class="tab-content" id="tab-theory">
    <div class="card">
      <div class="theory-nav" id="theoryNav"></div>
    </div>
    <div id="theoryContent"></div>
  </div>

  <!-- ═══════════════ TAB 4: PROGRESSIONS ═══════════════ -->
  <div class="tab-content" id="tab-progressions">
    <div class="card">
      <div class="prog-controls">
        <div class="field">
          <label for="progGenreSelect">Genre</label>
          <select id="progGenreSelect"></select>
        </div>
        <div class="field">
          <label for="progKeySelect">Key</label>
          <select id="progKeySelect"></select>
        </div>
        <div class="field">
          <label for="progModeSelect">Mode</label>
          <select id="progModeSelect">
            <option value="major">Major</option>
            <option value="minor">Minor</option>
          </select>
        </div>
        <div class="tempo-control">
          <label style="font-size:0.8rem;color:var(--muted);">Tempo</label>
          <input type="range" id="tempoSlider" min="60" max="180" value="100" />
          <span id="tempoDisplay">100 BPM</span>
        </div>
      </div>
    </div>
    <div class="prog-list" id="progList"></div>
  </div>

  <!-- ═══════════════ TAB 5: CIRCLE OF FIFTHS ═══════════════ -->
  <div class="tab-content" id="tab-circle">
    <div class="card">
      <div class="circle-container">
        <div class="circle-svg-wrap" id="circleSvgWrap"></div>
        <div class="circle-info" id="circleInfo"></div>
      </div>
    </div>
  </div>
</div>

<script>
/* ═══════════════════════════════════════════════════════
   CORE MUSIC THEORY DATA
   ═══════════════════════════════════════════════════════ */
const NOTE_NAMES_SHARP = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
const NOTE_NAMES_FLAT  = ["C","Db","D","Eb","E","F","Gb","G","Ab","A","Bb","B"];
const NOTE_ALIAS_TO_SHARP = {
  "Db":"C#","Eb":"D#","Gb":"F#","Ab":"G#","Bb":"A#",
  "Cb":"B","Fb":"E","E#":"F","B#":"C"
};
const GUITAR_STRINGS = [
  {label:"E2",midi:40},{label:"A2",midi:45},{label:"D3",midi:50},
  {label:"G3",midi:55},{label:"B3",midi:59},{label:"E4",midi:64}
];
const MAX_FRET = 14;

/* ── Chord Formulas ── */
const CHORD_FORMULAS = {
  "":[0,4,7], "m":[0,3,7], "5":[0,7], "dim":[0,3,6], "aug":[0,4,8],
  "sus2":[0,2,7], "sus4":[0,5,7],
  "6":[0,4,7,9], "m6":[0,3,7,9], "6/9":[0,2,4,7,9], "m6/9":[0,2,3,7,9],
  "7":[0,4,7,10], "maj7":[0,4,7,11], "m7":[0,3,7,10], "m(maj7)":[0,3,7,11],
  "dim7":[0,3,6,9], "m7b5":[0,3,6,10], "7b5":[0,4,6,10], "7#5":[0,4,8,10],
  "7sus4":[0,5,7,10],
  "add9":[0,2,4,7], "madd9":[0,2,3,7], "add11":[0,4,5,7], "madd11":[0,3,5,7],
  "add13":[0,4,7,9], "madd13":[0,3,7,9],
  "9":[0,2,4,7,10], "maj9":[0,2,4,7,11], "m9":[0,2,3,7,10],
  "7b9":[0,1,4,7,10], "7#9":[0,3,4,7,10], "9sus4":[0,2,5,7,10],
  "11":[0,2,4,5,7,10], "maj11":[0,2,4,5,7,11], "m11":[0,2,3,5,7,10],
  "13":[0,2,4,7,9,10], "maj13":[0,2,4,7,9,11], "m13":[0,2,3,7,9,10],
  "13sus4":[0,2,5,7,9,10], "maj7#11":[0,4,6,7,11], "7b13":[0,4,7,8,10]
};

/* ── Chord Explanations ── */
const CHORD_EXPLANATIONS = {
  "": "Major triad: root + major 3rd + perfect 5th. The most fundamental bright, happy chord.",
  "m": "Minor triad: root + minor 3rd + perfect 5th. Darker, sadder quality than major.",
  "5": "Power chord: root + perfect 5th only. Neither major nor minor — used heavily in rock.",
  "dim": "Diminished triad: root + minor 3rd + diminished 5th. Tense, unstable sound.",
  "aug": "Augmented triad: root + major 3rd + augmented 5th. Mysterious, dreamy quality.",
  "sus2": "Suspended 2nd: root + major 2nd + perfect 5th. The 3rd is replaced by 2nd — open, ambiguous.",
  "sus4": "Suspended 4th: root + perfect 4th + perfect 5th. The 3rd is replaced by 4th — wants to resolve.",
  "6": "Major 6th: major triad + major 6th. Sweet, jazzy quality. Common in jazz and bossa nova.",
  "m6": "Minor 6th: minor triad + major 6th. Bittersweet, used in jazz ballads.",
  "6/9": "6/9: major triad + 6th + 9th (no 7th). Rich, open voicing popular in jazz endings.",
  "m6/9": "Minor 6/9: minor triad + 6th + 9th. Complex minor color.",
  "7": "Dominant 7th: major triad + minor 7th. Creates tension that wants to resolve — the V chord in jazz.",
  "maj7": "Major 7th: major triad + major 7th. Lush, dreamy. The 'pretty' jazz chord.",
  "m7": "Minor 7th: minor triad + minor 7th. Smooth, mellow. The ii chord in jazz.",
  "m(maj7)": "Minor-major 7th: minor triad + major 7th. Dark and mysterious, used in film noir.",
  "dim7": "Diminished 7th: diminished triad + diminished 7th (=major 6th). Highly tense, symmetric chord.",
  "m7b5": "Half-diminished: minor triad with b5 + minor 7th. The ii chord in minor key jazz.",
  "7b5": "Dominant 7 flat 5: dom7 with diminished 5th. Tritone substitution chord.",
  "7#5": "Dominant 7 sharp 5: dom7 with augmented 5th. Altered dominant, strong resolution tendency.",
  "7sus4": "Dominant 7 sus4: sus4 + minor 7th. Suspended dominant, common before resolution.",
  "add9": "Add 9: major triad + 9th (no 7th). Adds brightness without the jazz complexity of a full 9th chord.",
  "madd9": "Minor add 9: minor triad + 9th. Moody, atmospheric sound.",
  "add11": "Add 11: major triad + 11th (=4th). Adds a suspended quality while keeping the 3rd.",
  "madd11": "Minor add 11: minor triad + 11th. Rich minor color.",
  "add13": "Add 13: major triad + 13th (=6th). Same notes as 6th chord, different context.",
  "madd13": "Minor add 13: minor triad + 13th. Same as m6, different naming context.",
  "9": "Dominant 9th: dom7 + major 9th. Funky, soulful. Common in R&B and funk.",
  "maj9": "Major 9th: maj7 + major 9th. Beautiful, lush. Neo-soul staple.",
  "m9": "Minor 9th: m7 + major 9th. Smooth, sophisticated minor sound.",
  "7b9": "Dominant 7 flat 9: dom7 + minor 9th. Dark, Spanish/flamenco flavor.",
  "7#9": "Dominant 7 sharp 9: dom7 + augmented 9th. The 'Hendrix chord' — gritty, bluesy.",
  "9sus4": "9 sus4: 7sus4 + 9th. Open, modern sound.",
  "11": "Dominant 11th: dom9 + 11th. Complex, stacked. Often played without the 3rd to avoid clash.",
  "maj11": "Major 11th: maj9 + 11th. Ethereal, wide voicing.",
  "m11": "Minor 11th: m9 + 11th. Very common in neo-soul and contemporary jazz.",
  "13": "Dominant 13th: dom7 + 9th + 13th. Full, rich sound. Common in jazz and funk.",
  "maj13": "Major 13th: maj7 + 9th + 13th. The ultimate lush major voicing.",
  "m13": "Minor 13th: m7 + 9th + 13th. Deep, complex minor sound.",
  "13sus4": "13 sus4: 7sus4 + 9th + 13th. Wide, modern voicing.",
  "maj7#11": "Major 7 sharp 11: maj7 + #11. Lydian sound — bright, floating, cinematic.",
  "7b13": "Dominant 7 flat 13: dom7 + b13 (= #5). Altered dominant color."
};

/* ── Scale Formulas ── */
const SCALE_DATA = {
  "Diatonic Modes": {
    "Ionian (Major)": {
      intervals: [0,2,4,5,7,9,11], formula: "W-W-H-W-W-W-H",
      description: "The standard major scale. Bright, happy, resolved.",
      history: "The Ionian mode is what we simply call the 'major scale' — the foundation of Western music. It was formalized during the Renaissance as part of the church modes system, but its pattern of whole and half steps became the default scale of tonal music from the Baroque era onward. Nearly all Western music theory — chord progressions, harmony, counterpoint — is built relative to this scale. When you hear a nursery rhyme, a national anthem, or a pop chorus, chances are it's in Ionian. Its characteristic sound comes from the major 3rd (bright) and the leading tone (7th degree, just one semitone below the octave), which creates a strong pull back to the root.",
      tags: ["Foundation","Western Music","Church Modes","Tonal Center"]
    },
    "Dorian": {
      intervals: [0,2,3,5,7,9,10], formula: "W-H-W-W-W-H-W",
      description: "Minor scale with a raised 6th. Jazzy, sophisticated minor.",
      history: "Dorian is the 2nd mode of the major scale (play D to D on white keys). Named after the ancient Greek Dorians, though the Greek usage was different from the medieval church mode. What makes Dorian special is its raised 6th degree compared to natural minor — this single note gives it a brighter, more optimistic quality than Aeolian. It became the go-to minor sound in jazz (Miles Davis's 'So What' is entirely Dorian), funk, and folk music. Carlos Santana, Pink Floyd ('Another Brick in the Wall'), and Daft Punk ('Get Lucky') all use Dorian extensively. It's also the default minor mode in many Celtic and Irish folk traditions.",
      tags: ["Jazz","Funk","Celtic","Miles Davis","2nd Mode"]
    },
    "Phrygian": {
      intervals: [0,1,3,5,7,8,10], formula: "H-W-W-W-H-W-W",
      description: "Minor scale with a flat 2nd. Dark, Spanish/Middle Eastern flavor.",
      history: "Phrygian is the 3rd mode of the major scale (E to E on white keys). Its defining feature is the flat 2nd (b2) — just one semitone above the root — which gives it an immediately exotic, dark quality. This half-step tension is what creates the 'Spanish' or 'Middle Eastern' sound that Western ears associate with flamenco and Arabic music. In metal, Phrygian is extremely popular for heavy riffs (Metallica, Slayer). The mode is named after the ancient Phrygians of Anatolia (modern Turkey). The Andalusian cadence (iv-III-II-I), one of the most recognizable chord progressions in music, is built from the Phrygian mode.",
      tags: ["Flamenco","Metal","Spanish","Middle Eastern","3rd Mode"]
    },
    "Lydian": {
      intervals: [0,2,4,6,7,9,11], formula: "W-W-W-H-W-W-H",
      description: "Major scale with a raised 4th. Dreamy, floating, cinematic.",
      history: "Lydian is the 4th mode (F to F on white keys) and differs from major by just one note: a raised 4th (#4). This single alteration removes the only 'dark' interval in the major scale (the perfect 4th's slight pull downward) and replaces it with a tritone from the root, creating a bright, floating, almost weightless quality. Film composers love it — John Williams uses it extensively (the 'flying' theme from E.T., parts of Star Wars). Joe Satriani's 'Flying in a Blue Dream' is pure Lydian. In jazz, the Lydian Chromatic Concept by George Russell (1953) argued that Lydian, not Ionian, is the true 'parent scale' of tonal music.",
      tags: ["Film Scores","Cinematic","John Williams","George Russell","4th Mode"]
    },
    "Mixolydian": {
      intervals: [0,2,4,5,7,9,10], formula: "W-W-H-W-W-H-W",
      description: "Major scale with a flat 7th. Bluesy, dominant. The scale of the V chord.",
      history: "Mixolydian is the 5th mode (G to G on white keys). It sounds like major but with a flat 7th, giving it a bluesy, rock edge. This is THE scale that defines dominant 7th chords — when you see G7, you think G Mixolydian. The Beatles used it constantly ('Norwegian Wood', 'Tomorrow Never Knows'). The Rolling Stones, AC/DC, and Lynyrd Skynyrd all lean heavily on Mixolydian. In blues, almost every riff implies Mixolydian harmony. It's also fundamental in Irish folk music and Indian classical music (where it corresponds to the Khamaj thaat).",
      tags: ["Blues","Rock","Beatles","Dominant 7th","5th Mode"]
    },
    "Aeolian (Natural Minor)": {
      intervals: [0,2,3,5,7,8,10], formula: "W-H-W-W-H-W-W",
      description: "The natural minor scale. Melancholic, dark.",
      history: "The Aeolian mode is the natural minor scale — the 6th mode of major (A to A on white keys). It's the foundation of minor-key music across all genres. While the major scale sounds resolved and happy, Aeolian sounds sad, introspective, and sometimes dark. The flat 3rd, flat 6th, and flat 7th all contribute to its melancholic character. Compared to harmonic minor, it lacks the leading tone, giving it a more 'floating' sadness without the dramatic tension. R.E.M.'s 'Losing My Religion', Adele's 'Rolling in the Deep', and countless classical pieces use this mode. It's one of the two most important scales in all of Western music.",
      tags: ["Foundation","Minor Key","Melancholy","Classical","6th Mode"]
    },
    "Locrian": {
      intervals: [0,1,3,5,6,8,10], formula: "H-W-W-H-W-W-W",
      description: "Diminished scale with flat 2nd and flat 5th. Very unstable.",
      history: "Locrian is the 7th and most dissonant mode (B to B on white keys). It's unique because its 5th degree is diminished (b5), meaning even its most basic triad is a diminished chord — there's no stable 'home' to rest on. For centuries it was considered unusable as a tonal center, and even today it's the least-used mode. However, progressive metal bands (Dream Theater, Meshuggah) and avant-garde jazz musicians deliberately exploit its instability. In practice, Locrian passages are usually short and transition quickly to a more stable mode. It's more of a color or effect than a key to compose in.",
      tags: ["Unstable","Diminished","Progressive Metal","Avant-garde","7th Mode"]
    }
  },
  "Minor Variants": {
    "Harmonic Minor": {
      intervals: [0,2,3,5,7,8,11], formula: "W-H-W-W-H-3H-H",
      description: "Natural minor with a raised 7th. Creates a leading tone.",
      history: "The harmonic minor scale was 'invented' to solve a problem: in natural minor, the 7th degree is a whole step below the root, so there's no strong pull (leading tone) back to the tonic. By raising the 7th, composers created that half-step tension that makes V→i resolutions feel conclusive. The side effect is the exotic-sounding augmented 2nd gap between the b6 and raised 7th (3 semitones), which gives harmonic minor its distinctive Middle Eastern/classical flavor. It's the source of the dominant V chord in minor keys and generates the Phrygian Dominant mode (its 5th mode). Bach, Mozart, and virtually all classical composers used it constantly.",
      tags: ["Classical","Leading Tone","Middle Eastern","V chord in minor"]
    },
    "Melodic Minor (asc)": {
      intervals: [0,2,3,5,7,9,11], formula: "W-H-W-W-W-W-H",
      description: "Natural minor with raised 6th and 7th ascending.",
      history: "Melodic minor was created to smooth out the awkward augmented 2nd gap in harmonic minor. By also raising the 6th degree, the scale has no gaps larger than a whole step, making melodies flow more naturally upward. Traditionally, the raised notes only apply ascending — descending, it reverts to natural minor. In jazz, however, melodic minor is used in both directions and serves as the parent scale for several crucial jazz modes: the Altered scale (7th mode), Lydian Dominant (4th mode), and Locrian #2 (6th mode). It's arguably more important in jazz theory than the major scale itself.",
      tags: ["Jazz Foundation","Smooth Voice Leading","Altered Scale Source","Classical"]
    }
  },
  "Pentatonic & Blues": {
    "Major Pentatonic": {
      intervals: [0,2,4,7,9], formula: "W-W-3H-W-3H",
      description: "5-note major scale. Universal, found worldwide.",
      history: "The major pentatonic is perhaps the most universal scale in human music. It appears independently in Chinese, Japanese, Celtic, African, Native American, and countless other musical traditions — suggesting something fundamental about how humans perceive these intervals. It's the major scale with the 4th and 7th removed, eliminating all semitone tensions, so every note sounds 'good' against every other note. Bobby McFerrin famously demonstrated its universality by getting any audience worldwide to sing it spontaneously. 'Amazing Grace', 'My Girl' by The Temptations, and most folk melodies worldwide use this scale.",
      tags: ["Universal","Folk","World Music","Bobby McFerrin","5 Notes"]
    },
    "Minor Pentatonic": {
      intervals: [0,3,5,7,10], formula: "3H-W-W-3H-W",
      description: "5-note minor scale. Backbone of blues, rock, and pop soloing.",
      history: "The minor pentatonic is the single most important scale in popular music soloing. It's the first scale most guitarists learn, and for good reason — it works over almost everything. B.B. King built an entire legendary career around essentially five notes. Led Zeppelin's 'Stairway to Heaven' solo, Guns N' Roses' 'Sweet Child O' Mine', AC/DC's 'Back in Black' — all minor pentatonic. It comes from the natural minor scale with the 2nd and 6th removed, eliminating the notes that create the most dissonance. The result is a scale that's practically mistake-proof.",
      tags: ["Blues","Rock","Guitar Essential","B.B. King","Mistake-proof"]
    },
    "Blues Scale": {
      intervals: [0,3,5,6,7,10], formula: "3H-W-H-H-3H-W",
      description: "Minor pentatonic + blue note (b5). Essential blues/rock.",
      history: "The blues scale adds one note to the minor pentatonic: the 'blue note' (b5/tritone). This single addition transforms the scale from folk-like to distinctly bluesy. The blue note doesn't belong to any diatonic scale — it exists in the 'cracks' of Western tuning, reflecting the African-American vocal tradition of bending notes between the standard pitches. Blues musicians often slide through the blue note rather than landing on it, creating the characteristic 'dirty' sound. The blues scale (and blues music) is the root of virtually all modern popular music: jazz, rock, R&B, hip-hop, and pop all descend from the blues.",
      tags: ["Blues","African-American","Blue Note","Root of Popular Music"]
    },
    "Major Blues": {
      intervals: [0,2,3,4,7,9], formula: "W-H-H-3H-W-3H",
      description: "Major pentatonic + blue note (b3). Sweet, soulful quality.",
      history: "The major blues scale adds a chromatic passing tone (the b3, or 'blue note') to the major pentatonic, creating a sweet, soulful color that blurs the line between major and minor. This ambiguity is central to the blues — the music isn't quite happy, isn't quite sad. Country blues players, gospel musicians, and jazz soloists frequently mix major and minor blues scales in the same solo, creating emotional complexity. It's particularly effective for sounding 'sweet' over dominant 7th chords. Allman Brothers, Eric Clapton's acoustic work, and much of gospel piano use this scale extensively.",
      tags: ["Gospel","Country Blues","Major-Minor Ambiguity","Soulful"]
    }
  },
  "Symmetric": {
    "Whole Tone": {
      intervals: [0,2,4,6,8,10], formula: "W-W-W-W-W-W",
      description: "All whole steps. Dreamy, floaty, no clear tonal center.",
      history: "The whole tone scale divides the octave into 6 equal whole steps, creating perfect symmetry — there are only 2 possible whole tone scales. Because every interval is identical, there's no sense of 'home' or resolution; the scale seems to float in space. Claude Debussy was the first major composer to exploit this quality, using it to create the shimmering, impressionistic soundscapes of pieces like 'Voiles'. In film, it's the go-to sound for dream sequences, dissolves, and magical moments. Stevie Wonder used it in 'You Are the Sunshine of My Life'. Thelonious Monk and Wayne Shorter also explored it in jazz.",
      tags: ["Debussy","Impressionism","Dream Sequences","Only 2 Transpositions"]
    },
    "Diminished (H-W)": {
      intervals: [0,1,3,4,6,7,9,10], formula: "H-W-H-W-H-W-H-W",
      description: "Alternating half-whole steps. Symmetric, dominant function.",
      history: "The half-whole diminished scale (also called the 'dominant diminished' or 'octatonic scale') alternates half and whole steps, creating an 8-note symmetric scale with only 3 possible transpositions. In jazz, it's used over dominant 7th chords because it contains the root, 3rd, 5th, and b7 of the chord plus all the juicy altered tensions (b9, #9, #11, 13). Russian composers Rimsky-Korsakov and Stravinsky used it extensively — Stravinsky's 'Rite of Spring' features it prominently. In jazz, it's a standard tool for creating tension over dominant chords.",
      tags: ["Jazz","Stravinsky","8 Notes","3 Transpositions","Altered Tensions"]
    },
    "Diminished (W-H)": {
      intervals: [0,2,3,5,6,8,9,11], formula: "W-H-W-H-W-H-W-H",
      description: "Alternating whole-half steps. Over diminished 7th chords.",
      history: "The whole-half diminished scale is the complement of the half-whole version — same pattern, starting from the other step. It's primarily used over diminished 7th chords, where it sounds perfectly 'inside'. Because diminished 7th chords are themselves symmetric (all minor 3rds), this scale maps perfectly onto them. It contains every note of the diminished 7th chord plus passing tones that fill in the gaps smoothly. Classical composers used diminished passages for centuries to create tension and drama (think villain music, storm scenes).",
      tags: ["Diminished 7th Chords","Classical Drama","Symmetric","8 Notes"]
    },
    "Chromatic": {
      intervals: [0,1,2,3,4,5,6,7,8,9,10,11], formula: "All half steps",
      description: "All 12 notes. Passing tones and chromatic runs.",
      history: "The chromatic scale includes all 12 semitones in Western music. It's not really a 'scale' you compose in — rather, it's the complete set of available notes. Chromatic passages (runs through consecutive semitones) are used for drama, virtuosity, and voice leading. Bach's 'Chromatic Fantasy and Fugue', Chopin's etudes, and Liszt's showpieces feature chromatic runs. In jazz, chromatic approach notes (playing a half step above or below your target note before landing on it) are a fundamental improvisation technique. The 12-tone technique of Schoenberg uses all 12 chromatic notes equally, avoiding any tonal center.",
      tags: ["All 12 Notes","Virtuosity","Schoenberg","Passing Tones"]
    }
  },
  "World & Ethnic": {
    "Phrygian Dominant": {
      intervals: [0,1,4,5,7,8,10], formula: "H-3H-H-W-H-W-W",
      description: "5th mode of harmonic minor. Spanish/flamenco, Jewish music.",
      history: "Phrygian Dominant is the 5th mode of the harmonic minor scale. It combines the exotic flat 2nd of Phrygian with a major 3rd, creating a distinctive 3-semitone gap between b2 and 3 that sounds unmistakably Spanish, Middle Eastern, or Jewish. It's called 'Phrygian Dominant' because it works perfectly over a dominant chord built on a Phrygian root. In flamenco, this is the fundamental scale — the 'Spanish Phrygian'. In Jewish liturgical music, it's called 'Freygish' or 'Ahava Rabbah'. In Arabic music, it corresponds to the Hijaz jins. Dick Dale's 'Misirlou' (later used in Pulp Fiction) is a famous example.",
      tags: ["Flamenco","Jewish/Freygish","Arabic/Hijaz","Misirlou","Harmonic Minor Mode 5"]
    },
    "Hungarian Minor": {
      intervals: [0,2,3,6,7,8,11], formula: "W-H-3H-H-H-3H-H",
      description: "Exotic scale with two augmented 2nds. Dark, dramatic.",
      history: "The Hungarian Minor (also called the Double Harmonic Minor or Gypsy Minor) has two augmented 2nd intervals, giving it an intensely exotic and dramatic character. Despite its name, it's used across Eastern Europe, the Balkans, and the Middle East. Liszt and Brahms incorporated 'Hungarian' elements inspired by Romani (gypsy) musicians they heard in cafes and concerts. In modern music, it appears in metal (for its dark intensity), film scores (especially for Eastern European or 'exotic' settings), and progressive rock. The scale evokes mystery, danger, and ancient traditions.",
      tags: ["Eastern European","Romani/Gypsy","Liszt","Two Augmented 2nds","Dark"]
    },
    "Double Harmonic Major": {
      intervals: [0,1,4,5,7,8,11], formula: "H-3H-H-W-H-3H-H",
      description: "Byzantine scale. Middle Eastern, Indian classical music.",
      history: "The Double Harmonic Major (Byzantine scale, Arabic scale, or Bhairav raga) has two augmented 2nds symmetrically placed, giving it a 'mirror' quality. It sounds exotic to Western ears but is home territory for Middle Eastern, North African, and Indian musicians. In Indian classical music, it corresponds to the Bhairav thaat/raga, traditionally performed at dawn. The scale appears in Greek Orthodox and Byzantine church music, hence the 'Byzantine' name. In modern Western music, it's used when composers want to evoke the Middle East or India without using simpler stereotypes.",
      tags: ["Byzantine","Arabic","Indian/Bhairav","Dawn Raga","Mirror Symmetry"]
    },
    "Hirajoshi": {
      intervals: [0,2,3,7,8], formula: "W-H-2W-H-2W",
      description: "Japanese pentatonic scale. Mysterious, meditative.",
      history: "The Hirajoshi scale is a Japanese pentatonic scale that became widely known in Western music through its use in film and video game soundtracks. Its combination of the minor 3rd, large gaps (2 whole steps), and the haunting flat 6th create an immediately recognizable 'Japanese' quality. Traditional koto (13-string zither) music frequently uses Hirajoshi tuning. In Western rock and metal, guitarists like Marty Friedman (Megadeth) and Steve Vai have used it to add an Eastern flavor. The scale works beautifully for ambient, meditative music due to its sparse, open quality.",
      tags: ["Japanese","Koto","Meditative","Marty Friedman","5 Notes"]
    },
    "In Sen": {
      intervals: [0,1,5,7,10], formula: "H-2W-W-3H-W",
      description: "Japanese scale. Dark, atmospheric.",
      history: "The In Sen scale is associated with the shakuhachi (Japanese bamboo flute) tradition and has a darker, more austere quality than Hirajoshi. The half-step at the beginning creates tension, while the large gaps (2 and 3 semitone jumps) create an open, sparse atmosphere. 'In' refers to the 'in' (yin/shade) scale system in Japanese music theory, as opposed to the brighter 'yo' system. The scale is used in Zen Buddhist meditation music and has been adopted by ambient and atmospheric black metal musicians for its dark, contemplative quality.",
      tags: ["Japanese","Shakuhachi","Zen Buddhist","Dark Atmosphere","5 Notes"]
    },
    "Yo": {
      intervals: [0,2,5,7,9], formula: "W-3H-W-W-3H",
      description: "Japanese pentatonic. Bright, pastoral.",
      history: "The Yo scale represents the bright ('yang/sun') side of Japanese pentatonic music, as opposed to the darker 'in' scales. It's found in Japanese folk songs, festival music, and children's songs. Without any semitone intervals, it has a warm, open quality similar to the Western major pentatonic but with a distinctly different character due to its specific interval pattern. Traditional min'yo (folk songs), matsuri (festival) music, and Okinawan music use scales closely related to Yo. Its pastoral, joyful quality makes it perfect for evoking rural Japan.",
      tags: ["Japanese Folk","Festival/Matsuri","Pastoral","Bright","5 Notes"]
    }
  },
  "Jazz": {
    "Bebop Dominant": {
      intervals: [0,2,4,5,7,9,10,11], formula: "W-W-H-W-W-H-H-H",
      description: "Mixolydian + passing natural 7th. Keeps chord tones on beats.",
      history: "The bebop dominant scale was codified by jazz theorist David Baker, though Charlie Parker, Dizzy Gillespie, and other bebop pioneers used it intuitively. The 'trick' is simple but brilliant: by adding a chromatic passing tone (the natural 7th) to the Mixolydian scale, you get an 8-note scale where all the chord tones (root, 3rd, 5th, b7) fall on downbeats when you play continuous 8th notes. This means your lines always outline the chord clearly, even at blazing tempos. It's the reason bebop lines sound so coherent despite their complexity.",
      tags: ["Bebop","Charlie Parker","8 Notes","Chord Tones on Beats","David Baker"]
    },
    "Bebop Major": {
      intervals: [0,2,4,5,7,8,9,11], formula: "W-W-H-W-H-H-W-H",
      description: "Major scale + b6 passing tone. Smooth chromatic movement.",
      history: "The bebop major scale adds a chromatic passing tone (#5/b6) to the standard major scale, again creating an 8-note scale where chord tones align with beats. It's used over major 7th chords and creates smooth chromatic movement in the upper part of the scale. Barry Harris, the legendary Detroit pianist and educator, built an entire teaching method around the bebop major scale and its relationship to diminished chords. His approach shows how a single scale can generate virtually all the harmonic vocabulary of bebop.",
      tags: ["Bebop","Barry Harris","Major 7th Chords","8 Notes","Chromatic"]
    },
    "Bebop Dorian": {
      intervals: [0,2,3,4,5,7,9,10], formula: "W-H-H-H-W-W-H-W",
      description: "Dorian + passing major 3rd. Jazz improv over minor chords.",
      history: "The bebop Dorian scale adds a chromatic passing tone (the major 3rd) between the minor 3rd and the perfect 4th of the Dorian mode. This creates the same 'chord tones on beats' effect for minor 7th chords. The passing major 3rd also creates a momentary major-minor ambiguity that gives bebop its characteristic 'blue' color over minor chords. It's especially common in hard bop and post-bop, where musicians like Cannonball Adderley and Horace Silver used it to blend the sophistication of bebop with the earthiness of blues and gospel.",
      tags: ["Hard Bop","Minor 7th Chords","Cannonball Adderley","8 Notes","Blues Feel"]
    },
    "Altered (Super Locrian)": {
      intervals: [0,1,3,4,6,8,10], formula: "H-W-H-W-W-W-W",
      description: "7th mode of melodic minor. All tensions altered.",
      history: "The altered scale (Super Locrian) is the 7th mode of melodic minor and contains EVERY possible alteration of a dominant chord: b9, #9, b5 (#11), and #5 (b13). It's the 'maximum tension' scale for dominant 7th chords resolving to I. When a jazz musician sees 'G7alt', they play G altered. The beauty is that all this complexity comes from a simple source — it's just Ab melodic minor played over a G bass note. John Coltrane, McCoy Tyner, and Herbie Hancock use it constantly. It's the sound of modern jazz tension at its most intense.",
      tags: ["Maximum Tension","Melodic Minor Mode 7","Coltrane","All Alterations","V7alt"]
    },
    "Lydian Dominant": {
      intervals: [0,2,4,6,7,9,10], formula: "W-W-W-H-W-H-W",
      description: "4th mode of melodic minor. Lydian + b7.",
      history: "Lydian Dominant is the 4th mode of melodic minor — it combines the bright, raised 4th of Lydian with the flat 7th of Mixolydian. The result is a scale that sounds both 'bright and floating' (from the #4) and 'dominant/bluesy' (from the b7). It's the primary scale for tritone substitutions in jazz — when you substitute Db7 for G7, Db Lydian Dominant gives you all the right tensions. It's also used for dominant chords with a #11 voicing, which has a distinctly modern, sophisticated sound. Wayne Shorter and Chick Corea use this scale extensively.",
      tags: ["Tritone Substitution","Melodic Minor Mode 4","#11 Voicings","Wayne Shorter","Modern Jazz"]
    }
  }
};

/* ── Interval Names ── */
const INTERVAL_NAMES = [
  {semitones:0, name:"Unison (P1)", short:"P1"},
  {semitones:1, name:"Minor 2nd (m2)", short:"m2"},
  {semitones:2, name:"Major 2nd (M2)", short:"M2"},
  {semitones:3, name:"Minor 3rd (m3)", short:"m3"},
  {semitones:4, name:"Major 3rd (M3)", short:"M3"},
  {semitones:5, name:"Perfect 4th (P4)", short:"P4"},
  {semitones:6, name:"Tritone (TT)", short:"TT"},
  {semitones:7, name:"Perfect 5th (P5)", short:"P5"},
  {semitones:8, name:"Minor 6th (m6)", short:"m6"},
  {semitones:9, name:"Major 6th (M6)", short:"M6"},
  {semitones:10, name:"Minor 7th (m7)", short:"m7"},
  {semitones:11, name:"Major 7th (M7)", short:"M7"},
  {semitones:12, name:"Octave (P8)", short:"P8"}
];

/* ── Chord Progressions by Genre ── */
const PROGRESSIONS = {
  "Pop": [
    { name: "The Most Common", roman: "I – V – vi – IV", degrees: [0,4,5,3], qualities: ["","","m",""], description: "The most-used progression in pop music. 'Let It Be', 'No Woman No Cry', 'With or Without You', countless modern hits." },
    { name: "50s Progression", roman: "I – vi – IV – V", degrees: [0,5,3,4], qualities: ["","m","",""], description: "Doo-wop classic. 'Stand by Me', 'Every Breath You Take'. Smooth, nostalgic cycle." },
    { name: "Axis of Awesome", roman: "vi – IV – I – V", degrees: [5,3,0,4], qualities: ["m","","",""], description: "Same chords as I-V-vi-IV starting from vi. 'Despacito', 'Africa' by Toto, 'Poker Face'." },
    { name: "Plagal Life", roman: "I – IV – V – IV", degrees: [0,3,4,3], qualities: ["","","",""], description: "Rock-pop staple. Simple, driving feel. 'Twist and Shout', 'La Bamba'." },
    { name: "Canon Progression", roman: "I – V – vi – iii – IV – I – IV – V", degrees: [0,4,5,2,3,0,3,4], qualities: ["","","m","m","","","",""], description: "Pachelbel's Canon in D. Descending bass line. 'Basket Case', 'Graduation' by Vitamin C." }
  ],
  "Jazz": [
    { name: "ii-V-I Major", roman: "ii – V – I", degrees: [1,4,0], qualities: ["m7","7","maj7"], description: "THE fundamental jazz cadence. Found in virtually every jazz standard. The V7 creates tension that resolves to I." },
    { name: "ii-V-i Minor", roman: "ii – V – i", degrees: [1,4,0], qualities: ["m7b5","7","m7"], minor: true, description: "Minor key version. The ii is half-diminished, V is often dominant 7(b9). Dark, sophisticated." },
    { name: "Rhythm Changes Turnaround", roman: "I – vi – ii – V", degrees: [0,5,1,4], qualities: ["maj7","m7","m7","7"], description: "From Gershwin's 'I Got Rhythm'. The basis for hundreds of jazz tunes. Cyclic, propulsive." },
    { name: "Extended Turnaround", roman: "iii – vi – ii – V", degrees: [2,5,1,4], qualities: ["m7","m7","m7","7"], description: "Starts from iii for a longer approach to I. Common in jazz intros and turnarounds." },
    { name: "Jazz Blues (first 4 bars)", roman: "I7 – IV7 – I7 – I7", degrees: [0,3,0,0], qualities: ["7","7","7","7"], description: "Opening of the 12-bar jazz blues. All dominant 7th chords. Add ii-V's for more color." },
    { name: "Coltrane Changes", roman: "I – bIII – V – I", degrees_abs: [0,4,8,0], qualities: ["maj7","maj7","maj7","maj7"], description: "John Coltrane's 'Giant Steps'. Major thirds cycle. One of the most challenging progressions in jazz." }
  ],
  "Bossa Nova": [
    { name: "Classic Bossa", roman: "Imaj7 – ii(m7) – V7 – Imaj7", degrees: [0,1,4,0], qualities: ["maj7","m7","7","maj7"], description: "Standard bossa nova cycle. Gentle, swaying. Play with syncopated rhythm, light touch." },
    { name: "Girl from Ipanema Style", roman: "Imaj7 – bIImaj7 – ii(m7) – V7", degrees_abs: [0,1,1,4], qualities: ["maj7","maj7","m7","7"], description: "Chromatic movement from I to bII creates the signature bossa color. Dreamy, sophisticated." },
    { name: "Bossa Turnaround", roman: "Imaj7 – vi(m7) – ii(m7) – V7", degrees: [0,5,1,4], qualities: ["maj7","m7","m7","7"], description: "Same as jazz turnaround but played with bossa rhythm. Light, floating feel." }
  ],
  "Flamenco": [
    { name: "Andalusian Cadence", roman: "iv – III – II – I", degrees: [3,2,1,0], qualities: ["m","","",""], phrygian: true, description: "THE flamenco progression. In Phrygian mode, descending. 'Hit the Road Jack', 'Hava Nagila'. The I chord is often played as major." },
    { name: "Phrygian Dominant", roman: "i – bVII – bVI – V", degrees_abs: [0,10,8,7], qualities: ["m","","",""], description: "Uses the Phrygian dominant scale. Exotic, intense. Common in flamenco guitar." },
    { name: "Buleria Pattern", roman: "i – bVII – bVI – V – i", degrees_abs: [0,10,8,7,0], qualities: ["m","","","","m"], description: "Extended flamenco pattern with return to i. Fast, rhythmic, percussive." }
  ],
  "Blues": [
    { name: "12-Bar Blues", roman: "I7 – I7 – I7 – I7 – IV7 – IV7 – I7 – I7 – V7 – IV7 – I7 – V7", degrees: [0,0,0,0,3,3,0,0,4,3,0,4], qualities: ["7","7","7","7","7","7","7","7","7","7","7","7"], description: "The foundation of blues, rock 'n' roll, and much of popular music. All dominant 7th chords." },
    { name: "Minor Blues", roman: "i7 – i7 – i7 – i7 – iv7 – iv7 – i7 – i7 – bVI7 – V7 – i7 – V7", degrees_abs: [0,0,0,0,5,5,0,0,8,7,0,7], qualities: ["m7","m7","m7","m7","m7","m7","m7","m7","7","7","m7","7"], description: "Darker blues variant. Minor i chord, uses bVI and V for turnaround. Thrill Is Gone." },
    { name: "8-Bar Blues", roman: "I7 – V7 – IV7 – IV7 – I7 – V7 – I7 – V7", degrees: [0,4,3,3,0,4,0,4], qualities: ["7","7","7","7","7","7","7","7"], description: "Shorter blues form. 'Key to the Highway', 'Heartbreak Hotel'." },
    { name: "Jazz Blues", roman: "I7 – IV7 – I7 – vi-ii – V – ii7 – V7 – I7 – vi-ii – V7 – I7 – ii-V", degrees: [0,3,0,0,4,1,4,0,0,4,0,1], qualities: ["7","7","7","7","7","m7","7","7","7","7","7","m7"], description: "Blues with jazz substitutions. ii-V turnarounds added for harmonic richness." }
  ],
  "Rock": [
    { name: "Classic Rock", roman: "I – IV – V", degrees: [0,3,4], qualities: ["","",""], description: "The foundation of rock 'n' roll. 'Johnny B. Goode', 'Wild Thing'. Pure energy." },
    { name: "Rock Cadence", roman: "I – bVII – IV – I", degrees_abs: [0,10,5,0], qualities: ["","","",""], description: "Flat seventh approach. 'Sweet Home Alabama' (in a way), 'Hey Jude' ending." },
    { name: "Grunge / Alt Rock", roman: "I – bIII – bVII – IV", degrees_abs: [0,3,10,5], qualities: ["","","",""], description: "Minor-flavored rock. Power chords work great. 'Smells Like Teen Spirit' vibe." },
    { name: "Power Ballad", roman: "I – V – vi – IV", degrees: [0,4,5,3], qualities: ["5","5","5","5"], description: "Same as pop but with power chords and distortion. Anthemic, stadium-filling." }
  ],
  "Classical": [
    { name: "Authentic Cadence", roman: "I – IV – V – I", degrees: [0,3,4,0], qualities: ["","","",""], description: "The most fundamental cadence in Western music. Tension (V) resolves to rest (I)." },
    { name: "Minor Authentic", roman: "i – iv – V – i", degrees: [0,3,4,0], qualities: ["m","m","","m"], description: "Minor key cadence. The V is often major (harmonic minor) for stronger resolution." },
    { name: "Deceptive Cadence", roman: "I – IV – V – vi", degrees: [0,3,4,5], qualities: ["","","","m"], description: "Instead of resolving V→I, it goes V→vi. Surprise! Creates beautiful unexpected turns." },
    { name: "Circle of Fifths", roman: "I – IV – viio – iii – vi – ii – V – I", degrees: [0,3,6,2,5,1,4,0], qualities: ["","","dim","m","m","m","",""], description: "Descending fifths through all diatonic chords. Bach's favorite. Ultimate harmonic completeness." }
  ],
  "R&B / Neo-Soul": [
    { name: "Neo-Soul Staple", roman: "Imaj9 – IV9 – vi(m9) – V13", degrees: [0,3,5,4], qualities: ["maj9","9","m9","13"], description: "Rich extended chords. Erykah Badu, D'Angelo, Anderson .Paak territory. Warm, sophisticated." },
    { name: "Gospel Turn", roman: "ii(m11) – V13 – Imaj9", degrees: [1,4,0], qualities: ["m11","13","maj9"], description: "Jazz ii-V-I with bigger voicings. Gospel-influenced. Kirk Franklin, Snarky Puppy." },
    { name: "Smooth R&B", roman: "Imaj7 – iii(m7) – vi(m7) – V7", degrees: [0,2,5,4], qualities: ["maj7","m7","m7","7"], description: "Smooth, seductive. SZA, Daniel Caesar, Frank Ocean. Extended voicings essential." },
    { name: "Dark R&B", roman: "i(m9) – bVII(9) – bVI(maj9) – V(7#9)", degrees_abs: [0,10,8,7], qualities: ["m9","9","maj9","7#9"], description: "Minor key R&B with altered dominants. The Weeknd, Bryson Tiller. Moody, atmospheric." }
  ],
  "Country": [
    { name: "Classic Country", roman: "I – IV – V – I", degrees: [0,3,4,0], qualities: ["","","",""], description: "Simple, honest. The backbone of country music. Hank Williams, Johnny Cash." },
    { name: "Country Waltz", roman: "I – V – I – IV – I – V – I", degrees: [0,4,0,3,0,4,0], qualities: ["","","","","","",""], description: "3/4 time, gentle. 'Tennessee Waltz'. Simple but timeless." },
    { name: "Nashville Turnaround", roman: "I – IV – I – V", degrees: [0,3,0,4], qualities: ["","","",""], description: "The Nashville Number System uses numbers instead of note names. This is the most basic pattern." },
    { name: "Country Rock", roman: "I – bVII – IV – I", degrees_abs: [0,10,5,0], qualities: ["","","",""], description: "Adds the flat VII from Mixolydian. Lynyrd Skynyrd, The Allman Brothers." }
  ]
};

/* ── Theory Content ── */
const THEORY_SECTIONS = [
  {
    id: "intervals", title: "Intervals",
    content: `<div class="theory-text">
      <p>An <strong>interval</strong> is the distance between two notes, measured in semitones (half steps). Intervals are the building blocks of all chords and scales.</p>
      <p>Each interval has a unique sound quality — from the tight dissonance of a <strong>minor 2nd</strong> to the perfect consonance of an <strong>octave</strong>.</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Interval</th><th>Semitones</th><th>Sound Quality</th><th>Example (from C)</th><th></th></tr></thead>
      <tbody>
        <tr><td>Unison (P1)</td><td>0</td><td>Same note</td><td>C → C</td><td><button class="play-interval-btn" data-st="0">Play</button></td></tr>
        <tr><td>Minor 2nd (m2)</td><td>1</td><td>Tense, dissonant — 'Jaws' theme</td><td>C → Db</td><td><button class="play-interval-btn" data-st="1">Play</button></td></tr>
        <tr><td>Major 2nd (M2)</td><td>2</td><td>Bright step — 'Happy Birthday' start</td><td>C → D</td><td><button class="play-interval-btn" data-st="2">Play</button></td></tr>
        <tr><td>Minor 3rd (m3)</td><td>3</td><td>Sad, dark — minor chord sound</td><td>C → Eb</td><td><button class="play-interval-btn" data-st="3">Play</button></td></tr>
        <tr><td>Major 3rd (M3)</td><td>4</td><td>Happy, bright — major chord sound</td><td>C → E</td><td><button class="play-interval-btn" data-st="4">Play</button></td></tr>
        <tr><td>Perfect 4th (P4)</td><td>5</td><td>Open, hymn-like — 'Here Comes the Bride'</td><td>C → F</td><td><button class="play-interval-btn" data-st="5">Play</button></td></tr>
        <tr><td>Tritone (TT)</td><td>6</td><td>Unstable, devilish — 'The Simpsons' theme</td><td>C → F#</td><td><button class="play-interval-btn" data-st="6">Play</button></td></tr>
        <tr><td>Perfect 5th (P5)</td><td>7</td><td>Strong, stable — power chord</td><td>C → G</td><td><button class="play-interval-btn" data-st="7">Play</button></td></tr>
        <tr><td>Minor 6th (m6)</td><td>8</td><td>Bittersweet — love themes</td><td>C → Ab</td><td><button class="play-interval-btn" data-st="8">Play</button></td></tr>
        <tr><td>Major 6th (M6)</td><td>9</td><td>Warm, nostalgic — 'My Bonnie'</td><td>C → A</td><td><button class="play-interval-btn" data-st="9">Play</button></td></tr>
        <tr><td>Minor 7th (m7)</td><td>10</td><td>Bluesy, wanting resolution</td><td>C → Bb</td><td><button class="play-interval-btn" data-st="10">Play</button></td></tr>
        <tr><td>Major 7th (M7)</td><td>11</td><td>Dreamy, jazzy tension</td><td>C → B</td><td><button class="play-interval-btn" data-st="11">Play</button></td></tr>
        <tr><td>Octave (P8)</td><td>12</td><td>Same note, higher — 'Somewhere Over the Rainbow'</td><td>C → C</td><td><button class="play-interval-btn" data-st="12">Play</button></td></tr>
      </tbody>
    </table>`
  },
  {
    id: "triads", title: "Triads",
    content: `<div class="theory-text">
      <p>A <strong>triad</strong> is a three-note chord built by stacking thirds. There are four types of triads, each with a distinct emotional quality:</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Triad</th><th>Formula</th><th>Intervals</th><th>Sound</th><th>Example</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>Major</strong></td><td>1 – 3 – 5</td><td>Root + M3 + P5</td><td>Happy, bright, stable</td><td>C E G</td><td><button class="play-interval-btn" data-chord="0,4,7">Play</button></td></tr>
        <tr><td><strong>Minor</strong></td><td>1 – b3 – 5</td><td>Root + m3 + P5</td><td>Sad, dark, introspective</td><td>C Eb G</td><td><button class="play-interval-btn" data-chord="0,3,7">Play</button></td></tr>
        <tr><td><strong>Diminished</strong></td><td>1 – b3 – b5</td><td>Root + m3 + TT</td><td>Tense, unstable, anxious</td><td>C Eb Gb</td><td><button class="play-interval-btn" data-chord="0,3,6">Play</button></td></tr>
        <tr><td><strong>Augmented</strong></td><td>1 – 3 – #5</td><td>Root + M3 + m6</td><td>Mysterious, dreamlike</td><td>C E G#</td><td><button class="play-interval-btn" data-chord="0,4,8">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>How to think about it:</strong> The 3rd determines major vs minor feel. The 5th determines stability (perfect = stable, diminished = tense, augmented = floating).</p>
    </div>`
  },
  {
    id: "sevenths", title: "7th Chords",
    content: `<div class="theory-text">
      <p><strong>7th chords</strong> add a fourth note — the 7th — on top of a triad. This adds richness and complexity. There are several types:</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>7th Chord</th><th>Formula</th><th>Built From</th><th>Sound / Usage</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>Dominant 7th</strong> (C7)</td><td>1 – 3 – 5 – b7</td><td>Major triad + m7</td><td>Bluesy tension, wants to resolve. The V chord.</td><td><button class="play-interval-btn" data-chord="0,4,7,10">Play</button></td></tr>
        <tr><td><strong>Major 7th</strong> (Cmaj7)</td><td>1 – 3 – 5 – 7</td><td>Major triad + M7</td><td>Lush, dreamy, beautiful. Jazz ballads, bossa nova.</td><td><button class="play-interval-btn" data-chord="0,4,7,11">Play</button></td></tr>
        <tr><td><strong>Minor 7th</strong> (Cm7)</td><td>1 – b3 – 5 – b7</td><td>Minor triad + m7</td><td>Smooth, mellow. The ii chord in jazz.</td><td><button class="play-interval-btn" data-chord="0,3,7,10">Play</button></td></tr>
        <tr><td><strong>Diminished 7th</strong> (Cdim7)</td><td>1 – b3 – b5 – bb7</td><td>Dim triad + dim7</td><td>Maximum tension, symmetric. Classical drama.</td><td><button class="play-interval-btn" data-chord="0,3,6,9">Play</button></td></tr>
        <tr><td><strong>Half-diminished</strong> (Cm7b5)</td><td>1 – b3 – b5 – b7</td><td>Dim triad + m7</td><td>Dark tension. The ii in minor-key jazz.</td><td><button class="play-interval-btn" data-chord="0,3,6,10">Play</button></td></tr>
        <tr><td><strong>Minor-Major 7th</strong> (Cm(maj7))</td><td>1 – b3 – 5 – 7</td><td>Minor triad + M7</td><td>Mysterious, noir. James Bond chord.</td><td><button class="play-interval-btn" data-chord="0,3,7,11">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>Key insight:</strong> The type of 7th (major or minor) combined with the type of triad creates different tensions. Dominant 7 = major triad + minor 7th — this mismatch is what creates the 'need to resolve'.</p>
    </div>`
  },
  {
    id: "suspended", title: "Suspended",
    content: `<div class="theory-text">
      <p><strong>Suspended chords</strong> replace the 3rd with either the 2nd or 4th. Since the 3rd defines major/minor, removing it creates an <strong>ambiguous, open</strong> sound that 'suspends' the resolution.</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Chord</th><th>Formula</th><th>What Happens</th><th>Sound</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>sus2</strong> (Csus2)</td><td>1 – 2 – 5</td><td>3rd replaced by major 2nd</td><td>Open, modern, airy. U2, The Police.</td><td><button class="play-interval-btn" data-chord="0,2,7">Play</button></td></tr>
        <tr><td><strong>sus4</strong> (Csus4)</td><td>1 – 4 – 5</td><td>3rd replaced by perfect 4th</td><td>Yearning, unresolved. Wants to fall to major 3rd.</td><td><button class="play-interval-btn" data-chord="0,5,7">Play</button></td></tr>
        <tr><td><strong>7sus4</strong> (C7sus4)</td><td>1 – 4 – 5 – b7</td><td>Dominant + suspended 4th</td><td>Floating tension. Common before V7 resolution.</td><td><button class="play-interval-btn" data-chord="0,5,7,10">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>Tip:</strong> sus4 → major is one of the most satisfying resolutions in music. Try playing Csus4 then C — you'll recognize it instantly from hundreds of songs.</p>
    </div>`
  },
  {
    id: "added", title: "Added Tones",
    content: `<div class="theory-text">
      <p><strong>Added tone chords</strong> take a basic triad and add one extra note <em>without</em> including the 7th. This distinguishes them from extended chords (9, 11, 13) which imply the 7th is present.</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Chord</th><th>Formula</th><th>What's Added</th><th>Sound</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>add9</strong> (Cadd9)</td><td>1 – 2 – 3 – 5</td><td>Major 9th (= 2nd up an octave)</td><td>Bright sparkle. Oasis 'Wonderwall', pop staple.</td><td><button class="play-interval-btn" data-chord="0,2,4,7">Play</button></td></tr>
        <tr><td><strong>madd9</strong> (Cm(add9))</td><td>1 – 2 – b3 – 5</td><td>Major 9th to minor triad</td><td>Moody, atmospheric. Radiohead territory.</td><td><button class="play-interval-btn" data-chord="0,2,3,7">Play</button></td></tr>
        <tr><td><strong>add11</strong> (Cadd11)</td><td>1 – 3 – 4 – 5</td><td>Perfect 11th (= 4th)</td><td>Tension with the 3rd. Use carefully.</td><td><button class="play-interval-btn" data-chord="0,4,5,7">Play</button></td></tr>
        <tr><td><strong>add13</strong> (Cadd13)</td><td>1 – 3 – 5 – 6</td><td>Major 13th (= 6th)</td><td>Same as a 6th chord. Context determines name.</td><td><button class="play-interval-btn" data-chord="0,4,7,9">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>add9 vs 9:</strong> Cadd9 = C E G D (no 7th). C9 = C E G Bb D (has the 7th). The add9 is simpler and more pop-friendly; the 9 is jazzier.</p>
    </div>`
  },
  {
    id: "extended", title: "Extended Chords",
    content: `<div class="theory-text">
      <p><strong>Extended chords</strong> stack thirds beyond the 7th: 9th, 11th, 13th. Each implies all lower extensions are present (a 13th chord technically has root, 3, 5, 7, 9, 11, 13 — though in practice some notes are omitted).</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Chord</th><th>Full Formula</th><th>Key Interval</th><th>Sound / Usage</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>9</strong> (C9)</td><td>1 – 3 – 5 – b7 – 9</td><td>Dom7 + M9</td><td>Funky, soulful. James Brown, Stevie Wonder.</td><td><button class="play-interval-btn" data-chord="0,4,7,10,14">Play</button></td></tr>
        <tr><td><strong>maj9</strong> (Cmaj9)</td><td>1 – 3 – 5 – 7 – 9</td><td>Maj7 + M9</td><td>Beautiful, lush. Neo-soul, dream pop.</td><td><button class="play-interval-btn" data-chord="0,4,7,11,14">Play</button></td></tr>
        <tr><td><strong>m9</strong> (Cm9)</td><td>1 – b3 – 5 – b7 – 9</td><td>Min7 + M9</td><td>Smooth, sophisticated. Contemporary R&B.</td><td><button class="play-interval-btn" data-chord="0,3,7,10,14">Play</button></td></tr>
        <tr><td><strong>11</strong> (C11)</td><td>1 – 3 – 5 – b7 – 9 – 11</td><td>Dom9 + P11</td><td>Wide, open. Often omit the 3rd to avoid clash.</td><td><button class="play-interval-btn" data-chord="0,4,7,10,14,17">Play</button></td></tr>
        <tr><td><strong>m11</strong> (Cm11)</td><td>1 – b3 – 5 – b7 – 9 – 11</td><td>Min9 + P11</td><td>Rich, deep. D'Angelo, Hiatus Kaiyote.</td><td><button class="play-interval-btn" data-chord="0,3,7,10,14,17">Play</button></td></tr>
        <tr><td><strong>13</strong> (C13)</td><td>1 – 3 – 5 – b7 – 9 – 13</td><td>Dom9 + M13</td><td>Full, shimmering. Jazz big band, funk horns.</td><td><button class="play-interval-btn" data-chord="0,4,7,10,14,21">Play</button></td></tr>
        <tr><td><strong>maj13</strong> (Cmaj13)</td><td>1 – 3 – 5 – 7 – 9 – 13</td><td>Maj9 + M13</td><td>The ultimate lush chord. Orchestral jazz.</td><td><button class="play-interval-btn" data-chord="0,4,7,11,14,21">Play</button></td></tr>
      </tbody>
    </table>`
  },
  {
    id: "altered", title: "Altered Chords",
    content: `<div class="theory-text">
      <p><strong>Altered chords</strong> modify (raise or lower) one or more notes of a standard chord to create extra tension or color. Most common on dominant 7th chords.</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Alteration</th><th>What It Does</th><th>Example Chord</th><th>Sound / Usage</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>b5</strong></td><td>Lowers the 5th by a half step</td><td>C7b5: C E Gb Bb</td><td>Tritone sub chord. Used for chromatic bass movement.</td><td><button class="play-interval-btn" data-chord="0,4,6,10">Play</button></td></tr>
        <tr><td><strong>#5</strong></td><td>Raises the 5th by a half step</td><td>C7#5: C E G# Bb</td><td>Augmented dominant. Strong pull to resolution.</td><td><button class="play-interval-btn" data-chord="0,4,8,10">Play</button></td></tr>
        <tr><td><strong>b9</strong></td><td>Lowers the 9th by a half step</td><td>C7b9: C E G Bb Db</td><td>Dark, Spanish flavor. Flamenco, minor key jazz.</td><td><button class="play-interval-btn" data-chord="0,4,7,10,13">Play</button></td></tr>
        <tr><td><strong>#9</strong></td><td>Raises the 9th by a half step</td><td>C7#9: C E G Bb D#</td><td>The 'Hendrix chord'. Purple Haze. Gritty, bluesy.</td><td><button class="play-interval-btn" data-chord="0,4,7,10,15">Play</button></td></tr>
        <tr><td><strong>#11</strong></td><td>Raises the 11th by a half step</td><td>Cmaj7#11: C E F# G B</td><td>Lydian sound. Bright, floating, cinematic.</td><td><button class="play-interval-btn" data-chord="0,4,6,7,11">Play</button></td></tr>
        <tr><td><strong>b13</strong></td><td>Lowers the 13th by a half step</td><td>C7b13: C E G Ab Bb</td><td>Augmented color in a dominant context.</td><td><button class="play-interval-btn" data-chord="0,4,7,8,10">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>The 'altered scale'</strong> (Super Locrian) contains ALL alterations: b9, #9, b5 (#11), #5 (b13). It's the ultimate tension scale over a V7 chord.</p>
    </div>`
  },
  {
    id: "inversions", title: "Slash Chords & Inversions",
    content: `<div class="theory-text">
      <p>A <strong>slash chord</strong> (e.g., C/E) means "play C chord with E in the bass." When the bass note is a chord tone, it's called an <strong>inversion</strong>.</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Position</th><th>Bass Note</th><th>Example</th><th>Sound</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>Root position</strong></td><td>Root (1st) in bass</td><td>C/C: C E G</td><td>Most stable, grounded.</td><td><button class="play-interval-btn" data-chord="0,4,7">Play</button></td></tr>
        <tr><td><strong>1st inversion</strong></td><td>3rd in bass</td><td>C/E: E G C</td><td>Lighter, flowing. Great for bass lines.</td><td><button class="play-interval-btn" data-chord="-8,0,4,7">Play</button></td></tr>
        <tr><td><strong>2nd inversion</strong></td><td>5th in bass</td><td>C/G: G C E</td><td>Open, less stable. Classical cadential 6/4.</td><td><button class="play-interval-btn" data-chord="-5,0,4,7">Play</button></td></tr>
        <tr><td><strong>3rd inversion</strong> (7th chords)</td><td>7th in bass</td><td>C7/Bb: Bb C E G</td><td>Smooth voice leading. Descending bass lines.</td><td><button class="play-interval-btn" data-chord="-2,0,4,7,10">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>Non-chord-tone slash chords</strong> put a note in the bass that isn't in the chord (e.g., C/F#). These create rich polychord sounds and are common in film scoring and jazz.</p>
      <p><strong>Practical use:</strong> Inversions create smooth, stepwise bass lines. Try: C → C/E → F → F/A → G/B → C. The bass walks up: C-E-F-A-B-C.</p>
    </div>`
  },
  {
    id: "power", title: "Power Chords",
    content: `<div class="theory-text">
      <p>A <strong>power chord</strong> is just the root + perfect 5th (often doubled at the octave). It contains NO 3rd, making it neither major nor minor.</p>
    </div>
    <table class="interval-table">
      <thead><tr><th>Chord</th><th>Formula</th><th>Notes</th><th></th></tr></thead>
      <tbody>
        <tr><td><strong>C5</strong></td><td>1 – 5</td><td>C G</td><td><button class="play-interval-btn" data-chord="0,7">Play</button></td></tr>
        <tr><td><strong>C5 (octave)</strong></td><td>1 – 5 – 8</td><td>C G C</td><td><button class="play-interval-btn" data-chord="0,7,12">Play</button></td></tr>
      </tbody>
    </table>
    <div class="theory-text" style="margin-top:14px;">
      <p><strong>Why power chords work with distortion:</strong> Distortion adds harmonics. A major or minor 3rd creates harsh overtones when distorted, but the perfect 5th's overtones reinforce each other cleanly. That's why rock and metal guitarists love them.</p>
      <p><strong>Common power chord progressions:</strong></p>
      <ul style="margin:8px 0 0 20px; line-height: 1.8;">
        <li>I5 – IV5 – V5 (punk rock: Ramones, Green Day)</li>
        <li>I5 – bVII5 – IV5 (hard rock: AC/DC)</li>
        <li>I5 – bIII5 – IV5 – I5 (grunge: Nirvana)</li>
      </ul>
    </div>`
  }
];

/* ═══════════════════════════════════════════════════════
   CORE UTILITY FUNCTIONS
   ═══════════════════════════════════════════════════════ */
let audioCtx = null;
function ensureAudio() {
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  if (audioCtx.state === "suspended") audioCtx.resume();
}

function normalizeNote(n) { return NOTE_ALIAS_TO_SHARP[n] || n; }
function noteToPc(n) { return NOTE_NAMES_SHARP.indexOf(normalizeNote(n)); }
function pcToNote(pc) { return NOTE_NAMES_SHARP[((pc%12)+12)%12]; }
function midiToFreq(m) { return 440 * Math.pow(2, (m - 69) / 12); }
function displayQuality(q) { return q === "" ? "major" : q; }
function chordName(rootPc, quality) { return pcToNote(rootPc) + (quality || ""); }
function chordPitchClasses(rootPc, quality) { return new Set(CHORD_FORMULAS[quality].map(i => (rootPc+i)%12)); }
function chordNotes(rootPc, quality) { return CHORD_FORMULAS[quality].map(i => pcToNote(rootPc+i)); }
function setEquals(a, b) { if (a.size !== b.size) return false; for (const v of a) if (!b.has(v)) return false; return true; }
function isSubset(a, b) { for (const v of a) if (!b.has(v)) return false; return true; }

/* ── Major scale degrees for key generation ── */
const MAJOR_SCALE = [0,2,4,5,7,9,11];
const MINOR_SCALE = [0,2,3,5,7,8,10];

function getScaleDegreeNote(keyRoot, degree, mode) {
  const scale = mode === "minor" ? MINOR_SCALE : MAJOR_SCALE;
  return (keyRoot + scale[degree]) % 12;
}

/* ── Audio synthesis ── */
function playPianoTone(freq, when = 0) {
  ensureAudio();
  const now = audioCtx.currentTime + when;
  const gain = audioCtx.createGain();
  const filter = audioCtx.createBiquadFilter();
  filter.type = "lowpass"; filter.frequency.setValueAtTime(4200, now); filter.Q.setValueAtTime(0.5, now);

  const partials = [
    {type:"sine", multiple:1, gain:0.8, detune:0},
    {type:"triangle", multiple:2, gain:0.28, detune:2},
    {type:"sine", multiple:3, gain:0.12, detune:-3}
  ];
  gain.gain.setValueAtTime(0.0001, now);
  gain.gain.exponentialRampToValueAtTime(0.35, now + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.001, now + 2.2);
  gain.connect(audioCtx.destination);
  filter.connect(gain);

  partials.forEach(p => {
    const osc = audioCtx.createOscillator();
    const pGain = audioCtx.createGain();
    osc.type = p.type; osc.frequency.setValueAtTime(freq * p.multiple, now); osc.detune.setValueAtTime(p.detune, now);
    pGain.gain.setValueAtTime(p.gain, now);
    osc.connect(pGain); pGain.connect(filter);
    osc.start(now); osc.stop(now + 2.5);
  });
}

function playPianoChord(midiNotes) {
  ensureAudio();
  midiNotes.forEach((m, i) => playPianoTone(midiToFreq(m), i * 0.03));
}

function playGuitarTone(freq, when = 0) {
  ensureAudio();
  const now = audioCtx.currentTime + when;
  const sr = audioCtx.sampleRate;
  const len = Math.round(sr / freq);
  const frames = sr * 2;
  const buffer = audioCtx.createBuffer(1, frames, sr);
  const data = buffer.getChannelData(0);

  for (let i = 0; i < len; i++) data[i] = Math.random() * 2 - 1;
  for (let i = len; i < frames; i++) {
    data[i] = (data[i - len] + data[i - len + 1]) * 0.5 * 0.996;
  }
  const src = audioCtx.createBufferSource();
  src.buffer = buffer;
  const gain = audioCtx.createGain();
  gain.gain.setValueAtTime(0.5, now);
  gain.gain.exponentialRampToValueAtTime(0.001, now + 2);
  src.connect(gain); gain.connect(audioCtx.destination);
  src.start(now); src.stop(now + 2.2);
}

function playGuitarShape(shape) {
  ensureAudio();
  let delay = 0;
  shape.forEach((fret, stringIdx) => {
    if (fret === null) return;
    playGuitarTone(midiToFreq(GUITAR_STRINGS[stringIdx].midi + fret), delay);
    delay += 0.05;
  });
}

/* ═══════════════════════════════════════════════════════
   TAB SYSTEM
   ═══════════════════════════════════════════════════════ */
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('tab-' + btn.dataset.tab).classList.add('active');
  });
});

/* ═══════════════════════════════════════════════════════
   TAB 1: CHORD LAB
   ═══════════════════════════════════════════════════════ */
const state = {
  selectedPiano: new Set(),
  selectedGuitar: Array(6).fill(null)
};

const rootSelect = document.getElementById("rootSelect");
const qualitySelect = document.getElementById("qualitySelect");
const browserName = document.getElementById("browserName");
const browserNotes = document.getElementById("browserNotes");
const chordTooltip = document.getElementById("chordTooltip");
const pianoEl = document.getElementById("piano");
const fretboardEl = document.getElementById("fretboard");
const pianoStatus = document.getElementById("pianoStatus");
const guitarStatus = document.getElementById("guitarStatus");
const pianoDetected = document.getElementById("pianoDetected");
const guitarDetected = document.getElementById("guitarDetected");

/* Piano key layout */
const pianoKeys = [];
function buildPianoKeyData() {
  const START_MIDI = 48, END_MIDI = 72;
  let whiteX = 0;
  for (let midi = START_MIDI; midi <= END_MIDI; midi++) {
    const pc = midi % 12;
    const isBlack = [1,3,6,8,10].includes(pc);
    if (!isBlack) {
      pianoKeys.push({ midi, pc, isBlack: false, left: whiteX, label: pcToNote(pc) + (Math.floor(midi/12)-1) });
      whiteX += 42;
    }
  }
  for (let midi = START_MIDI; midi <= END_MIDI; midi++) {
    const pc = midi % 12;
    const isBlack = [1,3,6,8,10].includes(pc);
    if (isBlack) {
      const prevWhite = pianoKeys.filter(k => !k.isBlack && k.midi < midi).pop();
      pianoKeys.push({ midi, pc, isBlack: true, left: prevWhite.left + 28, label: pcToNote(pc) + (Math.floor(midi/12)-1) });
    }
  }
}

function renderPiano() {
  pianoEl.innerHTML = "";
  pianoKeys.filter(k => !k.isBlack).forEach(k => pianoEl.appendChild(createPianoKey(k)));
  pianoKeys.filter(k => k.isBlack).forEach(k => pianoEl.appendChild(createPianoKey(k)));
}

function createPianoKey(key) {
  const el = document.createElement("div");
  el.className = key.isBlack ? "black-key" : "white-key";
  if (state.selectedPiano.has(key.midi)) el.classList.add("active");
  el.style.left = key.left + "px";
  el.textContent = key.label;
  el.title = `${key.label} (MIDI ${key.midi})`;
  el.addEventListener("click", () => {
    ensureAudio();
    if (state.selectedPiano.has(key.midi)) state.selectedPiano.delete(key.midi);
    else state.selectedPiano.add(key.midi);
    playPianoTone(midiToFreq(key.midi));
    updateChordLab();
  });
  return el;
}

function guitarNoteMidi(s, f) { return GUITAR_STRINGS[s].midi + f; }
function guitarNotePc(s, f) { return guitarNoteMidi(s, f) % 12; }

function guitarSelectedPcs() {
  const pcs = []; let bassPc = null;
  state.selectedGuitar.forEach((fret, s) => {
    if (fret === null) return;
    const pc = guitarNotePc(s, fret);
    pcs.push(pc);
    if (bassPc === null) bassPc = pc;
  });
  return { pcs: new Set(pcs), bassPc };
}

function renderFretboard() {
  fretboardEl.innerHTML = "";
  const header = document.createElement("div");
  header.className = "fret-row fret-header";
  header.innerHTML = `<div></div>${Array.from({length:MAX_FRET+1}, (_,i) => `<div style="text-align:center">${i}</div>`).join("")}`;
  fretboardEl.appendChild(header);

  GUITAR_STRINGS.forEach((sd, si) => {
    const row = document.createElement("div");
    row.className = "fret-row";
    const label = document.createElement("div");
    label.className = "string-label"; label.textContent = sd.label;
    row.appendChild(label);
    for (let f = 0; f <= MAX_FRET; f++) {
      const cell = document.createElement("div");
      cell.className = "string-cell" + (f === 0 ? " open-cell" : "");
      if (state.selectedGuitar[si] === f) cell.classList.add("active");
      const marker = document.createElement("div");
      marker.className = "marker"; marker.textContent = f === 0 ? "O" : "";
      cell.appendChild(marker);
      cell.title = `${sd.label} fret ${f} → ${pcToNote(guitarNotePc(si, f))}`;
      cell.addEventListener("click", () => {
        ensureAudio();
        state.selectedGuitar[si] = state.selectedGuitar[si] === f ? null : f;
        playGuitarTone(midiToFreq(guitarNoteMidi(si, f)));
        updateChordLab();
      });
      row.appendChild(cell);
    }
    fretboardEl.appendChild(row);
  });
}

function inferChords(selectedPcs, bassPc = null) {
  const pcs = [...selectedPcs];
  if (!pcs.length) return [];
  const exact = [], partial = [];
  for (let r = 0; r < 12; r++) {
    const intervals = new Set(pcs.map(p => (p - r + 12) % 12));
    for (const [q, formula] of Object.entries(CHORD_FORMULAS)) {
      const target = new Set(formula);
      if (setEquals(intervals, target)) exact.push({rootPc:r, quality:q, partial:false});
      else if (isSubset(intervals, target) && intervals.has(0) && intervals.size >= 2)
        partial.push({rootPc:r, quality:q, partial:true, missing:target.size - intervals.size});
    }
  }
  const fmt = m => {
    let n = chordName(m.rootPc, m.quality);
    if (bassPc !== null && bassPc !== m.rootPc && selectedPcs.has(bassPc)) n += `/${pcToNote(bassPc)}`;
    if (m.partial) n += " (partial)";
    return n;
  };
  if (exact.length) return [...new Set(exact.map(fmt))].sort((a,b) => a.length - b.length || a.localeCompare(b));
  const seen = new Set(), out = [];
  partial.sort((a,b) => a.missing - b.missing || chordName(a.rootPc,a.quality).length - chordName(b.rootPc,b.quality).length)
    .forEach(m => { const l = fmt(m); if (!seen.has(l) && out.length < 8) { out.push(l); seen.add(l); }});
  return out;
}

function parseChordLabel(label) {
  const clean = label.replace(" (partial)", "");
  const slashIdx = clean.indexOf("/");
  const noSlash = slashIdx >= 0 ? clean.slice(0, slashIdx) : clean;
  const roots = [...NOTE_NAMES_SHARP].sort((a,b) => b.length - a.length);
  const root = roots.find(n => noSlash.startsWith(n));
  if (!root) return null;
  return { rootPc: noteToPc(root), quality: noSlash.slice(root.length) };
}

function formatDetected(container, matches, emptyText) {
  container.innerHTML = "";
  const title = document.createElement("div");
  title.className = "detected-title"; title.textContent = "Detected chord candidates";
  container.appendChild(title);
  if (!matches.length) {
    const e = document.createElement("div"); e.className = "detected-empty"; e.textContent = emptyText;
    container.appendChild(e); return;
  }
  const list = document.createElement("div"); list.className = "detected-list";
  matches.forEach(match => {
    const chip = document.createElement("button");
    chip.className = "detected-item"; chip.textContent = match;
    chip.addEventListener("click", () => {
      const parsed = parseChordLabel(match);
      if (!parsed || !(parsed.quality in CHORD_FORMULAS)) return;
      rootSelect.value = pcToNote(parsed.rootPc); qualitySelect.value = parsed.quality;
      updateBrowserSummary();
      loadChordIntoPiano(parsed.rootPc, parsed.quality);
      loadChordIntoGuitar(parsed.rootPc, parsed.quality);
    });
    list.appendChild(chip);
  });
  container.appendChild(list);
}

function updateBrowserSummary() {
  const rootPc = noteToPc(rootSelect.value), quality = qualitySelect.value;
  browserName.textContent = `${pcToNote(rootPc)} ${displayQuality(quality)}`;
  browserNotes.textContent = chordNotes(rootPc, quality).join(", ");
  chordTooltip.textContent = CHORD_EXPLANATIONS[quality] || "";
}

function updatePianoStatus() {
  const selected = [...state.selectedPiano].sort((a,b) => a-b);
  const names = selected.map(m => `${pcToNote(m%12)}${Math.floor(m/12)-1}`);
  pianoStatus.innerHTML = `Selected notes: <strong>${names.length ? names.join(", ") : "none"}</strong>`;
  const pcs = new Set(selected.map(m => m%12));
  formatDetected(pianoDetected, inferChords(pcs), "Click piano keys to detect chords.");
}

function updateGuitarStatus() {
  const selected = [];
  state.selectedGuitar.forEach((fret, si) => {
    if (fret === null) return;
    selected.push(`${GUITAR_STRINGS[si].label} fret ${fret} → ${pcToNote(guitarNotePc(si, fret))}`);
  });
  const {pcs, bassPc} = guitarSelectedPcs();
  const bassText = bassPc === null ? "" : ` · bass: <strong>${pcToNote(bassPc)}</strong>`;
  guitarStatus.innerHTML = `Selected: <strong>${selected.length ? selected.join(" · ") : "none"}</strong>${bassText}`;
  formatDetected(guitarDetected, inferChords(pcs, bassPc), "Click frets to build a voicing.");
}

function updateChordLab() {
  renderPiano(); renderFretboard(); updateBrowserSummary(); updatePianoStatus(); updateGuitarStatus();
}

function loadChordIntoPiano(rootPc, quality) {
  const base = 60 + rootPc;
  state.selectedPiano = new Set(CHORD_FORMULAS[quality].map(i => base + i));
  updateChordLab();
}

function scoreShape(shape, chordPcs, rootPc) {
  const sounding = shape.map((f,i) => ({s:i, f})).filter(n => n.f !== null);
  if (sounding.length < 4) return -10000;
  const fretted = sounding.map(n => n.f).filter(f => f > 0);
  const span = fretted.length ? Math.max(...fretted) - Math.min(...fretted) : 0;
  if (span > 4) return -10000;
  const avg = fretted.length ? fretted.reduce((a,b) => a+b, 0) / fretted.length : 0;
  const pcs = sounding.map(n => guitarNotePc(n.s, n.f));
  const pcsSet = new Set(pcs);
  return (isSubset(chordPcs, pcsSet) ? 15 : 0) + pcsSet.size * 2
    + (pcs.length && pcs[0] === rootPc ? 8 : 0)
    + sounding.filter(n => n.f === 0).length - span * 2 - avg
    - shape.filter(f => f === null).length;
}

function productArrays(arrays) {
  return arrays.reduce((acc, cur) => {
    const out = []; acc.forEach(p => cur.forEach(i => out.push(p.concat([i])))); return out;
  }, [[]]);
}

function findGuitarVoicing(rootPc, quality) {
  const cPcs = chordPitchClasses(rootPc, quality);
  let best = null, bestScore = -10000;
  for (let start = 0; start <= 8; start++) {
    const perString = [];
    for (let si = 0; si < 6; si++) {
      const opts = [null];
      for (let f = 0; f <= MAX_FRET; f++) {
        if (!cPcs.has(guitarNotePc(si, f))) continue;
        if (f === 0 || (f >= start && f <= start + 4)) opts.push(f);
      }
      const limited = [...new Set(opts)].sort((a,b) => (a===null?-1:b===null?1:a-b)).slice(0, 5);
      perString.push(limited.length ? limited : [null]);
    }
    for (const shape of productArrays(perString)) {
      const pcs = []; let bass = null;
      shape.forEach((f, si) => { if (f === null) return; pcs.push(guitarNotePc(si, f)); if (bass === null) bass = guitarNotePc(si, f); });
      const pcsSet = new Set(pcs);
      if (!pcs.length || !pcsSet.has(rootPc) || pcsSet.size < Math.min(3, cPcs.size)) continue;
      if (!isSubset(pcsSet, cPcs)) continue;
      const score = scoreShape(shape, cPcs, rootPc);
      if (score > bestScore) { bestScore = score; best = [...shape]; }
    }
  }
  if (best) return best;
  return GUITAR_STRINGS.map((_, si) => { for (let f = 0; f <= MAX_FRET; f++) if (cPcs.has(guitarNotePc(si, f))) return f; return null; });
}

function loadChordIntoGuitar(rootPc, quality) {
  state.selectedGuitar = findGuitarVoicing(rootPc, quality);
  updateChordLab();
}

function playBrowserChord() {
  const rootPc = noteToPc(rootSelect.value), quality = qualitySelect.value;
  playPianoChord(CHORD_FORMULAS[quality].map(i => 60 + rootPc + i));
}

function populateBrowser() {
  NOTE_NAMES_SHARP.forEach(n => { const o = document.createElement("option"); o.value = n; o.textContent = n; rootSelect.appendChild(o); });
  Object.keys(CHORD_FORMULAS).forEach(q => { const o = document.createElement("option"); o.value = q; o.textContent = displayQuality(q); qualitySelect.appendChild(o); });
  rootSelect.value = "C"; qualitySelect.value = "";
  const grid = document.getElementById("supportedChords");
  Object.keys(CHORD_FORMULAS).forEach(q => { const d = document.createElement("div"); d.textContent = displayQuality(q); grid.appendChild(d); });
}

/* Chord Lab event listeners */
document.getElementById("loadPianoBtn").addEventListener("click", () => { ensureAudio(); loadChordIntoPiano(noteToPc(rootSelect.value), qualitySelect.value); playBrowserChord(); });
document.getElementById("loadGuitarBtn").addEventListener("click", () => { ensureAudio(); const r = noteToPc(rootSelect.value), q = qualitySelect.value; loadChordIntoGuitar(r, q); playGuitarShape(state.selectedGuitar); });
document.getElementById("loadBothBtn").addEventListener("click", () => { ensureAudio(); const r = noteToPc(rootSelect.value), q = qualitySelect.value; loadChordIntoPiano(r, q); loadChordIntoGuitar(r, q); playBrowserChord(); });
document.getElementById("playBrowserBtn").addEventListener("click", () => { ensureAudio(); playBrowserChord(); });
document.getElementById("clearAllBtn").addEventListener("click", () => { state.selectedPiano = new Set(); state.selectedGuitar = Array(6).fill(null); updateChordLab(); });
document.getElementById("playPianoBtn").addEventListener("click", () => { ensureAudio(); playPianoChord([...state.selectedPiano]); });
document.getElementById("clearPianoBtn").addEventListener("click", () => { state.selectedPiano = new Set(); updateChordLab(); });
document.getElementById("strumGuitarBtn").addEventListener("click", () => { ensureAudio(); playGuitarShape(state.selectedGuitar); });
document.getElementById("clearGuitarBtn").addEventListener("click", () => { state.selectedGuitar = Array(6).fill(null); updateChordLab(); });
rootSelect.addEventListener("change", updateBrowserSummary);
qualitySelect.addEventListener("change", updateBrowserSummary);

/* ═══════════════════════════════════════════════════════
   TAB 2: SCALE EXPLORER
   ═══════════════════════════════════════════════════════ */
const scaleRootSelect = document.getElementById("scaleRootSelect");
const scaleCategorySelect = document.getElementById("scaleCategorySelect");
const scaleTypeSelect = document.getElementById("scaleTypeSelect");
const scaleInfoGrid = document.getElementById("scaleInfoGrid");
const scalePianoEl = document.getElementById("scalePiano");
const scaleFretboardEl = document.getElementById("scaleFretboard");
const diatonicContainer = document.getElementById("diatonicChordsContainer");

function populateScaleControls() {
  NOTE_NAMES_SHARP.forEach(n => { const o = document.createElement("option"); o.value = n; o.textContent = n; scaleRootSelect.appendChild(o); });
  Object.keys(SCALE_DATA).forEach(cat => { const o = document.createElement("option"); o.value = cat; o.textContent = cat; scaleCategorySelect.appendChild(o); });
  updateScaleTypeOptions();
}

function updateScaleTypeOptions() {
  scaleTypeSelect.innerHTML = "";
  const cat = scaleCategorySelect.value;
  if (!SCALE_DATA[cat]) return;
  Object.keys(SCALE_DATA[cat]).forEach(name => {
    const o = document.createElement("option"); o.value = name; o.textContent = name; scaleTypeSelect.appendChild(o);
  });
  updateScaleDisplay();
}

function getScaleData() {
  const cat = scaleCategorySelect.value;
  const name = scaleTypeSelect.value;
  if (!SCALE_DATA[cat] || !SCALE_DATA[cat][name]) return null;
  return SCALE_DATA[cat][name];
}

function updateScaleDisplay() {
  const data = getScaleData();
  if (!data) return;
  const rootPc = noteToPc(scaleRootSelect.value);
  const notes = data.intervals.map(i => pcToNote((rootPc + i) % 12));
  const pcs = new Set(data.intervals.map(i => (rootPc + i) % 12));

  /* Info boxes */
  const degreeNames = ["1","b2","2","b3","3","4","b5/TT","5","b6","6","b7","7"];
  const degrees = data.intervals.map(i => degreeNames[i] || i);
  const intervalNames = data.intervals.map(i => {
    const iv = INTERVAL_NAMES.find(x => x.semitones === i);
    return iv ? iv.short : i;
  });

  scaleInfoGrid.innerHTML = `
    <div class="info-box"><div class="label">Scale</div><div class="value">${pcToNote(rootPc)} ${scaleTypeSelect.value}</div></div>
    <div class="info-box"><div class="label">Notes</div><div class="value">${notes.join(" – ")}</div></div>
    <div class="info-box"><div class="label">Formula</div><div class="value">${data.formula}</div></div>
    <div class="info-box"><div class="label">Degrees</div><div class="value">${degrees.join(" – ")}</div></div>
    <div class="info-box"><div class="label">Intervals</div><div class="value">${intervalNames.join(" – ")}</div></div>
    <div class="info-box" style="grid-column:1/-1"><div class="label">Description</div><div class="value" style="font-weight:400;font-size:0.88rem;">${data.description}</div></div>
  `;

  /* History / Theory panel */
  const historyPanel = document.getElementById("scaleHistoryPanel");
  if (data.history) {
    let tagsHtml = "";
    if (data.tags) tagsHtml = data.tags.map(t => `<span class="tag">${t}</span>`).join("");
    historyPanel.innerHTML = `<div class="scale-history">
      <h3>Theory &amp; History: ${pcToNote(rootPc)} ${scaleTypeSelect.value}</h3>
      ${tagsHtml ? '<div style="margin-bottom:10px;">' + tagsHtml + '</div>' : ''}
      <p>${data.history}</p>
    </div>`;
  } else {
    historyPanel.innerHTML = "";
  }

  /* Staff notation */
  renderStaffNotation(rootPc, data.intervals);

  /* Render scale piano */
  renderScalePiano(rootPc, pcs);
  renderScaleFretboard(rootPc, pcs);
  renderDiatonicChords(rootPc, data);
}

function renderScalePiano(rootPc, pcs) {
  scalePianoEl.innerHTML = "";
  const whites = pianoKeys.filter(k => !k.isBlack);
  const blacks = pianoKeys.filter(k => k.isBlack);
  [...whites, ...blacks].forEach(key => {
    const el = document.createElement("div");
    el.className = key.isBlack ? "black-key" : "white-key";
    if (pcs.has(key.pc)) {
      el.classList.add(key.pc === rootPc ? "scale-root" : "scale-highlight");
    }
    el.style.left = key.left + "px";
    el.textContent = key.label;
    el.addEventListener("click", () => { ensureAudio(); playPianoTone(midiToFreq(key.midi)); });
    scalePianoEl.appendChild(el);
  });
}

function renderScaleFretboard(rootPc, pcs) {
  scaleFretboardEl.innerHTML = "";
  const header = document.createElement("div");
  header.className = "fret-row fret-header";
  header.innerHTML = `<div></div>${Array.from({length:MAX_FRET+1}, (_,i) => `<div style="text-align:center">${i}</div>`).join("")}`;
  scaleFretboardEl.appendChild(header);

  GUITAR_STRINGS.forEach((sd, si) => {
    const row = document.createElement("div");
    row.className = "fret-row";
    const label = document.createElement("div");
    label.className = "string-label"; label.textContent = sd.label;
    row.appendChild(label);
    for (let f = 0; f <= MAX_FRET; f++) {
      const cell = document.createElement("div");
      cell.className = "string-cell" + (f === 0 ? " open-cell" : "");
      const pc = guitarNotePc(si, f);
      if (pcs.has(pc)) cell.classList.add(pc === rootPc ? "scale-root-dot" : "scale-dot");
      const marker = document.createElement("div");
      marker.className = "marker";
      if (pcs.has(pc)) marker.textContent = pcToNote(pc);
      cell.appendChild(marker);
      cell.title = `${sd.label} fret ${f} → ${pcToNote(pc)}`;
      cell.addEventListener("click", () => { ensureAudio(); playGuitarTone(midiToFreq(guitarNoteMidi(si, f))); });
      row.appendChild(cell);
    }
    scaleFretboardEl.appendChild(row);
  });
}

function renderDiatonicChords(rootPc, scaleData) {
  diatonicContainer.innerHTML = "";
  if (scaleData.intervals.length < 7) {
    diatonicContainer.innerHTML = '<div style="color:var(--muted);font-size:0.85rem;">Diatonic chord analysis works best with 7-note scales. This scale has ' + scaleData.intervals.length + ' notes.</div>';
    return;
  }
  const intervals = scaleData.intervals;

  /* Build triads and 7ths on each degree */
  const romanMaj = ["I","II","III","IV","V","VI","VII"];
  const container = document.createElement("div"); container.className = "diatonic-chords";

  for (let deg = 0; deg < 7; deg++) {
    const root = (rootPc + intervals[deg]) % 12;
    const third = (rootPc + intervals[(deg + 2) % 7]) % 12;
    const fifth = (rootPc + intervals[(deg + 4) % 7]) % 12;
    const seventh = intervals.length >= 7 ? (rootPc + intervals[(deg + 6) % 7]) % 12 : null;

    const i3 = ((third - root + 12) % 12);
    const i5 = ((fifth - root + 12) % 12);

    let triadQ = "";
    if (i3 === 4 && i5 === 7) triadQ = "";
    else if (i3 === 3 && i5 === 7) triadQ = "m";
    else if (i3 === 3 && i5 === 6) triadQ = "dim";
    else if (i3 === 4 && i5 === 8) triadQ = "aug";
    else triadQ = "?";

    let seventhQ = "";
    if (seventh !== null) {
      const i7 = ((seventh - root + 12) % 12);
      if (triadQ === "" && i7 === 11) seventhQ = "maj7";
      else if (triadQ === "" && i7 === 10) seventhQ = "7";
      else if (triadQ === "m" && i7 === 10) seventhQ = "m7";
      else if (triadQ === "m" && i7 === 11) seventhQ = "m(maj7)";
      else if (triadQ === "dim" && i7 === 10) seventhQ = "m7b5";
      else if (triadQ === "dim" && i7 === 9) seventhQ = "dim7";
      else if (triadQ === "aug" && i7 === 11) seventhQ = "aug(maj7)";
      else if (triadQ === "aug" && i7 === 10) seventhQ = "7#5";
      else seventhQ = triadQ + "7?";
    }

    let roman = romanMaj[deg];
    if (triadQ === "m" || triadQ === "dim") roman = roman.toLowerCase();
    if (triadQ === "dim") roman += "°";
    if (triadQ === "aug") roman += "+";

    const item = document.createElement("div");
    item.className = "diatonic-chord";
    item.innerHTML = `<div class="degree">${roman}</div><div class="chord-name">${pcToNote(root)}${triadQ}</div><div class="degree">${seventhQ ? pcToNote(root) + seventhQ : ""}</div>`;
    item.addEventListener("click", () => {
      ensureAudio();
      const q = triadQ === "?" ? "" : triadQ;
      if (q in CHORD_FORMULAS) {
        const midi = CHORD_FORMULAS[q].map(i => 60 + root + i);
        playPianoChord(midi);
      }
    });
    container.appendChild(item);
  }
  diatonicContainer.appendChild(container);
}

function playScaleAscending() {
  ensureAudio();
  const data = getScaleData(); if (!data) return;
  const rootPc = noteToPc(scaleRootSelect.value);
  data.intervals.forEach((interval, i) => {
    playPianoTone(midiToFreq(60 + rootPc + interval), i * 0.3);
  });
  playPianoTone(midiToFreq(60 + rootPc + 12), data.intervals.length * 0.3);
}

function playScaleDescending() {
  ensureAudio();
  const data = getScaleData(); if (!data) return;
  const rootPc = noteToPc(scaleRootSelect.value);
  const desc = [12, ...data.intervals.slice().reverse()];
  desc.forEach((interval, i) => {
    playPianoTone(midiToFreq(60 + rootPc + interval), i * 0.3);
  });
}

scaleCategorySelect.addEventListener("change", updateScaleTypeOptions);
scaleTypeSelect.addEventListener("change", updateScaleDisplay);
scaleRootSelect.addEventListener("change", updateScaleDisplay);
document.getElementById("playScaleUpBtn").addEventListener("click", playScaleAscending);
document.getElementById("playScaleDownBtn").addEventListener("click", playScaleDescending);
document.getElementById("clearScaleBtn").addEventListener("click", () => { updateScaleDisplay(); });

/* Guide toggle */
document.getElementById("guideToggle").addEventListener("click", () => {
  const panel = document.getElementById("guidePanel");
  const btn = document.getElementById("guideToggle");
  panel.classList.toggle("open");
  btn.textContent = panel.classList.contains("open") ? "Hide guide" : "How to read this page";
});

/* ── Staff Notation Renderer ── */
function renderStaffNotation(rootPc, intervals) {
  const container = document.getElementById("staffContainer");
  /*
    Staff: 5 lines, treble clef. We map pitch classes to staff positions.
    Staff position 0 = middle C (ledger line below staff).
    Each position = one diatonic step on the staff.

    We'll render notes from root (octave 4) to root+octave (octave 5).
  */
  const W = Math.max(500, (intervals.length + 2) * 55);
  const H = 160;
  const staffTop = 35;
  const lineGap = 12;
  const lines = [0,1,2,3,4]; /* staff lines from top */

  /* Map pc to staff position (semitones above C4 → line/space position) */
  /* Natural note positions on staff (from C4 upward): C=0, D=1, E=2, F=3, G=4, A=5, B=6, C5=7 */
  const pcToStaffPos = {
    0:0, 1:0, 2:1, 3:1, 4:2, 5:3, 6:3, 7:4, 8:4, 9:5, 10:5, 11:6
  };
  /* Which pcs need a sharp symbol */
  const pcNeedsSharp = new Set([1,3,6,8,10]);
  /* Which pcs need a flat (we'll use sharps for simplicity since we display sharp names) */

  /* Staff position to Y coordinate:
     Staff line 1 (top, F5) = staffTop
     Staff line 5 (bottom, E4) = staffTop + 4*lineGap
     Middle C (C4) = staffTop + 5.5*lineGap (below staff)
     Each staff position (diatonic step) = lineGap/2

     Bottom line (E4) = staff pos 2 (E is 2 steps above C)
     Top line (F5) = staff pos 10 (F5 = 3 + 7)

     y = staffTop + 4*lineGap - (staffPos - 2) * (lineGap/2)
  */
  function posToY(staffPos) {
    return staffTop + 4 * lineGap - (staffPos - 2) * (lineGap / 2);
  }

  let svg = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">`;

  /* Draw staff lines */
  for (let i = 0; i < 5; i++) {
    const y = staffTop + i * lineGap;
    svg += `<line x1="60" y1="${y}" x2="${W-20}" y2="${y}" stroke="rgba(148,163,184,0.4)" stroke-width="1"/>`;
  }

  /* Draw treble clef (simplified text glyph) */
  const clefY = staffTop + 2.5 * lineGap;
  svg += `<text x="68" y="${clefY}" font-size="48" fill="var(--muted)" font-family="serif" text-anchor="middle" dominant-baseline="central">&#119070;</text>`;

  /* Draw notes */
  const startX = 130;
  const noteSpacing = 50;

  /* We place the scale starting from root in octave 4 */
  const allNotes = [...intervals, 12]; /* include octave */

  allNotes.forEach((semitones, i) => {
    const absPc = (rootPc + semitones) % 12;
    const octaveOffset = Math.floor((rootPc + semitones) / 12) - Math.floor(rootPc / 12);
    const baseStaffPos = pcToStaffPos[absPc];
    const staffPos = baseStaffPos + octaveOffset * 7;
    const x = startX + i * noteSpacing;
    const y = posToY(staffPos);
    const isRoot = (semitones === 0 || semitones === 12);

    /* Ledger lines if needed */
    /* Middle C (pos 0) needs a ledger line */
    if (staffPos <= 0) {
      for (let lp = 0; lp >= staffPos; lp -= 2) {
        const ly = posToY(lp);
        svg += `<line x1="${x-14}" y1="${ly}" x2="${x+14}" y2="${ly}" stroke="rgba(148,163,184,0.4)" stroke-width="1"/>`;
      }
    }
    /* Above staff */
    if (staffPos >= 12) {
      for (let lp = 12; lp <= staffPos; lp += 2) {
        const ly = posToY(lp);
        svg += `<line x1="${x-14}" y1="${ly}" x2="${x+14}" y2="${ly}" stroke="rgba(148,163,184,0.4)" stroke-width="1"/>`;
      }
    }

    /* Note head */
    const fillColor = isRoot ? "#f59e0b" : "#a78bfa";
    svg += `<ellipse cx="${x}" cy="${y}" rx="8" ry="6" fill="${fillColor}" transform="rotate(-15,${x},${y})"/>`;

    /* Stem */
    const stemUp = staffPos < 6;
    if (stemUp) {
      svg += `<line x1="${x+7}" y1="${y}" x2="${x+7}" y2="${y-35}" stroke="${fillColor}" stroke-width="1.5"/>`;
    } else {
      svg += `<line x1="${x-7}" y1="${y}" x2="${x-7}" y2="${y+35}" stroke="${fillColor}" stroke-width="1.5"/>`;
    }

    /* Sharp symbol if needed */
    if (pcNeedsSharp.has(absPc)) {
      svg += `<text x="${x-14}" y="${y+4}" font-size="14" fill="var(--accent)" font-weight="700">#</text>`;
    }

    /* Note name below */
    svg += `<text x="${x}" y="${H-8}" text-anchor="middle" font-size="11" fill="${isRoot ? '#f59e0b' : 'var(--muted)'}" font-weight="${isRoot ? 700 : 400}">${pcToNote(absPc)}</text>`;

    /* Degree label above */
    if (i < intervals.length) {
      const degreeNames = ["1","b2","2","b3","3","4","b5","5","b6","6","b7","7"];
      const deg = degreeNames[semitones] || semitones;
      svg += `<text x="${x}" y="14" text-anchor="middle" font-size="10" fill="var(--muted)">${deg}</text>`;
    }
  });

  svg += `</svg>`;
  container.innerHTML = svg;
}

/* ═══════════════════════════════════════════════════════
   TAB 3: CHORD THEORY
   ═══════════════════════════════════════════════════════ */
function initTheory() {
  const nav = document.getElementById("theoryNav");
  const content = document.getElementById("theoryContent");

  THEORY_SECTIONS.forEach((section, i) => {
    const btn = document.createElement("button");
    btn.className = "theory-nav-btn" + (i === 0 ? " active" : "");
    btn.textContent = section.title;
    btn.addEventListener("click", () => {
      nav.querySelectorAll(".theory-nav-btn").forEach(b => b.classList.remove("active"));
      content.querySelectorAll(".theory-section").forEach(s => s.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById("theory-" + section.id).classList.add("active");
    });
    nav.appendChild(btn);

    const div = document.createElement("div");
    div.className = "theory-section card" + (i === 0 ? " active" : "");
    div.id = "theory-" + section.id;
    div.innerHTML = `<h3>${section.title}</h3>${section.content}`;
    content.appendChild(div);
  });

  /* Wire up play buttons */
  content.addEventListener("click", e => {
    const btn = e.target.closest(".play-interval-btn");
    if (!btn) return;
    ensureAudio();
    if (btn.dataset.st !== undefined) {
      const st = parseInt(btn.dataset.st);
      playPianoTone(midiToFreq(60), 0);
      if (st > 0) playPianoTone(midiToFreq(60 + st), 0.4);
    }
    if (btn.dataset.chord) {
      const intervals = btn.dataset.chord.split(",").map(Number);
      const midi = intervals.map(i => 60 + i);
      playPianoChord(midi);
    }
  });
}

/* ═══════════════════════════════════════════════════════
   TAB 4: CHORD PROGRESSIONS
   ═══════════════════════════════════════════════════════ */
const progGenreSelect = document.getElementById("progGenreSelect");
const progKeySelect = document.getElementById("progKeySelect");
const progModeSelect = document.getElementById("progModeSelect");
const progList = document.getElementById("progList");
const tempoSlider = document.getElementById("tempoSlider");
const tempoDisplay = document.getElementById("tempoDisplay");

let progPlaying = false, progTimeout = null;

function populateProgControls() {
  Object.keys(PROGRESSIONS).forEach(g => { const o = document.createElement("option"); o.value = g; o.textContent = g; progGenreSelect.appendChild(o); });
  NOTE_NAMES_SHARP.forEach(n => { const o = document.createElement("option"); o.value = n; o.textContent = n; progKeySelect.appendChild(o); });
}

function getProgTempo() { return parseInt(tempoSlider.value); }
tempoSlider.addEventListener("input", () => { tempoDisplay.textContent = tempoSlider.value + " BPM"; });

function resolveProgression(prog, keyRoot, mode) {
  const scale = mode === "minor" ? MINOR_SCALE : MAJOR_SCALE;
  const chords = [];

  if (prog.degrees_abs) {
    prog.degrees_abs.forEach((semitones, i) => {
      const notePc = (keyRoot + semitones) % 12;
      const q = prog.qualities[i] || "";
      chords.push({ notePc, quality: q, name: pcToNote(notePc) + q });
    });
  } else {
    prog.degrees.forEach((deg, i) => {
      const notePc = (keyRoot + scale[deg % 7]) % 12;
      const q = prog.qualities[i] || "";
      chords.push({ notePc, quality: q, name: pcToNote(notePc) + q });
    });
  }
  return chords;
}

function updateProgressions() {
  const genre = progGenreSelect.value;
  const keyRoot = noteToPc(progKeySelect.value);
  const mode = progModeSelect.value;
  const progs = PROGRESSIONS[genre] || [];

  progList.innerHTML = "";
  progs.forEach((prog, progIdx) => {
    const chords = resolveProgression(prog, keyRoot, mode);
    const item = document.createElement("div");
    item.className = "prog-item";

    const chordChips = chords.map((c, ci) =>
      `<span class="prog-chord-chip" data-prog="${progIdx}" data-chord="${ci}" data-pc="${c.notePc}" data-quality="${c.quality}">${c.name}</span>`
    ).join("");

    item.innerHTML = `
      <div class="prog-header">
        <span class="prog-name">${prog.name}</span>
        <button class="btn small primary play-prog-btn" data-prog="${progIdx}">Play</button>
      </div>
      <div class="prog-roman">${prog.roman}</div>
      <div class="prog-chords">${chordChips}</div>
      <div class="prog-desc">${prog.description}</div>
    `;
    progList.appendChild(item);
  });
}

progList.addEventListener("click", e => {
  const playBtn = e.target.closest(".play-prog-btn");
  if (playBtn) {
    ensureAudio();
    const genre = progGenreSelect.value;
    const keyRoot = noteToPc(progKeySelect.value);
    const mode = progModeSelect.value;
    const progIdx = parseInt(playBtn.dataset.prog);
    const prog = PROGRESSIONS[genre][progIdx];
    const chords = resolveProgression(prog, keyRoot, mode);
    playProgression(chords, progIdx);
    return;
  }
  const chip = e.target.closest(".prog-chord-chip");
  if (chip) {
    ensureAudio();
    const pc = parseInt(chip.dataset.pc);
    const q = chip.dataset.quality;
    if (q in CHORD_FORMULAS) {
      playPianoChord(CHORD_FORMULAS[q].map(i => 60 + pc + i));
    }
  }
});

function playProgression(chords, progIdx) {
  if (progPlaying) { stopProgression(); return; }
  progPlaying = true;
  const bpm = getProgTempo();
  const beatMs = (60 / bpm) * 1000 * 2;

  function playStep(i) {
    if (!progPlaying || i >= chords.length) { stopProgression(); return; }
    const c = chords[i];
    /* Highlight current chord */
    document.querySelectorAll(`[data-prog="${progIdx}"]`).forEach(el => {
      if (el.classList.contains("prog-chord-chip")) {
        el.classList.toggle("playing", parseInt(el.dataset.chord) === i);
      }
    });
    if (c.quality in CHORD_FORMULAS) {
      playPianoChord(CHORD_FORMULAS[c.quality].map(iv => 60 + c.notePc + iv));
    }
    progTimeout = setTimeout(() => playStep(i + 1), beatMs);
  }
  playStep(0);
}

function stopProgression() {
  progPlaying = false;
  if (progTimeout) clearTimeout(progTimeout);
  document.querySelectorAll(".prog-chord-chip.playing").forEach(el => el.classList.remove("playing"));
}

progGenreSelect.addEventListener("change", updateProgressions);
progKeySelect.addEventListener("change", updateProgressions);
progModeSelect.addEventListener("change", updateProgressions);

/* ═══════════════════════════════════════════════════════
   TAB 5: CIRCLE OF FIFTHS
   ═══════════════════════════════════════════════════════ */
const circleKeys = [
  {major:"C", minor:"Am", sharps:0, flats:0, sig:""},
  {major:"G", minor:"Em", sharps:1, flats:0, sig:"1#"},
  {major:"D", minor:"Bm", sharps:2, flats:0, sig:"2#"},
  {major:"A", minor:"F#m", sharps:3, flats:0, sig:"3#"},
  {major:"E", minor:"C#m", sharps:4, flats:0, sig:"4#"},
  {major:"B", minor:"G#m", sharps:5, flats:0, sig:"5#"},
  {major:"F#/Gb", minor:"D#m/Ebm", sharps:6, flats:6, sig:"6#/6b"},
  {major:"Db", minor:"Bbm", sharps:0, flats:5, sig:"5b"},
  {major:"Ab", minor:"Fm", sharps:0, flats:4, sig:"4b"},
  {major:"Eb", minor:"Cm", sharps:0, flats:3, sig:"3b"},
  {major:"Bb", minor:"Gm", sharps:0, flats:2, sig:"2b"},
  {major:"F", minor:"Dm", sharps:0, flats:1, sig:"1b"}
];

let selectedCircleKey = 0;

function buildCircleOfFifths() {
  const wrap = document.getElementById("circleSvgWrap");
  const size = 400, cx = size/2, cy = size/2, rOuter = 170, rInner = 115, rText = 145, rMinorText = 95;

  let svg = `<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}" style="cursor:pointer">`;
  svg += `<circle cx="${cx}" cy="${cy}" r="${rOuter}" fill="rgba(15,23,42,0.8)" stroke="rgba(148,163,184,0.2)" stroke-width="1"/>`;
  svg += `<circle cx="${cx}" cy="${cy}" r="${rInner}" fill="rgba(30,41,59,0.8)" stroke="rgba(148,163,184,0.15)" stroke-width="1"/>`;

  circleKeys.forEach((key, i) => {
    const angle = (i * 30 - 90) * Math.PI / 180;
    const nextAngle = ((i + 1) * 30 - 90) * Math.PI / 180;

    /* Major key text */
    const tx = cx + rText * Math.cos(angle);
    const ty = cy + rText * Math.sin(angle);
    const isSelected = i === selectedCircleKey;
    svg += `<text x="${tx}" y="${ty}" text-anchor="middle" dominant-baseline="central"
      font-size="${isSelected ? 16 : 13}" font-weight="${isSelected ? 800 : 600}"
      fill="${isSelected ? '#38bdf8' : '#e5e7eb'}" data-idx="${i}" class="circle-key">${key.major}</text>`;

    /* Minor key text */
    const mx = cx + rMinorText * Math.cos(angle);
    const my = cy + rMinorText * Math.sin(angle);
    svg += `<text x="${mx}" y="${my}" text-anchor="middle" dominant-baseline="central"
      font-size="${isSelected ? 12 : 10}" font-weight="${isSelected ? 700 : 400}"
      fill="${isSelected ? '#f59e0b' : '#94a3b8'}" data-idx="${i}" class="circle-key">${key.minor}</text>`;

    /* Divider lines */
    const midAngle = ((i - 0.5) * 30 - 90) * Math.PI / 180;
    const lx1 = cx + rInner * Math.cos(midAngle);
    const ly1 = cy + rInner * Math.sin(midAngle);
    const lx2 = cx + rOuter * Math.cos(midAngle);
    const ly2 = cy + rOuter * Math.sin(midAngle);
    svg += `<line x1="${lx1}" y1="${ly1}" x2="${lx2}" y2="${ly2}" stroke="rgba(148,163,184,0.1)" stroke-width="1"/>`;
  });

  /* Selection highlight arc */
  const startAngle = ((selectedCircleKey - 0.5) * 30 - 90) * Math.PI / 180;
  const endAngle = ((selectedCircleKey + 0.5) * 30 - 90) * Math.PI / 180;
  const x1 = cx + rOuter * Math.cos(startAngle), y1 = cy + rOuter * Math.sin(startAngle);
  const x2 = cx + rOuter * Math.cos(endAngle), y2 = cy + rOuter * Math.sin(endAngle);
  svg += `<path d="M ${cx} ${cy} L ${x1} ${y1} A ${rOuter} ${rOuter} 0 0 1 ${x2} ${y2} Z"
    fill="rgba(56,189,248,0.1)" stroke="rgba(56,189,248,0.3)" stroke-width="1"/>`;

  svg += `</svg>`;
  wrap.innerHTML = svg;

  wrap.addEventListener("click", e => {
    const t = e.target.closest(".circle-key");
    if (t) {
      selectedCircleKey = parseInt(t.dataset.idx);
      buildCircleOfFifths();
      updateCircleInfo();
    }
  });

  updateCircleInfo();
}

function updateCircleInfo() {
  const info = document.getElementById("circleInfo");
  const key = circleKeys[selectedCircleKey];
  const majorRoot = key.major.includes("/") ? key.major.split("/")[0] : key.major;
  const rootPc = noteToPc(normalizeNote(majorRoot));

  /* Diatonic chords in this key */
  const majorChordQualities = ["", "m", "m", "", "", "m", "dim"];
  const majorChord7Qualities = ["maj7", "m7", "m7", "maj7", "7", "m7", "m7b5"];
  const romanNumerals = ["I", "ii", "iii", "IV", "V", "vi", "vii°"];

  let chordsHtml = '<div class="key-chords-grid">';
  MAJOR_SCALE.forEach((interval, i) => {
    const notePc = (rootPc + interval) % 12;
    const q = majorChordQualities[i];
    const q7 = majorChord7Qualities[i];
    chordsHtml += `<div class="key-chord-item" data-pc="${notePc}" data-quality="${q}">
      <div class="deg">${romanNumerals[i]}</div>
      <div class="name">${pcToNote(notePc)}${q}</div>
      <div class="deg">${pcToNote(notePc)}${q7}</div>
    </div>`;
  });
  chordsHtml += '</div>';

  /* Neighbor keys */
  const prevIdx = (selectedCircleKey - 1 + 12) % 12;
  const nextIdx = (selectedCircleKey + 1) % 12;

  info.innerHTML = `
    <div class="info-box"><div class="label">Key</div><div class="value">${key.major} major / ${key.minor}</div></div>
    <div class="info-box"><div class="label">Key Signature</div><div class="value">${key.sig || 'No sharps or flats'} ${key.sharps ? '(' + key.sharps + ' sharp' + (key.sharps>1?'s':'') + ')' : ''} ${key.flats ? '(' + key.flats + ' flat' + (key.flats>1?'s':'') + ')' : ''}</div></div>
    <div class="info-box"><div class="label">Relative Minor</div><div class="value">${key.minor}</div></div>
    <div class="info-box"><div class="label">Closely Related Keys</div><div class="value">← ${circleKeys[prevIdx].major} (IV) | ${circleKeys[nextIdx].major} (V) →</div></div>
    <div class="info-box" style="grid-column:1/-1">
      <div class="label">Diatonic Chords in ${key.major} Major</div>
      ${chordsHtml}
    </div>
    <div class="info-box" style="grid-column:1/-1">
      <div class="label">Common Modulations</div>
      <div class="value" style="font-weight:400;font-size:0.88rem;">
        <strong>Dominant (V):</strong> → ${circleKeys[nextIdx].major} (one step clockwise — the most natural modulation)<br>
        <strong>Subdominant (IV):</strong> → ${circleKeys[prevIdx].major} (one step counter-clockwise)<br>
        <strong>Relative minor:</strong> → ${key.minor} (same key signature, different tonal center)<br>
        <strong>Parallel minor:</strong> → ${key.major.replace(/\/.*/, "")}m (same root, different mode)
      </div>
    </div>
  `;

  /* Wire up chord clicks */
  info.querySelectorAll(".key-chord-item").forEach(item => {
    item.addEventListener("click", () => {
      ensureAudio();
      const pc = parseInt(item.dataset.pc);
      const q = item.dataset.quality;
      if (q in CHORD_FORMULAS) {
        playPianoChord(CHORD_FORMULAS[q].map(i => 60 + pc + i));
      }
    });
  });
}

/* ═══════════════════════════════════════════════════════
   INITIALIZATION
   ═══════════════════════════════════════════════════════ */
buildPianoKeyData();
populateBrowser();
updateChordLab();
populateScaleControls();
initTheory();
populateProgControls();
updateProgressions();
buildCircleOfFifths();
</script>
</body>
</html>
"""

st.title("Music Theory Pro")
st.caption("Interactive chord lab, scales, theory, progressions & circle of fifths — all with live synthesized sound.")
components.html(HTML_APP, height=2800, scrolling=True)

with st.expander("Run locally"):
    st.code("pip install streamlit\nstreamlit run app.py", language="bash")
