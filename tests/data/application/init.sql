CREATE SCHEMA "sport_betting";

CREATE TABLE "sport_betting"."users_info" (
  "id" text UNIQUE NOT NULL,
  "name" text,
  "surname" text,
  PRIMARY KEY ("id")
);

CREATE TABLE "sport_betting"."private_users_info" (
  "id" text UNIQUE NOT NULL,
  "password" text NOT NULL,
  "approved" boolean,
  PRIMARY KEY ("id")
);

CREATE TABLE "sport_betting"."codes" (
  "id" text UNIQUE NOT NULL,
  "created_at" timestamp DEFAULT (now()),
  "secret_code" text NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "sport_betting"."login_token" (
  "id" text UNIQUE NOT NULL,
  "created_at" timestamp DEFAULT (now()),
  "token" text NOT NULL,
  PRIMARY KEY ("id")
);

ALTER TABLE "sport_betting"."private_users_info" ADD FOREIGN KEY ("id") REFERENCES "sport_betting"."users_info" ("id");

ALTER TABLE "sport_betting"."codes" ADD FOREIGN KEY ("id") REFERENCES "sport_betting"."users_info" ("id");

ALTER TABLE "sport_betting"."login_token" ADD FOREIGN KEY ("id") REFERENCES "sport_betting"."users_info" ("id");

CREATE TABLE "sport_betting"."competitions_info" (
  "id" text NOT NULL,
  "name" text NOT NULL,
  "start_time" timestamp NOT NULL,
  "end_time" timestamp,
  "is_active" boolean DEFAULT true,
  "parsing_ref" text,
  "created_by" text NOT NULL,
  "special_id" text UNIQUE NOT NULL,
  PRIMARY KEY ("id", "name", "special_id")
);

CREATE TABLE "sport_betting"."matches_info" (
  "competition_id" text UNIQUE NOT NULL,
  "id" text NOT NULL,
  "name" text NOT NULL,
  "start_time" timestamp NOT NULL,
  "end_time" timestamp,
  "first_team_name" text NOT NULL,
  "second_team_name" text NOT NULL,
  "first_team_result" integer,
  "second_team_result" integer,
  "is_active" boolean DEFAULT true,
  "parsing_ref" text,
  PRIMARY KEY ("competition_id", "id")
);

CREATE TABLE "sport_betting"."match_bets" (
  "match_id" text NOT NULL,
  "user_id" text NOT NULL,
  "created_at" timestamp DEFAULT (now()),
  "bets" json NOT NULL,
  "result" numeric,
  "competition_id" text NOT NULL,
  PRIMARY KEY ("match_id", "user_id", "competition_id")
);

CREATE TABLE "sport_betting"."special_created_bets" (
  "match_id" text NOT NULL,
  "created_at" timestamp DEFAULT (now()),
  "bet_name" text NOT NULL,
  "competition_id" text NOT NULL,
  PRIMARY KEY ("match_id", "competition_id")
);

CREATE TABLE "sport_betting"."competition_bets" (
  "competition_id" text NOT NULL,
  "user_id" text NOT NULL,
  "result" numeric,
  PRIMARY KEY ("competition_id", "user_id")
);

ALTER TABLE "sport_betting"."competitions_info" ADD FOREIGN KEY ("created_by") REFERENCES "sport_betting"."users_info" ("id");

ALTER TABLE "sport_betting"."matches_info" ADD FOREIGN KEY ("competition_id") REFERENCES "sport_betting"."competitions_info" ("special_id");

INSERT INTO sport_betting.users_info (id, name, surname) VALUES ('lol', '123', '123'), ('pok', '123', '123'), ('kek', '123', '123');
INSERT INTO sport_betting.private_users_info (id, password, approved) VALUES ('lol', '123', true), ('pok', '123', false), ('kek', '123', true);
INSERT INTO sport_betting.codes (id, secret_code) VALUES ('pok', 'value');
INSERT INTO sport_betting.login_token (id, token) VALUES ('lol', 'qw'), ('kek', 'qw');
INSERT INTO sport_betting.competitions_info (id, name, start_time, end_time, is_active, parsing_ref, created_by, special_id) VALUES ('1', '1', now(), NULL, true, NULL, 'lol', '1');
INSERT INTO sport_betting.matches_info (competition_id, id, name, start_time, end_time, first_team_name, second_team_name, first_team_result, second_team_result, parsing_ref, is_active) VALUES ('1', '1', '1',now(), NULL, '1', '2', 0, 1, NULL. false);
