// We wait for the HTML document to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function() {

    // This is the placeholder for your API Gateway URL.
    // We will replace this with the real URL after we build the backend.
    const apiGatewayUrl = 'https://8i7zdpyj12.execute-api.eu-north-1.amazonaws.com/views'; 

    // Find the HTML element where we will display the count
    const visitorCountElement = document.getElementById('visitor-count');

    // Use the fetch API to make a request to our backend
    fetch(apiGatewayUrl, {
        method: 'GET', // We are getting data from the API
    })
    .then(response => {
        // Check if the response was successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Parse the JSON data from the response
        return response.json();
    })
    .then(data => {
        // Update the HTML with the visitor count from the API
        // The API will return data in a format like: {"views": 123}
        visitorCountElement.textContent = data.views;
    })
    .catch(error => {
        // If there's an error (like the API not existing yet), log it to the console
        console.error('There was a problem with the fetch operation:', error);
        // Optionally, display a fallback message on the site
        visitorCountElement.textContent = 'N/A';
    });

});