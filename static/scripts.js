/*!
* Start Bootstrap - Business Casual v7.0.9 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page




//window.addEventListener('DOMContentLoaded', event => {
//    const listHoursArray = document.body.querySelectorAll('.list-hours li');
//    listHoursArray[new Date().getDay()].classList.add(('today'));
//})
//
//$(document).ready(function() {
//    // Hide dropdown menu initially
//    $('.dropdown-menu').hide();
//
//    // Toggle dropdown menu when button is clicked
//    $('#multiSelectDropdownButton').on('click', function () {
//        $('.dropdown-menu').toggle();
//    });
//
//    // Close dropdown when clicking outside
//    $(document).on('click', function (e) {
//        if (!$('.dropdown').is(e.target) && $('.dropdown').has(e.target).length === 0) {
//            $('.dropdown-menu').hide();
//        }
//    });
//
//    // Prevent dropdown menu from closing when clicking inside
//    $('.dropdown-menu').on('click', function (e) {
//        e.stopPropagation();
//    });
//});
//
//
//function preview() {
//    frame.src = URL.createObjectURL(event.target.files[0]);
//}
//
//function clearImage() {
//    document.getElementById('formFile').value = null;
//    frame.src = "";
//}
//
//const form = document.querySelector("form");
//form.addEventListener('submit', (e) => {
//    if (!form.checkValidity()) {
//        e.preventDefault();
//    }
//    form.classList.add('was-validated');
//}, false);

// Function to add "today" class to current day's list item
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    const currentDayIndex = new Date().getDay();
    if (listHoursArray.length > currentDayIndex) {
        listHoursArray[currentDayIndex].classList.add('today');
    }
});

//window.addEventListener('DOMContentLoaded', event => {
//    const listHoursArray = document.body.querySelectorAll('.list-hours li');
//    listHoursArray[new Date().getDay()].classList.add('today');
//});

// jQuery functions
$(document).ready(function() {
    // Hide dropdown menu initially
    $('.dropdown-menu').hide();

    // Toggle dropdown menu when button is clicked
    $('#multiSelectDropdownButton').on('click', function () {
        $('.dropdown-menu').toggle();
    });

    // Close dropdown when clicking outside
    $(document).on('click', function (e) {
        if (!$('.dropdown').is(e.target) && $('.dropdown').has(e.target).length === 0) {
            $('.dropdown-menu').hide();
        }
    });

    // Prevent dropdown menu from closing when clicking inside
    $('.dropdown-menu').on('click', function (e) {
        e.stopPropagation();
    });
});

// Function to preview uploaded image
function preview() {
    frame.src = URL.createObjectURL(event.target.files[0]);
}


// Function to clear uploaded image
function clearImage() {
    document.getElementById('formFile').value = null;
    frame.src = "";
}

// Form validation
const form = document.querySelector("form");
form.addEventListener('submit', (e) => {
    if (!form.checkValidity()) {
        e.preventDefault();
    }
    form.classList.add('was-validated');
}, false);


function validateImage() {
    var fileInput = document.getElementById('formFile');
    var errorMessage = document.querySelector('.invalid-feedback');
    var submitButton = document.querySelector('.btn');

    if (fileInput.files.length === 0) {
        errorMessage.style.display = 'block';
        submitButton.disabled = true;
    } else {
        errorMessage.style.display = 'none';
        submitButton.disabled = false;
    }
}
