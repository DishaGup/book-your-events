<template>
  <div class="carousel">
   
    <div v-if="images.length" class="carousel-box">
      <button class="arrow-prev" @click="prevImage"><i class="fas fa-chevron-left"></i></button>
      <div class="slide">
      
        <img :src="currentImage.src" alt="Image">
     
      </div>
      <div class="controls">
        <ul class="dots">
          <li v-for="(image, index) in images" :key="image.id" :class="{ active: index === currentIndex }"
            @click="goToImage(index)"></li>
        </ul>
      </div>
      <button class="arrow-next" @click="nextImage"><i class="fas fa-chevron-right"></i></button>
    </div>
    <div v-else>
      <p>No images found.</p>
    </div>
 
  </div>
</template>

<script>
export default {
  props: {
    images: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      currentIndex: 0,
    };
  },
  computed: {
    currentImage() {
      if (this.images.length > 0) {
        return this.images[this.currentIndex];
      } else {
        return null;
      }
    },
  },
  methods: {
    prevImage() {
      this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    },
    nextImage() {
      this.currentIndex = (this.currentIndex + 1) % this.images.length;
    },
    goToImage(index) {
      this.currentIndex = index;
    },
    startSlideshow() {
      setInterval(() => {
        this.nextImage();
      }, 2000);
    },
  },
  mounted() {
    // Start the slideshow when the component is mounted
    this.startSlideshow();
  },
};
</script>

<style>
/* Your styles here */

.carousel {
  width: 100%;
  height: 300px;
  margin: 0 auto;
  position: relative;
  /* overflow: hidden; */
}

.slide {
  width: 100%;
  height: 100%;
  transition: transform 0.5s ease;
}

.fas ,.fa-chevron-left,.fa-chevron-right{
  color: black;
  background-color: black;
}
img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.controls {
  margin-top: 10px;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 10px;
  display: flex;
  justify-content: center;
}

.arrow {
  background-color: #ccc;
  border: 1px solid #bbb;
  padding: 10px;
  cursor: pointer;
  color: #555;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.arrow:hover {
  background-color: #bbb;
}

.arrow-prev{
  position: absolute;
  left:2;
  font-size: 24px;
  size: 24px;
  /* background: 0 0; */
  outline: 0 0; 
}


.arrow-next{
  position: absolute;
  right:2;
  /* background: 0 0; */
  outline: 0 0;
}



.dots {
  display: flex;
  align-items: center;
  position: absolute;
  bottom: 5px;
  left: 50%;
  transform: translateX(-50%);
}

.dots li {
  width: 12px;
  height: 12px;
  background-color: #bbb;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
}

.dots li.active {
  background-color: #555;
}
</style>
