This repo uses Mistral trained model for the response and it can run on CPU.

Downlaod the model: wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf

Install the Dependencies: pip install ctransformers>=0.2.27

Place the downloaded model in the same folder as app.py, init_container etc are and then use docker to build it.

Further reading: https://medium.com/artificial-corner/run-mistral7b-quantized-for-free-on-any-computer-2cadc18b45a2
