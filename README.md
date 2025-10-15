## Repository for UAS Software Workshops, 2024-25.

### OpenCV:
- [Slides](https://docs.google.com/presentation/d/1rRTdnsBlnlugy5WanG4pukfRyN5jigxrdw0NAoYvZUs/edit#slide=id.p)
- [Recording](https://youtu.be/JcP3he21kAE)
- Project Tips:
  - You will definitely need to use contours,  color thresholding, and moments in your solution. Think about which order would be the most efficient.
  - If you used the color picker linked in slides, you would have noticed that in some images, the red hue is between 0-5 and in other images it is between 165-180. Each of these will need their own mask, but think about how you can use cv2.bitwise_or to combine the masks together
  - The saturation of the circle is higher than most of the other pixels in the image
  - Use np.shape(img)[1] to get the width of the image and np.shape(img)[0] to get the height. Remember that the shape of images is (height, width, # color channels) 

### Backend:
- [Slides](https://docs.google.com/presentation/d/1OuPDO9HHB0dZZ1Xfp9SHHYkY4qCGsCT3IC1jJ2O3wQ4/edit?usp=sharing)
- [Recording](https://www.youtube.com/watch?v=VbYiPv7hhZY)
- "Part 1" is [here](https://www.youtube.com/watch?v=J3tFKgVANps), but there were technical issues and basically all of this is covered in Part 2, so it's not needed.
- Running Flask in Google Colab (for those of you with installation issues)
  - [Video](https://youtu.be/WYS7nT_k6dE)
  - [Starter code for the project inside Colab](https://colab.research.google.com/drive/1ZdCUKD2MEipYxRyHdr4HteHzPgB3TESc?usp=sharing) (as opposed to just running it on your local machine)

### MAVSDK
- [Slides](https://docs.google.com/presentation/d/1cOrgiwGQyhu9IgvpCgisfMDgG0T6Wg0PCy-ZPfJdk8E/edit#slide=id.g311f17c0440_2_2)
- [Recording](https://youtu.be/nNokr18Qa54)

### Future workshops:
- Neural Networks with Pytorch
- Docker + Unit Testing + CI

---

Kahoot questions covering OpenCV and Backend [here](https://docs.google.com/document/d/1ffZ_ti_7WKDjJW8zYtqnVGwkkNS-Rlc51RRtuBZTw8s/edit?usp=sharing).
