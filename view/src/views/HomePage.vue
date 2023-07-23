<template>
  <div>
    <CarouselHomePage :images="images"></CarouselHomePage>
    <div>
      <div>
        <MovieRow title="Top Movies" :movies="topMovies" />
      </div>
      <MovieRow title="Other Movies" :movies="otherMovies" />
    </div>
  </div>
</template>

<script>
import MovieRow from '@/components/MovieRow.vue';
import CarouselHomePage from '@/components/HomePage/CarouselHomePage.vue';
import { mapState } from 'vuex';

export default {
  components: {
    MovieRow,
    CarouselHomePage,
  },
  computed: {
    ...mapState(['Allmovies']),
    topMovies() {
      const allMovies = this.Allmovies;
      return allMovies ? allMovies.filter((movie) => movie.rating >= 8) : [];
    },
    otherMovies() {
      const allMovies = this.Allmovies;
      return allMovies ? allMovies.filter((movie) => movie.rating < 8) : [];
    },
  },
  data() {
    return {
      images: [
        {
          id: 0,
          src: 'https://assets-in.bmscdn.com/promotions/cms/creatives/1687328911358_webbannernpa.jpg',
        },
        {
          id: 1,
          src: 'https://assets-in.bmscdn.com/promotions/cms/creatives/1689834634562_sunburngoadesktop.jpg',
        },
        {
          id: 2,
          src: 'https://assets-in.bmscdn.com/promotions/cms/creatives/1689317595041_gauravguptaliivedesktop.jpg',
        },
        {
          id: 3,
          src: 'https://assets-in.bmscdn.com/promotions/cms/creatives/1688970894022_bigweb.jpg',
        },
      ],
    };
  },
  mounted() {
    this.$store.dispatch('fetchAllMovie');
  },
};
</script>
