---
lang-ref: page
layout: page
title: Test Calendar
description: Testing calendar options
background: assets/images/cabra.jpg
imageLicence: "[_Polyommatus icarus_ (von Rottemburg, 1775)](https://www.gbif.org/occurrence/5828883558) observed in Armenia by Axel Gosseries [(licensed under CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)"
height: 70vh
permalink: /calendar0/
---

<link href='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.css' rel='stylesheet' />
<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.11/index.global.min.js'></script>

<div id="calendar" style="margin-top: 2rem;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
  const rawEvents = {{ site.data.events | jsonify }};

  const events = rawEvents.map(row => ({
    title: row['Event Title'] || row['Title'],
    start: row['Start Date'] || row['Date'],
    end: row['End Date'],
    extendedProps: { row }
  })).filter(e => e.start);

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,listWeek'
    },
    events: events,
    eventClick: function(info) {
      const row = info.event.extendedProps.row;
      let details = `<h3>${info.event.title}</h3>`;
      for (const [key, val] of Object.entries(row)) {
        if (val) details += `<p><strong>${key}:</strong> ${val}</p>`;
      }

      // Output to modal or panel
      console.log(details);
    }
  });
  calendar.render();
});
</script>
