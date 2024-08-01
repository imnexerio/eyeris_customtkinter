# Eyeris

## Overview
Eyeris is a real-time eye blink tracking application that utilizes your webcam. The main script, `main.py`, is the entry point of the application, leveraging the MediaPipe library for real-time face landmark detection and eye blink tracking.

## Installation

To get started with Eyeris, follow the steps below to install the necessary dependencies:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/imnexerio/eyeris_customtkinter.git
    cd eyeris_customtkinter
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Setup

Before running Eyeris, ensure that you have set up the necessary configurations:

1. **Assets Directory**: Ensure that the `assets` directory contains all the necessary files required by the project.

## Usage

To run the main script, use the following command:

```sh
python main.py
```

Alternatively, you can use the provided executable file for direct use without needing to set up a development environment.

## Project Structure

Here is an overview of the project's directory structure:

```
eyeris_customtkinter/
├── assets/
│   ├── [asset1]
│   ├── [asset2]
│   └── ...
├── main.py
├── requirements.txt
└── README.md
```

- **assets/**: This directory contains all the assets required by the project.
- **main.py**: The main script that serves as the entry point of the application.
- **requirements.txt**: A file listing all the dependencies required by the project.
- **README.md**: This file, providing an overview and instructions for the project.

## Contributing

If you would like to contribute to Eyeris, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to customize the content as per your project's specific details and requirements.