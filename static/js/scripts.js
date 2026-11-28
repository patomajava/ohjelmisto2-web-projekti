"use strict";

// HTML sivujen navigointi painikkeilla
const nappi_uusi = document.getElementById("uusi-peli");
const nappi_lataa = document.getElementById("lataa-peli");
const nappi_poistu = document.getElementById("poistu");
const valintanapit = document.querySelectorAll(".pelinappi");

nappi_uusi?.addEventListener("click", () => {window.location.href = "/peli_uusi"});
nappi_lataa?.addEventListener("click", () => {window.location.href = "/peli_lataa"});
nappi_poistu?.addEventListener("click", () => {window.location.href = "/"});

valintanapit?.forEach(nappi => {
    nappi.addEventListener("click", (event) => {
        paivitaPeli(event.currentTarget.dataset.valinta);
    });
});

// Flask serveriltä pelitilanteen fetchaus
async function paivitaPeli(valinta) {

    try {
        const response = await fetch(`http://127.0.0.1:3000/pelin_tilanne?valinta=${valinta}`);
        if (!response.ok) {
            throw new Error("HTTP-virhe. Koodi: " + response.status);
        }
        const data = await response.json();
        console.log("received gamestate:", data)

        nykyinen_huone(data);
        tarinatekstit(data);
        kontrollit(data);
        tavaraluettelo(data);
        esineet_ja_mekanismit(data);

        return //data;
    }
    catch (error) {
        console.log("Virhe datan haussa:", error)
    };
}

// Seuraavat funktiot päivittävät eri kohtia pelialueesta
function nykyinen_huone(data) {
    const tekstilaatikko = document.getElementById("nykyinen_huone");
    tekstilaatikko.textContent = data.nykyinen_huone;
    return
}

function tarinatekstit(data) {
    const tekstilaatikko = document.getElementById("tarinateksti");
    tekstilaatikko.textContent = data.tarinateksti;
    return
}

function kontrollit(data) {
    const kontrollit = document.getElementById("kontrollit");
    kontrollit.replaceChildren();
    
    for (let i in data.kontrollit) {
        const item = document.createElement("li");
        item.textContent = data.kontrollit[i];
        kontrollit.appendChild(item);
    }
    return
}

function tavaraluettelo(data) {
    const tavaraluettelo = document.getElementById("tavaraluettelo");
    tavaraluettelo.replaceChildren();
    
    for (let i in data.tavaraluettelo) {
        const item = document.createElement("li");
        item.textContent = data.tavaraluettelo[i];
        tavaraluettelo.appendChild(item);
    }
    return
}

function esineet_ja_mekanismit(data) {
    const esineet_ja_mekanismit = document.getElementById("esineet_ja_mekanismit");
    esineet_ja_mekanismit.replaceChildren();

    for (let i in data.esineet_ja_mekanismit) {
        const item = document.createElement("li");
        item.textContent = data.esineet_ja_mekanismit[i];
        esineet_ja_mekanismit.appendChild(item);
    }
    return
}