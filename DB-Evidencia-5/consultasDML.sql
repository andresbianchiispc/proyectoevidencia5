INSERT INTO usuarios (id_usuario, nombre, email) VALUES
(1, 'Ana', 'ana.garcia@email.com'),
(2, 'Luis', 'luis.perez@email.com');

INSERT INTO dispositivos (nombre_dispositivo, tipo_dispositivo, estado_dispositivo, id_usuario) VALUES
('luz Sala', 'Iluminación', 1, 1),
('Termostato', 'Climatización', 0, 1),
('Enchufe Cocina', 'Energía', 1, 2),
('Sensor Puerta', 'Seguridad', 0, 2);

INSERT INTO automatizaciones (descripcion, condicion, id_usuario) VALUES
('Encender luces al anochecer', 'Anochecer', 1),
('Apagar enchufe al salir', 'Salida del hogar', 2);

INSERT INTO acciones (tipo_accion, valor_configurado, id_automatizacion, id_dispositivo) VALUES
('encender', 'Luz Sala', 1, 1),
('cambiar_estado', 'Termostato', 1, 2),
('apagar', 'Enchufe Cocina', 2, 3),
('notificar', 'Sensor Puerta', 2, 4);

