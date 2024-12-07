const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
const PORT = 3000;

// MongoDB connection string
const MONGO_URI = "add your uri to connect to mongoDB";


mongoose.connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("Connected to MongoDB"))
    .catch(err => console.error("MongoDB connection error:", err));

const ctaSchema = new mongoose.Schema({
    line: String,
    data: Object,
}, { collection: 'cta_data' });

const CtaData = mongoose.model('CtaData', ctaSchema);


app.use(cors());
app.use(express.json());

// API endpoint to fetch data for a specific line
app.get('/api/cta/:line', async (req, res) => {
    const { line } = req.params;
    try {
        const result = await CtaData.findOne({ line }); // Adjust the query to your schema
        if (result) {
            res.json(result);
        } else {
            res.status(404).json({ message: `No data found for line: ${line}` });
        }
    } catch (error) {
        console.error("Error fetching data:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
