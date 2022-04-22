# Aakash FDE Assignment

## Pre-requisites

- Python >=3.8

## Build the project

1. Clone the repository

```bash
git clone 
```

2. Create a virtual environment and install dependencies (`using make utility of unix`)

```bash
make create-env
```

> Note: `API_KEY` is required in .env file.

4. Run the API

```bash
make run
```

5. API Endpoint is http://127.0.0.1:5000/

```bash
curl --request POST \
  --url http://127.0.0.1:5000/getAddressDetails \
  --header 'content-type: application/json' \
  --data '{"address": "#3582, 13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru,Karnataka 560008","output_format": "json"}'
```

###### Building and running with Docker `without reverse-proxy impl`

> Note: `API_KEY` is required in .env file.

```bash
make docker-build
make docker-run
```

###### Screenshots

![Alt text](https://github.com/aakashjangidme/verloop-fde/blob/main/screenshots/json_response.png?raw=true "Json Response")
![Alt text](https://github.com/aakashjangidme/verloop-fde/blob/main/screenshots/xml_response.png?raw=true "XML Response")
![Alt text](https://github.com/aakashjangidme/verloop-fde/blob/main/screenshots/error_validation.png?raw=true "Error Validation")
