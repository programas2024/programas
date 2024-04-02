-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-04-2024 a las 18:31:51
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `financiera`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `cedula` varchar(255) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `fecha_hora_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `cedula`, `nombre`, `apellidos`, `telefono`, `email`, `fecha_hora_registro`) VALUES
(1, '29814610', 'flor', 'amariles', '3207308939', 'jotac.2853@gmail.com', '2024-04-01 15:06:01'),
(3, '112233', 'pedro', 'ordonez', '321789456', 'pedro@gamil.com', '2024-04-01 17:00:57'),
(4, '44556677', 'luisa', 'moreno', '32678906', 'luisa@gamil.com', '2024-04-01 17:01:50');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultascuentas`
--

CREATE TABLE `consultascuentas` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `tiempo_transcurrido` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `consultascuentas`
--

INSERT INTO `consultascuentas` (`id`, `numero_cuenta`, `tiempo_transcurrido`) VALUES
(1, '', 5),
(2, '4333797211', 0),
(3, '4333797211', 0),
(4, '4333797211', 0),
(5, '4333797211', 0),
(6, NULL, 0),
(8, '4333797211', 22),
(9, '4333797211', 34),
(10, '4333797211', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta`
--

CREATE TABLE `cuenta` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `saldo` decimal(10,2) DEFAULT NULL,
  `cedula_cliente` varchar(255) DEFAULT NULL,
  `fecha_hora_creacion` datetime DEFAULT NULL,
  `momento_creacion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cuenta`
--

INSERT INTO `cuenta` (`id`, `numero_cuenta`, `saldo`, `cedula_cliente`, `fecha_hora_creacion`, `momento_creacion`) VALUES
(1, '4333797211', 280000.00, '29814610', '2024-04-01 15:10:33', 'de día'),
(2, '9531543133', 45000.00, '112233', '2024-04-01 17:02:16', 'de día'),
(3, '1651968205', 35000.00, '44556677', '2024-04-01 17:02:40', 'de día');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `deposito`
--

CREATE TABLE `deposito` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `numero_transaccion` varchar(255) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `deposito`
--

INSERT INTO `deposito` (`id`, `numero_cuenta`, `monto`, `numero_transaccion`, `fecha_hora`) VALUES
(1, '4333797211', 100000.00, '653185', '2024-04-01 15:11:48'),
(2, '1651968205', 10000.00, '934555', '2024-04-01 17:04:16'),
(3, '9531543133', 45000.00, '673206645729', '2024-04-01 17:04:45');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generar`
--

CREATE TABLE `generar` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `cedula_cliente` varchar(255) DEFAULT NULL,
  `saldo` decimal(10,2) DEFAULT NULL,
  `depositos` text DEFAULT NULL,
  `retiros` text DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `generar`
--

INSERT INTO `generar` (`id`, `numero_cuenta`, `cedula_cliente`, `saldo`, `depositos`, `retiros`, `fecha`) VALUES
(1, '1', '4333797211', 280000.00, '', '', '2024-04-01 20:50:25'),
(2, '1', '4333797211', 280000.00, '', '', '2024-04-01 20:52:58'),
(3, '1', '4333797211', 280000.00, '', '', '2024-04-01 20:54:42'),
(4, '1', '4333797211', 280000.00, '', '', '2024-04-01 20:58:28'),
(5, '1', '4333797211', 280000.00, '', '', '2024-04-01 20:58:31'),
(6, '1', '4333797211', 280000.00, '', '', '2024-04-01 21:00:52'),
(7, '1', '4333797211', 280000.00, '', '', '2024-04-01 21:00:59'),
(8, '1', '4333797211', 280000.00, '', '', '2024-04-01 21:02:44'),
(9, '1', '4333797211', 280000.00, '', NULL, '2024-04-01 21:08:11'),
(10, '1', '4333797211', 280000.00, '', NULL, '2024-04-01 21:08:16'),
(11, '1', '4333797211', 280000.00, '', NULL, '2024-04-01 21:08:16'),
(12, '1', '4333797211', 280000.00, '', NULL, '2024-04-01 21:08:17'),
(13, '1', '4333797211', 280000.00, '', NULL, '2024-04-01 21:08:17'),
(14, '1', '4333797211', 280000.00, '', NULL, '2024-04-01 21:10:18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellidos` varchar(255) DEFAULT NULL,
  `pais` varchar(100) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `usuario` varchar(100) DEFAULT NULL,
  `contrasena` varchar(255) DEFAULT NULL,
  `fecha_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registros`
--

INSERT INTO `registros` (`id`, `nombre`, `apellidos`, `pais`, `correo`, `usuario`, `contrasena`, `fecha_registro`) VALUES
(1, 'florecita', 'amariles', 'Colombia', 'jotac.2853@gmail.com', 'flor17', 'G=RmAwOg0X', '2024-04-01 15:20:28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `retiro`
--

CREATE TABLE `retiro` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `retiros`
--

CREATE TABLE `retiros` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `monto` decimal(10,2) DEFAULT NULL,
  `numero_transaccion` varchar(255) DEFAULT NULL,
  `fecha_hora` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `retiros`
--

INSERT INTO `retiros` (`id`, `numero_cuenta`, `monto`, `numero_transaccion`, `fecha_hora`) VALUES
(1, '4333797211', 20000.00, '456715', '2024-04-01 15:12:38'),
(2, '1651968205', 25000.00, '469493', '2024-04-01 17:05:24'),
(3, '9531543133', 20000.00, '875646107597', '2024-04-01 17:05:57');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `saldos`
--

CREATE TABLE `saldos` (
  `id` int(11) NOT NULL,
  `numero_cuenta` varchar(255) DEFAULT NULL,
  `cedula_cliente` varchar(255) DEFAULT NULL,
  `saldo` decimal(10,2) DEFAULT NULL,
  `tiempo_transcurrido` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `saldos`
--

INSERT INTO `saldos` (`id`, `numero_cuenta`, `cedula_cliente`, `saldo`, `tiempo_transcurrido`) VALUES
(1, '4333797211', '29814610', 280000.00, 18),
(2, '4333797211', '29814610', 280000.00, 11),
(3, '9531543133', '112233', 45000.00, 11),
(4, '1651968205', '44556677', 35000.00, 11);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `consultascuentas`
--
ALTER TABLE `consultascuentas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `deposito`
--
ALTER TABLE `deposito`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `generar`
--
ALTER TABLE `generar`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `retiro`
--
ALTER TABLE `retiro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `retiros`
--
ALTER TABLE `retiros`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `saldos`
--
ALTER TABLE `saldos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `consultascuentas`
--
ALTER TABLE `consultascuentas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `cuenta`
--
ALTER TABLE `cuenta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `deposito`
--
ALTER TABLE `deposito`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `generar`
--
ALTER TABLE `generar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `registros`
--
ALTER TABLE `registros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `retiro`
--
ALTER TABLE `retiro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `retiros`
--
ALTER TABLE `retiros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `saldos`
--
ALTER TABLE `saldos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
