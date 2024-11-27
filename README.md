# Neuronpedia Python Library

## Authentication

Some APIs on Neuronpedia require an API key. For example, if you want to bookmark something in your account, or upload a new vector, you'll need to identify yourself with a Neuronpedia API key.

### Setting the API Key (free)

1) Sign up for Neuronpedia at `neuronpedia.org`.
2) Get your Neuronpedia API key from `neuronpedia.org/account`.
3) Set the environment variable `NEURONPEDIA_API_KEY` to your API key. You can do this through a `.env` file or other similar methods.

### Example: Upload a Vector, then Steer With It

See the `examples/upload_vector_and_steer.ipynb` notebook.