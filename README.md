# SignCalci

A gesture-controlled calculator and text input system powered by Convolutional Neural Networks (CNNs), enabling real-time hand gesture recognition for interactive, touch-free use.

## 🧠 Overview

**SignCalci** is an AI-driven interface that recognizes hand gestures to perform arithmetic operations and basic text input. It uses computer vision and deep learning to deliver a touch-free, high-accuracy, and intuitive interaction experience.

## ✨ Features

- **Gesture Recognition**: Real-time classification of ~35 hand gestures using CNNs  
- **Dual-Mode Operation**: Seamlessly switch between calculator and text input modes using 't' (text) and 'c' (calculator)  
- **High Accuracy**:
  - Accuracy: **97.21%**
  - Precision: **97%**
  - Recall: **98%**
- **Image Preprocessing**: Uses contour detection and hand segmentation for improved recognition  
- **Interactive UI**: Visual feedback and intuitive mode switching for a smooth experience  


## 🛠️ Tech Stack

- **Programming Language**: Python  
- **Libraries/Frameworks**: TensorFlow, OpenCV, NumPy, Matplotlib, Scikit-learn  
- **Model Architecture**: CNN-based classifier for gesture recognition  

## 🚀 How to Use

1. **Clone the repository**
2. **Install the required packages**
3. **Set up the hand histogram:**
   - Run: `python set_hand_hist.py`
   - Keep your hand in the green box and press **'c'**
   - A threshold window will appear—if you're satisfied with the result, press **'s'** to save  
4. **Run the main application**:  
   `python final.py`  
5. **Switch between modes:**
   - Press **'t'** for text mode  
   - Press **'c'** for calculator mode  
6. **Gesture Flow (Calculator Mode):**
   - Show number gesture  
   - Show **'yo'** gesture to proceed  
   - Show operator gesture  
   - Show **'yo'** again  
   - Show second number  
   - Show **'yo'** once more to compute the result  


## 🔮 Future Improvements

- Improve robustness under varying lighting conditions and complex backgrounds  
- Add voice synthesis for enhanced accessibility  
- Integrate into mobile and web platforms using WebRTC or MediaPipe  
