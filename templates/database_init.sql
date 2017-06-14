CREATE TABLE Household(id INT PRIMARY KEY auto_increment, name VARCHAR(20) UNIQUE,space INT NOT NULL, status VARCHAR(20));
CREATE TABLE Chiefs(id INT PRIMARY KEY auto_increment, initials VARCHAR(20),adress VARCHAR(20),id_hshl INT , foreign key(id_hshl) references Household(id) ON DELETE cascade ON UPDATE cascade);
CREATE TABLE Workers(id INT PRIMARY KEY auto_increment, name VARCHAR(20),surname VARCHAR(20),midname VARCHAR(20), birthday date, adress VARCHAR(20), id_chief INT NOT NULL, foreign key(id_chief) references Chiefs(id) ON DELETE cascade ON UPDATE cascade );
CREATE TABLE Trees(id INT PRIMARY KEY auto_increment,  name VARCHAR(20) UNIQUE, type VARCHAR(20) );
CREATE TABLE density(id_hshl INT, id_tree INT, treedensity INT NOT NULL, middleage INT NOT NULL,UNIQUE(id_hshl,id_tree), foreign key(id_hshl) references Household(id) ON DELETE cascade ON UPDATE cascade,foreign key(id_tree) references Trees(id) ON DELETE cascade ON UPDATE cascade);
ALTER TABLE `gromova1`.`Household` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `gromova1`.`Chiefs` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `gromova1`.`Workers` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `gromova1`.`Trees` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE `gromova1`.`density` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO Household(name, space,status) VALUES ('Лесомедь',18, 'Удовлетворительно'),('Древострой',18,'Отлично');
INSERT INTO Chiefs(initials,adress,id_hshl) VALUES ('Домнин К.В.','Харьков, Пушкинская',1),('Кременчуцкий М.И.','Харьков, Алчевская',2),('Евтюгин Н.В','Харьков, Сумская',1);
INSERT INTO Workers(name, surname, midname, birthday, adress, id_chief) VALUES ('Илья','Маков','Сергеевич','1995.01.09','Харьков,Пушкинская',1),('Виктор','Жоров','Витальевич','1995.02.07','Харьков,Пушкинская',2),('Георгий','Ватров','Игнатьевич','1995.04.03','Харьков,Сумская',2),('Сергей','Макарец','Иванович','1995.11.21','Харьков,Пушкинская',3),('Никита','Байдин','Филлипович','1995.02.12','Харьков,Алчевская',1);
INSERT INTO Trees(name,type) VALUES ('Дуб','Листопадные'),('Сосна','Хвойные'),('Бук','Листопадные');
INSERT INTO density(id_hshl, id_tree, treedensity, middleage) values (1,1, 16, 15),(1,2, 80, 10),(1,3, 49, 10),(2,1, 14, 15),(2,2, 61, 10),(2,3, 8, 10);
CREATE TABLE Apparate(id int primary key auto_increment, type varchar(20));
ALTER TABLE `gromova1`.`Apparate` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO Apparate(type) values ('Буры'),('Тракторы'),('Комбаины');
CREATE TABLE App_Hous(id_hshl INT,id_app INT,UNIQUE(id_hshl,id_app),foreign key(id_hshl) references Household(id) ON DELETE cascade ON UPDATE cascade,foreign key(id_app) references Apparate(id) ON DELETE cascade ON UPDATE cascade);
ALTER TABLE `gromova1`.`App_Hous` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO App_Hous(id_hshl,id_app) values(1,1),(1,3),(2,1),(2,2);
CREATE TABLE Worktypes(id int primary key auto_increment, type VARCHAR(20) UNIQUE);
ALTER TABLE `gromova1`.`Worktypes` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO Worktypes(type) values ('Деревообработка'),('Лесозаготовка'),('Лакирование');
CREATE TABLE Wt_Wk(id_wk INT, id_wt INT,UNIQUE(id_wk,id_wt), foreign key(id_wt) references Worktypes(id) ON DELETE cascade ON UPDATE cascade,foreign key(id_wk) references Workers(id) ON DELETE cascade ON UPDATE cascade);
ALTER TABLE `gromova1`.`Wt_Wk` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO Wt_Wk(id_wk, id_wt) values (1,1),(1,2),(2,1),(2,3),(4,1),(5,1),(3,2),(3,1);
CREATE TABLE Wk_Salary(id_wk INT UNIQUE, salary REAL, foreign key(id_wk) references Workers(id) ON DELETE cascade ON UPDATE cascade);
ALTER TABLE `gromova1`.`Wk_Salary` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO Wk_Salary(id_wk, salary) values (1,4497.50),(2,4497.50),(3,5230.60),(4,3775.16),(5,6011.32);
CREATE TABLE Ch_Salary(id_chiefs INT UNIQUE, salary REAL, foreign key(id_chiefs) references Chiefs(id) ON DELETE cascade ON UPDATE cascade);
ALTER TABLE `gromova1`.`Ch_Salary` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
INSERT INTO Ch_Salary(id_chiefs, salary) values (1,14497.50),(2,9497.50),(3,11230.60);
