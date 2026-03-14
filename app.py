import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Chord Lab Pro", layout="wide")

HTML_APP = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Chord Lab Pro</title>
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

  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
    color: var(--text);
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }
  .app {
    max-width: 1400px;
    margin: 0 auto;
    padding: 20px;
  }
  .hero {
    padding: 20px 22px;
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 24px;
    background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.16), transparent 30%), rgba(15, 23, 42, 0.95);
    box-shadow: 0 20px 40px rgba(2, 6, 23, 0.35);
    margin-bottom: 18px;
  }
  .hero h1 {
    margin: 0 0 8px;
    font-size: 2.2rem;
    line-height: 1.1;
  }
  .hero p {
    margin: 0;
    color: var(--muted);
    font-size: 1rem;
  }
  .card {
    background: rgba(15, 23, 42, 0.86);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 24px;
    padding: 18px;
    box-shadow: 0 16px 32px rgba(2, 6, 23, 0.24);
  }
  .toolbar {
    display: grid;
    grid-template-columns: 1.6fr 1fr 1fr auto auto auto auto;
    gap: 12px;
    align-items: end;
    margin-bottom: 18px;
  }
  .field {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
  .field label {
    font-size: 0.85rem;
    color: var(--muted);
  }
  select, button {
    font: inherit;
  }
  select {
    width: 100%;
    padding: 12px 14px;
    border-radius: 14px;
    border: 1px solid var(--line);
    background: rgba(15, 23, 42, 0.9);
    color: var(--text);
  }
  .btn {
    border: 0;
    border-radius: 14px;
    padding: 12px 16px;
    cursor: pointer;
    transition: transform 0.12s ease, opacity 0.12s ease, background 0.12s ease;
    color: white;
    font-weight: 600;
    white-space: nowrap;
  }
  .btn:hover { transform: translateY(-1px); }
  .btn:active { transform: translateY(0); }
  .btn.primary { background: linear-gradient(135deg, #0ea5e9, #2563eb); }
  .btn.secondary { background: linear-gradient(135deg, #f59e0b, #ea580c); }
  .btn.ghost { background: rgba(148, 163, 184, 0.14); border: 1px solid rgba(148, 163, 184, 0.2); }
  .btn.success { background: linear-gradient(135deg, #22c55e, #16a34a); }
  .btn.danger { background: linear-gradient(135deg, #ef4444, #dc2626); }

  .browser-summary {
    grid-column: 1 / -1;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    color: var(--muted);
    font-size: 0.95rem;
  }
  .browser-summary strong { color: var(--text); }
  .chip {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 12px;
    border-radius: 999px;
    background: rgba(56, 189, 248, 0.14);
    color: #bae6fd;
    border: 1px solid rgba(56, 189, 248, 0.22);
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 18px;
  }
  .section-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 12px;
  }
  .section-head h2 {
    margin: 0;
    font-size: 1.2rem;
  }
  .mini-actions {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .mini-btn {
    border: 1px solid rgba(148, 163, 184, 0.18);
    background: rgba(148, 163, 184, 0.08);
    color: var(--text);
    padding: 8px 12px;
    border-radius: 12px;
    cursor: pointer;
  }
  .mini-btn:hover { background: rgba(148, 163, 184, 0.14); }
  .status {
    color: var(--muted);
    margin-bottom: 12px;
    line-height: 1.5;
  }
  .detected {
    margin-top: 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .detected-title {
    font-size: 0.9rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
  .detected-list {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .detected-item {
    padding: 10px 14px;
    border-radius: 999px;
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.2);
    color: #bbf7d0;
    cursor: pointer;
  }
  .detected-item:hover { background: rgba(34, 197, 94, 0.18); }
  .detected-empty {
    color: var(--muted);
    padding: 12px;
    border-radius: 14px;
    border: 1px dashed rgba(148, 163, 184, 0.18);
  }

  .piano-shell {
    overflow-x: auto;
    padding-bottom: 10px;
  }
  .piano {
    position: relative;
    width: 840px;
    height: 250px;
    margin: 0 auto;
    user-select: none;
  }
  .white-key {
    position: absolute;
    top: 0;
    width: 60px;
    height: 240px;
    border: 1px solid #cbd5e1;
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 68%, #dbe4ef 100%);
    color: #0f172a;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 16px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: inset 0 -8px 10px rgba(15, 23, 42, 0.08);
  }
  .white-key.active {
    background: linear-gradient(180deg, #fef3c7 0%, #fde68a 70%, #f59e0b 100%);
    color: #78350f;
  }
  .white-key:hover { filter: brightness(0.98); }
  .black-key {
    position: absolute;
    top: 0;
    width: 38px;
    height: 146px;
    border-radius: 0 0 10px 10px;
    background: linear-gradient(180deg, #111827 0%, #020617 72%, #334155 100%);
    color: #e2e8f0;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding-bottom: 12px;
    font-size: 0.72rem;
    cursor: pointer;
    z-index: 5;
    box-shadow: 0 8px 12px rgba(2, 6, 23, 0.4);
  }
  .black-key.active {
    background: linear-gradient(180deg, #0f172a 0%, #2563eb 68%, #38bdf8 100%);
    color: white;
  }

  .fretboard-wrap {
    overflow-x: auto;
    padding-bottom: 6px;
  }
  .fretboard {
    min-width: 900px;
    border-radius: 22px;
    padding: 18px 16px 16px;
    background:
      radial-gradient(circle at 26% 50%, rgba(255,255,255,0.12) 0 4px, transparent 5px),
      radial-gradient(circle at 42% 50%, rgba(255,255,255,0.12) 0 4px, transparent 5px),
      radial-gradient(circle at 58% 50%, rgba(255,255,255,0.12) 0 4px, transparent 5px),
      radial-gradient(circle at 74% 50%, rgba(255,255,255,0.12) 0 4px, transparent 5px),
      radial-gradient(circle at 90% 50%, rgba(255,255,255,0.18) 0 4px, transparent 5px),
      linear-gradient(180deg, var(--wood-2) 0%, var(--wood-1) 100%);
    border: 1px solid rgba(255,255,255,0.08);
  }
  .fret-row {
    display: grid;
    grid-template-columns: 70px repeat(13, 1fr);
    align-items: center;
    position: relative;
  }
  .fret-header {
    color: #fde68a;
    margin-bottom: 10px;
    font-size: 0.85rem;
  }
  .fret-row + .fret-row { margin-top: 6px; }
  .string-label {
    color: #f8fafc;
    font-weight: 700;
    padding-right: 10px;
    text-align: right;
  }
  .string-cell {
    position: relative;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  .string-cell::before {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    height: 2px;
    transform: translateY(-50%);
    background: linear-gradient(90deg, #f8fafc, #cbd5e1, #f8fafc);
    opacity: 0.78;
  }
  .string-cell:not(.open-cell)::after {
    content: "";
    position: absolute;
    right: -1px;
    top: 0;
    bottom: 0;
    width: 4px;
    border-radius: 99px;
    background: rgba(255,255,255,0.4);
  }
  .open-cell::before { left: 12px; }
  .marker {
    position: relative;
    z-index: 2;
    width: 18px;
    height: 18px;
    border-radius: 999px;
    border: 2px solid rgba(255,255,255,0.6);
    background: rgba(15, 23, 42, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 0.72rem;
    backdrop-filter: blur(4px);
  }
  .string-cell.active .marker {
    width: 28px;
    height: 28px;
    border-color: rgba(255,255,255,0.9);
    background: linear-gradient(135deg, #22c55e, #15803d);
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.24);
  }
  .string-cell:hover .marker {
    border-color: white;
  }

  .legend {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    color: var(--muted);
    margin-top: 12px;
    font-size: 0.9rem;
  }
  .legend span {
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .legend-dot {
    width: 12px;
    height: 12px;
    border-radius: 999px;
    background: linear-gradient(135deg, #22c55e, #15803d);
  }
  .legend-key {
    width: 16px;
    height: 16px;
    border-radius: 4px;
    background: linear-gradient(135deg, #fde68a, #f59e0b);
  }

  .support-card h3 {
    margin: 0 0 10px;
  }
  .support-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 10px;
  }
  .support-grid div {
    padding: 10px 12px;
    border-radius: 14px;
    background: rgba(148, 163, 184, 0.08);
    border: 1px solid rgba(148, 163, 184, 0.14);
    text-align: center;
    color: var(--text);
  }
  @media (max-width: 1100px) {
    .toolbar { grid-template-columns: 1fr 1fr; }
    .grid { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>
  <div class="app">
    <div class="hero">
      <h1>Chord Lab Pro</h1>
      <p>Interactive piano and guitar chord explorer. Click real-looking keys and frets, hear the notes instantly, detect complex chords, and load any chord back onto both instruments.</p>
    </div>

    <div class="card toolbar">
      <div class="field">
        <label for="rootSelect">Chord root</label>
        <select id="rootSelect"></select>
      </div>
      <div class="field">
        <label for="qualitySelect">Chord quality</label>
        <select id="qualitySelect"></select>
      </div>
      <button class="btn primary" id="loadPianoBtn">Show on piano</button>
      <button class="btn primary" id="loadGuitarBtn">Show on guitar</button>
      <button class="btn secondary" id="loadBothBtn">Show on both</button>
      <button class="btn success" id="playBrowserBtn">Play chord</button>
      <button class="btn ghost" id="clearAllBtn">Clear all</button>
      <div class="browser-summary">
        <span class="chip" id="browserName">C major</span>
        <span>Notes: <strong id="browserNotes">C, E, G</strong></span>
        <span>Tip: click a detected chord chip below either instrument to load it into the browser instantly.</span>
      </div>
    </div>

    <div class="grid">
      <section class="card">
        <div class="section-head">
          <h2>Piano</h2>
          <div class="mini-actions">
            <button class="mini-btn" id="playPianoBtn">Play selected notes</button>
            <button class="mini-btn" id="clearPianoBtn">Clear piano</button>
          </div>
        </div>
        <div class="status" id="pianoStatus">Selected notes: none</div>
        <div class="piano-shell">
          <div class="piano" id="piano"></div>
        </div>
        <div class="detected" id="pianoDetected"></div>
      </section>

      <section class="card">
        <div class="section-head">
          <h2>Guitar</h2>
          <div class="mini-actions">
            <button class="mini-btn" id="strumGuitarBtn">Strum selected shape</button>
            <button class="mini-btn" id="clearGuitarBtn">Clear guitar</button>
          </div>
        </div>
        <div class="status" id="guitarStatus">Selected notes: none</div>
        <div class="fretboard-wrap">
          <div class="fretboard" id="fretboard"></div>
        </div>
        <div class="legend">
          <span><span class="legend-dot"></span> active fret</span>
          <span><span class="legend-key"></span> active piano key</span>
          <span>lowest sounding guitar note is used as bass for slash-chord detection</span>
        </div>
        <div class="detected" id="guitarDetected"></div>
      </section>
    </div>

    <section class="card support-card">
      <h3>Supported chord qualities</h3>
      <div class="support-grid" id="supportedChords"></div>
    </section>
  </div>

<script>
  const NOTE_NAMES_SHARP = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
  const NOTE_ALIAS_TO_SHARP = {
    "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#",
    "Cb": "B", "Fb": "E", "E#": "F", "B#": "C"
  };
  const GUITAR_STRINGS = [
    {label: "E2", midi: 40},
    {label: "A2", midi: 45},
    {label: "D3", midi: 50},
    {label: "G3", midi: 55},
    {label: "B3", midi: 59},
    {label: "E4", midi: 64}
  ];
  const MAX_FRET = 12;
  const CHORD_FORMULAS = {
    "": [0, 4, 7],
    "m": [0, 3, 7],
    "5": [0, 7],
    "dim": [0, 3, 6],
    "aug": [0, 4, 8],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "6": [0, 4, 7, 9],
    "m6": [0, 3, 7, 9],
    "6/9": [0, 2, 4, 7, 9],
    "m6/9": [0, 2, 3, 7, 9],
    "7": [0, 4, 7, 10],
    "maj7": [0, 4, 7, 11],
    "m7": [0, 3, 7, 10],
    "m(maj7)": [0, 3, 7, 11],
    "dim7": [0, 3, 6, 9],
    "m7b5": [0, 3, 6, 10],
    "7b5": [0, 4, 6, 10],
    "7#5": [0, 4, 8, 10],
    "7sus4": [0, 5, 7, 10],
    "add9": [0, 2, 4, 7],
    "madd9": [0, 2, 3, 7],
    "add11": [0, 4, 5, 7],
    "madd11": [0, 3, 5, 7],
    "add13": [0, 4, 7, 9],
    "madd13": [0, 3, 7, 9],
    "9": [0, 2, 4, 7, 10],
    "maj9": [0, 2, 4, 7, 11],
    "m9": [0, 2, 3, 7, 10],
    "7b9": [0, 1, 4, 7, 10],
    "7#9": [0, 3, 4, 7, 10],
    "9sus4": [0, 2, 5, 7, 10],
    "11": [0, 2, 4, 5, 7, 10],
    "maj11": [0, 2, 4, 5, 7, 11],
    "m11": [0, 2, 3, 5, 7, 10],
    "13": [0, 2, 4, 7, 9, 10],
    "maj13": [0, 2, 4, 7, 9, 11],
    "m13": [0, 2, 3, 7, 9, 10],
    "13sus4": [0, 2, 5, 7, 9, 10],
    "maj7#11": [0, 4, 6, 7, 11],
    "7b13": [0, 4, 7, 8, 10]
  };

  const state = {
    selectedPiano: new Set(),
    selectedGuitar: Array(6).fill(null)
  };

  const rootSelect = document.getElementById("rootSelect");
  const qualitySelect = document.getElementById("qualitySelect");
  const browserName = document.getElementById("browserName");
  const browserNotes = document.getElementById("browserNotes");
  const pianoEl = document.getElementById("piano");
  const fretboardEl = document.getElementById("fretboard");
  const pianoStatus = document.getElementById("pianoStatus");
  const guitarStatus = document.getElementById("guitarStatus");
  const pianoDetected = document.getElementById("pianoDetected");
  const guitarDetected = document.getElementById("guitarDetected");

  let audioCtx = null;

  function ensureAudioContext() {
    if (!audioCtx) {
      const AC = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AC();
    }
    if (audioCtx.state === "suspended") audioCtx.resume();
  }

  function normalizeNote(note) {
    return NOTE_ALIAS_TO_SHARP[note] || note;
  }

  function noteToPc(note) {
    return NOTE_NAMES_SHARP.indexOf(normalizeNote(note));
  }

  function pcToNote(pc) {
    return NOTE_NAMES_SHARP[((pc % 12) + 12) % 12];
  }

  function chordName(rootPc, quality) {
    return pcToNote(rootPc) + (quality || "");
  }

  function displayQuality(quality) {
    return quality === "" ? "major" : quality;
  }

  function chordPitchClasses(rootPc, quality) {
    return new Set(CHORD_FORMULAS[quality].map(interval => (rootPc + interval) % 12));
  }

  function chordNotes(rootPc, quality) {
    return CHORD_FORMULAS[quality].map(interval => pcToNote(rootPc + interval));
  }

  function midiToFreq(midi) {
    return 440 * Math.pow(2, (midi - 69) / 12);
  }

  function playPianoTone(freq, when = 0) {
    ensureAudioContext();
    const now = audioCtx.currentTime + when;
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(4200, now);
    filter.Q.setValueAtTime(0.5, now);

    const partials = [
      {type: "sine", multiple: 1, gain: 0.8, detune: 0},
      {type: "triangle", multiple: 2, gain: 0.28, detune: 2},
      {type: "sine", multiple: 3, gain: 0.12, detune: -3}
    ];

    gain.gain.setValueAtTime(0.0001, now);
    gain.gain.exponentialRampToValueAtTime(0.45, now + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 2.2);

    partials.forEach(partial => {
      const osc = audioCtx.createOscillator();
      const oscGain = audioCtx.createGain();
      osc.type = partial.type;
      osc.frequency.setValueAtTime(freq * partial.multiple, now);
      osc.detune.setValueAtTime(partial.detune, now);
      oscGain.gain.setValueAtTime(partial.gain, now);
      osc.connect(oscGain).connect(filter);
      osc.start(now);
      osc.stop(now + 2.25);
    });

    filter.connect(gain).connect(audioCtx.destination);
  }

  function createKarplusStrongBuffer(freq, duration = 2.3) {
    ensureAudioContext();
    const sampleRate = audioCtx.sampleRate;
    const length = Math.floor(sampleRate * duration);
    const period = Math.max(2, Math.floor(sampleRate / freq));
    const data = new Float32Array(length);

    for (let i = 0; i < period; i++) {
      data[i] = (Math.random() * 2 - 1) * 0.8;
    }
    for (let i = period; i < length; i++) {
      data[i] = 0.5 * (data[i - period] + data[i - period + 1]) * 0.996;
    }

    const buffer = audioCtx.createBuffer(1, length, sampleRate);
    buffer.copyToChannel(data, 0);
    return buffer;
  }

  function playGuitarTone(freq, when = 0) {
    ensureAudioContext();
    const start = audioCtx.currentTime + when;
    const source = audioCtx.createBufferSource();
    source.buffer = createKarplusStrongBuffer(freq);

    const filter = audioCtx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.setValueAtTime(Math.min(freq * 12, 4200), start);
    filter.Q.setValueAtTime(0.8, start);

    const gain = audioCtx.createGain();
    gain.gain.setValueAtTime(0.0001, start);
    gain.gain.exponentialRampToValueAtTime(0.65, start + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, start + 2.1);

    source.connect(filter).connect(gain).connect(audioCtx.destination);
    source.start(start);
  }

  function playPianoChord(midiNotes) {
    if (!midiNotes.length) return;
    const sorted = [...midiNotes].sort((a, b) => a - b);
    sorted.forEach((midi, i) => playPianoTone(midiToFreq(midi), i * 0.025));
  }

  function playGuitarShape(shape) {
    const sequence = [];
    shape.forEach((fret, stringIdx) => {
      if (fret === null) return;
      const midi = GUITAR_STRINGS[stringIdx].midi + fret;
      sequence.push({stringIdx, midi});
    });
    sequence.forEach((note, i) => playGuitarTone(midiToFreq(note.midi), i * 0.055));
  }

  const pianoKeys = [];
  function buildPianoKeyData() {
    let whiteIndex = 0;
    for (let midi = 48; midi <= 72; midi++) {
      const pc = midi % 12;
      const isBlack = [1, 3, 6, 8, 10].includes(pc);
      if (isBlack) {
        pianoKeys.push({
          midi,
          pc,
          label: pcToNote(pc),
          isBlack: true,
          left: (whiteIndex * 60) - 19
        });
      } else {
        pianoKeys.push({
          midi,
          pc,
          label: pcToNote(pc),
          isBlack: false,
          left: whiteIndex * 60
        });
        whiteIndex += 1;
      }
    }
  }

  function renderPiano() {
    pianoEl.innerHTML = "";
    const whites = pianoKeys.filter(key => !key.isBlack);
    const blacks = pianoKeys.filter(key => key.isBlack);

    whites.forEach(key => pianoEl.appendChild(createPianoKey(key)));
    blacks.forEach(key => pianoEl.appendChild(createPianoKey(key)));
  }

  function createPianoKey(key) {
    const el = document.createElement("div");
    el.className = key.isBlack ? "black-key" : "white-key";
    if (state.selectedPiano.has(key.midi)) el.classList.add("active");
    el.style.left = key.left + "px";
    el.textContent = key.label;
    el.title = `${key.label} (${key.midi})`;
    el.addEventListener("click", () => {
      ensureAudioContext();
      if (state.selectedPiano.has(key.midi)) {
        state.selectedPiano.delete(key.midi);
      } else {
        state.selectedPiano.add(key.midi);
      }
      playPianoTone(midiToFreq(key.midi));
      updateAll();
    });
    return el;
  }

  function guitarNoteMidi(stringIdx, fret) {
    return GUITAR_STRINGS[stringIdx].midi + fret;
  }

  function guitarNotePc(stringIdx, fret) {
    return guitarNoteMidi(stringIdx, fret) % 12;
  }

  function guitarSelectedPcs() {
    const pcs = [];
    let bassPc = null;
    state.selectedGuitar.forEach((fret, stringIdx) => {
      if (fret === null) return;
      const pc = guitarNotePc(stringIdx, fret);
      pcs.push(pc);
      if (bassPc === null) bassPc = pc;
    });
    return { pcs: new Set(pcs), bassPc };
  }

  function renderFretboard() {
    fretboardEl.innerHTML = "";
    const header = document.createElement("div");
    header.className = "fret-row fret-header";
    header.innerHTML = `<div></div>${Array.from({length: 13}, (_, i) => `<div style="text-align:center;">${i}</div>`).join("")}`;
    fretboardEl.appendChild(header);

    GUITAR_STRINGS.forEach((stringData, stringIdx) => {
      const row = document.createElement("div");
      row.className = "fret-row";

      const label = document.createElement("div");
      label.className = "string-label";
      label.textContent = stringData.label;
      row.appendChild(label);

      for (let fret = 0; fret <= MAX_FRET; fret++) {
        const cell = document.createElement("div");
        cell.className = "string-cell" + (fret === 0 ? " open-cell" : "");
        if (state.selectedGuitar[stringIdx] === fret) cell.classList.add("active");
        const marker = document.createElement("div");
        marker.className = "marker";
        marker.textContent = fret === 0 ? "O" : "";
        cell.appendChild(marker);

        const noteName = pcToNote(guitarNotePc(stringIdx, fret));
        cell.title = `${stringData.label} fret ${fret} → ${noteName}`;
        cell.addEventListener("click", () => {
          ensureAudioContext();
          state.selectedGuitar[stringIdx] = state.selectedGuitar[stringIdx] === fret ? null : fret;
          playGuitarTone(midiToFreq(guitarNoteMidi(stringIdx, fret)));
          updateAll();
        });
        row.appendChild(cell);
      }

      fretboardEl.appendChild(row);
    });
  }

  function inferChords(selectedPcs, bassPc = null) {
    const pcs = [...selectedPcs];
    if (!pcs.length) return [];

    const exactMatches = [];
    const partialMatches = [];

    for (let rootPc = 0; rootPc < 12; rootPc++) {
      const intervals = new Set(pcs.map(pc => (pc - rootPc + 12) % 12));
      for (const [quality, formula] of Object.entries(CHORD_FORMULAS)) {
        const target = new Set(formula);
        if (setEquals(intervals, target)) {
          exactMatches.push({ rootPc, quality, partial: false });
        } else if (isSubset(intervals, target) && intervals.has(0) && intervals.size >= 2) {
          partialMatches.push({
            rootPc,
            quality,
            partial: true,
            missing: target.size - intervals.size
          });
        }
      }
    }

    const formatMatch = (match) => {
      let name = chordName(match.rootPc, match.quality);
      if (bassPc !== null && bassPc !== match.rootPc && selectedPcs.has(bassPc)) {
        name += `/${pcToNote(bassPc)}`;
      }
      if (match.partial) name += " (partial match)";
      return name;
    };

    if (exactMatches.length) {
      return [...new Set(exactMatches.map(formatMatch))].sort((a, b) => a.length - b.length || a.localeCompare(b));
    }

    const seen = new Set();
    const output = [];
    partialMatches
      .sort((a, b) => a.missing - b.missing || chordName(a.rootPc, a.quality).length - chordName(b.rootPc, b.quality).length)
      .forEach(match => {
        const label = formatMatch(match);
        if (!seen.has(label) && output.length < 8) {
          output.push(label);
          seen.add(label);
        }
      });
    return output;
  }

  function setEquals(a, b) {
    if (a.size !== b.size) return false;
    for (const value of a) if (!b.has(value)) return false;
    return true;
  }

  function isSubset(a, b) {
    for (const value of a) if (!b.has(value)) return false;
    return true;
  }

  function parseChordLabel(label) {
    const clean = label.replace(" (partial match)", "");
    const slashIndex = clean.indexOf("/");
    const noSlash = slashIndex >= 0 ? clean.slice(0, slashIndex) : clean;
    const roots = [...NOTE_NAMES_SHARP].sort((a, b) => b.length - a.length);
    const root = roots.find(note => noSlash.startsWith(note));
    if (!root) return null;
    return { rootPc: noteToPc(root), quality: noSlash.slice(root.length) };
  }

  function formatDetected(container, matches, emptyText) {
    container.innerHTML = "";
    const title = document.createElement("div");
    title.className = "detected-title";
    title.textContent = "Detected chord candidates";
    container.appendChild(title);

    if (!matches.length) {
      const empty = document.createElement("div");
      empty.className = "detected-empty";
      empty.textContent = emptyText;
      container.appendChild(empty);
      return;
    }

    const list = document.createElement("div");
    list.className = "detected-list";
    matches.forEach(match => {
      const chip = document.createElement("button");
      chip.className = "detected-item";
      chip.textContent = match;
      chip.addEventListener("click", () => {
        const parsed = parseChordLabel(match);
        if (!parsed || !(parsed.quality in CHORD_FORMULAS)) return;
        rootSelect.value = pcToNote(parsed.rootPc);
        qualitySelect.value = parsed.quality;
        updateBrowserSummary();
        loadChordIntoPiano(parsed.rootPc, parsed.quality);
        loadChordIntoGuitar(parsed.rootPc, parsed.quality);
      });
      list.appendChild(chip);
    });
    container.appendChild(list);
  }

  function updateBrowserSummary() {
    const rootPc = noteToPc(rootSelect.value);
    const quality = qualitySelect.value;
    browserName.textContent = `${pcToNote(rootPc)} ${displayQuality(quality)}`;
    browserNotes.textContent = chordNotes(rootPc, quality).join(", ");
  }

  function updatePianoStatus() {
    const selected = [...state.selectedPiano].sort((a, b) => a - b);
    const names = selected.map(midi => `${pcToNote(midi % 12)}${Math.floor(midi / 12) - 1}`);
    pianoStatus.innerHTML = `Selected notes: <strong>${names.length ? names.join(", ") : "none"}</strong>`;
    const pcs = new Set(selected.map(midi => midi % 12));
    formatDetected(pianoDetected, inferChords(pcs), "Click some piano keys to start detecting chords.");
  }

  function updateGuitarStatus() {
    const selected = [];
    state.selectedGuitar.forEach((fret, stringIdx) => {
      if (fret === null) return;
      selected.push(`${GUITAR_STRINGS[stringIdx].label} fret ${fret} → ${pcToNote(guitarNotePc(stringIdx, fret))}`);
    });
    const { pcs, bassPc } = guitarSelectedPcs();
    const bassText = bassPc === null ? "" : ` · bass: <strong>${pcToNote(bassPc)}</strong>`;
    guitarStatus.innerHTML = `Selected notes: <strong>${selected.length ? selected.join(" · ") : "none"}</strong>${bassText}`;
    formatDetected(guitarDetected, inferChords(pcs, bassPc), "Click a fret position on each string to build a voicing.");
  }

  function updateAll() {
    renderPiano();
    renderFretboard();
    updateBrowserSummary();
    updatePianoStatus();
    updateGuitarStatus();
  }

  function loadChordIntoPiano(rootPc, quality) {
    const baseMidi = 60 + rootPc;
    state.selectedPiano = new Set(CHORD_FORMULAS[quality].map(interval => baseMidi + interval));
    updateAll();
  }

  function scoreShape(shape, chordPcs, rootPc) {
    const sounding = shape.map((fret, i) => ({ stringIdx: i, fret })).filter(note => note.fret !== null);
    if (sounding.length < 4) return -10000;

    const fretted = sounding.map(note => note.fret).filter(fret => fret > 0);
    const span = fretted.length ? Math.max(...fretted) - Math.min(...fretted) : 0;
    if (span > 4) return -10000;
    const avgFret = fretted.length ? fretted.reduce((a, b) => a + b, 0) / fretted.length : 0;
    const pcs = sounding.map(note => guitarNotePc(note.stringIdx, note.fret));
    const pcsSet = new Set(pcs);
    const coverageBonus = isSubset(chordPcs, pcsSet) ? 15 : 0;
    const uniqueBonus = pcsSet.size * 2;
    const rootBonus = pcs.length && pcs[0] === rootPc ? 8 : 0;
    const openBonus = sounding.filter(note => note.fret === 0).length;
    const mutePenalty = shape.filter(fret => fret === null).length;
    return coverageBonus + uniqueBonus + rootBonus + openBonus - span * 2 - avgFret - mutePenalty;
  }

  function productArrays(arrays) {
    return arrays.reduce((acc, current) => {
      const out = [];
      acc.forEach(prefix => current.forEach(item => out.push(prefix.concat([item]))));
      return out;
    }, [[]]);
  }

  function findGuitarVoicing(rootPc, quality) {
    const chordPcs = chordPitchClasses(rootPc, quality);
    let bestShape = null;
    let bestScore = -10000;

    for (let start = 0; start <= 8; start++) {
      const perStringOptions = [];
      for (let stringIdx = 0; stringIdx < 6; stringIdx++) {
        const options = [null];
        for (let fret = 0; fret <= MAX_FRET; fret++) {
          const pc = guitarNotePc(stringIdx, fret);
          if (!chordPcs.has(pc)) continue;
          if (fret === 0 || (fret >= start && fret <= start + 4)) {
            options.push(fret);
          }
        }
        const limited = [...new Set(options)].sort((a, b) => (a === null ? -1 : b === null ? 1 : a - b)).slice(0, 5);
        perStringOptions.push(limited.length ? limited : [null]);
      }

      const shapes = productArrays(perStringOptions);
      for (const shape of shapes) {
        const pcs = [];
        let bass = null;
        shape.forEach((fret, stringIdx) => {
          if (fret === null) return;
          const pc = guitarNotePc(stringIdx, fret);
          pcs.push(pc);
          if (bass === null) bass = pc;
        });
        const pcsSet = new Set(pcs);
        if (!pcs.length || !pcsSet.has(rootPc) || pcsSet.size < Math.min(3, chordPcs.size)) continue;
        if (!isSubset(pcsSet, chordPcs)) continue;
        if (bass === null) continue;
        const score = scoreShape(shape, chordPcs, rootPc);
        if (score > bestScore) {
          bestScore = score;
          bestShape = [...shape];
        }
      }
    }

    if (bestShape) return bestShape;

    return GUITAR_STRINGS.map((_, stringIdx) => {
      for (let fret = 0; fret <= MAX_FRET; fret++) {
        if (chordPcs.has(guitarNotePc(stringIdx, fret))) return fret;
      }
      return null;
    });
  }

  function loadChordIntoGuitar(rootPc, quality) {
    state.selectedGuitar = findGuitarVoicing(rootPc, quality);
    updateAll();
  }

  function playBrowserChord() {
    const rootPc = noteToPc(rootSelect.value);
    const quality = qualitySelect.value;
    const pianoVoicing = CHORD_FORMULAS[quality].map(interval => 60 + rootPc + interval);
    playPianoChord(pianoVoicing);
  }

  function populateBrowser() {
    NOTE_NAMES_SHARP.forEach(note => {
      const option = document.createElement("option");
      option.value = note;
      option.textContent = note;
      rootSelect.appendChild(option);
    });
    Object.keys(CHORD_FORMULAS).forEach(quality => {
      const option = document.createElement("option");
      option.value = quality;
      option.textContent = displayQuality(quality);
      qualitySelect.appendChild(option);
    });
    rootSelect.value = "C";
    qualitySelect.value = "";

    const supportGrid = document.getElementById("supportedChords");
    Object.keys(CHORD_FORMULAS).forEach(quality => {
      const item = document.createElement("div");
      item.textContent = displayQuality(quality);
      supportGrid.appendChild(item);
    });
  }

  document.getElementById("loadPianoBtn").addEventListener("click", () => {
    ensureAudioContext();
    loadChordIntoPiano(noteToPc(rootSelect.value), qualitySelect.value);
    playBrowserChord();
  });
  document.getElementById("loadGuitarBtn").addEventListener("click", () => {
    ensureAudioContext();
    const rootPc = noteToPc(rootSelect.value);
    const quality = qualitySelect.value;
    loadChordIntoGuitar(rootPc, quality);
    playGuitarShape(state.selectedGuitar);
  });
  document.getElementById("loadBothBtn").addEventListener("click", () => {
    ensureAudioContext();
    const rootPc = noteToPc(rootSelect.value);
    const quality = qualitySelect.value;
    loadChordIntoPiano(rootPc, quality);
    loadChordIntoGuitar(rootPc, quality);
    playBrowserChord();
  });
  document.getElementById("playBrowserBtn").addEventListener("click", () => {
    ensureAudioContext();
    playBrowserChord();
  });
  document.getElementById("clearAllBtn").addEventListener("click", () => {
    state.selectedPiano = new Set();
    state.selectedGuitar = Array(6).fill(null);
    updateAll();
  });
  document.getElementById("playPianoBtn").addEventListener("click", () => {
    ensureAudioContext();
    playPianoChord([...state.selectedPiano]);
  });
  document.getElementById("clearPianoBtn").addEventListener("click", () => {
    state.selectedPiano = new Set();
    updateAll();
  });
  document.getElementById("strumGuitarBtn").addEventListener("click", () => {
    ensureAudioContext();
    playGuitarShape(state.selectedGuitar);
  });
  document.getElementById("clearGuitarBtn").addEventListener("click", () => {
    state.selectedGuitar = Array(6).fill(null);
    updateAll();
  });
  rootSelect.addEventListener("change", updateBrowserSummary);
  qualitySelect.addEventListener("change", updateBrowserSummary);

  buildPianoKeyData();
  populateBrowser();
  updateAll();
</script>
</body>
</html>
"""

st.title("Chord Lab Pro")
st.caption("A more realistic piano and guitar interface with live synthesized sound, chord detection, and reverse chord lookup.")
components.html(HTML_APP, height=1700, scrolling=True)

with st.expander("Run locally"):
    st.code("python -m streamlit run app.py")
