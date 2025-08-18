### 📌 Human Tracking in CCTV Systems

An advanced AI-powered surveillance solution that automates the detection, recognition, and tracking of individuals across multiple CCTV feeds. This project eliminates the need for manual monitoring, significantly reducing time, cost, and human error in large-scale surveillance systems.

---

#### 🚀 Key Highlights

* **Revolutionary Tracking Algorithm** – Combines **MTCNN face detection**, **FaceNet embeddings**, and a custom **Batch-Optimized FastMTCNN** pipeline.

  * *Novel batching technique*: processes frames in groups, skipping redundant frames with little or no motion.
  * *Background subtraction optimization*: ensures computation is focused only where changes occur.
  * *Strided detection*: detects faces at intervals while preserving accuracy, achieving speed-ups without quality loss.
* **Multi-Camera Synchronization** – Automatically stitches clips from different cameras into a single, timeline-accurate video.
* **High Accuracy & Performance** – Achieves **\~90.5% accuracy** with up to **42 FPS** on GPU-powered systems.
* **Real-Time Capability** – Designed to function in near real-time, enabling scalable deployment in security systems.

---

#### 📂 Workflow(code and explaination for same is in [fast-mtcnn-detector-55-fps-at-full-resolution-new.ipynb](https://github.com/divyanshsood00/human_tracking_through_CCTV_systems/blob/main/fast-mtcnn-detector-55-fps-at-full-resolution-new.ipynb))

1. **Input**: Suspect image(s) + synchronized CCTV video feeds
2. **Preprocessing**: Frame batching + background subtraction to eliminate redundancy
3. **Face Detection (MTCNN)** → **Face Recognition (FaceNet embeddings + Cosine Similarity)**
4. **Tracking**: Frames with positive matches are extracted and aligned by timestamp
5. **Output**: A consolidated video showing the suspect’s activity across all cameras

---

#### 🛠️ Tech Stack

* **Python, OpenCV, PyTorch, NumPy, Imutils**
* **MTCNN + FaceNet** for deep learning-based face detection and recognition
* **CUDA acceleration** for high-performance GPU processing

---

#### ✅ Testing & Results

* Detects **frontal, partial (side) faces** reliably
* Handles **multiple videos, multiple faces, and complex backgrounds**
* Produces **timestamped unified video output** of the tracked individual
* **Average Accuracy:** 90.47% across test cases
* **Results can be observed in output_ files in output videos folder:** [human_tracking_through_CCTV_systems/videos-outputs/cafefirst/](https://github.com/divyanshsood00/human_tracking_through_CCTV_systems/tree/main/videos-outputs/cafefirst)

---

#### 🔮 Future Enhancements

* **Body feature-based recognition** for cases where the face is not visible
* Enhanced robustness for **low-resolution or distant CCTV footage**
* Integration with **real-time alerting systems** for security applications

---

⚡ This project demonstrates a **cutting-edge AI surveillance framework** with a *revolutionary human tracking algorithm* that blends efficiency, scalability, and high accuracy.

