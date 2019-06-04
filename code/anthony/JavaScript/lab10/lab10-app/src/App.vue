<template>
  <v-app dark>
    <v-toolbar app height="100">
      <v-layout justify-center>
        <v-flex lg8>
          <form @submit.prevent="searchAPI" @click:append="searchAPI">
            <v-text-field append-icon="search" v-model="searchTerm" label="Search..." outline></v-text-field>
          </form>
        </v-flex>
      </v-layout>
    </v-toolbar>
    <v-container>
      <v-card>
        <v-card-title v-if="!loaded" class="display-1 text-xs-center">Use the search to get started</v-card-title>
      </v-card>
    </v-container>
    <v-container>
      <v-layout row wrap justify-start>
        <v-flex xs12 sm6 md4 lg3 v-for="movie in movieList" :key="movie.imdbID">
          <v-card class="ma-2">
            <v-card-title primary-title class="pb-0 headline font-weight-medium">{{movie.Title}}</v-card-title>
            <v-card-title class="caption pt-0">{{movie.Year}}</v-card-title>
            <v-img :src="movie.Poster"></v-img>
            <v-card-actions>
              <v-dialog max-width="600px">
                <v-btn flat slot="activator" @click="getInfo(movie)" class="green">More Info</v-btn>
                <v-card>
                  <v-card-title class="display-1">{{title}}</v-card-title>
                  <v-card-text>
                    <v-list>
                      <v-list-tile>Year: {{year}}</v-list-tile>
                      <v-list-tile>Rated: {{rated}}</v-list-tile>
                      <v-list-tile>Released: {{released}}</v-list-tile>
                      <v-list-tile>Runtime: {{runtime}}</v-list-tile>
                      <v-list-tile>Genre: {{genre}}</v-list-tile>
                      <v-list-tile>Director: {{director}}</v-list-tile>
                      <v-list-tile>Actors: {{actors}}</v-list-tile>
                      <v-list-tile>Plot: {{plot}}</v-list-tile>
                      <v-list-tile>Rotten Tomatoes: {{rottenRating}}</v-list-tile>
                      <v-list-tile>Metacritic: {{metaRating}}</v-list-tile>
                      <v-list-tile>imdbRating: {{imdbRating}}</v-list-tile>
                      <v-list-tile>imdbID: {{id}}</v-list-tile>
                    </v-list>
                  </v-card-text>
                  <v-card-actions>
                    <v-btn flat class="green" @click="travel(movie)">View on imdb</v-btn>
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>

<script>
const apiURL = "http://www.omdbapi.com/?apikey=bcd005c0";
export default {
  name: "App",
  data() {
    return {
      loaded: false,
      searchTerm: "",
      movieList: [],
      title: "",
      year: "",
      rated: "",
      released: "",
      runtime: "",
      genre: "",
      director: "",
      actors: "",
      plot: "",
      type: "",
      rottenRating: "",
      metaRating: "",
      imdbRating: "",
      id: ""
    };
  },
  methods: {
    searchAPI() {
      let url = `${apiURL}&s=${this.searchTerm}`;
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.movieList = data.Search;
          this.loaded = true;
        });
    },
    getInfo(movie) {
      let url = `${apiURL}&i=${movie.imdbID}`;
      fetch(url)
        .then(response => response.json())
        .then(data => {
          this.title = data.Title;
          this.year = data.Year;
          this.rated = data.Rated;
          this.released = data.Released;
          this.runtime = data.Runtime;
          this.genre = data.Genre;
          this.director = data.Director;
          this.actor = data.Actors;
          this.plot = data.Plot;
          this.type = data.Type;
          this.rottenRating = data.Ratings[1].Value;
          this.metaRating = data.Ratings[2].Value;
          this.imdbRating = data.indbRating;
          this.id = data.imdbID;
        });
    },
    travel(movie) {
      window.open(`https://www.imdb.com/title/${movie.imdbID}`);
    }
  }
};
</script>
<style scoped>
form {
  width: 100%;
}
.container {
  margin-top: 6em;
}
v-card {
  margin: 3em;
}
li {
  text-decoration: none;
}
</style>
