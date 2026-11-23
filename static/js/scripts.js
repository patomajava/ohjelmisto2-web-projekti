"use strict";

// Sivujen navigointi nappuloilla "uusi-peli"/"lataa-peli"/"poistu-pelistä" yms.

const nappi_uusi = document.getElementById("uusi-peli");
const nappi_lataa = document.getElementById("lataa-peli");
const nappi_poistu = document.getElementById("poistu");

nappi_uusi?.addEventListener("click", () => {window.location.href = "/peli_uusi"})
nappi_lataa?.addEventListener("click", () => {window.location.href = "/peli_lataa"})
nappi_poistu?.addEventListener("click", () => {window.location.href = "/"})