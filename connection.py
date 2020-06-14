import pymysql  # wymagana instalacja tego pakietu

def cls():
    clear = "\n" * 100
    print(clear)

conn = pymysql.connect(host='0.0.0.0', port=3306, user='username', passwd='pw', db='dbname') 

cur = conn.cursor()


# odkomentować przy nowej bazie danych do utworzenia tabel
# cur.execute("CREATE TABLE IF NOT EXISTS `core_notes`.`categories` ( `id` INT NOT NULL AUTO_INCREMENT , `name` TEXT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
# cur.execute("CREATE TABLE IF NOT EXISTS `notes` ( `id` int(11) NOT NULL,`title` text NOT NULL,`description` text NOT NULL,`deadline` date NOT NULL,`ended` int(11) NOT NULL,`category_id` int(11) DEFAULT NULL) ENGINE=MyISAM DEFAULT CHARSET=utf8; ALTER TABLE `notes`ADD PRIMARY KEY (`id`), ADD FOREIGN KEY (category_id) REFERENCES Categories(Id);")

