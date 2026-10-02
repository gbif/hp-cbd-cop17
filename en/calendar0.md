---
lang-ref: page
layout: page
title: Test Calendar
description: Testing calendar options
background: assets/images/cabra.jpg
imageLicence: "[_Polyommatus icarus_ (von Rottemburg, 1775)](https://www.gbif.org/occurrence/5828883558) observed in Armenia by Axel Gosseries [(licensed under CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)"
height: 50vh
permalink: /calendar0/
---

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Target potential GBIF hosted portal hero title containers
  const selectors = ['.page-heading', '.hero-banner .container', '.site-heading', '.hero__content'];
  selectors.forEach(selector => {
    document.querySelectorAll(selector).forEach(el => {
      el.style.background = 'transparent';
      el.style.backgroundColor = 'transparent';
      el.style.boxShadow = 'none';
      el.style.border = 'none';
      el.style.backdropFilter = 'none';
    });
  });
});
</script>

<link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.css' rel='stylesheet' />
<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.js'></script>

<div id="calendar" style="margin-top: 2rem;"></div>

<!-- Modal container for event details -->
<div id="event-modal" style="display:none; position:fixed; top:20%; left:50%; transform:translate(-50%, -20%); background:#fff; padding:2rem; box-shadow:0 4px 12px rgba(0,0,0,0.15); z-index:1000; max-width:600px; width:100%; border-radius:8px; color:#333;">
  <h3 id="modal-title" style="margin-top:0;"></h3>
  <div id="modal-body" style="max-height:60vh; overflow-y:auto;"></div>
  <button onclick="document.getElementById('event-modal').style.display='none'" style="margin-top:1rem; padding:0.5rem 1rem; background:#0066cc; color:#fff; border:none; border-radius:4px; cursor:pointer;">Close</button>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  const rawEvents = {{ site.data.events | jsonify }};

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
    .map(row => ({
      title: row['Event title'],
      start: parseDateTime(row['Date'], row['Start']),
      end: parseDateTime(row['Date'], row['End']),
      extendedProps: { row }
    }))
    .filter(e => e.start !== null);

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'listWeek',      /* Changed from dayGridMonth to listWeek */
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
      document.getElementById('modal-title').innerText = info.event.title;

      let html = '';
      for (const [key, val] of Object.entries(row)) {
        if (val && key.trim() !== '') {
          html += `<p><strong>${key}:</strong> ${val}</p>`;
        }
      }

      document.getElementById('modal-body').innerHTML = html;
      document.getElementById('event-modal').style.display = 'block';
    }
  });

  calendar.render();
});
</script>
