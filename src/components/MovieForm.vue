<template>
  <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" v-model="title" required />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Movie Description</label>
      <textarea name="description" class="form-control" v-model="description" required></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input type="file" name="poster" class="form-control" @change="handleFileChange" required />
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>

    <!-- Display relevant messages -->
    <div v-if="message" class="alert" :class="messageClass">{{ message }}</div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Reactive form values
const title = ref('');
const description = ref('');
const poster = ref(null);
const message = ref('');
const messageClass = ref('');
const csrfToken = ref('');

// Fetch CSRF token on mount
const getCsrfToken = async () => {
  try {
    const res = await fetch('/api/v1/csrf-token');
    const data = await res.json();
    csrfToken.value = data.csrf_token;
  } catch (error) {
    console.error("Error fetching CSRF token", error);
  }
};

onMounted(() => {
  getCsrfToken();
});

// Handle file input change
const handleFileChange = (event) => {
  poster.value = event.target.files[0];
};

// Save movie handler
const saveMovie = async () => {
  if (!csrfToken.value) {
    message.value = 'CSRF Token not found.';
    messageClass.value = 'alert-danger';
    return;
  }

  const formData = new FormData();
  formData.append('title', title.value);
  formData.append('description', description.value);
  formData.append('poster', poster.value);
  formData.append('csrf_token', csrfToken.value);

  try {
    const response = await fetch("/api/v1/movies", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();

    if (data.errors) {
      message.value = 'There were some errors in your submission.';
      messageClass.value = 'alert-danger';
    } else {
      message.value = 'Movie submitted successfully!';
      messageClass.value = 'alert-success';
      title.value = '';
      description.value = '';
      poster.value = null;
    }
    console.log("Response:", data);
  } catch (error) {
    message.value = 'An error occurred while submitting the form.';
    messageClass.value = 'alert-danger';
    console.error("Error:", error);
  }
};
</script>

<style scoped>
/* Add any custom styling here */
</style>
