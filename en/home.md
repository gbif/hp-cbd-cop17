---
lang-ref: home
layout: home
title: Data to Action Pavilion
description: _Connecting science and knowledge systems for biodiversity_
background: assets/images/https---www.gbif.org-occurrence-6353065929-bg.jpg
imageLicense: "[_Lacerta strigata_ Eichwald, 1831](https://www.gbif.org/occurrence/6353065929) observed in Armenia by Leonid A. Neymark licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode)"
height: 60vh
cta:
  - text: Programme
    href: /programme/
    isPrimary: true
  - text: Contact
    href: /contact/
permalink: /
---

<style>
  /* Set home page content width to 60rem, protecting the footer */
  .page-content, .home {
    max-width: 60rem !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }
  /* Ensure mobile hamburger dropdown menu displays properly when active */
  @media screen and (max-width: 1023px) {
    .navbar-menu.is-active {
      display: block !important;
      background-color: #ffffff !important;
      position: absolute !important;
      top: 100% !important;
      left: 0 !important;
      right: 0 !important;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1) !important;
      padding: 1rem !important;
      z-index: 1001 !important;
    }
  }
</style>

## The Data to Action Pavilion @ CBD COP17

### Yerevan, Armenia | 19-30 October 2026

The **Data to Action Pavilion** brings together organizations working across the biodiversity knowledge system—from scientific collections, monitoring and Earth observations to data infrastructure, decision-support tools, capacity development, applied research and policy support. The initiative convenes representatives from dozens of partner organizations for a dynamic programme that demonstrates [Kunming-Montreal Global Biodiversity Framework](https://cbd.int/gbf).

## Engaging at the Pavilion

* **Daily Sessions:** Browse the complete schedule of panel discussions and side events from October 19–30 via the [Programme](/programme/) page.

<script>
  document.addEventListener('click', function(event) {
    const burger = event.target.closest('.navbar-burger');
    if (burger) {
      const targetId = burger.dataset.target;
      const target = targetId ? document.getElementById(targetId) : burger.nextElementSibling;

      burger.classList.toggle('is-active');
      if (target && target.classList.contains('navbar-menu')) {
        target.classList.toggle('is-active');
      }
    }
  });
</script>
