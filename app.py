import cv2
import streamlit as st


def main():
    st.title("Webcam Picture Capture")

    # Initialize the webcam

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        st.error("Error: Could not open webcam.")

        return

    # Add a button to capture a picture

    if st.button("Capture Picture"):
        ret, frame = cap.read()

        if ret:
            # Display the captured image

            st.image(frame, channels="BGR")

            # Save the image to a file

            file_name = "captured_picture.jpg"

            cv2.imwrite(file_name, frame)

            st.success(f"Picture saved as {file_name}")

        else:
            st.warning("Could not capture a picture.")

    # Release the webcam when the app is closed

    cap.release()


if __name__ == "__main__":
    main()
