---
lang-ref: page
layout: home
title: Contact
background: assets/images/mariposa-opt.jpg
imageLicense: "[_Polyommatus icarus_ (von Rottemburg, 1775)](https://www.gbif.org/occurrence/5828883558) observed in Armenia by Axel Gosseries [(licensed under CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)"
height: 60vh
permalink: /contact/
---

<style>
  /* Set contact page content width to 60rem, protecting the footer */
  .page-content, .main-content {
    max-width: 60rem !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }
  /* Hide translation widget and language dropdown */
  .translation-widget,
  .language-switcher,
  .skiptranslate,
  .navbar-item.has-dropdown.js-language-dropdown,
  .language-selector {
    display: none !important;
  }
  /* Zoomable image styling */
  .zoomable-map {
    cursor: zoom-in;
    transition: opacity 0.2s;
  }
  .zoomable-map:hover {
    opacity: 0.95;
  }
  /* Modal styles for map zoom */
  #map-modal {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.85);
    z-index: 2000;
    justify-content: center;
    align-items: center;
    padding: 2rem;
  }
  #map-modal img {
    max-width: 90vw;
    max-height: 90vh;
    object-fit: contain;
    border-radius: 4px;
    background: #fff;
  }
  #map-modal-close {
    position: absolute;
    top: 1.5rem; right: 2rem;
    background: none; border: none;
    color: #fff; font-size: 2.5rem; cursor: pointer;
  }
</style>

## Find us

The Data to Action Pavilion is in the Blue Zone at the Meridian Expo and Event Centre, 1 Voskerichneri Street, Yerevan, Armenia.

<div style="margin: 1.5rem 0; text-align: center;">
  <img src="/assets/images/sitemap.svg" alt="Site Plan" class="zoomable-map" onclick="openMapModal(this.src)" style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #e5e7eb;">
  <p style="font-size: 0.85rem; color: #666; margin-top: 0.5rem;">Click map to zoom</p>
</div>

<!-- Map Zoom Modal -->
<div id="map-modal" onclick="closeMapModal()">
  <button id="map-modal-close" onclick="closeMapModal()">&times;</button>
  <img id="map-modal-img" src="" alt="Zoomed Site Plan">
</div>

<script>
  function openMapModal(src) {
    document.getElementById('map-modal-img').src = src;
    document.getElementById('map-modal').style.display = 'flex';
  }
  function closeMapModal() {
    document.getElementById('map-modal').style.display = 'none';
  }
</script>

## Get in Touch

For inquiries regarding the Data to Action Pavilion, please contact us at:

- **Email:** [contact@cop17pavilion.org](mailto:contact@cop17pavilion.org)
