import React, { useEffect } from "react";
import { useState } from "react";
import axios from "axios";
import YouTube from "react-youtube";
import "./App.css";

function App() {
  const API_URL = "https://api.themoviedb.org/3";
  const API_KEY = "859accd4fcb7c84d018f95056286dd9b";
  const IMAGE_PATH = "https://image.tmdb.org/t/p/original";

  // endpoint para las imagenes
  const URL_IMAGE = "https://image.tmdb.org/t/p/original";

  // variables de estado
  const [movies, setMovies] = useState([]);
  const [searchKey, setSearchKey] = useState("");
  // Agrega estos estados al comienzo de tu componente App.js
  const [favoriteMovies, setFavoriteMovies] = useState([]);
  const [isInFavorites, setIsInFavorites] = useState(false);
  //const [selectedMovie, setSelectedMovie] = useState({})
  const [trailer, setTrailer] = useState(null);
  const [movie, setMovie] = useState({ title: "Loading Movies" });
  const [playing, setPlaying] = useState(false);

  // funcion para realizar la peticion get a la api
  const fetchMovies = async (searchKey) => {
    const type = searchKey ? "search" : "discover";
    const {
      data: { results },
    } = await axios.get(`${API_URL}/${type}/movie`, {
      params: {
        api_key: API_KEY,
        query: searchKey,
      },
    });
    //console.log('data',results);
    //setSelectedMovie(results[0])

    setMovies(results);
    setMovie(results[0]);

    if (results.length) {
      await fetchMovie(results[0].id);
    }
  };

  // funcion para la peticion de un solo objeto y mostrar en reproductor de videos
  const fetchMovie = async (id) => {
    const { data } = await axios.get(`${API_URL}/movie/${id}`, {
      params: {
        api_key: API_KEY,
        append_to_response: "videos",
      },
    });

    if (data.videos && data.videos.results) {
      const trailer = data.videos.results.find(
        (vid) => vid.name === "Official Trailer"
      );
      setTrailer(trailer ? trailer : data.videos.results[0]);
    }
    //return data
    setMovie(data);
  };

  const selectMovie = async (movie) => {
    // const data = await fetchMovie(movie.id)
    // console.log(data);
    // setSelectedMovie(movie)
    fetchMovie(movie.id);

    setMovie(movie);
    window.scrollTo(0, 0);
  };

  //Función para buscar peliculas
  const searchMovies = (e) => {
    e.preventDefault();
    fetchMovies(searchKey);
  };

  // Función para agregar una película a la lista de favoritos
  const addToFavorites = () => {
    if (!isInFavorites) {
      setFavoriteMovies((prevFavorites) => [...prevFavorites, movie]);
      setIsInFavorites(true);
    }
  };

  // Función para eliminar una película de la lista de favoritos
  const removeFromFavorites = () => {
    if (isInFavorites) {
      const updatedFavorites = favoriteMovies.filter(
        (favorite) => favorite.id !== movie.id
      );
      setFavoriteMovies(updatedFavorites);
      setIsInFavorites(false);
    }
  };

  useEffect(() => {
    fetchMovies();
  }, []);

  return (
    <div className="Body">
      <div className="Head">
        <div className="logo-container">
          <img src="/img/LogoAPP.png" alt="MovieTime Logo" className="logo" />
          <h2 className="mt-0 mb-10">TimeToEnjoy</h2>
        </div>
        {/* Buscador */}
        <form className="container search-form" onSubmit={searchMovies}>
          <input
            type="text"
            placeholder="Search"
            onChange={(e) => setSearchKey(e.target.value)}
          />
          <button className="btn btn-primary" type="submit">
            Search
          </button>
        </form>
      </div>
      {/* contenedor para previsualizar  */}
      <div>
        <main>
          {movie ? (
            <div
              className="viewtrailer"
              style={{
                backgroundImage: `url("${IMAGE_PATH}${movie.backdrop_path}")`,
              }}
            >
              {playing ? (
                <>
                  <YouTube
                    videoId={trailer.key}
                    className="reproductor container"
                    containerClassName={"youtube-container amru"}
                    opts={{
                      width: "100%",
                      height: "100%",
                      playerVars: {
                        autoplay: 1,
                        controls: 0,
                        cc_load_policy: 0,
                        fs: 0,
                        iv_load_policy: 0,
                        modestbranding: 0,
                        rel: 0,
                        showinfo: 0,
                      },
                    }}
                  />
                  <button onClick={() => setPlaying(false)} className="boton">
                    Close
                  </button>
                </>
              ) : (
                <div className="container">
                  <div className="">
                    {trailer ? (
                      <>
                        <button
                          className="boton"
                          onClick={() => setPlaying(true)}
                          type="button"
                        >
                          Play Trailer
                        </button>
                        <button
                          className="boton"
                          onClick={addToFavorites}
                          type="button"
                          disabled={isInFavorites}
                        >
                          Add to Favorites
                        </button>
                        <button
                          className="boton"
                          onClick={removeFromFavorites}
                          type="button"
                          disabled={!isInFavorites}
                        >
                          Remove from Favorites
                        </button>
                      </>
                    ) : (
                      "Sorry, no trailer available"
                    )}
                    <h1 className="text-white">{movie.title}</h1>
                    <p className="text-white">{movie.overview}</p>
                  </div>
                </div>
              )}
            </div>
          ) : null}
        </main>
      </div>
      {/*Contenedor que va a mostrar posters de las peliculas actuales*/}
      <div className="Footer">
        <div className="container mt-1">
          <div className="row">
            {movies.map((movie) => (
              <div
                key={movie.id}
                className="col-md-4 mb-3"
                onClick={() => selectMovie(movie)}
              >
                <img
                  src={`${URL_IMAGE + movie.poster_path}`}
                  alt=""
                  height={600}
                  width="100%"
                />
                <h4 className="text-center">{movie.title}</h4>
              </div>
            ))}
            <div className="Favorites">
              <h2>Favorites</h2>
              <div className="row">
                {favoriteMovies.map((favorite) => (
                  <div key={favorite.id} className="col-md-4 mb-3">
                    <img
                      src={`${URL_IMAGE + favorite.poster_path}`}
                      alt=""
                      height={600}
                      width="100%"
                    />
                    <h4 className="text-center">{favorite.title}</h4>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
