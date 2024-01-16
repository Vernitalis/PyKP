export class ClassList {
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
