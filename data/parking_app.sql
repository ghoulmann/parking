PRAGMA foreign_keys = "1";
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM `main`.sqlite_master;
PRAGMA encoding
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
CREATE TABLE `Lot` (
	`capacity`	INTEGER,
	`used`	INTEGER,
	`available`	INTEGER,
	`ay`	TEXT,
	`season`	TEXT
);
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM `main`.sqlite_master;
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
CREATE TABLE `Permits` (
	`permit_id`	INTEGER NOT NULL,
	`status`	TEXT NOT NULL,
	`full_name`	TEXT
);
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM `main`.sqlite_master;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Lot` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Lot` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Lot` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Lot` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%0%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%0%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%00%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%00%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%a%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%a%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%av%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%av%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%ava%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%ava%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%avai%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%avai%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%avail%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%avail%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%availa%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%availa%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
INSERT INTO `main`.`Permits`(`permit_id`,`status`,`full_name`) VALUES (0,'',NULL);
UPDATE `main`.`Permits` SET `permit_id`=? WHERE _rowid_='1';
UPDATE `main`.`Permits` SET `status`=? WHERE _rowid_='1';
INSERT INTO `main`.`Permits`(`permit_id`,`status`,`full_name`) VALUES (0,'',NULL);
UPDATE `main`.`Permits` SET `permit_id`=? WHERE _rowid_='2';
UPDATE `main`.`Permits` SET `status`=? WHERE _rowid_='2';
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
INSERT INTO `main`.`Permits`(`permit_id`,`status`,`full_name`) VALUES (0,'',NULL);
UPDATE `main`.`Permits` SET `permit_id`=? WHERE _rowid_='3';
UPDATE `main`.`Permits` SET `status`=? WHERE _rowid_='3';
PRAGMA auto_vacuum
PRAGMA automatic_index
PRAGMA checkpoint_fullfsync
PRAGMA foreign_keys
PRAGMA fullfsync
PRAGMA ignore_check_constraints
PRAGMA journal_mode
PRAGMA journal_size_limit
PRAGMA locking_mode
PRAGMA max_page_count
PRAGMA page_size
PRAGMA recursive_triggers
PRAGMA secure_delete
PRAGMA synchronous
PRAGMA temp_store
PRAGMA user_version
PRAGMA wal_autocheckpoint
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
CREATE TABLE `hash` (
	`first name`	TEXT NOT NULL,
	`last name`	TEXT NOT NULL,
	`role`	TEXT NOT NULL,
	`email`	TEXT,
	`username`	TEXT
);
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM `main`.sqlite_master;
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA foreign_keys
PRAGMA database_list;
SELECT type,name,sql,tbl_name FROM `main`.sqlite_master;
PRAGMA auto_vacuum
PRAGMA automatic_index
PRAGMA checkpoint_fullfsync
PRAGMA foreign_keys
PRAGMA fullfsync
PRAGMA ignore_check_constraints
PRAGMA journal_mode
PRAGMA journal_size_limit
PRAGMA locking_mode
PRAGMA max_page_count
PRAGMA page_size
PRAGMA recursive_triggers
PRAGMA secure_delete
PRAGMA synchronous
PRAGMA temp_store
PRAGMA user_version
PRAGMA wal_autocheckpoint
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;
SELECT COUNT(*) FROM (SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC);
SELECT `_rowid_`,* FROM `main`.`Permits` WHERE `permit_id` LIKE '%001%' ESCAPE '\' AND `status` LIKE '%available%' ESCAPE '\' ORDER BY `_rowid_` ASC LIMIT 0, 50000;

