# Estructura de Datos para una App de Recomendación de Películas

# Película
pelicula = {
    'id': 1, 
    'titulo': 'Aventuras en la Ciudad Perdida', 
    'descripción': 'Una emocionante búsqueda en busca de tesoros perdidos.', 
    'poster': 'aventuras_ciudad_perdida.jpg', 
    'trailer': 'youtube.com/aventuras_ciudad_perdida',

    'id': 2, 
    'titulo': 'El Secreto del Bosque Encantado', 
    'descripción': 'Un misterioso bosque guarda secretos que cambiarán el destino.', 
    'poster': 'secreto_bosque_encantado.jpg', 
    'trailer': 'youtube.com/secreto_bosque_encantado',

    'id': 3, 
    'titulo': 'Amor en París', 
    'descripción': 'Una romántica comedia ambientada en las calles de la Ciudad de la Luz.', 
    'poster': 'amor_en_paris.jpg', 
    'trailer': 'youtube.com/amor_en_paris',

    'id': 30, 
    'titulo': 'Amanecer en el Desierto', 
    'descripción': 'Una historia de supervivencia en el desierto donde la esperanza nunca muere.', 
    'poster': 'amanecer_desierto.jpg', 
    'trailer': 'youtube.com/amanecer_desierto',

    'id': 31, 
    'titulo': 'El Misterio del Reloj Perdido', 
    'descripción': 'Una emocionante trama de detectives que involucra un reloj antiguo y oscuros secretos.', 
    'poster': 'misterio_reloj_perdido.jpg', 
    'trailer': 'youtube.com/misterio_reloj_perdido',

    'id': 32, 
    'titulo': 'El Último Viaje Espacial', 
    'descripción': 'Un grupo de astronautas se embarca en una misión épica hacia los confines del universo.',
    'poster': 'ultimo_viaje_espacial.jpg', 
    'trailer': 'youtube.com/ultimo_viaje_espacial',

    'id': 33, 'titulo': 'Canción de Amor Prohibido', 
    'descripción': 'Una historia de amor épica entre dos almas destinadas a estar juntas en contra de todas las probabilidades.', 
    'poster': 'cancion_amor_prohibido.jpg', 
    'trailer': 'youtube.com/cancion_amor_prohibido',

    'id': 40, 
    'titulo': 'Intriga en el Pasillo 13', 
    'descripción': 'Un thriller lleno de suspense que tiene lugar en un oscuro pasillo de un edificio misterioso.', 
    'poster': 'intriga_pasillo_13.jpg', 
    'trailer': 'youtube.com/intriga_pasillo_13',

    'id': 41, 
    'titulo': 'El Enigma del Espejo Mágico', 
    'descripción': 'Un espejo mágico revela secretos ocultos y transporta a los protagonistas a mundos inexplorados.', 
    'poster': 'enigma_espejo_magico.jpg', 
    'trailer': 'youtube.com/enigma_espejo_magico',
    
    'id': 42, 
    'titulo': 'La Leyenda del Unicornio Dorado', 
    'descripción': 'Una aventura fantástica en la que un grupo de héroes busca el mítico unicornio dorado para salvar su reino.', 
    'poster': 'leyenda_unicornio_dorado.jpg', 
    'trailer': 'youtube.com/leyenda_unicornio_dorado',
    
    'id': 43, 
    'titulo': 'El Tango del Crepúsculo', 
    'descripción': 'En la mística Buenos Aires, un bailarín de tango descubre un secreto ancestral mientras persigue su pasión.', 
    'poster': 'tango_crepusculo.jpg', 
    'trailer': 'youtube.com/tango_crepusculo',
    
    'id': 44, 
    'titulo': 'Odisea Submarina', 
    'descripción': 'Exploradores submarinos se aventuran en las profundidades del océano para descubrir criaturas asombrosas y antiguos tesoros.', 
    'poster': 'odisea_submarina.jpg', 
    'trailer': 'youtube.com/odisea_submarina',
    
    'id': 45, 
    'titulo': 'El Jardín de los Sueños', 
    'descripción': 'Un mágico jardín esconde secretos que cambiarán la vida de quienes se atrevan a entrar.', 
    'poster': 'jardin_suenos.jpg', 
    'trailer': 'youtube.com/jardin_suenos',

    'id': 46, 
    'titulo': 'El Misterio de la Estrella Perdida', 
    'descripción': 'Un grupo de astrónomos amateurs descubre una estrella perdida con propiedades sorprendentes.', 
    'poster': 'misterio_estrella_perdida.jpg', 
    'trailer': 'youtube.com/misterio_estrella_perdida',
    
    'id': 47, 
    'titulo': 'El Último Baile de las Sombras', 
    'descripción': 'En una noche mágica, las sombras cobran vida y danzan en un espectáculo único y emocionante.', 
    'poster': 'ultimo_baile_sombras.jpg', 
    'trailer': 'youtube.com/ultimo_baile_sombras',
    
    'id': 48, 
    'titulo': 'El Laberinto de los Recuerdos', 
    'descripción': 'Un viaje psicológico a través de un laberinto surrealista donde los recuerdos se entrelazan de manera inesperada.', 
    'poster': 'laberinto_recuerdos.jpg', 
    'trailer': 'youtube.com/laberinto_recuerdos',
    
    'id': 49, 
    'titulo': 'El Elixir de la Eterna Juventud', 
    'descripción': 'Una búsqueda épica en busca de un elixir mágico que concede la eterna juventud, pero a un precio muy alto.', 
    'poster': 'elixir_eterna_juventud.jpg', 
    'trailer': 'youtube.com/elixir_eterna_juventud',
    
    'id': 50, 
    'titulo': 'Cielo Estrellado sobre Montañas', 
    'descripción': 'Una historia conmovedora de amor y pérdida ambientada en las majestuosas montañas, donde los cielos estrellados guardan secretos.', 
    'poster': 'cielo_estrellado_montanas.jpg', 
    'trailer': 'youtube.com/cielo_estrellado_montanas',
}

# Actividad del Usuario
actividad_usuario = {
    'usuario_id': 1,
    'tipo': 'favorita',
    'pelicula_id': 10,

    'usuario_id': 2,
    'tipo': 'favorita',
    'pelicula_id': 30,
}

# Lista de Reproducción
lista_reproduccion = {
    'id': 201,
    'nombre': 'Lista de Mis Favoritas',
    'usuario_id': 1,
    'peliculas': [10, 43, 50],

    'id': 214,
    'nombre': 'Lista de Mis Favoritas',
    'usuario_id': 2,
    'peliculas': [11, 33, 13],
}

# Base de Datos
base_datos = {
    'peliculas': {10: pelicula, 
                  43: pelicula,},
    'actividades': [actividad_usuario, 
                    actividad_usuario,],
    'listas_reproduccion': {201: lista_reproduccion, 
                            214: lista_reproduccion,},
}