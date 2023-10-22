const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();

// Replace with your MongoDB connection string
mongoose.connect('mongodb+srv://ykhullar:findec123@fin-dec.mvtowtg.mongodb.net/?retryWrites=true&w=majority', { useNewUrlParser: true });

// Define a MongoDB schema and model for the form submissions
const submissionSchema = new mongoose.Schema({
  name: String,
  age: Number,
  plannedRetirement: Number,
  typeA: String,
  incomemonthly: String,
  employer401k: Number,
  estimatedMonthly: Number,
  monthlySpending: Number,
});

const Submission = mongoose.model('Submission', submissionSchema);

// Use body-parser to parse form submissions
app.use(bodyParser.urlencoded({ extended: true }));

// Handle POST requests from the form
app.post('/submit-form', (req, res) => {
  // Create a new submission document
  const newSubmission = new Submission({
    name: req.body['q37_name37[first]'] + ' ' + req.body['q37_name37[last]'],
    age: req.body.q27_age,
    plannedRetirement: req.body.q28_plannedRetirement,
    typeA: req.body.q31_typeA,
    incomemonthly: req.body.q32_incomemonthly,
    employer401k: req.body.q33_employer401k,
    estimatedMonthly: req.body.q35_estimatedMonthly,
    monthlySpending: req.body.q36_monthlySpending,
  });

  // Save the submission to MongoDB
  newSubmission.save((err) => {
    if (err) {
      console.error(err);
      res.status(500).send('Error saving the submission.');
    } else {
      res.send('Submission saved to MongoDB.');
    }
  });
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
