---
lang-ref: page
layout: page
height: 0vh
permalink: /calendar0/
---

<style>
  /* Collapse zero-height banner */
  .hero-banner, .site-header--hero, .page-header {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    margin-bottom: 1rem !important;
  }

  /* Forcefully expand and center theme containers to 60rem */
  .container,
  .wrapper,
  .page-content,
  .site-content,
  main {
    max-width: 60rem !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }

  /* Outline Pill Legend styling */
  #calendar-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    justify-content: center;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
  }

  .legend-pill {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.4rem 1rem;
    border-radius: 50px;
    border: 2px solid;
    background: #fff;
    font-size: 0.85rem;
    font-weight: 500;
  }

  .legend-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    display: inline-block;
  }

  /* Mobile responsiveness for FullCalendar controls */
  @media (max-width: 768px) {
    .fc .fc-toolbar {
      flex-direction: column;
      align-items: stretch;
      gap: 0.75rem;
    }
    .fc .fc-toolbar-chunk {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0.3rem;
    }
    .fc .fc-button {
      padding: 0.4rem 0.6rem !important;
      font-size: 0.85rem !important;
      line-height: 1.2 !important;
    }
    .fc .fc-toolbar-title {
      font-size: 1.15rem !important;
      text-align: center;
    }
    #calendar-legend {
      flex-direction: column;
      align-items: stretch;
      padding: 0 1rem;
    }
    .legend-pill {
      justify-content: center;
    }
  }

  /* Modal styling overlay */
  #modal-backdrop {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(2px);
    z-index: 999;
  }

  /* Modern event modal box */
  #event-modal {
    display: none;
    position: fixed;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    background: #fff;
    padding: 2.5rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    z-index: 1000;
    max-width: 600px;
    width: 90%;
    border-radius: 12px;
    color: #333;
    font-family: inherit;
  }

  .modal-meta-item {
    margin-bottom: 1rem;
    font-size: 0.95rem;
    line-height: 1.5;
  }

  .modal-meta-item strong {
    color: #444;
    display: inline-block;
    width: 140px;
  }

  .modal-close-btn {
    margin-top: 1.5rem;
    padding: 0.6rem 1.5rem;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    transition: background 0.2s;
  }

  .modal-close-btn:hover {
    background: #111;
  }
</style>

<link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.css' rel='stylesheet' />
<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.js'></script>

<div id="calendar" style="margin-top: 1rem;"></div>

<!-- Outline Pill Legend -->
<div id="calendar-legend">
  <div class="legend-pill" style="border-color: #669941; color: #669941;">
    <span class="legend-dot" style="background: #669941;"></span> Building Capacity for Biodiversity Action
  </div>
  <div class="legend-pill" style="border-color: #307b98; color: #307b98;">
    <span class="legend-dot" style="background: #307b98;"></span> From Data to Decisions
  </div>
  <div class="legend-pill" style="border-color: #f6aa3c; color: #b87410;">
    <span class="legend-dot" style="background: #f6aa3c;"></span> Monitoring, Technology & Innovation
  </div>
  <div class="legend-pill" style="border-color: #d46833; color: #d46833;">
    <span class="legend-dot" style="background: #d46833;"></span> Data Gaps & Governance
  </div>
</div>

<!-- Modal Backdrop and Container -->
<div id="modal-backdrop" onclick="closeModal()"></div>
<div id="event-modal">
  <h2 id="modal-title" style="margin-top:0; margin-bottom: 1.5rem; font-size: 1.4rem; color: #111;"></h2>
  <div id="modal-body" style="max-height:50vh; overflow-y:auto; border-top: 1px solid #eee; border-bottom: 1px solid #eee; padding: 1rem 0;"></div>
  <button class="modal-close-btn" onclick="closeModal()">Close</button>
</div>

<script>
function closeModal() {
  document.getElementById('event-modal').style.display = 'none';
  document.getElementById('modal-backdrop').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  const rawEvents = {{ site.data.events | jsonify }};

  const themeColors = {
    "Building Capacity for Biodiversity Action": { background: "#669941", text: "#ffffff" },
    "From Data to Decisions": { background: "#307b98", text: "#ffffff" },
    "Monitoring, Technology & Innovation": { background: "#f6aa3c", text: "#111111" },
    "Data Gaps & Governance": { background: "#d46833", text: "#ffffff" }
  };
  const defaultColor = { background: "#6d6e71", text: "#ffffff" };

  function parseDateTime(dateStr, timeStr) {
    if (!dateStr || !timeStr) return null;

    const dayMatch = dateStr.match(/\b(\d{1,2})\b/);
    if (!dayMatch) return null;
    const day = dayMatch[1].padStart(2, '0');

    let [hours, minutes] = timeStr.trim().split(':');
    if (!hours) return null;
    hours = hours.padStart(2, '0');
    minutes = (minutes || '00').padStart(2, '0');

    return `2026-10-${day}T${hours}:${minutes}:00`;
  }

  const events = rawEvents
    .filter(row => row['Event title'] && row['Date'] && row['Start'] && row['Start'].trim() !== '')
    .map(row => {
      const theme = row['Primary theme'] || '';
      const colors = themeColors[theme] || defaultColor;

      return {
        title: row['Event title'],
        start: parseDateTime(row['Date'], row['Start']),
        end: parseDateTime(row['Date'], row['End']),
        backgroundColor: colors.background,
        borderColor: colors.background,
        textColor: colors.text,
        extendedProps: { row, colors }
      };
    })
    .filter(e => e.start !== null);

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'listWeek',
    initialDate: '2026-10-18',
    validRange: {
      start: '2026-10-18',
      end: '2026-11-01'
    },
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,listWeek'
    },
    events: events,
    eventClick: function(info) {
      const row = info.event.extendedProps.row;
      const colors = info.event.extendedProps.colors;
      document.getElementById('modal-title').innerText = info.event.title;

      let html = '';
      if (row['Lead organization']) {
        html += `<div class="modal-meta-item"><strong>Lead Organization:</strong> ${row['Lead organization']}</div>`;
      }
      if (row['Date'] && row['Start']) {
        html += `<div class="modal-meta-item"><strong>Date & Time:</strong> ${row['Date']} | ${row['Start']} - ${row['End']}</div>`;
      }
      if (row['Primary theme']) {
        html += `<div class="modal-meta-item"><strong>Primary Theme:</strong><br><span style="display: inline-flex; align-items: center; gap: 0.5rem; background: #fff; border: 2px solid ${colors.background}; color: ${colors.background === '#f6aa3c' ? '#b87410' : colors.background}; padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.85rem; font-weight: 500; margin-top: 0.25rem;"><span style="width: 8px; height: 8px; border-radius: 50%; background: ${colors.background}; display: inline-block;"></span>${row['Primary theme']}</span></div>`;
      }
      if (row['Paired thematic focus']) {
        html += `<div class="modal-meta-item" style="margin-top: 1rem;"><strong>Thematic Focus:</strong> ${row['Paired thematic focus']}</div>`;
      }

      document.getElementById('modal-body').innerHTML = html;
      document.getElementById('event-modal').style.display = 'block';
      document.getElementById('modal-backdrop').style.display = 'block';
    }
  });

  calendar.render();
});
</script>
