-- Tabla: idioma
CREATE TABLE `idioma` (
  `id_idioma` INT NOT NULL AUTO_INCREMENT,
  `nombre_idioma` VARCHAR(50) NOT NULL,
  `familia_linguistica` VARCHAR(50),
  `nivel_dificultad_promedio` VARCHAR(20),
  `num_hablantes_estimado` BIGINT,
  `es_popular` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_idioma`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: curso_idioma
CREATE TABLE `curso_idioma` (
  `id_curso` INT NOT NULL AUTO_INCREMENT,
  `nombre_curso` VARCHAR(100) NOT NULL,
  `id_idioma` INT NOT NULL,
  `nivel_curso` VARCHAR(50),
  `duracion_semanas` INT,
  `precio` DECIMAL(10,2),
  `cupo_maximo` INT,
  `horario_clase` VARCHAR(100),
  `material_incluido` TEXT,
  `fecha_inicio_oferta` DATE,
  PRIMARY KEY (`id_curso`),
  INDEX `idx_curso_idioma` (`id_idioma`),
  CONSTRAINT `fk_curso_idioma_idioma` FOREIGN KEY (`id_idioma`) REFERENCES `idioma` (`id_idioma`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: estudiante_idioma
CREATE TABLE `estudiante_idioma` (
  `id_estudiante` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `fecha_nacimiento` DATE,
  `email` VARCHAR(100),
  `telefono` VARCHAR(20),
  `idioma_nativo` VARCHAR(50),
  `fecha_inscripcion` DATE,
  `nivel_conocimiento_idioma` VARCHAR(50),
  PRIMARY KEY (`id_estudiante`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: profesor_idioma
CREATE TABLE `profesor_idioma` (
  `id_profesor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `apellido` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100),
  `telefono` VARCHAR(20),
  `idioma_enseñanza` VARCHAR(50),
  `nivel_dominio` VARCHAR(50),
  `fecha_contratacion` DATE,
  `salario_hora` DECIMAL(5,2),
  `nacionalidad` VARCHAR(50),
  PRIMARY KEY (`id_profesor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: inscripcion_idioma
CREATE TABLE `inscripcion_idioma` (
  `id_inscripcion` INT NOT NULL AUTO_INCREMENT,
  `id_estudiante` INT NOT NULL,
  `id_curso` INT NOT NULL,
  `fecha_inscripcion` DATE,
  `estado_inscripcion` VARCHAR(50),
  `nota_final_curso` DECIMAL(4,2),
  `fecha_finalizacion` DATE,
  `id_profesor_asignado` INT,
  PRIMARY KEY (`id_inscripcion`),
  INDEX `idx_insc_estudiante` (`id_estudiante`),
  INDEX `idx_insc_curso` (`id_curso`),
  INDEX `idx_insc_profesor` (`id_profesor_asignado`),
  CONSTRAINT `fk_insc_estudiante` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante_idioma` (`id_estudiante`) ON DELETE CASCADE,
  CONSTRAINT `fk_insc_curso` FOREIGN KEY (`id_curso`) REFERENCES `curso_idioma` (`id_curso`) ON DELETE CASCADE,
  CONSTRAINT `fk_insc_profesor` FOREIGN KEY (`id_profesor_asignado`) REFERENCES `profesor_idioma` (`id_profesor`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: material_didactico
CREATE TABLE `material_didactico` (
  `id_material` INT NOT NULL AUTO_INCREMENT,
  `nombre_material` VARCHAR(255) NOT NULL,
  `tipo_material` VARCHAR(50),
  `descripcion` TEXT,
  `editorial` VARCHAR(100),
  `costo` DECIMAL(10,2),
  `id_idioma` INT,
  `nivel_asociado` VARCHAR(50),
  `fecha_publicacion` DATE,
  `es_obligatorio` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_material`),
  INDEX `idx_material_idioma` (`id_idioma`),
  CONSTRAINT `fk_material_idioma` FOREIGN KEY (`id_idioma`) REFERENCES `idioma` (`id_idioma`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: evaluacion_idioma
CREATE TABLE `evaluacion_idioma` (
  `id_evaluacion` INT NOT NULL AUTO_INCREMENT,
  `id_inscripcion` INT NOT NULL,
  `tipo_evaluacion` VARCHAR(50),
  `fecha_evaluacion` DATE,
  `puntaje_obtenido` DECIMAL(5,2),
  `ponderacion` DECIMAL(3,2),
  `comentarios_profesor` TEXT,
  `habilidades_evaluadas` TEXT,
  PRIMARY KEY (`id_evaluacion`),
  INDEX `idx_eval_inscripcion` (`id_inscripcion`),
  CONSTRAINT `fk_eval_inscripcion` FOREIGN KEY (`id_inscripcion`) REFERENCES `inscripcion_idioma` (`id_inscripcion`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

