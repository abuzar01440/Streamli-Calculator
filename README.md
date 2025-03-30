# Streamlit-Calculator
In this repo, I used python Library streamlit to create a calculator app

# Streamlit Scientific Calculator

A simple yet functional scientific calculator web application built using Python and the Streamlit library. It provides a user-friendly interface for performing common mathematical operations, dynamically adjusting the input fields based on the selected operation.


## Features

* **Arithmetic Operations:** Addition, Subtraction, Multiplication, Division
* **Exponents & Roots:** Power, Square, Square Root, Cube, Cube Root
* **Logarithms:** Logarithm (Base 10), Natural Logarithm (ln)
* **Other:** Factorial
* **Dynamic UI:** Intelligently shows only the necessary number input fields (one or two) based on the selected mathematical operation.
* **Error Handling:** Includes basic checks for common errors like division by zero, square root of negative numbers, logarithm of non-positive numbers, and factorial of non-integers/negative numbers.

## Technologies Used

* Python 3.x
* Streamlit
* Math (Python Standard Library)

## Setup and Installation

Follow these steps to get the calculator running on your local machine.

1.  **Prerequisites:**
    * Ensure you have Python 3.7 or higher installed.
    * Ensure you have `pip` (Python package installer) available.



2.  **Install Dependencies:**
    Create a file named `requirements.txt` in the project's root directory with the following content:
    ```txt
    streamlit
    ```
    Then, install the required package:
    ```bash
    pip install steamlit
    ```

## Usage

1.  Make sure you are in the project's root directory (`Streamlit-Calculator `) in your terminal.
2.  Ensure your virtual environment (if created) is activated.
3.  Run the Streamlit application using the following command:
    ```bash
    streamlit run calculator_app.py
    ```
    *(Replace `calculator_app.py` with the actual name of your Python script file if it's different.)*

Streamlit will start the server, and the calculator application should automatically open in your default web browser.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/your-repo-name/issues) (if you plan to use it) or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (Optional: you can add an MIT License file if you wish).

## Author

* **Abuzar Shahid**
