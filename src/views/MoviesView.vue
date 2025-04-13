<template>
  <div class="movies-view">
    <h2>Movies</h2>
    <div class="movie-cards">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img :src="movie.poster" alt="Movie Poster" class="movie-poster" />
        <h3>{{ movie.title }}</h3>
        <p>{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

// Define a reactive property for movies
const movies = ref([]);

// Fetch movies from the Flask API
const fetchMovies = async () => {
  try {
    const response = await fetch('/api/v1/movies');
    const data = await response.json();
    movies.value = data.movies;
  } catch (error) {
    console.error("Error fetching movies:", error);
  }
};

// Fetch movies when the component is mounted
onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movie-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.movie-card {
  background: #fff;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  width: 200px;
  text-align: center;
}

.movie-poster {
  width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: cover;
}
</style>
