// Define the mapping of predictors and intervals to model file names (simulated)
const predictorMapping = {
    "PF": {
        "SF": {
            "Admission SF": "best_sf_pf_SF_PF.pkl",
            "0-6 hrs SF": "best_sf_pf_0-6_SF_0-6_PF.pkl",
            "6-12 hrs SF": "best_sf_pf_6-12_SF_6-12_PF.pkl",
            "12-24 hrs SF": "best_sf_pf_12-24_SF_12-24_PF.pkl",
            "24-48 hrs SF": "best_sf_pf_24-48_SF_24-48_PF.pkl",
            "48-72 hrs SF": "best_sf_pf_48-72_SF_48-72_PF.pkl",
            "After 72 hrs SF": "best_sf_pf_After_72_SF_After_72_PF.pkl"
        }
    },
    "OI": {
        "OSI": {
            "Admission OSI": "best_osi_oi_OSI_OI.pkl",
            "0-6 hrs OSI": "best_osi_oi_0-6_OSI_0-6_OI.pkl",
            "6-12 hrs OSI": "best_osi_oi_6-12_OSI_6-12_OI.pkl",
            "12-24 hrs OSI": "best_osi_oi_12-24_OSI_12-24_OI.pkl",
            "24-48 hrs OSI": "best_osi_oi_24-48_OSI_24-48_OI.pkl",
            "48-72 hrs OSI": "best_osi_oi_48-72_OSI_48-72_OI.pkl",
            "After 72 hrs OSI": "best_osi_oi_After_72_OSI_After_72_OI.pkl"
        }
    }
};

// Function to simulate model loading and prediction (since we can't use joblib in JS)
function loadModelAndPredict(filePath, inputValue) {
    // Simulate a prediction (for demonstration purposes)
    const prediction = inputValue * Math.random();  // Randomized prediction
    return prediction.toFixed(4);  // Return prediction with 4 decimal places
}

// Handle Prediction button click
document.getElementById("predict-btn").addEventListener("click", function() {
    const predictor = document.getElementById("predictor").value;
    const hourInterval = document.getElementById("interval").value;
    const inputValue = parseFloat(document.getElementById("input-value").value);

    if (isNaN(inputValue)) {
        alert("Please enter a valid number.");
        return;
    }

    // Get model file path
    const modelFile = predictorMapping[predictor]["SF"][hourInterval];
    
    // Simulate model prediction
    const prediction = loadModelAndPredict(modelFile, inputValue);

    // Display the result
    const resultDiv = document.getElementById("prediction-result");
    resultDiv.innerHTML = `Prediction for <b>${predictor}</b> (${hourInterval}): <span>${prediction}</span>`;
});
