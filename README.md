# OSProject
 Page Replacement Algorithm Simulator Project

Introduction
A Page Replacement Algorithm Simulator is a software tool that demonstrates different page replacement strategies used in operating systems to manage virtual memory. When a system runs out of physical memory (RAM) and needs to load new pages, it decides which page to remove using various algorithms like FIFO, LRU, and Optimal.

This project aims to simulate and compare these algorithms by providing visual feedback on page faults and memory usage.

Project Features
✅ User Inputs:

Page reference string (sequence of memory accesses).

Number of available frames (size of RAM).

✅ Algorithms Simulated:

FIFO (First-In-First-Out)

LRU (Least Recently Used)

Optimal Page Replacement

✅ Output Display:

Page Faults Count: Number of times a page replacement occurs.

Page Hits Count: Number of times a requested page is already in memory.

Memory State Visualization: Steps showing how memory changes over time.

Popup Window (Optional): Displays results using tkinter.

✅ Frontend + Backend:

Backend: Flask (Python) for algorithm execution.

Frontend: HTML, CSS, JavaScript for user interaction.

Page Replacement Algorithms Explained
🔹 FIFO (First-In-First-Out) The oldest loaded page is removed first when memory is full.

Example: Pages: 1, 2, 3, 4, 1, 5 Frames: 3 Step 1: [1]
Step 2: [1, 2]
Step 3: [1, 2, 3]
Step 4: [2, 3, 4] (1 removed, new page 4 added)
Step 5: [3, 4, 1] (2 removed, new page 1 added)
Step 6: [4, 1, 5] (3 removed, new page 5 added)
Total Page Faults: 6

🔹 LRU (Least Recently Used) Removes the least recently used page.

Example: Pages: 1, 2, 3, 4, 1, 5 Frames: 3 Step 1: [1]
Step 2: [1, 2]
Step 3: [1, 2, 3]
Step 4: [2, 3, 4] (1 removed, 4 added)
Step 5: [3, 4, 1] (2 removed, 1 added)
Step 6: [4, 1, 5] (3 removed, 5 added)
Total Page Faults: 6

🔹 Optimal Page Replacement Replaces the page that will not be used for the longest time in the future.

Example: Pages: 1, 2, 3, 4, 1, 5 Frames: 3 Step 1: [1]
Step 2: [1, 2]
Step 3: [1, 2, 3]
Step 4: [1, 2, 4] (3 removed as it's used farthest in the future)
Step 5: [1, 2, 4] (No change, 1 is already in memory)
Step 6: [1, 4, 5] (2 removed, as it's not needed in future)
Total Page Faults: 5

How to Run the Project python app.py

Expected Output

Input: Pages: 1, 2, 3, 4, 1, 5 Frames: 3

✅ Output in Flask UI: Page Faults: 6

✅ Popup Window (Tkinter):

Algorithm: FIFO Page Faults: 6 Step 1: [1] Step 2: [1, 2] Step 3: [1, 2, 3] Step 4: [2, 3, 4] Step 5: [3, 4, 1] Step 6: [4, 1, 5]

Enhancements (Future Scope)
✅ Add More Algorithms (LRU, Optimal) ✅ Graphical Visualization (Matplotlib or JS-based charts) ✅ Compare All Algorithms Side-by-Side ✅ Host on a Web Server for Public Access

Conclusion

This Page Replacement Simulator helps in understanding how different page replacement algorithms work. Using Flask for backend processing and Tkinter for popups makes it both interactive and easy to use!