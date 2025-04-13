import cv2
import streamlit as st
from datetime import datetime
import os
import time

# Create absolute path for saved images
SAVE_DIR = os.path.abspath('saved_faces')
os.makedirs(SAVE_DIR, exist_ok=True)

# Initialize face cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def detect_faces(scale_factor, min_neighbors, rect_color):
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    message_placeholder = st.empty()
    
    # Initialize snapshot counter in session state
    if 'snapshot_counter' not in st.session_state:
        st.session_state.snapshot_counter = 0
    
    while cap.isOpened() and not st.session_state.stop_detection:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera error")
            break
            
        # Face detection and drawing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=scale_factor,
            minNeighbors=min_neighbors,
            minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), rect_color, 2)
        
        # Display frame
        frame_placeholder.image(frame, channels="BGR")
        
      # Handle snapshot requests
        if st.session_state.take_snapshot:
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filename = os.path.join(SAVE_DIR, f"face_{timestamp}.jpg")
                cv2.imwrite(filename, frame)
                
                # Show success message
                with message_placeholder:
                    st.success("✅ Snapshot saved successfully!")
                
            except Exception as e:
                with message_placeholder:
                    st.error(f"❌ Error: {str(e)}")
            finally:
                st.session_state.take_snapshot = False
                time.sleep(2)  # Show message for 2 seconds
                message_placeholder.empty()
        
        time.sleep(0.01)  # Allow UI updates
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    st.title("Face Detection App")
    
    # Initialize session state
    st.session_state.setdefault('take_snapshot', False)
    st.session_state.setdefault('stop_detection', False)
    st.session_state.setdefault('snapshot_counter', 0)

    # Instructions
    with st.expander("Instructions"):
        st.markdown("""
        1. Click **Start Detection**
        2. Adjust parameters below
        3. Click buttons to control
        """)
    
    # Control panel
    with st.sidebar:
        st.header("Controls")
        
        # Color picker
        color_hex = st.color_picker("Rectangle Color", "#00FF00")
        rect_color = tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))[::-1]
        
        # Detection parameters
        scale_factor = st.slider("Scale Factor", 1.01, 1.5, 1.1, 0.01)
        min_neighbors = st.slider("Min Neighbors", 1, 10, 5)
        
        # Buttons
        if st.button("📸 Save Snapshot") and not st.session_state.stop_detection:
            st.session_state.take_snapshot = True
            
        if st.button("🛑 Stop Detection"):
            st.session_state.stop_detection = True
            
        st.write(f"Snapshots will be saved to: `{SAVE_DIR}`")
    
    # Start detection
    if st.button("🚀 Start Detection"):
        st.session_state.stop_detection = False
        detect_faces(scale_factor, min_neighbors, rect_color)

if __name__ == "__main__":
    main()