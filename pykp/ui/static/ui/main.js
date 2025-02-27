import { PykpMap } from "./map.js";
import { createTooltip } from "./components.js";
import { ClassList } from "./utils.js";

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
		}
		else {
			this.onShowClass.remove(this.element);
			this.onHideClass.add(this.element);
		}
	},
	toggle: function() {
		this.isEnabled = !this.isEnabled;
	}
}

sideMenuButton.addEventListener("click", () => {
	sideMenu.toggle();
});
