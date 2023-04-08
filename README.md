# Brain-Tumor-Classification

Brain Tumor Classification is a Python-based project that utilizes deep learning models to classify brain tumor images and derma diseases. The project uses Keras to load the models and RabbitMQ to handle messaging between the various components. This repository contains the main code for processing and classifying images.

Requirements
------------

*   Python 3.x
*   Keras
*   TensorFlow
*   Pillow (PIL)
*   NumPy
*   pika
*   RabbitMQ
*   ssl

Setup
-----

1.  Clone the repository:

bash

```bash
git clone https://github.com/KinoThe-Kafkaesque/Brain-cancer.git
```

2.  Install the required packages:

bash

```bash
pip install -r requirements.txt
```

3.  Run the RabbitMQ server in the background.
    
4.  Run the main script:
    

bash

```bash
python database.py
```

Usage
-----

The script can be used for classifying brain tumor and derma diseases images. The main function `main()` will start consuming messages from two RabbitMQ queues: `rpc_brain` and `rpc_retino`. The function `riddle()` processes the brain tumor images, and the function `riddleRetina()` processes the derma diseases images. After classification, the script will send the result back as a response with the confidence level.

Contributing
------------

To contribute to the project, please fork the repository, make your changes, and submit a pull request.

License
-------

This project is licensed under the MIT License.

Contact
-------

For any inquiries, please open an issue.
