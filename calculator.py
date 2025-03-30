import streamlit as st
import math

# lets create a function for the calculator
def calculator():
    
    st.title("Scientific Calculator")

    # Define operations
    operations_list = [
        "Addition", "Subtraction", "Multiplication", "Division", "Power", # Two operands
        "Square", "Square Root", "Cube", "Cube Root", "Log (base 10)",
        "Natural Log (ln)", "Factorial" # One operand
    ]

    # Operations that require two numbers
    two_operand_ops = {"Addition", "Subtraction", "Multiplication", "Division", "Power"}

    # lets add a select box for the user to select the operation
    operation = st.selectbox("Select Operation", operations_list)

    # Initialize num2 to None. It will be assigned a value only if needed.
    num1 = None
    num2 = None

    # Always get the first number
    # Use columns for better layout, especially when two inputs are shown
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter Number", key="num1", value=0.0, format="%.3f") 

    # Only show the second number input if the operation requires it
    if operation in two_operand_ops:
        with col2:
            num2 = st.number_input("Enter Second Number", key="num2", value=0.0, format="%.5f")

    # --- Calculation Button and Logic ---
    if st.button("Calculate"):
        try:
            result = None # Initialize result

            # --- Perform Calculation based on operation ---

            if operation == "Addition":
                if num1 is not None and num2 is not None:
                    result = num1 + num2
                    st.success(f"Result: {num1} + {num2} = {result}")
                else:
                     st.warning("Please ensure both numbers are entered for Addition.")

            elif operation == "Subtraction":
                if num1 is not None and num2 is not None:
                    result = num1 - num2
                    st.success(f"Result: {num1} - {num2} = {result}")
                else:
                     st.warning("Please ensure both numbers are entered for Subtraction.")

            elif operation == "Multiplication":
                if num1 is not None and num2 is not None:
                    result = num1 * num2
                    st.success(f"Result: {num1} * {num2} = {result}")
                else:
                     st.warning("Please ensure both numbers are entered for Multiplication.")

            elif operation == "Division":
                if num1 is not None and num2 is not None:
                    if num2 == 0:
                        st.error("Error: Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        st.success(f"Result: {num1} / {num2} = {result}")
                else:
                     st.warning("Please ensure both numbers are entered for Division.")

            elif operation == "Power":
                if num1 is not None and num2 is not None:
                    result = num1 ** num2
                    st.success(f"Result: {num1} ^ {num2} = {result}")
                else:
                     st.warning("Please ensure both numbers are entered for Power.")

            # --- Single Operand Operations ---

            elif operation == "Square":
                 if num1 is not None:
                    result = num1 ** 2
                    st.success(f"Result: Square of {num1} = {result}")
                 else:
                    st.warning("Please enter a number.")


            elif operation == "Square Root":
                 if num1 is not None:
                    if num1 < 0:
                        st.error("Error: Cannot calculate the square root of a negative number.")
                    else:
                        result = math.sqrt(num1)
                        st.success(f"Result: Square Root of {num1} = {result}")
                 else:
                    st.warning("Please enter a number.")

            elif operation == "Cube":
                if num1 is not None:
                    result = num1 ** 3
                    st.success(f"Result: Cube of {num1} = {result}")
                else:
                    st.warning("Please enter a number.")

            elif operation == "Cube Root":
                if num1 is not None:
                    # Handle negative numbers correctly for real cube roots
                    result = abs(num1) ** (1/3) * (1 if num1 >= 0 else -1)
                    st.success(f"Result: Cube Root of {num1} = {result}")
                else:
                    st.warning("Please enter a number.")

            elif operation == "Log (base 10)":
                if num1 is not None:
                    if num1 <= 0:
                        st.error("Error: Logarithm requires a positive number.")
                    else:
                        result = math.log10(num1)
                        st.success(f"Result: Log₁₀({num1}) = {result}")
                else:
                    st.warning("Please enter a number.")


            elif operation == "Natural Log (ln)":
                if num1 is not None:
                    if num1 <= 0:
                        st.error("Error: Natural Logarithm requires a positive number.")
                    else:
                        result = math.log(num1)
                        st.success(f"Result: ln({num1}) = {result}")
                else:
                    st.warning("Please enter a number.")


            elif operation == "Factorial":
                if num1 is not None:
                    # Factorial requires a non-negative integer
                    if num1 < 0 or not float(num1).is_integer():
                        st.error("Error: Factorial is only defined for non-negative integers.")
                    else:
                        result = math.factorial(int(num1))
                        st.success(f"Result: Factorial of {int(num1)} ({int(num1)}!) = {result}")
                else:
                    st.warning("Please enter a number.")


        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# lets call the function
if __name__ == "__main__":
    calculator()