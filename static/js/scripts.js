"use strict";

// Sivujen navigointi nappuloilla "uusi-peli"/"lataa-peli"/"poistu-pelistä" yms.

const nappi_uusi = document.getElementById("uusi-peli");
const nappi_lataa = document.getElementById("lataa-peli");
const nappi_poistu = document.getElementById("poistu");
const valintanapit = document.querySelectorAll("#pelinappi");

nappi_uusi?.addEventListener("click", () => {window.location.href = "/peli_uusi"});
nappi_lataa?.addEventListener("click", () => {window.location.href = "/peli_lataa"});
nappi_poistu?.addEventListener("click", () => {window.location.href = "/"});

valintanapit?.forEach(nappi => {
    nappi.addEventListener("click", (event) => {
        paivitaPeli(event.currentTarget.dataset.valinta);
    });
});

async function paivitaPeli(valinta) {

    try {
        const response = await fetch(`http://127.0.0.1:3000/pelin_tilanne?valinta=${valinta}`);
        if (!response.ok) {
            throw new Error("HTTP-virhe. Koodi: " + response.status);
        }
        const data = await response.json();

        nykyinen_huone(data);
        tarinatekstit(data);
        tavaraluettelo(data);
        esineet_ja_mekanismit(data);

        return data;
    }
    catch (error) {
        console.log("Virhe datan haussa:", error)
    };
}

function nykyinen_huone(data) {
    const tekstilaatikko = document.getElementById("nykyinen_huone");
    tekstilaatikko.innerHTML = "";

    tekstilaatikko.textContent = data.testitieto2.testitieto3;
    return
}

function tarinatekstit(data) {
    const tekstilaatikko = document.getElementById("tarinateksti");
    tekstilaatikko.innerHTML = "";

    tekstilaatikko.textContent = data.testitieto;
    return
}

function tavaraluettelo(data) {
    const tavaraluettelo = document.getElementById("tavaraluettelo");
    
    for (let i = 0; i < data.tavaraluettelo.length; i++) {
        let item = document.createElement("li");
        item.textContent = data.tavaraluettelo[i];
        tavaraluettelo.appendChild(item)
    }
    return
}

function esineet_ja_mekanismit(data) {
    const esineet_ja_mekanismit = document.getElementById("esineet_ja_mekanismit");

    for (let i = 0; i < data.esineet_ja_mekanismit.length; i++) {
        let item = document.createElement("li");
        item.textContent = data.esineet_ja_mekanismit[i];
        esineet_ja_mekanismit.appendChild(item)
    }
    return
}