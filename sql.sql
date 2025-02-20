create table Rol(
    id_rol serial primary key not null,
    nombre_rol varchar(50) check (nombre_rol in ('aprendiz', 'pasante', 'instructor')),
    fecha_creacion date
);

create table usuarios(
    identificacion bigint primary key not null unique,
    nombre varchar(50),
    contrasena varchar(50),
    email varchar(50),
    fk_id_rol int,
    foreign key (fk_id_rol) references Rol(id_rol)
);

create table herramientas(
    id_herramienta serial primary key not null,
    nombre_h varchar(50),
    fecha_prestamo date,
    estado varchar(50)
);

create table insumos(
    id_insumo serial primary key not null,
    nombre varchar(50),
    tipo varchar(50),
    precio_unidad int,
    cantidad int,
    unidad_medida varchar(50)
);


create table actividad(
    id_actividad serial primary key not null,
    nombre_actividad varchar(50),
    descripcion text
);

create table calendario_lunar(
    id_calendario_lunar serial primary key not null,
    fecha date,
    descripcion_evento text,
    evento varchar(50)
);

create table asignacion_actividad(
    id_asignacion_actividad serial primary key not null,
    fecha date,
    fk_id_actividad int,
    foreign key (fk_id_actividad) references actividad(id_actividad),
    fk_identificacion int,
    foreign key (fk_identificacion) references usuarios(identificacion)
);

create table programacion(
    id_programacion serial primary key not null,
    estado varchar(50),
    fecha_programada date,
    duracion int,
    fk_id_asignacion_actividad int,
    foreign key (fk_id_asignacion_actividad) references asignacion_actividad(id_asignacion_actividad),
    fk_id_calendario_lunar int,
    foreign key (fk_id_calendario_lunar) references calendario_lunar(id_calendario_lunar)
);

create table notificacion(
    id_notificacion serial primary key not null,
    titulo varchar(50),
    mensaje varchar(50),
    fk_id_programacion int,
    foreign key (fk_id_programacion) references programacion(id_programacion)
);

create table requiere(
    id_requiere serial primary key not null,
    fk_id_herramienta int,
    foreign key (fk_id_herramienta) references herramientas(id_herramienta),
    fk_id_asignacion_actividad int,
    foreign key (fk_id_asignacion_actividad) references asignacion_actividad(id_asignacion_actividad)
);

create table utiliza(
    id_utiliza serial primary key not null,
    fk_id_insumo int,
    foreign key (fk_id_insumo) references insumos(id_insumo),
    fk_id_asignacion_actividad int,
    foreign key (fk_id_asignacion_actividad) references asignacion_actividad(id_asignacion_actividad)
);

create table PEA(
    id_pea serial primary key not null,
    nombre varchar(50),
    descripcion text
);

create table ubicacion (
    id_ubicacion serial primary key,
    latitud decimal(9,6),  -- Mejor tipo para coordenadas geográficas
    longitud decimal(9,6)
);

create table lote (
    id_lote serial primary key,
    dimension int,
    nombre_lote varchar(50),
    fk_id_ubicacion int,
    constraint ubicacion_lote foreign key (fk_id_ubicacion) references ubicacion(id_ubicacion),
    estado varchar(50)
);

create table eras (
    id_eras serial primary key,
    descripcion varchar(50),
    fk_id_lote int,
    constraint lote_era foreign key (fk_id_lote) references lote(id_lote)
);

create table tipo_cultivo (
    id_tipo_cultivo serial primary key,
    nombre varchar(50),
    descripcion text
);

create table especie (
    id_especie serial primary key,
    nombre_comun varchar(50),
    nombre_cientifico varchar(50),
    descripcion text,
    fk_id_tipo_cultivo int,
    constraint tipo_especie foreign key (fk_id_tipo_cultivo) references tipo_cultivo(id_tipo_cultivo)
);

create table semilleros(
    id_semillero serial primary key,
    nombre_semilla varchar(50),
    fecha_siembra date,
    fecha_estimada date,
    cantidad int
);

create table cultivo (
    id_cultivo serial primary key,
    fecha_plantacion date not null,
    nombre_cultivo varchar(50),
    descripcion text,
    fk_id_especie int,
    constraint especie_cultivo foreign key (fk_id_especie) references especie(id_especie),
    fk_id_semillero int,
    constraint semillero_cultivo foreign key (fk_id_semillero) references semilleros(id_semillero)
);

create table realiza(
    id_realiza serial primary key,
    fk_id_cultivo int,
    foreign key (fk_id_cultivo) references cultivo(id_cultivo),
    fk_id_actividad int,
    constraint actividad_realiza foreign key (fk_id_actividad) references actividad(id_actividad)
);

create table plantacion(
    id_plantacion serial primary key,
    fk_id_cultivo int,
    foreign key (fk_id_cultivo) references cultivo(id_cultivo),
    fk_id_era int,
    constraint era_plantacion foreign key (fk_id_era) references eras(id_eras)
);

create table desarrollan (
    id_desarrollan serial primary key,
    fk_id_cultivo int,
    foreign key (fk_id_cultivo) references cultivo(id_cultivo),
    fk_id_pea int,
    constraint pea_desarrollan foreign key (fk_id_pea) references PEA(id_pea)
);

-- Creación de la tabla Producción
CREATE TABLE produccion (
    id_produccion SERIAL PRIMARY KEY,
    cantidad_produccion DECIMAL(20,10) NULL,
    fecha DATE NOT NULL
);

-- Creación de la tabla Cultivo


-- Creación de la tabla Genera
CREATE TABLE genera (
    id_genera SERIAL PRIMARY KEY,
    fk_id_cultivo INT NULL,
    fk_id_produccion INT NULL,
    FOREIGN KEY (fk_id_cultivo) REFERENCES Cultivo(id_cultivo) ON DELETE SET NULL,
    FOREIGN KEY (fk_id_produccion) REFERENCES Produccion(id_produccion) ON DELETE SET NULL
);

-- Creación de la tabla Venta
CREATE TABLE venta (
    id_venta SERIAL PRIMARY KEY,
    precio_unidad DECIMAL(10,2) NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    fk_id_produccion INT NULL,
    FOREIGN KEY (fk_id_produccion) REFERENCES Produccion(id_produccion) ON DELETE SET NULL
);

create table sensores(
    id_sensor serial primary key not null,
    nombre_sensor varchar(50),
    tipo_sensor varchar(50),
    unidad_medida varchar(50),
    descripcion text,
    medida_minima float,
    medida_maxima float
);

create table mide (
    id_mide serial primary key not null,
    fk_id_sensor int,
    foreign key (fk_id_sensor) references sensores(id_sensor),
    fk_id_era int,
    constraint era_mide foreign key (fk_id_era) references eras(id_eras)
);

create table tipo_residuos(
    id_tipo_residuo serial primary key,
    nombre_residuo varchar(50),
    descripcion text
);

create table residuos(
    id_residuo serial primary key,
    nombre varchar(50),
    fecha date,
    descripcion text,
    fk_id_tipo_residuo int,
    constraint tipo_residuo_residuo foreign key (fk_id_tipo_residuo) references tipo_residuos(id_tipo_residuo),
    fk_id_cultivo int,
    constraint cultivo_residuo foreign key (fk_id_cultivo) references cultivo(id_cultivo)
);

create table control_fitosanitario(
    id_control_fitosanitario serial primary key,
    fecha_control date,
    descripcion text,
    fk_id_desarrollan int,
    constraint desarrollan_control_fitosanitario foreign key (fk_id_desarrollan) references desarrollan(id_desarrollan)
);

create table control_usa_insumo(
    id_control_usa_insumo serial primary key,
    fk_id_insumo int,
    foreign key (fk_id_insumo) references insumos(id_insumo),
    fk_id_control_fitosanitario int,
    constraint control_fitosanitario_usa_insumo foreign key (fk_id_control_fitosanitario) references control_fitosanitario(id_control_fitosanitario),
    cantidad int
);