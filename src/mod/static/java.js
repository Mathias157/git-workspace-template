async function get_figure() {

    // Get x and y lims
    let x0 = parseInt(document.getElementById('user-inputx0').value);
    let x1 = parseInt(document.getElementById('user-inputx1').value);
    let y0 = parseInt(document.getElementById('user-inputy0').value);
    let y1 = parseInt(document.getElementById('user-inputy1').value);
    

    // Get figure data from python
    let imageData = await eel.make_figure(x0, x1, y0, y1)();
    
    // Get the image element
    let imageElement = document.getElementById('figure');
    
    // Set the src attribute of the image to display the returned data
    // Assuming your Python function returns a base64 encoded image or a URL
    imageElement.src = imageData;
    
    // Optional: Add alt text for accessibility
    imageElement.alt = 'Generated figure from Python';
  }

// Function to send input text to Python
async function sendInput() {
    // Get the input value
    let inputText = document.getElementById('user-input').value;
    
    if (inputText.trim() === '') {
        document.getElementById('python-response').textContent = 'Please enter some text first';
        return;
    }
    
    try {
        // Send the input to Python and wait for response
        let response = await eel.process_input(inputText)();
        
        // Display the response
        document.getElementById('python-response').textContent = response;
    } catch (error) {
        document.getElementById('python-response').textContent = 'Error: ' + error;
    }
}