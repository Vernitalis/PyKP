import {PykpMap} from "./map.js";
import {createTooltip} from "./components.js";
import {ClassList} from "./utils.js";

const map = new PykpMap("map-container");

const sideMenuButton = document.querySelector("#side-menu-button");
const sideMenu = {
    element: document.querySelector("#side-menu"),
    onHideClass: new ClassList(["hidden"]),
    onShowClass: new ClassList([]),
    __enabled__: false,
    get isEnabled() {
        return this.__enabled__;
    },
    set isEnabled(value) {
        this.__enabled__ = value;
        if (this.isEnabled) {
            this.onHideClass.remove(this.element);
            this.onShowClass.add(this.element);
        } else {
            this.onShowClass.remove(this.element);
            this.onHideClass.add(this.element);
        }
    },
    toggle: function () {
        this.isEnabled = !this.isEnabled;
    }
}

sideMenuButton.addEventListener("click", () => {
    sideMenu.toggle();
});

const stationCardTemplate = document.querySelector("[data-station-template]")
const stationCardContainer = document.querySelector("[data-station-cards-container]")
const searchInput = document.querySelector("[data-search]")

let stations = []

searchInput.addEventListener("input", e => {
    const value = e.target.value.toLowerCase()
  let visibleCount = 0
    stations.forEach(station => {
        const isVisible =
            station.name.toLowerCase().includes(value)
        station.element.classList.toggle("hide", !isVisible)
        if (isVisible) {
            visibleCount++;
        }
    })
stationCardContainer.style.overflowY = visibleCount > 10 ? "scroll" : "hidden";
})

fetch("/geo/GetLocations")
    .then(res => res.json())
    .then(data => {
        stations = data.features.map(station => {
            const card = stationCardTemplate.content.cloneNode(true).children[0]
            const header = card.querySelector("[data-header]")
            header.textContent = station.properties.name
            card.classList.add("hide")
            stationCardContainer.append(card)
            return {name: station.properties.name, element: card}
        })
    })