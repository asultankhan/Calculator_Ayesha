import streamlit as st

def main():
    st.set_page_config(page_title="Simple Calculator", page_icon="🧮")
    st.title("🧮 Simple Calculator (Streamlit)")
    st.write("Enter two numbers and choose an operation.")

    # Number inputs
    num1 = st.number_input("First Number", value=0.0, format="%.4f")
    num2 = st.number_input("Second Number", value=0.0, format="%.4f")

    # Operation
    operation = st.selectbox(
        "Select Operation",
        ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
    )

    result = None
    error_msg = ""

    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
            elif operation == "Subtraction (-)":
                result = num1 - num2
            elif operation == "Multiplication (×)":
                result = num1 * num2
            elif operation == "Division (÷)":
                if num2 == 0:
                    error_msg = "Error: Division by zero is not allowed."
                else:
                    result = num1 / num2
        except Exception as e:
            error_msg = f"An error occurred: {e}"

    # Show output
    if error_msg:
        st.error(error_msg)
    elif result is not None:
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()
