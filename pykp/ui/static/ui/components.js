import { ClassList } from "./utils.js";

export function createTooltip(dataTip) {
	let element = document.createElement("div");
	(new ClassList(["tooltip"])).add(element);

	element.open = function() {
		this.classList.add("tooltip-open");
	};
	element.close = function() {
		this.classList.remove("tooltip-open");
	};
	element.isOpened = function() {
		this.classList.contains("tooltip-open");
	}

	element.setDataTip = function(dataTip) {
		this.setAttribute("data-tip", dataTip);
	}

	element.setDataTip(dataTip);

	return element;
}
