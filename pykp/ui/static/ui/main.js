class ClassList {
	constructor(classes = []) {
		this.list = classes;
	}

	add(element) {
		this.list.forEach(item => {
			element.classList.add(item);
		});
	}

	remove(element) {
		this.list.forEach(item => {
			element.classList.remove(item);
		});
	}

}

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
		// console.info(`Side Menu toggled to ${this.isEnabled}`);
	}
}

sideMenuButton.addEventListener("click", () => {
	sideMenu.toggle();
});
