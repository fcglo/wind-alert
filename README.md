# wind-alert

This repo allows me to deploy a simple AWS Lambda function that checks the BBC wind speed forecast for the next day, and sends a text to my chosen number when the wind speed is above a given threshold. This should allow me to move the plants on my balcony out of harm's way in advance when the wind is going to be too strong.

## Deployment

Make sure to copy `.env.template` to a new `.env` file and fill it with values that match your needs.
Run

```bash
npm run deploy
```

## BBC Weather RSS feed

BBC weather has an RSS feed that gives 3 days forecast for a chosen location, with some documentation [here](https://www.bbc.co.uk/weather/about/17543675). This is the source of information for this wind alert lambda.
To find the id for the location you're interested in just search for that location on the BBC weather website and you can copy it from the URL. For example that's the URL for Birmingham [https://www.bbc.co.uk/weather/2655603](https://www.bbc.co.uk/weather/2655603) and the id that can be used in the `.env` file is 2655603
