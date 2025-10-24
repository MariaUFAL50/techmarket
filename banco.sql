CREATE DATABASE techmarket;
USE techmarket;

CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  preco DECIMAL(10,2)
);

INSERT INTO produtos (nome, preco) VALUES
('Notebook Dell', 4500.00),
('Smartphone Samsung', 2500.00),
('Headset Gamer', 350.00);
