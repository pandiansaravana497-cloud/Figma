/**
 * main.js — Sports Events Registration
 * Client-side logic: navigation, validation, event rendering.
 */

"use strict";

// ── Event Data (mirrors DB seed) ──────────────────────────────
const EVENTS = [
  { id: 1, icon: "🏃", name: "Marathon Championship", date: "December 15, 2025", venue: "City Sports Complex",  participants: 500, tag: "Running"    },
  { id: 2, icon: "🏀", name: "Basketball Tournament", date: "January 10, 2026",  venue: "Downtown Arena",      participants: 16,  tag: "Basketball" },
  { id: 3, icon: "🏊", name: "Swimming Competition",  date: "December 28, 2025", venue: "Olympic Pool Center",  participants: 200, tag: "Swimming"   },
  { id: 4, icon: "⚽", name: "Football League",        date: "February 5, 2026",  venue: "National Stadium",    participants: 300, tag: "Football"   },
  { id: 5, icon: "🎾", name: "Tennis Open",            date: "March 12, 2026",    venue: "Central Tennis Club", participants: 64,  tag: "Tennis"     },
];

// ── Session storage helpers ───────────────────────────────────
const session = {
  set: (key, val) => sessionStorage.setItem(key, val),
  get: (key)      => sessionStorage.getItem(key),
};

// ── Validation ────────────────────────────────────────────────
function validateRegistration(name, email) {
  const errors = {};
  if (!name.trim())               errors.name  = "Full name is required.";
  else if (name.trim().length < 2) errors.name  = "Name must be at least 2 characters.";

  const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email.trim())              errors.email = "Email address is required.";
  else if (!emailRe.test(email))  errors.email = "Please enter a valid email address.";

  return errors;
}

// ── Screen 1 → Screen 2 ──────────────────────────────────────
function goToEvents() {
  const nameEl  = document.getElementById("fullname");
  const emailEl = document.getElementById("email");
  if (!nameEl || !emailEl) return;

  const errors = validateRegistration(nameEl.value, emailEl.value);

  // Clear previous errors
  ["name", "email"].forEach(f => {
    const el = document.getElementById(`err-${f}`);
    if (el) el.textContent = "";
  });
  [nameEl, emailEl].forEach(el => el.classList.remove("error"));

  if (Object.keys(errors).length) {
    if (errors.name)  { document.getElementById("err-name").textContent  = errors.name;  nameEl.classList.add("error");  }
    if (errors.email) { document.getElementById("err-email").textContent = errors.email; emailEl.classList.add("error"); }
    return;
  }

  session.set("reg_name",  nameEl.value.trim());
  session.set("reg_email", emailEl.value.trim());
  window.location.href = "events.html";
}

// ── Render Events List ────────────────────────────────────────
function renderEvents() {
  const container = document.getElementById("eventsList");
  if (!container) return;

  container.innerHTML = EVENTS.map(e => `
    <div class="event-card" onclick="registerEvent(${e.id})">
      <div class="event-icon">${e.icon}</div>
      <div class="event-info">
        <h3>${e.name}</h3>
        <div class="event-meta">
          <span>📅 ${e.date}</span>
          <span>📍 ${e.venue}</span>
          <span>👥 ${e.participants} participants</span>
        </div>
        <span class="tag">${e.tag}</span>
      </div>
    </div>
  `).join("");
}

// ── Event selected → Screen 3 ─────────────────────────────────
function registerEvent(eventId) {
  const ev = EVENTS.find(e => e.id === eventId);
  if (ev) session.set("selected_event", JSON.stringify(ev));
  window.location.href = "success.html";
}

// ── Auto-init ─────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("eventsList")) renderEvents();
});
