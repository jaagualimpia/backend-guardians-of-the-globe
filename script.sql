DELETE FROM api_abilities WHERE true;
DELETE FROM api_weakness WHERE true;
DELETE FROM api_sponsorship WHERE true;
DELETE FROM api_battle WHERE true;
DELETE FROM api_schedule WHERE true;
DELETE FROM api_relationships WHERE true;

DELETE FROM api_hero WHERE true;
DELETE FROM api_villain WHERE true;
DELETE FROM api_sponsor WHERE true;

ALTER SEQUENCE api_abilities_id_seq RESTART WITH 1;                
ALTER SEQUENCE api_battle_id_seq RESTART WITH 1;                   
ALTER SEQUENCE api_hero_id_seq RESTART WITH 1;                     
ALTER SEQUENCE api_relationships_id_seq RESTART WITH 1;            
ALTER SEQUENCE api_schedule_id_seq RESTART WITH 1;                 
ALTER SEQUENCE api_sponsor_id_seq RESTART WITH 1;                  
ALTER SEQUENCE api_sponsorship_id_seq RESTART WITH 1;              
ALTER SEQUENCE api_villain_id_seq RESTART WITH 1;                  
ALTER SEQUENCE api_weakness_id_seq RESTART WITH 1;                 


-- 1
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('John', '1990-03-25', 'Male', 'Super strength');

-- 2
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Emily', '1985-09-08', 'Female', 'Telepathic abilities');

-- 3
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Alex', '1998-11-30', 'Non-binary', 'Invisibility powers');

-- 4
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Victor', '1975-07-18', 'Male', 'Technological genius');

-- 5
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Diana', '1983-05-02', 'Female', 'Master archer');

-- 6
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Sam', '2005-12-15', 'Male', 'Super speed');

-- 7
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Mia', '1993-04-07', 'Female', 'Time manipulation');

-- 8
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Chris', '1988-08-22', 'Non-binary', 'Shape-shifting abilities');

-- 9
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Olivia', '2000-01-10', 'Female', 'Teleportation skills');

-- 10
INSERT INTO public.api_hero(name, "dateOfBirth", gender, description)
	VALUES ('Riley', '1970-06-05', 'Male', 'Weather control');

-- 1
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Crimson Shadow', '1980-07-12', 'Male', 'Mysterious background');

-- 2
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Viper Queen', '1995-04-18', 'Female', 'Experiments gone wrong');

-- 3
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Dark Matter', '1978-11-05', 'Male', 'Interdimensional being');

-- 4
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Venomous Witch', '1986-02-28', 'Female', 'Cursed by ancient powers');

-- 5
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Shadowcaster', '1990-09-15', 'Male', 'Master of dark arts');

-- 6
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Serpent Siren', '1983-06-30', 'Female', 'Transformed by forbidden rituals');

-- 7
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Dr. Malevolence', '1975-03-22', 'Male', 'Genius scientist turned evil');

-- 8
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Enchantress of Chaos', '1998-12-10', 'Female', 'Manipulator of reality');

-- 9
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Necrofiend', '1987-08-05', 'Male', 'Raised from the dead with dark magic');

-- 10
INSERT INTO public.api_villain(name, "dateOfBirth", gender, origin)
	VALUES ('Malefic Mistress', '2000-05-18', 'Female', 'Cursed bloodline');

-- 1
INSERT INTO public.api_sponsor(name, "netWorth", gender, "dateOfbirth", fortune_origin)
	VALUES ('Sophia', 8000000000, 'Female', '1990-12-15', 'Technology');

-- 2
INSERT INTO public.api_sponsor(name, "netWorth", gender, "dateOfbirth", fortune_origin)
	VALUES ('David', 12000000000, 'Male', '1985-05-20', 'Finance');

-- 3
INSERT INTO public.api_sponsor(name, "netWorth", gender, "dateOfbirth", fortune_origin)
	VALUES ('Isabella', 1500000000, 'Female', '1978-08-10', 'Real Estate');

-- 4
INSERT INTO public.api_sponsor(name, "netWorth", gender, "dateOfbirth", fortune_origin)
	VALUES ('Elijah', 500000000, 'Male', '1995-03-28', 'Healthcare');

-- 5
INSERT INTO public.api_sponsor(name, "netWorth", gender, "dateOfbirth", fortune_origin)
	VALUES ('Olivia', 7000000000, 'Female', '1982-11-02', 'Entertainment');


-- Abilities for Heroes
INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (1, false, 'Super Strength');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (2, false, 'Telepathy');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (3, false, 'Invisibility');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (4, false, 'Technological Genius');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (5, false, 'Master Archer');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (6, false, 'Super Speed');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (7, false, 'Time Manipulation');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (8, false, 'Shape-shifting');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (9, false, 'Teleportation');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (10, false, 'Weather Control');


-- Abilities for Villains
INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (1, true, 'Shadow Manipulation');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (2, true, 'Venomous Bite');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (3, true, 'Mind Control');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (4, true, 'Dark Magic');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (5, true, 'Teleportation');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (6, true, 'Illusions');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (7, true, 'Technological Warfare');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (8, true, 'Reality Manipulation');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (9, true, 'Necromancy');

INSERT INTO public.api_abilities(id_person, is_villain, ability)
	VALUES (10, true, 'Cursed Aura');


-- Weaknesses for Heroes
INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (1, false, 'Fear of heights');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (2, false, 'Super Laziness');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (3, false, 'Inability to swim');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (4, false, 'Emotionally vulnerable');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (5, false, 'Allergic to bees');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (6, false, 'Impatience');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (7, false, 'Temporal instability');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (8, false, 'Vulnerability to silver');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (9, false, 'Fear of confined spaces');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (10, false, 'Susceptible to extreme temperatures');


-- Weaknesses for Villains
INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (1, true, 'Fear of light');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (2, true, 'Laziness');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (3, true, 'Water phobia');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (4, true, 'Sentimental attachments');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (5, true, 'Allergic to silver');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (6, true, 'Impulsive');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (7, true, 'Temporal paradox');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (8, true, 'Vulnerability to sound');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (9, true, 'Fear of heights');

INSERT INTO public.api_weakness(id_person, is_villain, weakness)
	VALUES (10, true, 'Susceptible to extreme pressures');


-- Battle Relations
INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2013-09-13', true, 1, 1);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2014-05-20', false, 2, 2);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2015-11-08', true, 3, 3);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2016-03-15', false, 4, 4);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2017-09-02', true, 5, 5);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2018-12-10', false, 6, 6);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2019-07-18', true, 7, 7);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2020-02-28', false, 8, 8);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2021-06-05', true, 9, 9);

INSERT INTO public.api_battle(date, winned, hero_id, villain_id)
	VALUES ('2022-11-30', false, 10, 10);


-- Sponsorship Relations for 10 Heroes and 5 Sponsors
INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (15000, 1, 1);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (20000, 2, 2);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (18000, 3, 3);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (25000, 4, 4);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (22000, 5, 5);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (30000, 6, 1);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (17000, 7, 2);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (21000, 8, 3);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (26000, 9, 4);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (23000, 10, 5);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (18000, 1, 2);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (22000, 2, 3);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (24000, 3, 4);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (27000, 4, 5);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (19000, 5, 1);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (28000, 6, 2);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (20000, 7, 3);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (25000, 8, 4);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (21000, 9, 5);

INSERT INTO public.api_sponsorship(amount, hero_id, sponsor_id)
	VALUES (19000, 10, 1);