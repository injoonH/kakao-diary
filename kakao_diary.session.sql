-- @BLOCK
CREATE TABLE User(
    id INT PRIMARY KEY,
    nickname VARCHAR(255) NOT NULL
);

-- @BLOCK
CREATE TABLE Chat(
    id INT AUTO_INCREMENT,
    usr_id INT NOT NULL,
    content TEXT NOT NULL,
    post_date DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (usr_id) REFERENCES User(id)
);

-- @BLOCK
CREATE TABLE Diary(
    id INT AUTO_INCREMENT,
    usr_id INT NOT NULL,
    content TEXT NOT NULL,
    post_date DATETIME NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (usr_id) REFERENCES User(id)
);