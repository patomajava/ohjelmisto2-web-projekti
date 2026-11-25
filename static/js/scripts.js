"use strict";

// Sivujen navigointi nappuloilla "uusi-peli"/"lataa-peli"/"poistu-pelistä" yms.

const nappi_uusi = document.getElementById("uusi-peli");
const nappi_lataa = document.getElementById("lataa-peli");
const nappi_poistu = document.getElementById("poistu");
const valintanapit = document.querySelectorAll("#pelinappi");

nappi_uusi?.addEventListener("click", () => {window.location.href = "/peli_uusi"});
nappi_lataa?.addEventListener("click", () => {window.location.href = "/peli_lataa"});
nappi_poistu?.addEventListener("click", () => {window.location.href = "/"});

valintanapit?.forEach(nappi => {nappi.addEventListener("click", paivitaPeli)});

async function paivitaPeli() {

    try {
        const response = await fetch("http://127.0.0.1:3000/pelin_tilanne");
        if (!response.ok) {
            throw new Error("HTTP-virhe. Koodi: " + response.status);
        }
        const data = await response.json();

        tarinatekstit(data);

        return data;
    }
    catch (error) {
        console.log("Virhe datan haussa:", error)
    };
}

function tarinatekstit(data) {

    const tekstilaatikko = document.getElementById("tarinateksti");
    tekstilaatikko.innerHTML = "";
        
    tekstilaatikko.textContent = data.tarinateksti;

}