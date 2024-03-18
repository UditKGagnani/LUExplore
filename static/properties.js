document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form_properties');
    const area = document.getElementById('formArea');
    const bedrooms = document.getElementById('formBedrooms');
    const multiSelect = document.getElementById('multiSelectOptions');
    const communeSelect = document.getElementById('communeSelect');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        validateInputs();

        // Get the selected values from the multi-select dropdown
        const selectedOptions = Array.from(multiSelect.selectedOptions).map(option => option.value);

        // Get other form values
        const areaValue = area.value;
        const bedroomsValue = bedrooms.value;
        const communeValue = communeSelect.value;

        // Log or use the values as needed
        console.log('Selected options:', selectedOptions);
        console.log('Area:', areaValue);
        console.log('Bedrooms:', bedroomsValue);
        console.log('Commune:', communeValue);

        // Add code to submit the form or perform other actions
        // form.submit(); // Uncomment this line to submit the form
    });
});
