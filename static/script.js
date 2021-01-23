// https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
var loadFile = function(e) {
	let output = null;
	if (e.target.id == 'submit1') {
		output = document.getElementById('upload1');
	} else if (e.target.id == 'submit2') {
		output = document.getElementById('upload2');
	}
	console.log(output);
	output.src = URL.createObjectURL(e.target.files[0]);
	output.onload = function() {
		URL.revokeObjectURL(output.src); // free memory
	};
};

let mode = null;
//handle four types of process
function handleGS() {
	mode = 'GS';
	renderOneImagePage();
}

function handleFD() {
	mode = 'FD';
	renderOneImagePage();
}

function handleRF() {
	mode = 'RF';
	renderTwoImagePage();
}

function handleFS() {
	mode = 'FS';
	renderTwoImagePage();
}

//for Greyscale and face Detection(only need one picture)
function renderOneImagePage() {
	document.querySelector('#submit1').style.display = 'block';
	document.querySelector('#submit2').style.display = 'none';
	document.querySelector('#submitButton').style.display = 'block';
	showMode();
	var upload2 = document.getElementById('upload2');
	var output = document.getElementById('output');
	upload2.src = '';
	output.src = '';
}

//for Replace Face and face Detection(need two pictures)
function renderTwoImagePage(mode) {
	document.querySelector('#submit1').style.display = 'block';
	document.querySelector('#submit2').style.display = 'block ';
	document.querySelector('#submitButton').style.display = 'block';
	showMode();
	var output = document.getElementById('output');
	output.src = '';
}

//play mode
function showMode() {
	const guide = {
		GS: 'get the greysacle!',
		FD: 'Face detection from opencv Haar-cascade Detection.',
		RF: 'The face in the first image will be replaced by the second image!',
		FS: 'The face in the first picture and the face in the second picture will swap.'
	};
	document.getElementsByClassName('modeDisplay')[0].innerText = guide[mode];
}

//handle submit
const form = document.getElementById('form');
const image1 = document.getElementById('submit1');
const image2 = document.getElementById('submit2');

form.addEventListener('submit', (e) => {
	e.preventDefault();

	if (mode == 'GS' || mode == 'FD') {
		fetchWithOne();
	}
	if (mode == 'RF' || mode == 'FS') {
		fetchWithTwo();
	}
});

//for greyscale and face detection
function fetchWithOne() {
	const url1 = 'http://127.0.0.1:5000/process/togrey';
	const url2 = 'http://127.0.0.1:5000/process/detectface';
	let url = '';
	if (mode == 'GS') {
		url = url1;
	} else if (mode == 'FD') {
		url = url2;
	}

	const formData = new FormData();
	formData.append('image1', image1.files[0]);

	const request = new Request(url, {
		method: 'post',
		body: formData
	});
	fetch(request)
		.then((res) => {
			console.log('2312312');
			return res.blob();
		})
		.then((blob) => {
			console.log('blob');
			var output = document.getElementById('output');
			var objectURL = URL.createObjectURL(blob);
			output.src = objectURL;
		})
		.catch((error) => {
			// if an error occured it will be logged to the JavaScript console here.
			console.log('An error occured with fetch:', error);
		});
}

function fetchWithTwo() {
	const url1 = 'http://127.0.0.1:5000/process/replaceface';
	const url2 = 'http://127.0.0.1:5000/process/swapface';
	let url = '';
	if (mode == 'RF') {
		url = url1;
	} else if (mode == 'FS') {
		url = url2;
	}

	const formData = new FormData();
	formData.append('image1', image1.files[0]);
	formData.append('image2', image2.files[0]);

	const request = new Request(url, {
		method: 'post',
		body: formData
	});
	fetch(request)
		.then((res) => {
			return res.blob();
		})
		.then((blob) => {
			var output = document.getElementById('output');
			var objectURL = URL.createObjectURL(blob);
			output.src = objectURL;
		})
		.catch((error) => {
			// if an error occured it will be logged to the JavaScript console here.
			console.log('An error occured with fetch:', error);
		});
}
