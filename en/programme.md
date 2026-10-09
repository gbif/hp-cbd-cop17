---
lang-ref: page
layout: page
height: 0vh
permalink: /programme/
---

<style>
  /* Collapse theme banner and layout headers completely */
  .hero-banner, .site-header--hero, .page-header, .page-banner {
    padding: 0 !important;
    margin: 0 !important;
    min-height: 0 !important;
    height: 0 !important;
    display: none !important;
  }

  /* Set container max-width without zeroing out global padding */
  .container,
  .wrapper,
  .site-content,
  main {
    max-width: 60rem !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }

  /* Pull inner page content up */
  .page-content {
    padding-top: 0 !important;
    margin-top: 0 !important;
  }

  /* Pull the calendar up to eliminate remaining gap */
  #calendar {
    margin-top: -1.5rem !important;
  }

  /* Restore spacing above the footer */
  .site-footer, footer {
    margin-top: 3rem !important;
  }

  /* Hide language selector on this page */
  .language-selector,
  .site-header__languages,
  .navbar-languages,
  .lang-switcher {
    display: none !important;
  }

  /* Interactive Filter Pills container & label */
  #calendar-legend-container {
    margin-top: 2.5rem;
    margin-bottom: 2rem;
  }

  .filter-label {
    font-size: 0.9rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  #calendar-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: flex-start;
  }

  .legend-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.3rem 0.6rem;
    border-radius: 50px;
    border: 1.5px solid;
    background: #fff;
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.1s, background 0.2s;
    user-select: none;
  }

  .legend-pill:hover {
    transform: translateY(-1px);
  }

  .legend-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    display: inline-block;
  }

  /* Mobile responsiveness: hide view switcher chunk entirely and stack controls */
  @media (max-width: 768px) {
    .fc .fc-toolbar-chunk:last-child {
      display: none !important;
    }
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
      align-items: flex-start;
      padding: 0 0.5rem;
    }
    .legend-pill {
      justify-content: flex-start;
      width: auto;
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

<div id="calendar"></div>

<!-- Interactive Outline Filter Pills -->
<div id="calendar-legend-container">
  <div class="filter-label">Filter schedule by theme:</div>
  <div id="calendar-legend">
    <div class="legend-pill" data-theme="Building Capacity for Biodiversity Action" style="border-color: #669941; color: #669941;">
      <span class="legend-dot" style="background: #669941;"></span> Building Capacity for Biodiversity Action
    </div>
    <div class="legend-pill" data-theme="From Data to Decisions" style="border-color: #307b98; color: #307b98;">
      <span class="legend-dot" style="background: #307b98;"></span> From Data to Decisions
    </div>
    <div class="legend-pill" data-theme="Monitoring, Technology & Innovation" style="border-color: #f6aa3c; color: #b87410;">
      <span class="legend-dot" style="background: #f6aa3c;"></span> Monitoring, Technology & Innovation
    </div>
    <div class="legend-pill" data-theme="Data Gaps & Governance" style="border-color: #d46833; color: #d46833;">
      <span class="legend-dot" style="background: #d46833;"></span> Data Gaps & Governance
    </div>
  </div>
</div>

<h2 style="margin-top: 3rem; margin-bottom: 1rem;">Thematic Focus</h2>

<p>The pavilion’s programme centers around four core pillars supporting the Kunming-Montreal Global Biodiversity Framework:</p>

<ul style="list-style-type: none; padding-left: 0; margin-top: 1rem;">
  <li style="margin-bottom: 1rem;"><span style="color: #669941; font-size: 1.2rem; margin-right: 0.5rem; line-height: 1;">&bull;</span><strong style="color: #669941;">Building Capacity for Biodiversity Action:</strong> Strengthening regional and institutional readiness to manage and apply biodiversity data.</li>
  <li style="margin-bottom: 1rem;"><span style="color: #307b98; font-size: 1.2rem; margin-right: 0.5rem; line-height: 1;">&bull;</span><strong style="color: #307b98;">From Data to Decisions:</strong> Translating monitoring data into actionable policy, reporting, and management outcomes.</li>
  <li style="margin-bottom: 1rem;"><span style="color: #d46833; font-size: 1.2rem; margin-right: 0.5rem; line-height: 1;">&bull;</span><strong style="color: #d46833;">Monitoring, Technology & Innovation:</strong> Showcasing new tools, earth observations, and digital architectures for biodiversity tracking.</li>
  <li style="margin-bottom: 1rem;"><span style="color: #f6aa3c; font-size: 1.2rem; margin-right: 0.5rem; line-height: 1;">&bull;</span><strong style="color: #f6aa3c;">Data Gaps & Governance:</strong> Addressing data equity, standardisation, and legal or institutional frameworks required for robust monitoring.</li>
</ul>

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

  const allEvents = rawEvents
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
        extendedProps: { row, colors, theme }
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
    events: allEvents,
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

  // Filter functionality for calendar legend pills
  const activeThemes = new Set(Object.keys(themeColors));
  const filterPills = document.querySelectorAll('#calendar-legend .legend-pill');

  filterPills.forEach(pill => {
    pill.addEventListener('click', function() {
      const theme = this.getAttribute('data-theme');

      if (activeThemes.has(theme)) {
        activeThemes.delete(theme);
        this.style.opacity = '0.35';
        this.style.background = '#f3f4f6';
      } else {
        activeThemes.add(theme);
        this.style.opacity = '1';
        this.style.background = '#fff';
      }

      // If all are deselected, reset and select all again
      if (activeThemes.size === 0) {
        filterPills.forEach(p => {
          const t = p.getAttribute('data-theme');
          activeThemes.add(t);
          p.style.opacity = '1';
          p.style.background = '#fff';
        });
      }

      // Filter and update calendar events
      const filteredEvents = allEvents.filter(event => activeThemes.has(event.extendedProps.theme));
      calendar.setOption('events', filteredEvents);
    });
  });
});
</script>
