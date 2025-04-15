--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

-- *not* creating schema, since initdb creates it


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: databasechangelog; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.databasechangelog (
    id character varying(255) NOT NULL,
    author character varying(255) NOT NULL,
    filename character varying(255) NOT NULL,
    dateexecuted timestamp without time zone NOT NULL,
    orderexecuted integer NOT NULL,
    exectype character varying(10) NOT NULL,
    md5sum character varying(35),
    description character varying(255),
    comments character varying(255),
    tag character varying(255),
    liquibase character varying(20),
    contexts character varying(255),
    labels character varying(255),
    deployment_id character varying(10)
);


--
-- Name: databasechangeloglock; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.databasechangeloglock (
    id integer NOT NULL,
    locked boolean NOT NULL,
    lockgranted timestamp without time zone,
    lockedby character varying(255)
);


--
-- Name: department; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.department (
    id bigint NOT NULL,
    disable boolean DEFAULT false,
    name character varying(255) NOT NULL
);


--
-- Name: department_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.department_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: department_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.department_id_seq OWNED BY public.department.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.groups (
    id bigint NOT NULL,
    disable boolean DEFAULT false,
    title character varying(35) NOT NULL,
    sort_order integer
);


--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: lessons; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.lessons (
    id bigint NOT NULL,
    hours integer NOT NULL,
    lessontype character varying(255) NOT NULL,
    subject_for_site character varying(255) NOT NULL,
    group_id bigint NOT NULL,
    subject_id bigint NOT NULL,
    teacher_id bigint NOT NULL,
    grouped boolean DEFAULT false,
    semester_id bigint NOT NULL,
    link_to_meeting character varying(255),
    CONSTRAINT lessons_hours_check CHECK ((hours >= 1))
);


--
-- Name: lessons_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.lessons_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: lessons_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.lessons_id_seq OWNED BY public.lessons.id;


--
-- Name: periods; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.periods (
    id bigint NOT NULL,
    end_time time without time zone NOT NULL,
    name character varying(35) NOT NULL,
    start_time time without time zone NOT NULL
);


--
-- Name: periods_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.periods_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: periods_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.periods_id_seq OWNED BY public.periods.id;


--
-- Name: room_types; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.room_types (
    id bigint NOT NULL,
    description character varying(40) NOT NULL
);


--
-- Name: room_types_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.room_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: room_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.room_types_id_seq OWNED BY public.room_types.id;


--
-- Name: rooms; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.rooms (
    id bigint NOT NULL,
    disable boolean DEFAULT false,
    name character varying(35) NOT NULL,
    room_type_id bigint,
    sort_order integer
);


--
-- Name: rooms_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rooms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: rooms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.rooms_id_seq OWNED BY public.rooms.id;


--
-- Name: schedules; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.schedules (
    id bigint NOT NULL,
    day_of_week character varying(35) NOT NULL,
    evenodd character varying(255) NOT NULL,
    lesson_id bigint NOT NULL,
    period_id bigint NOT NULL,
    room_id bigint NOT NULL
);


--
-- Name: schedules_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.schedules_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: schedules_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.schedules_id_seq OWNED BY public.schedules.id;


--
-- Name: semester_day; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.semester_day (
    semester_id bigint NOT NULL,
    day character varying(255)
);


--
-- Name: semester_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.semester_group (
    semester_id bigint NOT NULL,
    group_id bigint NOT NULL
);


--
-- Name: semester_period; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.semester_period (
    semester_id bigint NOT NULL,
    period_id bigint NOT NULL
);


--
-- Name: semesters; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.semesters (
    id bigint NOT NULL,
    current_semester boolean DEFAULT false,
    description character varying(255),
    disable boolean DEFAULT false,
    end_day date NOT NULL,
    start_day date NOT NULL,
    year integer NOT NULL,
    default_semester boolean DEFAULT false,
    CONSTRAINT semesters_year_check CHECK ((year >= 1999))
);


--
-- Name: semesters_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.semesters_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: semesters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.semesters_id_seq OWNED BY public.semesters.id;


--
-- Name: students; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.students (
    id bigint NOT NULL,
    name character varying(35) NOT NULL,
    patronymic character varying(35) NOT NULL,
    surname character varying(35) NOT NULL,
    group_id bigint NOT NULL,
    user_id bigint
);


--
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.students_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- Name: subjects; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.subjects (
    id bigint NOT NULL,
    disable boolean DEFAULT false,
    name character varying(80) NOT NULL
);


--
-- Name: subjects_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.subjects_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: subjects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.subjects_id_seq OWNED BY public.subjects.id;


--
-- Name: teachers; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.teachers (
    id bigint NOT NULL,
    disable boolean DEFAULT false,
    name character varying(35) NOT NULL,
    patronymic character varying(35) NOT NULL,
    "position" character varying(35) NOT NULL,
    surname character varying(35) NOT NULL,
    user_id bigint,
    department_id bigint
);


--
-- Name: teachers_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.teachers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: teachers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.teachers_id_seq OWNED BY public.teachers.id;


--
-- Name: temporary_schedule; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.temporary_schedule (
    id bigint NOT NULL,
    date date NOT NULL,
    grouped boolean DEFAULT false,
    lessontype character varying(255),
    subject_for_site character varying(255),
    vacation boolean DEFAULT false,
    group_id bigint,
    period_id bigint,
    room_id bigint,
    semester_id bigint,
    subject_id bigint,
    teacher_id bigint,
    notification boolean DEFAULT false,
    schedule_id bigint,
    link_to_meeting character varying(255)
);


--
-- Name: temporary_schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.temporary_schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: temporary_schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.temporary_schedule_id_seq OWNED BY public.temporary_schedule.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    email character varying(40) NOT NULL,
    password character varying(255) NOT NULL,
    role character varying(32) DEFAULT 'ROLE_USER'::character varying,
    token character varying(255)
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: department id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.department ALTER COLUMN id SET DEFAULT nextval('public.department_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Name: lessons id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lessons ALTER COLUMN id SET DEFAULT nextval('public.lessons_id_seq'::regclass);


--
-- Name: periods id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.periods ALTER COLUMN id SET DEFAULT nextval('public.periods_id_seq'::regclass);


--
-- Name: room_types id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.room_types ALTER COLUMN id SET DEFAULT nextval('public.room_types_id_seq'::regclass);


--
-- Name: rooms id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rooms ALTER COLUMN id SET DEFAULT nextval('public.rooms_id_seq'::regclass);


--
-- Name: schedules id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schedules ALTER COLUMN id SET DEFAULT nextval('public.schedules_id_seq'::regclass);


--
-- Name: semesters id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semesters ALTER COLUMN id SET DEFAULT nextval('public.semesters_id_seq'::regclass);


--
-- Name: students id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- Name: subjects id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subjects ALTER COLUMN id SET DEFAULT nextval('public.subjects_id_seq'::regclass);


--
-- Name: teachers id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teachers ALTER COLUMN id SET DEFAULT nextval('public.teachers_id_seq'::regclass);


--
-- Name: temporary_schedule id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule ALTER COLUMN id SET DEFAULT nextval('public.temporary_schedule_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: databasechangelog; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.databasechangelog (id, author, filename, dateexecuted, orderexecuted, exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id) FROM stdin;
1642775490693-1	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.308637	1	EXECUTED	8:aa5f97d9722ad33a04b1b2604046bdbf	createSequence sequenceName=department_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-2	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.316322	2	MARK_RAN	8:4896ada120320a0099ac0a904738457a	createTable tableName=department		\N	4.6.2	\N	\N	3304852089
1642775490693-3	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.323814	3	EXECUTED	8:8ed2ff06276e50ed7df1252d5e964474	createSequence sequenceName=groups_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-4	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.327729	4	MARK_RAN	8:0a68a94209f06f338b787eee9b8c57c8	createTable tableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-5	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.334689	5	EXECUTED	8:a1bd6eab09d5f33081a2b68a290c47ce	createSequence sequenceName=lessons_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-6	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.341283	6	EXECUTED	8:6b79bf22a12c0dfdc6223d215fee1fe4	createSequence sequenceName=lessons_group_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-7	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.348928	7	EXECUTED	8:223d25bd1534e0266e2f3826eb2aa3ec	createSequence sequenceName=lessons_subject_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-8	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.356245	8	EXECUTED	8:6748c77819ff10f3adfef668487463c4	createSequence sequenceName=lessons_teacher_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-9	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.362916	9	EXECUTED	8:9e0b93e60a718df788ea9ee88f76c4ac	createSequence sequenceName=lessons_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-10	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.367251	10	MARK_RAN	8:e66111b48e5cae5e152ae2a669db4804	createTable tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-11	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.374242	11	EXECUTED	8:29e36d7770f7324389a1e645d2aa0c64	createSequence sequenceName=periods_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-12	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.377939	12	MARK_RAN	8:3017bf41941925296ba9ea4268c326a4	createTable tableName=periods		\N	4.6.2	\N	\N	3304852089
1642775490693-13	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.384531	13	EXECUTED	8:83d7f1ccac23afb00541a32bb8789f89	createSequence sequenceName=room_types_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-14	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.388246	14	MARK_RAN	8:2d9b1495eb58ec31cf1257b63c5ca093	createTable tableName=room_types		\N	4.6.2	\N	\N	3304852089
1642775490693-15	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.39597	15	EXECUTED	8:9216eda2c38e21fed8e1b4f7e0de15b7	createSequence sequenceName=rooms_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-16	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.404173	16	EXECUTED	8:9dce0005a32a5cb4d6c021be7db05afa	createSequence sequenceName=rooms_room_type_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-17	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.40865	17	MARK_RAN	8:42355d333e41bbf56e72d723d7618738	createTable tableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-18	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.420351	18	EXECUTED	8:5ed500717ecbce8f13a26fe2d3049fcf	createSequence sequenceName=schedules_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-19	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.427197	19	EXECUTED	8:9be95727039ac12224e43765fa41ee62	createSequence sequenceName=schedules_lesson_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-20	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.434088	20	EXECUTED	8:0b055e793e9c3f6d4c48d6821a59bd0d	createSequence sequenceName=schedules_period_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-21	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.440305	21	EXECUTED	8:7a63c25c4030c4cb70ec39a9a69dacaf	createSequence sequenceName=schedules_room_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-22	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.443774	22	MARK_RAN	8:89146ae8ad9af9e430a8dab09338c2a9	createTable tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-23	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.45109	23	EXECUTED	8:6a63364cd9b7187764be3877dec94e6a	createSequence sequenceName=semester_day_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-24	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.455344	24	MARK_RAN	8:4dafb3ef4261b4006d46bf3bc7c36369	createTable tableName=semester_day		\N	4.6.2	\N	\N	3304852089
1642775490693-25	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.461523	25	EXECUTED	8:4f9d33e17a227c2e8c9f2aa48a61d890	createSequence sequenceName=semester_period_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-26	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.467802	26	EXECUTED	8:b8e3e4811e1ec5e2163038d6fa3ad970	createSequence sequenceName=semester_period_period_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-27	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.471526	27	MARK_RAN	8:5ff42a04568a8902488b504a06a2c7e0	createTable tableName=semester_period		\N	4.6.2	\N	\N	3304852089
1642775490693-28	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.477843	28	EXECUTED	8:6862c6f3a7ca7d1e8a47b2c256cc1d60	createSequence sequenceName=semesters_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-29	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.481582	29	MARK_RAN	8:f8b0d745274e244a11e71a8249c68258	createTable tableName=semesters		\N	4.6.2	\N	\N	3304852089
1642775490693-30	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.488154	30	EXECUTED	8:41f4a310e93e676e815571ae83e33766	createSequence sequenceName=students_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-31	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.49185	31	MARK_RAN	8:aeadb27a46fb0269adac892f5d30b2ff	createTable tableName=students		\N	4.6.2	\N	\N	3304852089
1642775490693-32	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.498534	32	EXECUTED	8:84690b8ed6999897da78d6cd7c1d3e91	createSequence sequenceName=subjects_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-33	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.502073	33	MARK_RAN	8:b19c14bdfa1f1e670d7a5026ec99b9c9	createTable tableName=subjects		\N	4.6.2	\N	\N	3304852089
1642775490693-34	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.508496	34	EXECUTED	8:aec286ed2878ffe6b71cd3427104460a	createSequence sequenceName=teachers_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-35	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.512331	35	MARK_RAN	8:86995232d247ea06c1a839ceef591dfc	createTable tableName=teachers		\N	4.6.2	\N	\N	3304852089
1642775490693-36	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.519105	36	EXECUTED	8:f0cdf595819a9dfc9c422e2fa261ec19	createSequence sequenceName=temporary_schedule_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-37	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.525355	37	EXECUTED	8:7508d26727002cf9c1b534bb1561aa39	createSequence sequenceName=temporary_schedule_group_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-38	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.531591	38	EXECUTED	8:240a5f936579d49f730c1328fb667ddf	createSequence sequenceName=temporary_schedule_period_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-39	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.543346	39	EXECUTED	8:99732f27b396fde52313a6c0f7d9bb9f	createSequence sequenceName=temporary_schedule_room_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-40	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.549584	40	EXECUTED	8:911d56ba64649b525d2664a0e283b475	createSequence sequenceName=temporary_schedule_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-41	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.556039	41	EXECUTED	8:de2ec953bfe5ea6e8d40edbf9b353a00	createSequence sequenceName=temporary_schedule_subject_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-42	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.562319	42	EXECUTED	8:6a8e5302703d9359f375e32e3e2d95f2	createSequence sequenceName=temporary_schedule_teacher_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-43	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.565836	43	MARK_RAN	8:5a212ec5297598066d10ce281ee18408	createTable tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-44	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.572214	44	EXECUTED	8:1fc72d3f0ba1f7821fa95765a828d81f	createSequence sequenceName=users_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-45	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.576242	45	MARK_RAN	8:4f383803e2e73d127b6a0624e22ceca4	createTable tableName=users		\N	4.6.2	\N	\N	3304852089
1642775490693-46	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.579985	46	MARK_RAN	8:4232f84c6bcd4e03074b154e7dc19177	createTable tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-47	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.585323	47	MARK_RAN	8:b0bf6d019ccdd5b69d56fd21104e4c23	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-48	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.59005	48	MARK_RAN	8:e1cc48a2fc60ea73e1ca3dafdc77e6f7	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-49	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.595098	49	MARK_RAN	8:dd670767f3e7f98351a8a4a5f739fac7	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-50	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.600745	50	MARK_RAN	8:616dfae1e362f59afa65af500632da1e	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-51	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.606187	51	MARK_RAN	8:d392f2e6fa728990e7dc6601cf1d87c1	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-52	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.610566	52	MARK_RAN	8:ba66cc1d4be5293a7000b68f4103b628	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-53	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.615874	53	MARK_RAN	8:f84c42c82b26547a41a134bd57b937f7	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-54	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.620632	54	MARK_RAN	8:19506382dc5b6c9f788fc9a655941a5b	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-55	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.625355	55	MARK_RAN	8:70d8fd0dcba2ce1a439c4c44c6ecc335	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-56	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.629606	56	MARK_RAN	8:2b312df599de7463eb572810947fd0a4	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-57	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.634411	57	MARK_RAN	8:45185e227ea186f350f9f496cebead43	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-58	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.639209	58	MARK_RAN	8:ca7d2a588be5114d6a638a42e8e072c8	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-59	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.644314	59	MARK_RAN	8:47c8f4b18daebb3908ce03f47288acf3	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-60	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.649008	60	MARK_RAN	8:118b1a15bcedff399acbadb2f6b92229	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-61	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.653982	61	MARK_RAN	8:c598d35e3a1a3727a4e2161cae12b59f	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-62	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.659492	62	MARK_RAN	8:2a6597848aa164d2db2ef51f0c0e4cee	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-63	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.664996	63	MARK_RAN	8:aa895b06f6db9b86f7222540496af958	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-64	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.67408	64	MARK_RAN	8:a46f19ef46e891039b9a4b6d428fbb42	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-65	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.67873	65	MARK_RAN	8:49b0ad140200aaf68d3335c3ef37af34	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-66	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.682953	66	MARK_RAN	8:e8b46acb519e8ea12df94c256d9ad22b	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-67	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.687505	67	MARK_RAN	8:da1610fa29dc67dabf249369c4c3325b	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-68	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.691772	68	MARK_RAN	8:f0d6852310ad0436794babb2a4ca6e5a	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-69	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.696197	69	MARK_RAN	8:bb13e4f59ba39e1fea31648fc9cee68a	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-70	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.701565	70	MARK_RAN	8:84ccaccf28493e7589cb7143fc7b249d	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-71	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.706943	71	MARK_RAN	8:86a0d37ed9d956c63ed58af883e87988	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-72	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.711532	72	MARK_RAN	8:faf66c2827cc5a196fd6b6facad399c5	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-73	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.716389	73	MARK_RAN	8:fe0f3c5c60ef1c63fb1a13068d42aff4	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-74	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.722126	74	MARK_RAN	8:692a67a26c178eb0710cd256a6f1c0d3	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-75	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.726881	75	MARK_RAN	8:ef04e306378056fe343e37afd3308eb8	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-76	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.734877	76	MARK_RAN	8:542fc5834480107a9a2019c53155c373	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-77	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.872516	77	MARK_RAN	8:d6605bd16f9fa778f4666b33e4c17592	addForeignKeyConstraint baseTableName=teachers, constraintName=fkl19hwymwn2ra2gwwty5trvyas, referencedTableName=department		\N	4.6.2	\N	\N	3304852089
1642775490693-78	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:12.927049	78	MARK_RAN	8:92e410f164024b025b39f791c615ddcb	addUniqueConstraint constraintName=uk_biw7tevwc07g3iutlbmkes0cm, tableName=department		\N	4.6.2	\N	\N	3304852089
1642775490693-79	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.181619	79	MARK_RAN	8:465c63a8d0aad41af7715824a6811e76	addForeignKeyConstraint baseTableName=temporary_schedule, constraintName=fka1bsm9fsuxn5t098i2cb7nncu, referencedTableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-80	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.288884	80	MARK_RAN	8:1f599d60e1a0ee82e55a2e8432a6583a	addForeignKeyConstraint baseTableName=students, constraintName=fkmsev1nou0j86spuk5jrv19mss, referencedTableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-81	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.404146	81	MARK_RAN	8:c2ce82437856bf0de8f73b1e21c68247	addForeignKeyConstraint baseTableName=semester_group, constraintName=fkpf19s66cmi8qpqc0iaeigbrhh, referencedTableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-82	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.56793	82	MARK_RAN	8:85c3d7011d3bc89475e66a218f6fe5ad	addForeignKeyConstraint baseTableName=lessons, constraintName=fktdolsaotaqlwxbxwaxt00kimk, referencedTableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-83	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.613132	83	MARK_RAN	8:1df26f8066f87c9cacf341066d12d61b	addUniqueConstraint constraintName=uk_ct3jhny5hfe6uj2osyn8a4p83, tableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-84	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.814556	84	MARK_RAN	8:1e1856a98e992362e9ab38f2848de099	addForeignKeyConstraint baseTableName=schedules, constraintName=fk7f954gltrwny6pe4see76kpw8, referencedTableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-85	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:13.96347	85	MARK_RAN	8:bc72e72b5b0365d6f49c067b3394f1ca	addForeignKeyConstraint baseTableName=lessons, constraintName=fkbr76cuebuufbbltujpfq04tto, referencedTableName=teachers		\N	4.6.2	\N	\N	3304852089
1642775490693-86	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.114507	86	MARK_RAN	8:81e7637290fb17036b3661fecc1d789c	addForeignKeyConstraint baseTableName=lessons, constraintName=fke94a0k21xpi7glv89af90lwjv, referencedTableName=subjects		\N	4.6.2	\N	\N	3304852089
1642775490693-87	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.279996	87	MARK_RAN	8:1bc0cf8f1426b6cd71582595f79e40d3	addForeignKeyConstraint baseTableName=lessons, constraintName=fkil1jt6gri8x6yfaa3ijf7d6d9, referencedTableName=semesters		\N	4.6.2	\N	\N	3304852089
1642775490693-88	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.489622	88	MARK_RAN	8:80d91bbd4140a4695b1fcbbe2051ba30	addForeignKeyConstraint baseTableName=schedules, constraintName=fk4g2p59v3jm7hk6a9ufdufy8ie, referencedTableName=periods		\N	4.6.2	\N	\N	3304852089
1642775490693-89	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.606179	89	MARK_RAN	8:2c350da08193fe556a01900172cf850a	addForeignKeyConstraint baseTableName=semester_period, constraintName=fkm237asf73ugk3vvw47aq266kl, referencedTableName=periods		\N	4.6.2	\N	\N	3304852089
1642775490693-90	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.803291	90	MARK_RAN	8:ea07065afa17f3cc89e5e6e5d9e6e778	addForeignKeyConstraint baseTableName=temporary_schedule, constraintName=fkr76lbhlv0di8ix7iviixs0p4g, referencedTableName=periods		\N	4.6.2	\N	\N	3304852089
1642775490693-91	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.836314	91	MARK_RAN	8:a4b42c93e1b2f18d49d612f5fb7cd3e4	addUniqueConstraint constraintName=uk_bgj9vbqf54b7iryxqu895bggh, tableName=periods		\N	4.6.2	\N	\N	3304852089
1642775490693-92	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.9456	92	MARK_RAN	8:d76a837afcdadae3d25413843c321915	addForeignKeyConstraint baseTableName=rooms, constraintName=fkh9m2n1paq5hmd3u0klfl7wsfv, referencedTableName=room_types		\N	4.6.2	\N	\N	3304852089
1642775490693-93	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:14.984319	93	MARK_RAN	8:bdaf4cec3aa0a4d5f53aa223a80ba939	addUniqueConstraint constraintName=uk_gunh6313ruq1dghti9p00529u, tableName=room_types		\N	4.6.2	\N	\N	3304852089
1642775490693-94	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:15.189373	94	MARK_RAN	8:bfd6aacdf47b887c990faf116da73f82	addForeignKeyConstraint baseTableName=schedules, constraintName=fk34r5t4jexlcas19pleifb8ihv, referencedTableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-95	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:15.37333	95	MARK_RAN	8:0f9fadd0354b14b3f54b846d04abcb72	addForeignKeyConstraint baseTableName=temporary_schedule, constraintName=fk3hid2313ah5gjqqye9d3eik2g, referencedTableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-96	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:15.493153	96	MARK_RAN	8:495474e8b7a4d5af182d08b7373ed7a6	addForeignKeyConstraint baseTableName=semester_day, constraintName=fk36f17dewxqjhb23rhlmc7slk3, referencedTableName=semesters		\N	4.6.2	\N	\N	3304852089
1642775490693-97	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:15.625168	97	MARK_RAN	8:53da83c0a726bb47762c3a651d742968	addForeignKeyConstraint baseTableName=semester_period, constraintName=fk94poii1rmjhoevjx7bsymtbtd, referencedTableName=semesters		\N	4.6.2	\N	\N	3304852089
1642775490693-98	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:15.743076	98	MARK_RAN	8:4975056c1d0a39f3e6759a176c870661	addForeignKeyConstraint baseTableName=semester_group, constraintName=fk4j15tivie8ttfhl0s7x3o3syv, referencedTableName=semesters		\N	4.6.2	\N	\N	3304852089
1642775490693-99	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:15.950036	99	MARK_RAN	8:af1fa9da5c42068c9da41f5aacbe0544	addForeignKeyConstraint baseTableName=temporary_schedule, constraintName=fkaqmj2bajc0ud8wproqn4843pk, referencedTableName=semesters		\N	4.6.2	\N	\N	3304852089
1642775490693-100	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:16.012622	100	MARK_RAN	8:3334c996979993bafdab1fa3be1b3fd6	addUniqueConstraint constraintName=uk_e2rndfrsx22acpq2ty1caeuyw, tableName=students		\N	4.6.2	\N	\N	3304852089
1642775490693-101	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:16.194456	101	MARK_RAN	8:bf49fb25ba5f2a530326d65285a2c469	addForeignKeyConstraint baseTableName=temporary_schedule, constraintName=fkqn6ufkok0nhqdkn46ctqckb76, referencedTableName=subjects		\N	4.6.2	\N	\N	3304852089
1642775490693-102	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:16.22784	102	MARK_RAN	8:0d0dc8e776721f293d981e1bf40b480c	addUniqueConstraint constraintName=uk_aodt3utnw0lsov4k9ta88dbpr, tableName=subjects		\N	4.6.2	\N	\N	3304852089
1642775490693-103	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:16.415814	103	MARK_RAN	8:b5f3e48312b92ce1c8d606087feea4c8	addForeignKeyConstraint baseTableName=temporary_schedule, constraintName=fko7tild8vhrqlodd3oaf8acvyw, referencedTableName=teachers		\N	4.6.2	\N	\N	3304852089
1642775490693-104	SaneQQQQ	db/changelog/initial-schema.yaml	2023-01-10 00:54:16.453053	104	MARK_RAN	8:930ca191405d374f276f19715b20d1b7	addUniqueConstraint constraintName=uk_6dotkott2kjsp8vw4d0m25fb7, tableName=users		\N	4.6.2	\N	\N	3304852089
1642775490693-105	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.457418	105	EXECUTED	8:10321f44b60d2c561d72a8c72b64a1d1	addColumn tableName=groups		\N	4.6.2	\N	\N	3304852089
1642775490693-106	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.460705	106	EXECUTED	8:42d9501e3337b724e4462939571ee5f2	createSequence sequenceName=sorting_order_sequence		\N	4.6.2	\N	\N	3304852089
1642775490693-107	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.468491	107	EXECUTED	8:f284a97909c948c5202647e82989d574	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-108	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.472719	108	EXECUTED	8:efd43fc6321ad8d944d03972d1e94a57	addColumn tableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-109	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.476471	109	EXECUTED	8:7825fbb05324f80b3b1152538de9cc02	createSequence sequenceName=sort_order_sequence		\N	4.6.2	\N	\N	3304852089
1642775490693-110	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.479951	110	EXECUTED	8:bc0f2b8b4e0cc5a70f678ecdbd231467	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-111	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.482895	111	EXECUTED	8:0ba76dec1bc756a0fb890c9bbefc8336	createSequence sequenceName=semester_group_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-112	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.487291	112	EXECUTED	8:6aefa45b11ebb5dcdbdb01e1c106446b	addDefaultValue columnName=semester_id, tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-113	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.490724	113	EXECUTED	8:d6f83e9cabb791f2096ab63dd2373439	createSequence sequenceName=semester_group_group_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-114	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.494346	114	EXECUTED	8:a2a0ab383b40b69cb57f64f8780c5cff	addDefaultValue columnName=group_id, tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-115	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.497605	115	EXECUTED	8:87ced3bd1c87b927544343e97ae954d2	addColumn tableName=students		\N	4.6.2	\N	\N	3304852089
1642775490693-116	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.506919	116	EXECUTED	8:efff72f0775752b90765801a6893c763	addForeignKeyConstraint baseTableName=students, constraintName=user_id_fk, referencedTableName=users		\N	4.6.2	\N	\N	3304852089
1642775490693-117	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.510443	117	EXECUTED	8:25e7d0e93b9bf75318818823125240ef	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-118	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.515376	118	EXECUTED	8:f37777b07c0fbd5686349263bfb84b59	dropColumn columnName=email, tableName=students		\N	4.6.2	\N	\N	3304852089
1642775490693-119	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.521075	119	EXECUTED	8:a928ea0676d296c8daf28606a41843ef	modifyDataType columnName=user_id, tableName=teachers		\N	4.6.2	\N	\N	3304852089
1642775490693-120	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.523943	120	EXECUTED	8:f77ada9c5aa5aa6094a3048e16f422d4	dropColumn columnName=lesson_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-121	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.52673	121	EXECUTED	8:dae9fb6baa1f293aa01722044c4cea0c	dropColumn columnName=teacher_for_site, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-122	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.531072	122	EXECUTED	8:32c00fe103876b8e56d30b44444d77bd	dropSequence sequenceName=sort_order_sequence		\N	4.6.2	\N	\N	3304852089
1642775490693-123	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.535163	123	EXECUTED	8:35099e4db18af2a4ca175ac95ea6b0cc	dropSequence sequenceName=sorting_order_sequence		\N	4.6.2	\N	\N	3304852089
1642775490693-124	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.538669	124	EXECUTED	8:1008a89e30f6c17fba04f5b604d376af	dropNotNullConstraint columnName=group_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-125	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.541862	125	EXECUTED	8:34e6693a8cfdefed793334a24de26fca	dropNotNullConstraint columnName=period_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-126	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.545397	126	EXECUTED	8:cbd9f5a0788008a2a5a2fd2842afc30d	dropNotNullConstraint columnName=room_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-127	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.548857	127	EXECUTED	8:8535a69b9c33f3df8b17868eaa67e090	dropNotNullConstraint columnName=room_type_id, tableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-128	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.552055	128	EXECUTED	8:dd8de81e18018b429783da039b3e97b2	dropNotNullConstraint columnName=semester_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-129	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.555007	129	EXECUTED	8:f989bc4abbb973dda43cfc5602994bc3	dropNotNullConstraint columnName=subject_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-130	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.557771	130	EXECUTED	8:df3a4ef19feb0c6923839274f00d55be	dropNotNullConstraint columnName=teacher_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-131	vchornyy12	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.560865	131	EXECUTED	8:d4d6d78dca0d8b2035c6471d6447b90c	delete tableName=students		\N	4.6.2	\N	\N	3304852089
1642775490693-132	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.564529	132	EXECUTED	8:a18e1ac1ea080d5f9e012e62577c63e4	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-133	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.567848	133	EXECUTED	8:20eebf8805602fc09404e556e078ce86	sql		\N	4.6.2	\N	\N	3304852089
1642775490693-134	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.570883	134	EXECUTED	8:c017b83ff51b6a70048be2a7dea5d31f	dropDefaultValue columnName=group_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-135	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.585024	135	EXECUTED	8:b4f3146b8b2e18e233a1f95f1da4630d	modifyDataType columnName=group_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-136	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.589989	136	EXECUTED	8:f22ebbe7a3903e2b9d7fc43ed839b94f	dropSequence sequenceName=lessons_group_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-137	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.593411	137	EXECUTED	8:51baf8e5166c0cc5859956630cb42318	dropDefaultValue columnName=semester_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-138	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.604456	138	EXECUTED	8:581300a10d3b525692bef085daf3c201	modifyDataType columnName=semester_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-139	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.60757	139	EXECUTED	8:731785025bd4392fef9945a985776f22	dropSequence sequenceName=lessons_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-140	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.610475	140	EXECUTED	8:672a62effd789acb76132b9ed3b3af11	dropDefaultValue columnName=subject_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-141	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.622277	141	EXECUTED	8:f0e8b4d913b62b92f28952fd91e441c3	modifyDataType columnName=subject_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-142	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.625414	142	EXECUTED	8:feffd59078b8ac1cbfbc257fa5d48ae6	dropSequence sequenceName=lessons_subject_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-143	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.6283	143	EXECUTED	8:67b6f9273e4622976c45ab7c576dde8e	dropDefaultValue columnName=teacher_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-144	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.641862	144	EXECUTED	8:26169cb4f37e64e583acf9f891b97d8f	modifyDataType columnName=teacher_id, tableName=lessons		\N	4.6.2	\N	\N	3304852089
1642775490693-145	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.644986	145	EXECUTED	8:d2e2ad799accd360ef53ab006c7ea21f	dropSequence sequenceName=lessons_teacher_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-146	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.648026	146	EXECUTED	8:49adfdce8b9cc6b4d5efeebd4acd1f46	dropDefaultValue columnName=room_type_id, tableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-147	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.653948	147	EXECUTED	8:c37cfe648bf725745088d4042b3f79e8	modifyDataType columnName=room_type_id, tableName=rooms		\N	4.6.2	\N	\N	3304852089
1642775490693-148	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.65744	148	EXECUTED	8:449729f3816c5c7cfe947a5d42c70dcb	dropSequence sequenceName=rooms_room_type_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-149	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.66043	149	EXECUTED	8:87283be462c2c7ac0e57ee3bd0325290	dropDefaultValue columnName=lesson_id, tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-150	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.672177	150	EXECUTED	8:d6633ae95b80efc0bec4ee1b2c4fc45c	modifyDataType columnName=lesson_id, tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-151	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.675564	151	EXECUTED	8:c668f41841404c56f0fbe9d222bae8bd	dropSequence sequenceName=schedules_lesson_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-152	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.678642	152	EXECUTED	8:d4b76f0f28b7aa9a47e15f6e20c57d25	dropDefaultValue columnName=period_id, tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-153	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.692323	153	EXECUTED	8:694545abc17ac55cd47b4c8bc8d656fc	modifyDataType columnName=period_id, tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-154	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.696234	154	EXECUTED	8:8a955e2590a32d688ab42b9c1190edb0	dropSequence sequenceName=schedules_period_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-155	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.699492	155	EXECUTED	8:b7f3f05cb8fbcdcdba1068301595aefe	dropDefaultValue columnName=room_id, tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-156	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.7171	156	EXECUTED	8:22d7f4d81555776ddd049dc149f10bca	modifyDataType columnName=room_id, tableName=schedules		\N	4.6.2	\N	\N	3304852089
1642775490693-157	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.720834	157	EXECUTED	8:5acc3c57bcd26c536ac2a59eac96bf80	dropSequence sequenceName=schedules_room_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-158	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.724436	158	EXECUTED	8:32129a6b3d276ea56ded71c807abc6a6	dropDefaultValue columnName=semester_id, tableName=semester_day		\N	4.6.2	\N	\N	3304852089
1642775490693-159	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.729256	159	EXECUTED	8:1d6c875b213cb928798311040c8c362b	modifyDataType columnName=semester_id, tableName=semester_day		\N	4.6.2	\N	\N	3304852089
1642775490693-160	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.732292	160	EXECUTED	8:bacff4b797297a1f903c4923a4115182	dropSequence sequenceName=semester_day_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-161	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.735005	161	EXECUTED	8:c148c9109ecbe4193f29782be66e9e7d	dropDefaultValue columnName=group_id, tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-162	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.741019	162	EXECUTED	8:5791479959cd9c1290e0f94b8f271671	modifyDataType columnName=group_id, tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-163	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.744323	163	EXECUTED	8:fce54fe695b703f28132b28bba37bf00	dropSequence sequenceName=semester_group_group_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-164	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.747524	164	EXECUTED	8:86a24f64e9e372564c94e38fff246288	dropDefaultValue columnName=semester_id, tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-165	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.753977	165	EXECUTED	8:a5592c1017d9ee2b45b261d5283649bd	modifyDataType columnName=semester_id, tableName=semester_group		\N	4.6.2	\N	\N	3304852089
1642775490693-166	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.757485	166	EXECUTED	8:7e58b91e4ef8a8da617a59dcc3bed5eb	dropSequence sequenceName=semester_group_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-167	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.760449	167	EXECUTED	8:a842b484eaaebf20934b76087393b28a	dropDefaultValue columnName=period_id, tableName=semester_period		\N	4.6.2	\N	\N	3304852089
1642775490693-168	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.766226	168	EXECUTED	8:0990d1a552dc6674c0d8cdf966f2e110	modifyDataType columnName=period_id, tableName=semester_period		\N	4.6.2	\N	\N	3304852089
1642775490693-169	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.769408	169	EXECUTED	8:208e59596226fad60e997ed06a251d79	dropSequence sequenceName=semester_period_period_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-170	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.772228	170	EXECUTED	8:d40183e646e8acbd3432b2f7f1386327	dropDefaultValue columnName=semester_id, tableName=semester_period		\N	4.6.2	\N	\N	3304852089
1642775490693-171	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.777669	171	EXECUTED	8:aa4e7d10441bab87a29bf3955f01e67e	modifyDataType columnName=semester_id, tableName=semester_period		\N	4.6.2	\N	\N	3304852089
1642775490693-172	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.780689	172	EXECUTED	8:c069e1e09acaa7aaf8a6de4f66195763	dropSequence sequenceName=semester_period_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-173	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.783799	173	EXECUTED	8:ff592de6322cb52f0dc14ba4c03dd689	dropDefaultValue columnName=group_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-174	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.790758	174	EXECUTED	8:549c16aa402e0a27029d044a73e6c331	modifyDataType columnName=group_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-175	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.793779	175	EXECUTED	8:a50734a8f82c1b02d150a3d5da89e55c	dropSequence sequenceName=temporary_schedule_group_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-176	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.796815	176	EXECUTED	8:bd503d8314dcaf7a5af4e52250b4fca5	dropDefaultValue columnName=period_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-177	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.804519	177	EXECUTED	8:5c8fd0f13dbf796b4c7230ba6a2bf6c8	modifyDataType columnName=period_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-178	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.80765	178	EXECUTED	8:ad5ce0416f6e31d999d1d7aee39d2ee2	dropSequence sequenceName=temporary_schedule_period_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-179	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.810567	179	EXECUTED	8:9d95d343e131eb7bcd5f25ba3b85cd12	dropDefaultValue columnName=room_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-180	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.816712	180	EXECUTED	8:a6905f0ddd94333a2674dbd746e044dc	modifyDataType columnName=room_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-181	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.819479	181	EXECUTED	8:9828723df3085b83283fb76bc43cbb4f	dropSequence sequenceName=temporary_schedule_room_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-182	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.822378	182	EXECUTED	8:079e403c2f1eb89222a40ccaeae67f09	dropDefaultValue columnName=semester_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-183	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.8298	183	EXECUTED	8:f5e2f0c4db249765d0d1b390b295a17f	modifyDataType columnName=semester_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-184	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.833154	184	EXECUTED	8:a47756409b37689995022aa750dfb92c	dropSequence sequenceName=temporary_schedule_semester_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-185	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.836084	185	EXECUTED	8:e1f5841ac4b048c06b6d37d09a6359cd	dropDefaultValue columnName=subject_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-186	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.842538	186	EXECUTED	8:d2b8a810281004ab1b0be2b240d2f8a3	modifyDataType columnName=subject_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-187	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.845745	187	EXECUTED	8:bf3c8abc9761f2b6e47cf50e5b0ede88	dropSequence sequenceName=temporary_schedule_subject_id_seq		\N	4.6.2	\N	\N	3304852089
1642775490693-188	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.848717	188	EXECUTED	8:69095186b0bd9908df7f5141affcabda	dropDefaultValue columnName=teacher_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-189	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.855313	189	EXECUTED	8:4a8c0747ea06b4396b729e218cf99435	modifyDataType columnName=teacher_id, tableName=temporary_schedule		\N	4.6.2	\N	\N	3304852089
1642775490693-190	SaneQQQQ	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.858331	190	EXECUTED	8:30027935fd55013a359f4dd372b92bcb	dropSequence sequenceName=temporary_schedule_teacher_id_seq		\N	4.6.2	\N	\N	3304852089
1653908145376-191	RuslanSlobodian	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.86277	191	EXECUTED	8:9e4cd7cb34395a3b9e084191d1b091c3	modifyDataType columnName=sort_order, tableName=rooms		\N	4.6.2	\N	\N	3304852089
1653908145376-192	petrokrechunyak	db/changelog/changeset/v1.0/db.changelog-v1.0.yaml	2023-01-10 00:54:16.866016	192	EXECUTED	8:b670fa15db3b634c34b8c00ac80bda7a	renameColumn newColumnName=sort_order, oldColumnName=sorting_order, tableName=groups		\N	4.6.2	\N	\N	3304852089
\.


--
-- Data for Name: databasechangeloglock; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.databasechangeloglock (id, locked, lockgranted, lockedby) FROM stdin;
1	f	\N	\N
\.


--
-- Data for Name: department; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.department (id, disable, name) FROM stdin;
1	f	Математичного моделювання
3	f	Математичного аналізу
4	f	Прикладної математики та інформаційних технологій
5	f	Диференціальних рівнянь
6	f	Алгебри та інформатики
13	t	Алгебри 
\.


--
-- Data for Name: groups; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.groups (id, disable, title, sort_order) FROM stdin;
30	f	101-А	6
100	f	511ббб	128
5	f	111-А	11
85	f	111-Б	12
105	f	611ббб	129
84	f	211-А	27
93	f	211-Б	28
27	f	102-А	18
26	f	102-Б	19
31	f	106	23
28	f	105	24
51	f	201-А	25
52	f	201-Б	26
33	f	108	22
86	f	107	13
29	f	101-Б	7
38	f	221ккк	130
90	t	test	166
17	t	Ch-099.UI	165
46	f	222ккк	131
54	f	202-А	35
87	f	202-Б	36
53	f	207	30
106	f	608	127
63	f	601	121
98	f	508	120
58	f	501	107
60	f	507	116
59	f	502	117
61	f	505	118
104	f	411	99
65	f	607	123
64	f	602	124
66	f	605	125
67	f	606	126
62	f	506	119
71	f	405	106
94	f	311-Б	48
70	f	422	103
95	f	311-А	46
72	f	408	104
73	f	406	105
49	f	421	100
50	f	407	101
68	f	402	102
45	f	401	96
55	f	208	40
36	f	301-А	44
37	f	301-Б	45
57	f	205	42
56	f	206	41
102	f	312-А	55
40	f	302-А	53
103	f	302-Б	54
39	f	307	49
42	f	308	93
43	f	306	94
44	f	305	95
41	f	312-Б	56
\.


--
-- Data for Name: lessons; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.lessons (id, hours, lessontype, subject_for_site, group_id, subject_id, teacher_id, grouped, semester_id, link_to_meeting) FROM stdin;
5425	2	LECTURE	Диференціальні рівняння	51	45	108	t	57	\N
5426	2	LECTURE	Диференціальні рівняння	52	45	108	t	57	\N
5427	2	LECTURE	Диференціальні рівняння	84	45	108	t	57	\N
5428	2	LECTURE	Диференціальні рівняння	93	45	108	t	57	\N
5430	2	LECTURE	Диференціальні рівняння	55	45	108	t	57	\N
5431	2	PRACTICAL	Диференціальні рівняння	51	45	108	t	57	\N
5432	2	PRACTICAL	Диференціальні рівняння	52	45	108	t	57	\N
5433	2	PRACTICAL	Диференціальні рівняння	84	45	108	f	57	\N
5434	2	PRACTICAL	Диференціальні рівняння	93	45	108	f	57	\N
5436	2	PRACTICAL	Диференціальні рівняння	55	45	108	f	57	\N
5437	2	LECTURE	Комп'ютерні мережі	51	50	70	t	57	\N
5438	2	LECTURE	Комп'ютерні мережі	52	50	70	t	57	\N
5439	2	LECTURE	Комп'ютерні мережі	84	50	70	t	57	\N
5440	2	LECTURE	Комп'ютерні мережі	93	50	70	t	57	\N
5442	2	LECTURE	Комп'ютерні мережі	53	50	70	t	57	\N
5443	2	LECTURE	Комп'ютерні мережі	54	50	70	t	57	\N
5444	2	LECTURE	Комп'ютерні мережі	87	50	70	t	57	\N
5446	2	LECTURE	Комп'ютерні мережі	55	50	70	t	57	\N
5449	2	LABORATORY	Комп'ютерні мережі	84	50	70	f	57	\N
5452	2	LABORATORY	Комп'ютерні мережі	53	50	70	f	57	\N
5454	2	LABORATORY	Комп'ютерні мережі	87	50	70	f	57	\N
5457	3	LECTURE	Об'єктно-орієнтоване програмування	51	46	71	t	57	\N
5458	3	LECTURE	Об'єктно-орієнтоване програмування	52	46	71	t	57	\N
5459	3	LECTURE	Об'єктно-орієнтоване програмування	84	46	71	t	57	\N
5460	3	LECTURE	Об'єктно-орієнтоване програмування	93	46	71	t	57	\N
5462	3	LECTURE	Об'єктно-орієнтоване програмування	53	46	71	t	57	\N
5463	3	LECTURE	Об'єктно-орієнтоване програмування	54	46	71	t	57	\N
5464	3	LECTURE	Об'єктно-орієнтоване програмування	87	46	71	t	57	\N
5467	2	LABORATORY	Об'єктно-орієнтоване програмування	52	46	71	f	57	\N
5471	2	LABORATORY	Об'єктно-орієнтоване програмування	53	46	71	f	57	\N
5472	2	LABORATORY	Об'єктно-орієнтоване програмування	54	46	71	f	57	\N
5473	2	LABORATORY	Об'єктно-орієнтоване програмування	87	46	71	f	57	\N
5475	2	LECTURE	Основи інтернет-технологгій	51	40	73	t	57	\N
5476	2	LECTURE	Основи інтернет-технологгій	52	40	73	t	57	\N
5477	2	LECTURE	Основи інтернет-технологгій	84	40	73	t	57	\N
5478	2	LECTURE	Основи інтернет-технологгій	93	40	73	t	57	\N
5453	2	LABORATORY	Комп'ютерні мережі	54	50	233	f	57	\N
5468	2	LABORATORY	Об'єктно-орієнтоване програмування	84	46	75	f	57	\N
5469	2	LABORATORY	Об'єктно-орієнтоване програмування	93	46	75	f	57	\N
5456	2	LABORATORY	Комп'ютерні мережі	55	50	203	f	57	\N
5450	2	LABORATORY	Комп'ютерні мережі	93	50	233	f	57	\N
5448	2	LABORATORY	Комп'ютерні мережі	52	50	70	f	57	\N
5480	2	LECTURE	Основи інтернет-технологгій	53	40	73	t	57	\N
5481	2	LECTURE	Основи інтернет-технологгій	55	40	73	t	57	\N
5482	2	LECTURE	Основи інтернет-технологгій	57	40	73	t	57	\N
5484	2	LABORATORY	Основи інтернет-технологгій	52	40	73	f	57	\N
5486	2	LABORATORY	Основи інтернет-технологгій	93	40	73	f	57	\N
5488	2	LABORATORY	Основи інтернет-технологгій	53	40	73	f	57	\N
5490	2	LABORATORY	Основи інтернет-технологгій	57	40	73	f	57	\N
5483	2	LABORATORY	Основи інтернет-технологгій	51	40	189	f	57	\N
5485	2	LABORATORY	Основи інтернет-технологгій	84	40	189	f	57	\N
5497	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	55	43	149	f	57	\N
5489	2	LABORATORY	Основи інтернет-технологгій	55	40	189	f	57	\N
5844	3	LECTURE	Комплексний аналіз	44	58	22	f	57	\N
5845	2	PRACTICAL	Комплексний аналіз	44	58	22	f	57	\N
5846	3	LECTURE	Теорія міри та інтеграла	44	59	21	f	57	\N
5491	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	51	43	216	f	57	\N
5847	3	PRACTICAL	Теорія міри та інтеграла	44	59	105	f	57	\N
5492	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	52	43	87	f	57	\N
5493	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	84	43	87	f	57	\N
5494	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	93	43	187	f	57	\N
5496	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	53	43	226	f	57	\N
5499	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	54	43	149	f	57	\N
5500	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	87	43	149	f	57	\N
5502	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	56	43	187	f	57	\N
5498	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	57	43	187	f	57	\N
5503	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	36	43	91	f	57	\N
5504	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	37	43	226	f	57	\N
5505	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	95	43	226	f	57	\N
5506	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	94	43	149	f	57	\N
5507	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	39	43	149	f	57	\N
5508	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	40	43	226	f	57	\N
5509	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	103	43	226	f	57	\N
5510	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	102	43	216	f	57	\N
5511	2	PRACTICAL	Іноземна мова (за професійним спрямуванням)	41	43	216	f	57	\N
5530	2	LABORATORY	Програмування мовою Python	51	48	36	f	57	\N
5531	2	LABORATORY	Програмування мовою Python	52	48	36	f	57	\N
5535	2	LABORATORY	Програмування мовою Python	53	48	36	f	57	\N
5575	2	LECTURE	Теорія алгоритмів	93	36	203	t	57	\N
5536	1	LECTURE	Використання MS Excel y BigData	51	258	34	t	57	\N
5537	1	LECTURE	Використання MS Excel y BigData	52	258	34	t	57	\N
5538	1	LECTURE	Використання MS Excel y BigData	84	258	34	t	57	\N
5539	1	LECTURE	Використання MS Excel y BigData	93	258	34	t	57	\N
5541	1	LECTURE	Використання MS Excel y BigData	53	258	34	t	57	\N
5544	2	LABORATORY	Використання MS Excel y BigData	84	258	34	f	57	\N
5545	2	LABORATORY	Використання MS Excel y BigData	93	258	34	f	57	\N
5548	1	LECTURE	Програмування мовою Python	51	48	36	t	57	\N
5549	1	LECTURE	Програмування мовою Python	52	48	36	t	57	\N
5550	1	LECTURE	Програмування мовою Python	84	48	36	t	57	\N
5551	1	LECTURE	Програмування мовою Python	93	48	36	t	57	\N
5553	1	LECTURE	Програмування мовою Python	53	48	36	t	57	\N
5554	2	PRACTICAL	Фізичне виховання	51	13	97	t	57	\N
5555	2	PRACTICAL	Фізичне виховання	52	13	97	t	57	\N
5556	2	PRACTICAL	Фізичне виховання	84	13	97	t	57	\N
5557	2	PRACTICAL	Фізичне виховання	93	13	97	t	57	\N
5558	2	PRACTICAL	Фізичне виховання	54	13	97	t	57	\N
5559	2	PRACTICAL	Фізичне виховання	87	13	97	t	57	\N
5560	2	PRACTICAL	Фізичне виховання	57	13	97	t	57	\N
5561	2	PRACTICAL	Фізичне виховання	36	13	97	t	57	\N
5563	2	PRACTICAL	Фізичне виховання	94	13	97	t	57	\N
5564	2	PRACTICAL	Фізичне виховання	44	13	97	t	57	\N
5566	2	PRACTICAL	Фізичне виховання	40	13	97	t	57	\N
5567	2	PRACTICAL	Фізичне виховання	103	13	97	t	57	\N
5568	2	PRACTICAL	Фізичне виховання	102	13	97	t	57	\N
5569	2	PRACTICAL	Громадське здоров'я та медицина порятунку	51	49	97	t	57	\N
5570	2	PRACTICAL	Громадське здоров'я та медицина порятунку	93	49	97	t	57	\N
5571	2	LECTURE	Теорія алгоритмів	53	36	203	t	57	\N
5572	2	LECTURE	Теорія алгоритмів	51	36	203	t	57	\N
5573	2	LECTURE	Теорія алгоритмів	52	36	203	t	57	\N
5574	2	LECTURE	Теорія алгоритмів	84	36	203	t	57	\N
5577	3	LABORATORY	Теорія алгоритмів	53	36	203	f	57	\N
5580	3	LABORATORY	Теорія алгоритмів	84	36	203	f	57	\N
5581	3	LABORATORY	Теорія алгоритмів	93	36	203	f	57	\N
5578	3	LABORATORY	Теорія алгоритмів	51	36	33	f	57	\N
5579	3	LABORATORY	Теорія алгоритмів	52	36	33	f	57	\N
5466	2	LABORATORY	Об'єктно-орієнтоване програмування	51	46	75	f	57	\N
5542	2	LABORATORY	Використання MS Excel y BigData	51	258	31	f	57	\N
5543	2	LABORATORY	Використання MS Excel y BigData	52	258	31	f	57	\N
5532	2	LABORATORY	Програмування мовою Python	84	48	221	f	57	\N
5533	2	LABORATORY	Програмування мовою Python	93	48	221	f	57	\N
5583	2	LECTURE	Прикладний функціональний аналіз	53	51	21	t	57	\N
5584	2	LECTURE	Прикладний функціональний аналіз	54	51	21	t	57	\N
5565	2	PRACTICAL	Фізичне виховання	42	13	97	f	57	\N
5447	2	LABORATORY	Комп'ютерні мережі	51	50	233	f	57	\N
5562	2	PRACTICAL	Фізичне виховання	37	13	97	f	57	\N
5585	2	LECTURE	Прикладний функціональний аналіз	87	51	21	t	57	\N
5587	1	PRACTICAL	Прикладний функціональний аналіз	53	51	21	t	57	\N
5588	1	PRACTICAL	Прикладний функціональний аналіз	54	51	21	t	57	\N
5589	1	PRACTICAL	Прикладний функціональний аналіз	87	51	21	t	57	\N
5547	2	LABORATORY	Використання MS Excel y BigData	53	258	31	f	57	\N
5591	2	LECTURE	Диференціальні рівняння	53	45	230	t	57	\N
5592	2	LECTURE	Диференціальні рівняння	54	45	230	t	57	\N
5593	2	LECTURE	Диференціальні рівняння	87	45	230	t	57	\N
5595	2	LECTURE	Диференціальні рівняння	56	45	230	t	57	\N
5596	2	LECTURE	Диференціальні рівняння	57	45	230	t	57	\N
5597	2	PRACTICAL	Диференціальні рівняння	53	45	230	f	57	\N
5598	2	PRACTICAL	Диференціальні рівняння	54	45	230	f	57	\N
5599	2	PRACTICAL	Диференціальні рівняння	87	45	230	f	57	\N
5601	2	PRACTICAL	Диференціальні рівняння	56	45	230	f	57	\N
5602	2	PRACTICAL	Диференціальні рівняння	57	45	230	f	57	\N
5603	2	LECTURE	Бази даних та знань	54	184	34	t	57	\N
5604	2	LECTURE	Бази даних та знань	87	184	34	t	57	\N
5606	3	LABORATORY	Бази даних та знань	54	184	63	f	57	\N
5607	3	LABORATORY	Бази даних та знань	87	184	34	f	57	\N
5609	2	LECTURE	Алгоритми і структури даних	54	44	190	t	57	\N
5610	2	LECTURE	Алгоритми і структури даних	87	44	190	t	57	\N
5612	2	LABORATORY	Алгоритми і структури даних	54	44	190	f	57	\N
5613	2	LABORATORY	Алгоритми і структури даних	87	44	190	f	57	\N
5615	2	LECTURE	Психологія (загальна, вікова, педагогічна)	55	52	76	t	57	\N
5616	2	LECTURE	Психологія (загальна, вікова, педагогічна)	56	52	76	t	57	\N
5617	2	PRACTICAL	Психологія (загальна, вікова, педагогічна)	55	52	76	f	57	\N
5618	2	PRACTICAL	Психологія (загальна, вікова, педагогічна)	56	52	76	f	57	\N
5619	2	LECTURE	Дискретна математика	55	17	199	t	57	\N
5620	2	LECTURE	Дискретна математика	56	17	199	t	57	\N
5621	2	LECTURE	Дискретна математика	57	17	199	t	57	\N
5622	1	PRACTICAL	Дискретна математика	55	17	199	f	57	\N
5623	1	PRACTICAL	Дискретна математика	56	17	199	f	57	\N
5624	2	PRACTICAL	Дискретна математика	57	17	199	f	57	\N
5625	2	LECTURE	Об'єктно-орієнтоване програмування	55	46	32	f	57	\N
5626	2	LABORATORY	Об'єктно-орієнтоване програмування	55	46	32	f	57	\N
5627	2	LECTURE	Бази даних у навчальному процесі	56	324	34	f	57	\N
5628	2	LABORATORY	Бази даних у навчальному процесі	56	324	63	f	57	\N
5629	1	LECTURE	Основи інформаційних систем та технологій	56	53	194	f	57	\N
5630	2	LABORATORY	Основи інформаційних систем та технологій	56	53	194	f	57	\N
5633	2	PRACTICAL	Алгебра і теорія чисел	56	56	47	t	57	\N
5634	2	PRACTICAL	Алгебра і теорія чисел	57	56	47	t	57	\N
5635	1	LECTURE	Практикум з тригонометрії	56	341	44	t	57	\N
5636	1	LECTURE	Практикум з тригонометрії	57	341	44	t	57	\N
5639	4	LECTURE	Математичний аналіз2	57	54	26	f	57	\N
5640	4	PRACTICAL	Математичний аналіз2	57	54	105	f	57	\N
5641	2	LECTURE	Комп'ютерне моделювання жорстких процесів та систем	36	328	30	t	57	\N
5642	2	LECTURE	Комп'ютерне моделювання жорстких процесів та систем	37	328	30	t	57	\N
5643	2	LECTURE	Комп'ютерне моделювання жорстких процесів та систем	95	328	30	t	57	\N
5644	2	LECTURE	Комп'ютерне моделювання жорстких процесів та систем	94	328	30	t	57	\N
5645	2	LECTURE	Комп'ютерне моделювання жорстких процесів та систем	39	328	30	t	57	\N
5647	2	LABORATORY	Комп'ютерне моделювання жорстких процесів та систем	95	328	30	f	57	\N
5646	2	LABORATORY	Комп'ютерне моделювання жорстких процесів та систем	36	328	63	f	57	\N
5648	2	LABORATORY	Комп'ютерне моделювання жорстких процесів та систем	37	328	63	f	57	\N
5649	2	LABORATORY	Комп'ютерне моделювання жорстких процесів та систем	94	328	63	f	57	\N
5650	2	LABORATORY	Комп'ютерне моделювання жорстких процесів та систем	39	328	63	f	57	\N
5656	2	LABORATORY	Операційні системи	36	27	42	f	57	\N
5657	2	LABORATORY	Операційні системи	37	27	42	f	57	\N
5661	2	LABORATORY	Операційні системи	42	27	42	f	57	\N
5668	2	LECTURE	Основи штучного інтелекту	36	329	32	t	57	\N
5669	2	LECTURE	Основи штучного інтелекту	37	329	32	t	57	\N
5670	2	LECTURE	Основи штучного інтелекту	95	329	32	t	57	\N
5671	2	LECTURE	Основи штучного інтелекту	94	329	32	t	57	\N
5672	2	LECTURE	Основи штучного інтелекту	39	329	32	t	57	\N
5673	2	LECTURE	Основи штучного інтелекту	44	329	32	t	57	\N
5675	2	LABORATORY	Основи штучного інтелекту	37	329	32	f	57	\N
5677	2	LABORATORY	Основи штучного інтелекту	94	329	32	f	57	\N
5678	2	LABORATORY	Основи штучного інтелекту	39	329	32	f	57	\N
5679	2	LABORATORY	Основи штучного інтелекту	44	329	32	f	57	\N
5680	2	LECTURE	Теорія ймовірностей та математична статистика	36	30	35	t	57	\N
5681	2	LECTURE	Теорія ймовірностей та математична статистика	37	30	35	t	57	\N
5682	2	LECTURE	Теорія ймовірностей та математична статистика	95	30	35	t	57	\N
5683	2	LECTURE	Теорія ймовірностей та математична статистика	94	30	35	t	57	\N
5684	2	LECTURE	Теорія ймовірностей та математична статистика	39	30	35	t	57	\N
5685	2	LECTURE	Теорія ймовірностей та математична статистика	40	30	35	t	57	\N
5686	2	LECTURE	Теорія ймовірностей та математична статистика	103	30	35	t	57	\N
5687	2	LECTURE	Теорія ймовірностей та математична статистика	102	30	35	t	57	\N
5688	2	LECTURE	Теорія ймовірностей та математична статистика	41	30	35	t	57	\N
5659	2	LABORATORY	Операційні системи	94	27	189	f	57	\N
5660	2	LABORATORY	Операційні системи	39	27	189	f	57	\N
5676	2	LABORATORY	Основи штучного інтелекту	95	329	221	f	57	\N
5662	1	LECTURE	Операційні системи	36	27	42	t	57	\N
5663	1	LECTURE	Операційні системи	37	27	42	t	57	\N
5658	2	LABORATORY	Операційні системи	95	27	189	f	57	\N
5690	3	PRACTICAL	Теорія ймовірностей та математична статистика	37	30	40	f	57	\N
5637	1	PRACTICAL	Практикум з тригонометрії	56	341	44	t	57	\N
5689	3	PRACTICAL	Теорія ймовірностей та математична статистика	36	30	40	f	57	\N
5638	1	PRACTICAL	Практикум з тригонометрії	57	341	44	t	57	\N
5694	3	PRACTICAL	Теорія ймовірностей та математична статистика	40	30	40	t	57	\N
5695	3	PRACTICAL	Теорія ймовірностей та математична статистика	103	30	40	t	57	\N
5696	3	PRACTICAL	Теорія ймовірностей та математична статистика	102	30	40	t	57	\N
5697	3	PRACTICAL	Теорія ймовірностей та математична статистика	41	30	40	t	57	\N
5698	1	LECTURE	Поглиблена 3D графіка	36	181	42	t	57	\N
5699	1	LECTURE	Поглиблена 3D графіка	37	181	42	t	57	\N
5700	1	LECTURE	Поглиблена 3D графіка	95	181	42	t	57	\N
5701	1	LECTURE	Поглиблена 3D графіка	94	181	42	t	57	\N
5702	1	LECTURE	Поглиблена 3D графіка	39	181	42	t	57	\N
5703	1	LECTURE	Поглиблена 3D графіка	44	181	42	t	57	\N
5704	2	LABORATORY	Поглиблена 3D графіка	36	181	42	f	57	\N
5705	2	LABORATORY	Поглиблена 3D графіка	37	181	42	f	57	\N
5706	2	LABORATORY	Поглиблена 3D графіка	95	181	42	f	57	\N
5707	2	LABORATORY	Поглиблена 3D графіка	94	181	42	f	57	\N
5708	2	LABORATORY	Поглиблена 3D графіка	39	181	42	f	57	\N
5709	2	LABORATORY	Поглиблена 3D графіка	44	181	42	f	57	\N
5710	2	LECTURE	Створення веб-додатків з використанням фреймворку Django мови Python	36	325	36	t	57	\N
5711	2	LECTURE	Створення веб-додатків з використанням фреймворку Django мови Python	37	325	36	t	57	\N
5712	2	LECTURE	Створення веб-додатків з використанням фреймворку Django мови Python	95	325	36	t	57	\N
5713	2	LECTURE	Створення веб-додатків з використанням фреймворку Django мови Python	94	325	36	t	57	\N
5714	2	LECTURE	Створення веб-додатків з використанням фреймворку Django мови Python	44	325	36	t	57	\N
5715	2	LECTURE	Створення веб-додатків з використанням фреймворку Django мови Python	42	325	36	t	57	\N
5716	2	LABORATORY	Створення веб-додатків з використанням фреймворку Django мови Python	36	325	36	f	57	\N
5717	2	LABORATORY	Створення веб-додатків з використанням фреймворку Django мови Python	37	325	36	f	57	\N
5718	2	LABORATORY	Створення веб-додатків з використанням фреймворку Django мови Python	95	325	36	f	57	\N
5719	2	LABORATORY	Створення веб-додатків з використанням фреймворку Django мови Python	94	325	36	f	57	\N
5720	2	LABORATORY	Створення веб-додатків з використанням фреймворку Django мови Python	44	325	36	f	57	\N
5721	2	LABORATORY	Створення веб-додатків з використанням фреймворку Django мови Python	42	325	36	f	57	\N
5722	1	LECTURE	Сучасні СУБД	36	35	34	t	57	\N
5723	1	LECTURE	Сучасні СУБД	37	35	34	t	57	\N
5724	1	LECTURE	Сучасні СУБД	95	35	34	t	57	\N
5725	1	LECTURE	Сучасні СУБД	94	35	34	t	57	\N
5726	1	LECTURE	Сучасні СУБД	39	35	34	t	57	\N
5727	2	LABORATORY	Сучасні СУБД	36	35	34	f	57	\N
5728	2	LABORATORY	Сучасні СУБД	37	35	34	f	57	\N
5729	2	LABORATORY	Сучасні СУБД	95	35	34	t	57	\N
5730	2	LABORATORY	Сучасні СУБД	94	35	34	t	57	\N
5731	2	LABORATORY	Сучасні СУБД	39	35	34	t	57	\N
5732	2	LECTURE	Технології програмування на Java	36	32	62	t	57	\N
5733	2	LECTURE	Технології програмування на Java	37	32	62	t	57	\N
5734	2	LECTURE	Технології програмування на Java	95	32	62	t	57	\N
5735	2	LECTURE	Технології програмування на Java	94	32	62	t	57	\N
5736	2	LECTURE	Технології програмування на Java	39	32	62	t	57	\N
5737	2	LECTURE	Технології програмування на Java	40	32	62	t	57	\N
5738	2	LECTURE	Технології програмування на Java	103	32	62	t	57	\N
5739	2	LECTURE	Технології програмування на Java	102	32	62	t	57	\N
5693	3	PRACTICAL	Теорія ймовірностей та математична статистика	39	30	35	f	57	\N
5692	3	PRACTICAL	Теорія ймовірностей та математична статистика	94	30	35	f	57	\N
5740	2	LECTURE	Технології програмування на Java	41	32	62	t	57	\N
5741	2	PRACTICAL	Технології програмування на Java	36	32	220	f	57	\N
5742	2	PRACTICAL	Технології програмування на Java	37	32	220	f	57	\N
5746	1	LECTURE	Фреймворки JavaScript	36	330	61	t	57	\N
5747	1	LECTURE	Фреймворки JavaScript	37	330	61	t	57	\N
5748	1	LECTURE	Фреймворки JavaScript	95	330	61	t	57	\N
5749	1	LECTURE	Фреймворки JavaScript	94	330	61	t	57	\N
5750	1	LECTURE	Фреймворки JavaScript	39	330	61	t	57	\N
5753	2	LABORATORY	Фреймворки JavaScript	95	330	61	f	57	\N
5754	2	LABORATORY	Фреймворки JavaScript	94	330	61	f	57	\N
5756	2	LECTURE	Основи теорії систем	36	37	64	t	57	\N
5757	2	LECTURE	Основи теорії систем	37	37	64	t	57	\N
5758	2	LECTURE	Основи теорії систем	95	37	64	t	57	\N
5759	2	LECTURE	Основи теорії систем	94	37	64	t	57	\N
5760	2	LECTURE	Основи теорії систем	39	37	64	t	57	\N
5761	2	LABORATORY	Основи теорії систем	36	37	64	t	57	\N
5762	2	LABORATORY	Основи теорії систем	37	37	64	t	57	\N
5763	2	LABORATORY	Основи теорії систем	95	37	64	t	57	\N
5764	2	LABORATORY	Основи теорії систем	94	37	64	t	57	\N
5765	2	LABORATORY	Основи теорії систем	39	37	64	t	57	\N
5752	2	LABORATORY	Фреймворки JavaScript	37	330	189	f	57	\N
5751	2	LABORATORY	Фреймворки JavaScript	36	330	189	f	57	\N
5674	2	LABORATORY	Основи штучного інтелекту	36	329	221	f	57	\N
5743	2	LABORATORY	Технології програмування на Java	95	32	220	f	57	\N
5744	2	LABORATORY	Технології програмування на Java	94	32	220	f	57	\N
5664	1	LECTURE	Операційні системи	95	27	42	t	57	\N
5665	1	LECTURE	Операційні системи	94	27	42	t	57	\N
5666	1	LECTURE	Операційні системи	39	27	42	t	57	\N
5667	1	LECTURE	Операційні системи	42	27	42	t	57	\N
5745	2	LABORATORY	Технології програмування на Java	39	32	220	f	57	\N
5755	2	LABORATORY	Фреймворки JavaScript	39	330	189	f	57	\N
5766	2	LECTURE	Числові методи	40	39	65	t	57	\N
5767	2	LECTURE	Числові методи	103	39	65	t	57	\N
5768	2	LECTURE	Числові методи	102	39	65	t	57	\N
5769	2	LECTURE	Числові методи	41	39	65	t	57	\N
5770	2	LABORATORY	Числові методи	40	39	65	t	57	\N
5771	2	LABORATORY	Числові методи	103	39	65	t	57	\N
5772	2	LABORATORY	Числові методи	102	39	75	t	57	\N
5773	2	LABORATORY	Числові методи	41	39	75	t	57	\N
5774	2	LABORATORY	Технології програмування на Java	40	32	62	f	57	\N
5775	2	LABORATORY	Технології програмування на Java	103	32	62	f	57	\N
5776	2	LABORATORY	Технології програмування на Java	102	32	62	f	57	\N
5777	2	LABORATORY	Технології програмування на Java	41	32	62	f	57	\N
5778	2	LECTURE	Математична теорія ризиків	40	41	66	t	57	\N
5779	2	LECTURE	Математична теорія ризиків	103	41	66	t	57	\N
5780	2	LECTURE	Математична теорія ризиків	102	41	66	t	57	\N
5781	2	LECTURE	Математична теорія ризиків	41	41	66	t	57	\N
5782	2	LABORATORY	Математична теорія ризиків	40	41	66	f	57	\N
5783	2	LABORATORY	Математична теорія ризиків	103	41	66	f	57	\N
5784	2	LABORATORY	Математична теорія ризиків	102	41	66	f	57	\N
5785	2	LABORATORY	Математична теорія ризиків	41	41	66	f	57	\N
5786	2	LECTURE	Комп'ютерна математика	40	42	60	t	57	\N
5787	2	LECTURE	Комп'ютерна математика	103	42	60	t	57	\N
5788	2	LECTURE	Комп'ютерна математика	102	42	60	t	57	\N
5789	2	LECTURE	Комп'ютерна математика	41	42	60	t	57	\N
5790	1	LABORATORY	Комп'ютерна математика	40	42	60	f	57	\N
5791	1	LABORATORY	Комп'ютерна математика	103	42	60	f	57	\N
5792	1	LABORATORY	Комп'ютерна математика	102	42	60	f	57	\N
5793	1	LABORATORY	Комп'ютерна математика	41	42	60	f	57	\N
5794	2	LECTURE	Управління проектами	40	331	67	t	57	\N
5795	2	LECTURE	Управління проектами	103	331	67	t	57	\N
5796	2	LECTURE	Управління проектами	102	331	67	t	57	\N
5797	2	LECTURE	Управління проектами	41	331	67	t	57	\N
5798	1	LABORATORY	Управління проектами	40	331	67	f	57	\N
5799	1	LABORATORY	Управління проектами	103	331	67	f	57	\N
5800	1	LABORATORY	Управління проектами	102	331	67	f	57	\N
5801	1	LABORATORY	Управління проектами	41	331	67	f	57	\N
5802	2	LECTURE	Web-дизайн	40	205	220	t	57	\N
5803	2	LECTURE	Web-дизайн	103	205	220	t	57	\N
5804	2	LECTURE	Web-дизайн	102	205	220	t	57	\N
5805	2	LECTURE	Web-дизайн	41	205	220	t	57	\N
5806	1	LABORATORY	Web-дизайн	40	205	220	f	57	\N
5807	1	LABORATORY	Web-дизайн	103	205	220	f	57	\N
5808	1	LABORATORY	Web-дизайн	102	205	220	f	57	\N
5809	1	LABORATORY	Web-дизайн	41	205	220	f	57	\N
5810	2	LECTURE	Бази даних та інформаційні системи	42	326	34	f	57	\N
5811	2	LABORATORY	Бази даних та інформаційні системи	42	326	34	f	57	\N
5812	2	LECTURE	Методика викладання інформатики	42	64	205	f	57	\N
5813	2	LABORATORY	Методика викладання інформатики	42	64	205	f	57	\N
5818	2	LECTURE	Методика позакласної роботи з інформатики	42	382	79	f	57	\N
5819	2	LABORATORY	Методика позакласної роботи з інформатики	42	382	79	f	57	\N
5820	1	LECTURE	Векторна та растрова графіка	42	191	77	f	57	\N
5821	1	PRACTICAL	Векторна та растрова графіка	42	191	77	f	57	\N
5823	2	LABORATORY	Розробка програмних додатків для мобільних пристроїв	42	217	61	f	57	\N
5824	2	LECTURE	Розробка програмних додатків для мобільних пристроїв	42	217	61	t	57	\N
5825	2	LECTURE	Розробка програмних додатків для мобільних пристроїв	45	217	61	t	57	\N
5826	2	LECTURE	Розробка програмних додатків для мобільних пристроїв	104	217	61	t	57	\N
5827	2	LECTURE	Розробка програмних додатків для мобільних пристроїв	49	217	61	t	57	\N
5828	2	LECTURE	Розробка програмних додатків для мобільних пристроїв	50	217	61	t	57	\N
5829	2	LECTURE	Розробка програмних додатків для мобільних пристроїв	71	217	61	t	57	\N
5830	2	LECTURE	Основи інклюзивної освіти	43	264	191	f	57	\N
5831	1	PRACTICAL	Основи інклюзивної освіти	43	264	191	f	57	\N
5832	2	LECTURE	Методика викладання математики	43	63	46	f	57	\N
5833	2	PRACTICAL	Методика викладання математики	43	63	46	f	57	\N
5834	2	LECTURE	Методика викладання інформатики	43	64	45	f	57	\N
5835	2	LABORATORY	Методика викладання інформатики	43	64	45	f	57	\N
5840	1	LECTURE	Стереометрія в задачах	43	269	46	f	57	\N
5841	2	PRACTICAL	Стереометрія в задачах	43	269	46	f	57	\N
5842	2	LECTURE	Диференціальна геометрія	44	57	44	f	57	\N
5843	2	PRACTICAL	Диференціальна геометрія	44	57	44	f	57	\N
5838	2	PRACTICAL	Олімпіадні задачі з алгебри і теорії чисел	43	271	105	f	57	\N
5837	1	LECTURE	Олімпіадні задачі з алгебри і теорії чисел	71	271	105	f	57	\N
5839	2	PRACTICAL	Олімпіадні задачі з алгебри і теорії чисел	71	271	105	f	57	\N
5815	1	LECTURE	Здоров'язбережувальні технології та домедична допомога	43	332	231	f	57	\N
5814	1	LECTURE	Здоров'язбережувальні технології та домедична допомога	42	332	234	f	57	\N
5816	2	PRACTICAL	Здоров'язбережувальні технології та домедична допомога	42	332	234	f	57	\N
5848	3	LECTURE	Рівняння математичної фізики	44	60	232	f	57	\N
5849	2	PRACTICAL	Рівняння математичної фізики	44	60	232	f	57	\N
5850	2	LECTURE	Елементарна математика і методика викладання математики	44	61	46	f	57	\N
5851	2	PRACTICAL	Елементарна математика і методика викладання математики	44	61	46	f	57	\N
5852	2	LECTURE	Методи оптимізації та дослідження операцій	45	66	40	t	57	\N
5853	2	LECTURE	Методи оптимізації та дослідження операцій	104	66	40	t	57	\N
5854	2	LECTURE	Методи оптимізації та дослідження операцій	49	66	40	t	57	\N
5855	2	LECTURE	Методи оптимізації та дослідження операцій	50	66	40	t	57	\N
5857	1	PRACTICAL	Методи оптимізації та дослідження операцій	45	66	35	f	57	\N
5858	1	PRACTICAL	Методи оптимізації та дослідження операцій	104	66	35	f	57	\N
5859	1	PRACTICAL	Методи оптимізації та дослідження операцій	49	66	40	t	57	\N
5860	1	PRACTICAL	Методи оптимізації та дослідження операцій	50	66	40	t	57	\N
5861	2	LECTURE	Платформи корпоративних інформаційних систем	45	67	80	t	57	\N
5862	2	LECTURE	Платформи корпоративних інформаційних систем	104	67	80	t	57	\N
5863	2	LECTURE	Платформи корпоративних інформаційних систем	49	67	80	t	57	\N
5864	2	LECTURE	Платформи корпоративних інформаційних систем	50	67	80	t	57	\N
5865	2	LABORATORY	Платформи корпоративних інформаційних систем	45	67	80	f	57	\N
5866	2	LABORATORY	Платформи корпоративних інформаційних систем	104	67	80	f	57	\N
5867	2	LABORATORY	Платформи корпоративних інформаційних систем	49	67	80	f	57	\N
5868	2	LABORATORY	Платформи корпоративних інформаційних систем	50	67	80	f	57	\N
5869	1	LECTURE	Системи та методи прийняття рішень	45	69	40	t	57	\N
5870	1	LECTURE	Системи та методи прийняття рішень	104	69	40	t	57	\N
5871	1	LECTURE	Системи та методи прийняття рішень	49	69	40	t	57	\N
5872	1	LECTURE	Системи та методи прийняття рішень	50	69	40	t	57	\N
5873	2	LABORATORY	Системи та методи прийняття рішень	45	69	40	f	57	\N
5874	2	LABORATORY	Системи та методи прийняття рішень	104	69	40	f	57	\N
5875	2	LABORATORY	Системи та методи прийняття рішень	49	69	40	f	57	\N
5876	2	LABORATORY	Системи та методи прийняття рішень	50	69	40	f	57	\N
5877	2	LECTURE	Інформаційні системи обліку та логістика	45	70	73	t	57	\N
5878	2	LECTURE	Інформаційні системи обліку та логістика	104	70	73	t	57	\N
5879	2	LECTURE	Інформаційні системи обліку та логістика	49	70	73	t	57	\N
5880	2	LECTURE	Інформаційні системи обліку та логістика	50	70	73	t	57	\N
5881	2	LABORATORY	Інформаційні системи обліку та логістика	45	70	73	f	57	\N
5882	2	LABORATORY	Інформаційні системи обліку та логістика	104	70	73	f	57	\N
5883	2	LABORATORY	Інформаційні системи обліку та логістика	49	70	73	f	57	\N
5884	2	LABORATORY	Інформаційні системи обліку та логістика	50	70	73	f	57	\N
5885	2	PRACTICAL	Комунікаційні технології в управлінні проектами	45	71	42	f	57	\N
5887	2	PRACTICAL	Комунікаційні технології в управлінні проектами	49	71	42	f	57	\N
5890	2	LABORATORY	Розробка програмних додатків для мобільних пристроїв	104	217	61	f	57	\N
5886	2	PRACTICAL	Комунікаційні технології в управлінні проектами	104	71	107	f	57	\N
5888	2	PRACTICAL	Комунікаційні технології в управлінні проектами	50	71	107	f	57	\N
5856	2	LECTURE	Методи оптимізації та дослідження операцій	71	66	40	f	57	\N
5889	2	LABORATORY	Розробка програмних додатків для мобільних пристроїв	45	217	61	f	57	\N
5892	2	LABORATORY	Розробка програмних додатків для мобільних пристроїв	50	217	61	f	57	\N
5895	2	LABORATORY	Розробка програмних додатків для мобільних пристроїв	71	217	61	f	57	\N
5896	2	LECTURE	Теорія керування	45	72	37	t	57	\N
5897	2	LECTURE	Теорія керування	104	72	37	t	57	\N
5898	2	LECTURE	Теорія керування	50	72	37	t	57	\N
5899	2	LECTURE	Теорія керування	49	72	37	t	57	\N
5900	2	LABORATORY	Теорія керування	45	72	37	t	57	\N
5901	2	LABORATORY	Теорія керування	104	72	37	t	57	\N
5902	2	LABORATORY	Теорія керування	49	72	37	t	57	\N
5903	2	LABORATORY	Теорія керування	50	72	37	f	57	\N
5904	1	LECTURE	Управління ІТ проектами	45	331	34	t	57	\N
5905	1	LECTURE	Управління ІТ проектами	104	331	34	t	57	\N
5906	1	LECTURE	Управління ІТ проектами	50	331	34	t	57	\N
5907	1	LECTURE	Управління ІТ проектами	49	331	34	t	57	\N
5908	1	LECTURE	Управління ІТ проектами	45	331	61	t	57	\N
5909	1	LECTURE	Управління ІТ проектами	104	331	61	t	57	\N
5910	1	LECTURE	Управління ІТ проектами	50	331	61	t	57	\N
5911	1	LECTURE	Управління ІТ проектами	49	331	61	t	57	\N
5912	1	LABORATORY	Управління ІТ проектами	45	331	34	f	57	\N
5913	1	LABORATORY	Управління ІТ проектами	104	331	34	f	57	\N
5914	1	LABORATORY	Управління ІТ проектами	49	331	61	t	57	\N
5915	1	LABORATORY	Управління ІТ проектами	50	331	61	t	57	\N
5916	2	LECTURE	Прикладний статистичний аналіз з використанням Python	45	337	36	t	57	\N
5917	2	LECTURE	Прикладний статистичний аналіз з використанням Python	50	337	36	t	57	\N
5918	2	LABORATORY	Прикладний статистичний аналіз з використанням Python	45	337	36	t	57	\N
5919	2	LABORATORY	Прикладний статистичний аналіз з використанням Python	50	337	36	t	57	\N
5923	2	LECTURE	Нечітка логіка в інтелектуальних системах	45	379	35	t	57	\N
5924	2	LECTURE	Нечітка логіка в інтелектуальних системах	50	379	35	t	57	\N
5925	2	LECTURE	Нечітка логіка в інтелектуальних системах	104	379	35	t	57	\N
5926	2	LECTURE	Нечітка логіка в інтелектуальних системах	49	379	35	t	57	\N
5927	2	LABORATORY	Нечітка логіка в інтелектуальних системах	104	379	35	t	57	\N
5928	2	LABORATORY	Нечітка логіка в інтелектуальних системах	49	379	35	t	57	\N
5929	2	LABORATORY	Розробка програмних додатків для мобільних пристроїв	49	217	61	f	57	\N
5930	2	LABORATORY	Нечітка логіка в інтелектуальних системах	45	379	35	f	57	\N
5931	2	LABORATORY	Нечітка логіка в інтелектуальних системах	50	379	35	f	57	\N
5921	2	PRACTICAL	Випадкові процеси	45	74	166	f	57	\N
5920	2	LECTURE	Випадкові процеси	45	74	166	f	57	\N
5922	2	PRACTICAL	Випадкові процеси	50	74	166	f	57	\N
5932	2	LECTURE	Випадкові процеси	50	74	166	f	57	\N
5933	2	LECTURE	Операційні системи	68	27	60	t	57	\N
5934	2	LECTURE	Операційні системи	70	27	60	t	57	\N
5935	2	LABORATORY	Операційні системи	68	27	60	f	57	\N
5936	2	LABORATORY	Операційні системи	70	27	60	f	57	\N
5937	2	LECTURE	Методи оптимізації	68	75	35	t	57	\N
5938	2	LECTURE	Методи оптимізації	70	75	35	t	57	\N
5939	1	PRACTICAL	Методи оптимізації	68	75	35	t	57	\N
5940	1	PRACTICAL	Методи оптимізації	70	75	35	t	57	\N
5941	2	LABORATORY	Методи оптимізації	68	75	35	t	57	\N
5942	2	LABORATORY	Методи оптимізації	70	75	35	t	57	\N
5943	2	LECTURE	Основи математичного моделювання та системного аналізу	68	76	81	t	57	\N
5944	2	LECTURE	Основи математичного моделювання та системного аналізу	70	76	81	t	57	\N
5945	2	LABORATORY	Основи математичного моделювання та системного аналізу	68	76	81	f	57	\N
5946	2	LABORATORY	Основи математичного моделювання та системного аналізу	70	76	81	f	57	\N
5947	2	LECTURE	Технології програмування мовою Python	68	77	19	t	57	\N
5948	2	LECTURE	Технології програмування мовою Python	70	77	19	t	57	\N
5949	2	LABORATORY	Технології програмування мовою Python	68	77	19	f	57	\N
5950	2	LABORATORY	Технології програмування мовою Python	70	77	19	f	57	\N
5951	1	LECTURE	Frontend-розробка Web-додатків	68	78	195	t	57	\N
5952	1	LECTURE	Frontend-розробка Web-додатків	70	78	195	t	57	\N
5953	2	LABORATORY	Frontend-розробка Web-додатків	68	78	195	t	57	\N
5954	2	LABORATORY	Frontend-розробка Web-додатків	70	78	195	t	57	\N
5955	2	LECTURE	C# та NET: Розробка програмного забезпечення	68	383	66	t	57	\N
5956	2	LECTURE	C# та NET: Розробка програмного забезпечення	70	383	66	t	57	\N
5957	2	LABORATORY	C# та NET: Розробка програмного забезпечення	68	383	66	t	57	\N
5958	2	LABORATORY	C# та NET: Розробка програмного забезпечення	70	383	66	t	57	\N
5959	1	LECTURE	Основи DevOps	68	339	62	t	57	\N
5960	1	LECTURE	Основи DevOps	70	339	62	t	57	\N
5961	2	LABORATORY	Основи DevOps	68	339	62	t	57	\N
5962	2	LABORATORY	Основи DevOps	70	339	62	t	57	\N
5836	1	LECTURE	Олімпіадні задачі з алгебри і теорії чисел	43	271	105	f	57	\N
5963	1	LECTURE	Олімпіадні задачі з алгебри і теорії чисел	73	271	105	f	57	\N
5964	2	PRACTICAL	Олімпіадні задачі з алгебри і теорії чисел	73	271	105	f	57	\N
5965	1	PRACTICAL	Методи оптимізації та дослідження операцій	71	66	40	f	57	\N
5966	3	LECTURE	Варіаційне числення і методи оптимізації	71	222	82	f	57	\N
5967	2	PRACTICAL	Варіаційне числення і методи оптимізації	71	222	82	f	57	\N
5968	2	LECTURE	Математична логіка	71	86	28	t	57	\N
5969	2	LECTURE	Математична логіка	73	86	28	t	57	\N
5970	1	PRACTICAL	Математична логіка	71	86	28	t	57	\N
5971	1	PRACTICAL	Математична логіка	73	86	28	t	57	\N
5972	2	LECTURE	Математична статистика з елементами теорії випадкових процесів	71	342	26	f	57	\N
5973	1	PRACTICAL	Математична статистика з елементами теорії випадкових процесів	71	342	26	f	57	\N
5974	2	LECTURE	Перші типи топологічних векторних просторів	71	384	21	f	57	\N
5975	1	PRACTICAL	Перші типи топологічних векторних просторів	71	384	21	f	57	\N
5976	1	LECTURE	Задачі прикладного характеру	71	268	45	t	57	\N
5977	1	LECTURE	Задачі прикладного характеру	72	268	45	t	57	\N
5978	1	LECTURE	Задачі прикладного характеру	73	268	45	t	57	\N
5984	2	LECTURE	Історія математики	71	267	78	t	57	\N
5985	2	LECTURE	Історія математики	73	267	78	t	57	\N
5979	2	PRACTICAL	Задачі прикладного характеру	71	268	45	t	57	\N
5980	2	PRACTICAL	Задачі прикладного характеру	72	268	45	t	57	\N
5981	2	PRACTICAL	Задачі прикладного характеру	73	268	45	t	57	\N
5986	2	LECTURE	Базові алгоритми олімпіадних задач з інформатики	73	224	203	t	57	\N
5987	2	LECTURE	Базові алгоритми олімпіадних задач з інформатики	72	224	203	t	57	\N
5988	2	LABORATORY	Базові алгоритми олімпіадних задач з інформатики	73	224	203	f	57	\N
5989	2	LABORATORY	Базові алгоритми олімпіадних задач з інформатики	72	224	203	f	57	\N
5990	1	LECTURE	Вибрані питання шкільного курсу математики	73	365	49	t	57	\N
5991	1	LECTURE	Вибрані питання шкільного курсу математики	72	365	49	t	57	\N
5992	2	PRACTICAL	Вибрані питання шкільного курсу математики	73	365	49	t	57	\N
5993	2	PRACTICAL	Вибрані питання шкільного курсу математики	72	365	49	t	57	\N
5994	1	LECTURE	Стереометрія в задачах	73	269	46	f	57	\N
5995	2	PRACTICAL	Стереометрія в задачах	73	269	46	f	57	\N
5996	1	LECTURE	Методика організації позаурочної роботи з математики	73	318	49	f	57	\N
5997	2	PRACTICAL	Методика організації позаурочної роботи з математики	73	318	49	f	57	\N
5998	2	LECTURE	Методика розв'язування олімп. задач з ІТ	73	82	78	t	57	\N
5999	2	LECTURE	Методика розв'язування олімп. задач з ІТ	72	82	78	t	57	\N
6000	2	LABORATORY	Методика розв'язування олімп. задач з ІТ	73	82	78	f	57	\N
6001	2	LABORATORY	Методика розв'язування олімп. задач з ІТ	72	82	78	f	57	\N
6002	1	LECTURE	Основи інформаційної безпеки	72	201	61	f	57	\N
6003	1	LABORATORY	Основи інформаційної безпеки	72	201	61	f	57	\N
6004	3	LABORATORY	Інформаційно-комунікаційні технології в освіті	72	80	78	f	57	\N
6005	1	LECTURE	Система комп'ютерної математики Maxima	72	385	194	f	57	\N
6006	1	LABORATORY	Система комп'ютерної математики Maxima	72	385	194	f	57	\N
6007	1	LECTURE	Комп'ютерні технології у тестуванні	72	320	78	f	57	\N
6008	1	LABORATORY	Комп'ютерні технології у тестуванні	72	320	78	f	57	\N
5691	3	PRACTICAL	Теорія ймовірностей та математична статистика	95	30	35	f	57	\N
6009	5	PRACTICAL	Науковий семінар	63	94	35	t	57	\N
6010	5	PRACTICAL	Науковий семінар	65	94	35	t	57	\N
6011	2	LECTURE	Професійна комунікація та управління конфліктами	63	354	70	t	57	\N
6012	2	LECTURE	Професійна комунікація та управління конфліктами	65	354	70	t	57	\N
6013	3	LABORATORY	Професійна комунікація та управління конфліктами	63	354	70	t	57	\N
6014	3	LABORATORY	Професійна комунікація та управління конфліктами	65	354	70	t	57	\N
6015	4	LECTURE	Системи та методи прийняття рішень в соціальних та економічних системах	63	386	40	f	57	\N
6016	4	LABORATORY	Системи та методи прийняття рішень в соціальних та економічних системах	63	386	40	f	57	\N
6017	4	LECTURE	Теоретичні основи прикладних досліджень	63	355	35	t	57	\N
6018	4	LECTURE	Теоретичні основи прикладних досліджень	65	355	35	t	57	\N
6019	3	LABORATORY	Теоретичні основи прикладних досліджень	63	355	35	t	57	\N
6020	3	LABORATORY	Теоретичні основи прикладних досліджень	65	355	35	t	57	\N
6021	4	LECTURE	Методи і засоби викладання фахових дисциплін та наукових досліджень	64	387	65	f	57	\N
6022	3	LABORATORY	Методи і засоби викладання фахових дисциплін та наукових досліджень	64	387	65	f	57	\N
6023	7	PRACTICAL	Магістерський семінар 1	64	246	65	f	57	\N
6028	4	LECTURE	Філософія освіти і науки	66	100	83	t	57	\N
6026	3	LABORATORY	Професійна комунікація та управління конфліктами	66	354	70	f	57	\N
6027	2	LECTURE	Професійна комунікація та управління конфліктами	66	354	70	f	57	\N
6029	4	LECTURE	Філософія освіти і науки	67	100	83	t	57	\N
6030	4	PRACTICAL	Філософія освіти і науки	66	100	83	t	57	\N
6031	4	PRACTICAL	Філософія освіти і науки	67	100	83	t	57	\N
6032	5	LECTURE	Чинники успішного працевлаштування	66	322	46	t	57	\N
6033	5	LECTURE	Чинники успішного працевлаштування	67	322	46	t	57	\N
6034	5	PRACTICAL	Чинники успішного працевлаштування	66	322	46	t	57	\N
6035	5	PRACTICAL	Чинники успішного працевлаштування	67	322	46	t	57	\N
6036	2	LECTURE	Організація наукової роботи учнів з математики та інформатики в НУШ	67	359	198	f	57	\N
6037	2	LABORATORY	Організація наукової роботи учнів з математики та інформатики в НУШ	67	359	198	f	57	\N
6038	4	LECTURE	Сучасні проблеми інформатики	106	360	205	f	57	\N
6039	4	LABORATORY	Сучасні проблеми інформатики	106	360	205	f	57	\N
6040	4	LECTURE	Середовище блочного програмування	106	388	79	f	57	\N
6042	4	LECTURE	Управління навчальними проектами	106	389	77	f	57	\N
6043	4	LABORATORY	Управління навчальними проектами	106	389	77	f	57	\N
5631	6	LECTURE	Алгебра і теорія чисел	56	56	46	t	57	\N
5632	6	LECTURE	Алгебра і теорія чисел	57	56	46	t	57	\N
6041	4	LABORATORY	Середовище блочного програмування	106	388	79	f	57	\N
6044	2	LECTURE	Психологія (загальна, вікова, педагогічна)	57	52	76	f	57	\N
6045	2	PRACTICAL	Психологія (загальна, вікова, педагогічна)	57	52	76	f	57	\N
6046	2	PRACTICAL	Німецька мова	53	133	88	t	57	\N
6047	2	PRACTICAL	Німецька мова	54	133	88	t	57	\N
6048	2	PRACTICAL	Німецька мова	87	133	88	t	57	\N
6049	2	PRACTICAL	Німецька мова	55	133	88	t	57	\N
6050	2	PRACTICAL	Німецька мова	56	133	88	t	57	\N
6051	2	PRACTICAL	Німецька мова	57	133	88	t	57	\N
6052	2	LECTURE	Математичний аналіз2	56	54	26	f	57	\N
6053	2	PRACTICAL	Математичний аналіз2	56	54	105	f	57	\N
6057	2	LECTURE	Фінансова грамотність	56	390	97	t	57	\N
6058	2	LECTURE	Фінансова грамотність	44	390	97	t	57	\N
6059	2	LECTURE	Фінансова грамотність	104	390	97	t	57	\N
6062	2	LECTURE	Python для Data Science	71	323	26	t	57	\N
6063	2	LECTURE	Python для Data Science	51	323	26	t	57	\N
6064	2	LECTURE	Python для Data Science	84	323	26	t	57	\N
6065	1	LABORATORY	Python для Data Science	71	323	26	t	57	\N
6066	1	LABORATORY	Python для Data Science	51	323	26	t	57	\N
6067	1	LABORATORY	Python для Data Science	84	323	26	t	57	\N
5817	2	PRACTICAL	Здоров'язбережувальні технології та домедична допомога	43	332	231	f	57	\N
6068	6	LECTURE	Інтелектуальна власність в ІТ-галузі	64	97	67	t	57	\N
6069	6	LECTURE	Інтелектуальна власність в ІТ-галузі	63	97	67	t	57	\N
6070	6	LECTURE	Інтелектуальна власність в ІТ-галузі	65	97	67	t	57	\N
6071	6	LABORATORY	Інтелектуальна власність в ІТ-галузі	64	97	67	t	57	\N
6072	6	LABORATORY	Інтелектуальна власність в ІТ-галузі	63	97	67	t	57	\N
6073	6	LABORATORY	Інтелектуальна власність в ІТ-галузі	65	97	67	t	57	\N
\.


--
-- Data for Name: periods; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.periods (id, end_time, name, start_time) FROM stdin;
8	17:30:00	6	16:10:00
1	09:40:00	1	08:20:00
2	11:10:00	2	09:50:00
3	12:50:00	3	11:30:00
4	14:20:00	4	13:00:00
7	16:00:00	5	14:40:00
\.


--
-- Data for Name: room_types; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.room_types (id, description) FROM stdin;
25	Лекційна
26	практична
27	лабораторія
6	кафедра ПМіІТ
7	кафедра диф.рівнянь
8	кафедра мат.моделювання
9	кафедра алгебри та інформатики
\.


--
-- Data for Name: rooms; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.rooms (id, disable, name, room_type_id, sort_order) FROM stdin;
52	f	1 к. 15 ауд.	27	14
55	f	1 к. 19 ауд.	27	15
56	f	1 к. 21 ауд.	27	16
60	f	1 к. 27 ауд.	27	17
63	f	1 к. 31 ауд.	27	18
118	f	1 к. 13 ауд.	9	19
111	f	1 к. 17 ауд.	8	20
110	f	1 к. 26 ауд.	6	21
108	f	1 К. 36 АУД.	7	23
114	t	14 корпус 60 ауд.	25	48
113	t	14 корпус 54 ауд.	25	49
112	t	14 корпус 1-А	25	50
74	f	1 к. 40 ауд.	25	25
107	f	1 К. 44 АУД.	27	26
50	f	1 к. 7 ауд.	25	27
109	t	6 к. 22 ауд.	25	29
115	t	6 к. 26 ауд.	25	30
119	f	Проводиться онлайн	25	47
72	f	Факультет ФКтаЗЛ	26	46
68	f	1 к. 39 ауд.	25	1
65	f	1 к. 33 ауд.	25	2
53	f	1 к. 18 ауд.	25	3
59	f	1 к. 22 ауд.	25	4
61	f	1 к. 28 ауд.	25	5
54	f	1 к. 3 ауд.	25	6
51	f	1 к. 11 ауд.	26	7
57	f	1 к. 23 ауд.	25	8
58	f	1 к. 24 ауд.	25	9
66	f	1 к. 37 ауд.	25	10
67	f	1 к. 38 ауд.	25	11
62	f	1 к. 29 ауд.	26	12
64	f	1 к. 32 ауд.	27	13
120	f	1к. 43 ауд.	26	48
121	f	Ботанічний сад	27	49
122	f	1 к. 45 ауд.	27	50
123	f	1 к. 46 ауд.	27	51
\.


--
-- Data for Name: schedules; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.schedules (id, day_of_week, evenodd, lesson_id, period_id, room_id) FROM stdin;
11467	MONDAY	ODD	5575	3	68
11468	MONDAY	ODD	5571	3	68
11469	MONDAY	ODD	5572	3	68
11470	MONDAY	ODD	5573	3	68
11471	MONDAY	ODD	5574	3	68
11473	MONDAY	EVEN	5575	3	68
11474	MONDAY	EVEN	5571	3	68
11475	MONDAY	EVEN	5572	3	68
11476	MONDAY	EVEN	5573	3	68
11477	MONDAY	EVEN	5574	3	68
11479	MONDAY	ODD	5548	4	68
11480	MONDAY	ODD	5549	4	68
11481	MONDAY	ODD	5550	4	68
11482	MONDAY	ODD	5551	4	68
11484	MONDAY	ODD	5553	4	68
11485	MONDAY	EVEN	5536	4	68
11486	MONDAY	EVEN	5537	4	68
11487	MONDAY	EVEN	5538	4	68
11488	MONDAY	EVEN	5539	4	68
11490	MONDAY	EVEN	5541	4	68
11491	MONDAY	ODD	5447	7	52
11492	MONDAY	EVEN	5447	7	52
11493	MONDAY	ODD	5530	8	55
11494	MONDAY	EVEN	5530	8	55
11495	TUESDAY	ODD	5425	1	74
11496	TUESDAY	ODD	5426	1	74
11497	TUESDAY	ODD	5427	1	74
11498	TUESDAY	ODD	5428	1	74
11500	TUESDAY	ODD	5430	1	74
11501	TUESDAY	EVEN	5425	1	74
11502	TUESDAY	EVEN	5426	1	74
11503	TUESDAY	EVEN	5427	1	74
11504	TUESDAY	EVEN	5428	1	74
11506	TUESDAY	EVEN	5430	1	74
11507	TUESDAY	ODD	5491	2	57
11508	TUESDAY	EVEN	5491	2	57
11509	TUESDAY	ODD	5457	3	68
11510	TUESDAY	ODD	5458	3	68
11511	TUESDAY	ODD	5459	3	68
11512	TUESDAY	ODD	5460	3	68
11514	TUESDAY	ODD	5462	3	68
11515	TUESDAY	ODD	5463	3	68
11516	TUESDAY	ODD	5464	3	68
11518	TUESDAY	EVEN	5457	3	68
11519	TUESDAY	EVEN	5458	3	68
11520	TUESDAY	EVEN	5459	3	68
11521	TUESDAY	EVEN	5460	3	68
11523	TUESDAY	EVEN	5462	3	68
11524	TUESDAY	EVEN	5463	3	68
11525	TUESDAY	EVEN	5464	3	68
11527	WEDNESDAY	ODD	5437	1	68
11528	WEDNESDAY	ODD	5438	1	68
11529	WEDNESDAY	ODD	5439	1	68
11530	WEDNESDAY	ODD	5440	1	68
11532	WEDNESDAY	ODD	5442	1	68
11533	WEDNESDAY	ODD	5443	1	68
11534	WEDNESDAY	ODD	5444	1	68
11536	WEDNESDAY	ODD	5446	1	68
11537	WEDNESDAY	EVEN	5437	1	68
11538	WEDNESDAY	EVEN	5438	1	68
11539	WEDNESDAY	EVEN	5439	1	68
11540	WEDNESDAY	EVEN	5440	1	68
11542	WEDNESDAY	EVEN	5442	1	68
11543	WEDNESDAY	EVEN	5443	1	68
11544	WEDNESDAY	EVEN	5444	1	68
11546	WEDNESDAY	EVEN	5446	1	68
11547	WEDNESDAY	ODD	5578	2	56
11548	WEDNESDAY	EVEN	5578	2	56
11549	WEDNESDAY	ODD	5457	3	68
11550	WEDNESDAY	ODD	5458	3	68
11551	WEDNESDAY	ODD	5459	3	68
11552	WEDNESDAY	ODD	5460	3	68
11554	WEDNESDAY	ODD	5462	3	68
11555	WEDNESDAY	ODD	5463	3	68
11556	WEDNESDAY	ODD	5464	3	68
11558	WEDNESDAY	ODD	5554	4	72
11559	WEDNESDAY	ODD	5555	4	72
11560	WEDNESDAY	ODD	5556	4	72
11561	WEDNESDAY	ODD	5557	4	72
11562	WEDNESDAY	ODD	5558	4	72
11563	WEDNESDAY	ODD	5559	4	72
11564	WEDNESDAY	ODD	5560	4	72
11565	WEDNESDAY	ODD	5561	4	72
11567	WEDNESDAY	ODD	5563	4	72
11568	WEDNESDAY	ODD	5564	4	72
12697	WEDNESDAY	ODD	5976	4	59
11570	WEDNESDAY	ODD	5566	4	72
11571	WEDNESDAY	ODD	5567	4	72
11572	WEDNESDAY	ODD	5568	4	72
11573	WEDNESDAY	EVEN	5554	4	72
11574	WEDNESDAY	EVEN	5555	4	72
11575	WEDNESDAY	EVEN	5556	4	72
11576	WEDNESDAY	EVEN	5557	4	72
11577	WEDNESDAY	EVEN	5558	4	72
11578	WEDNESDAY	EVEN	5559	4	72
11579	WEDNESDAY	EVEN	5560	4	72
11580	WEDNESDAY	EVEN	5561	4	72
11582	WEDNESDAY	EVEN	5563	4	72
11583	WEDNESDAY	EVEN	5564	4	72
12698	WEDNESDAY	ODD	5977	4	59
11585	WEDNESDAY	EVEN	5566	4	72
11586	WEDNESDAY	EVEN	5567	4	72
11587	WEDNESDAY	EVEN	5568	4	72
11592	THURSDAY	ODD	5431	1	66
11593	THURSDAY	ODD	5432	1	66
11594	THURSDAY	EVEN	5431	1	66
11595	THURSDAY	EVEN	5432	1	66
11597	THURSDAY	EVEN	5483	2	56
12699	WEDNESDAY	ODD	5978	4	59
12703	WEDNESDAY	ODD	5837	3	74
12707	TUESDAY	EVEN	5969	1	57
12708	WEDNESDAY	ODD	5963	3	74
12713	WEDNESDAY	ODD	5836	3	74
11596	THURSDAY	ODD	5483	2	56
11598	THURSDAY	EVEN	5578	3	64
11599	FRIDAY	ODD	5466	2	55
11600	FRIDAY	EVEN	5466	2	55
11601	FRIDAY	ODD	5475	3	68
11602	FRIDAY	ODD	5476	3	68
11603	FRIDAY	ODD	5477	3	68
11604	FRIDAY	ODD	5478	3	68
11606	FRIDAY	ODD	5480	3	68
11607	FRIDAY	ODD	5481	3	68
11608	FRIDAY	ODD	5482	3	68
11609	FRIDAY	EVEN	5475	3	68
11610	FRIDAY	EVEN	5476	3	68
11611	FRIDAY	EVEN	5477	3	68
11612	FRIDAY	EVEN	5478	3	68
11614	FRIDAY	EVEN	5480	3	68
11615	FRIDAY	EVEN	5481	3	68
11616	FRIDAY	EVEN	5482	3	68
11617	FRIDAY	ODD	5542	1	55
11618	FRIDAY	EVEN	5542	1	55
11619	FRIDAY	ODD	5543	1	55
11620	FRIDAY	EVEN	5543	1	55
11621	MONDAY	ODD	5579	7	56
11622	MONDAY	EVEN	5579	7	56
11623	TUESDAY	ODD	5492	2	62
11624	TUESDAY	EVEN	5492	2	62
11625	TUESDAY	ODD	5531	4	52
11626	TUESDAY	EVEN	5531	4	52
11627	WEDNESDAY	ODD	5467	2	55
11628	WEDNESDAY	EVEN	5467	2	55
11629	THURSDAY	ODD	5448	2	120
11630	THURSDAY	EVEN	5448	2	120
11631	THURSDAY	ODD	5579	3	64
11632	FRIDAY	ODD	5484	2	52
11633	FRIDAY	EVEN	5484	2	52
11634	MONDAY	ODD	5544	7	55
11635	MONDAY	EVEN	5544	7	55
11636	MONDAY	ODD	5532	8	56
11637	MONDAY	EVEN	5532	8	56
11638	TUESDAY	ODD	5493	2	62
11639	TUESDAY	EVEN	5493	2	62
11640	TUESDAY	ODD	5580	4	60
11641	TUESDAY	EVEN	5580	4	60
11642	WEDNESDAY	ODD	5449	2	60
11643	WEDNESDAY	EVEN	5449	2	60
11644	THURSDAY	ODD	5485	1	52
11645	THURSDAY	EVEN	5485	1	52
11646	THURSDAY	ODD	5433	2	67
11647	THURSDAY	EVEN	5433	2	67
11648	FRIDAY	ODD	5468	4	55
11649	FRIDAY	EVEN	5468	4	55
11650	MONDAY	ODD	5545	7	55
11651	MONDAY	EVEN	5545	7	55
11652	TUESDAY	ODD	5494	2	61
11653	TUESDAY	EVEN	5494	2	61
11656	WEDNESDAY	ODD	5469	2	120
11657	WEDNESDAY	EVEN	5469	2	120
11658	THURSDAY	ODD	5434	2	67
11659	THURSDAY	EVEN	5434	2	67
11660	THURSDAY	ODD	5581	3	56
11661	THURSDAY	EVEN	5581	3	56
11662	THURSDAY	ODD	5486	4	52
11663	THURSDAY	EVEN	5486	4	52
11664	FRIDAY	ODD	5450	4	120
11665	FRIDAY	EVEN	5450	4	120
11666	FRIDAY	ODD	5533	7	56
11667	FRIDAY	EVEN	5533	7	56
11668	MONDAY	ODD	5583	2	59
11669	MONDAY	ODD	5584	2	59
11670	MONDAY	ODD	5585	2	59
11672	MONDAY	EVEN	5583	2	59
11673	MONDAY	EVEN	5584	2	59
11674	MONDAY	EVEN	5585	2	59
11676	MONDAY	ODD	5452	7	60
11677	MONDAY	EVEN	5452	7	60
11680	TUESDAY	ODD	5535	4	52
11681	TUESDAY	EVEN	5535	4	52
11682	WEDNESDAY	ODD	5577	2	64
11683	WEDNESDAY	EVEN	5577	2	64
11684	WEDNESDAY	EVEN	5587	3	68
11685	WEDNESDAY	EVEN	5588	3	68
11686	WEDNESDAY	EVEN	5589	3	68
11688	WEDNESDAY	ODD	5471	4	55
11689	WEDNESDAY	EVEN	5471	4	55
11690	THURSDAY	ODD	5591	1	68
11691	THURSDAY	ODD	5592	1	68
11692	THURSDAY	ODD	5593	1	68
11694	THURSDAY	ODD	5595	1	68
11695	THURSDAY	ODD	5596	1	68
11696	THURSDAY	EVEN	5591	1	68
11697	THURSDAY	EVEN	5592	1	68
11698	THURSDAY	EVEN	5593	1	68
11700	THURSDAY	EVEN	5595	1	68
11701	THURSDAY	EVEN	5596	1	68
11702	THURSDAY	ODD	5597	2	66
11703	THURSDAY	EVEN	5597	2	66
11704	FRIDAY	ODD	5547	1	55
11679	TUESDAY	EVEN	5496	2	59
11705	FRIDAY	EVEN	5547	1	55
12700	WEDNESDAY	EVEN	5979	4	59
12701	WEDNESDAY	EVEN	5980	4	59
11716	WEDNESDAY	ODD	5603	2	53
11717	WEDNESDAY	ODD	5604	2	53
11722	THURSDAY	ODD	5499	2	65
11723	THURSDAY	EVEN	5499	2	65
11732	FRIDAY	EVEN	5612	3	60
12702	WEDNESDAY	EVEN	5981	4	59
12706	TUESDAY	EVEN	5968	1	57
12711	MONDAY	ODD	5817	3	121
12716	MONDAY	EVEN	5640	1	67
12715	MONDAY	ODD	5640	1	67
12717	MONDAY	ODD	6053	1	67
12718	MONDAY	EVEN	6053	1	67
12712	MONDAY	EVEN	5817	3	121
11706	FRIDAY	ODD	5488	4	52
11707	FRIDAY	EVEN	5488	4	52
12704	TUESDAY	ODD	5968	1	57
12705	TUESDAY	ODD	5969	1	57
12709	TUESDAY	ODD	5709	4	55
12710	TUESDAY	EVEN	5709	4	55
12714	WEDNESDAY	ODD	5815	4	121
12719	MONDAY	ODD	6052	4	66
12720	MONDAY	EVEN	6052	4	66
12749	WEDNESDAY	EVEN	6019	1	119
12751	WEDNESDAY	EVEN	6019	2	119
12752	WEDNESDAY	EVEN	6020	2	119
12753	THURSDAY	EVEN	5693	1	58
12758	MONDAY	ODD	6032	2	119
12759	MONDAY	ODD	6033	2	119
12760	THURSDAY	EVEN	6032	2	119
12761	THURSDAY	EVEN	6033	2	119
12762	MONDAY	ODD	6034	3	119
12763	MONDAY	ODD	6035	3	119
12721	THURSDAY	ODD	6057	7	119
12722	THURSDAY	ODD	6058	7	119
11713	TUESDAY	EVEN	5598	1	66
11719	WEDNESDAY	EVEN	5603	2	53
11720	WEDNESDAY	EVEN	5604	2	53
11724	THURSDAY	ODD	5606	3	55
11728	FRIDAY	EVEN	5609	2	54
11729	FRIDAY	EVEN	5610	2	54
11731	FRIDAY	ODD	5612	3	60
12723	THURSDAY	ODD	6059	7	119
12750	WEDNESDAY	EVEN	6020	1	119
11712	TUESDAY	ODD	5598	1	66
11714	TUESDAY	ODD	5472	2	55
11715	TUESDAY	EVEN	5472	2	55
11725	FRIDAY	ODD	5609	2	54
11726	FRIDAY	ODD	5610	2	54
11733	FRIDAY	ODD	5473	3	55
11734	FRIDAY	EVEN	5473	3	55
11735	FRIDAY	ODD	5613	4	60
11736	FRIDAY	EVEN	5613	4	60
11737	MONDAY	ODD	5454	3	60
11738	MONDAY	EVEN	5454	3	60
11739	TUESDAY	ODD	5599	1	66
11740	TUESDAY	EVEN	5599	1	66
11741	TUESDAY	ODD	5607	2	52
11742	TUESDAY	EVEN	5607	2	52
11743	THURSDAY	ODD	5500	2	65
11744	THURSDAY	EVEN	5500	2	65
12724	THURSDAY	EVEN	6057	7	119
11746	MONDAY	ODD	5456	2	60
11747	MONDAY	EVEN	5456	2	60
11748	MONDAY	ODD	5615	3	59
11749	MONDAY	ODD	5616	3	59
11750	MONDAY	EVEN	5615	3	59
11751	MONDAY	EVEN	5616	3	59
11752	MONDAY	ODD	5617	4	51
11753	MONDAY	EVEN	5617	4	51
11756	TUESDAY	ODD	5436	3	67
11757	TUESDAY	EVEN	5436	3	67
11758	THURSDAY	ODD	5625	3	58
11759	THURSDAY	EVEN	5625	3	58
11760	THURSDAY	ODD	5626	4	56
11761	THURSDAY	EVEN	5626	4	56
12725	THURSDAY	EVEN	6058	7	119
12726	THURSDAY	EVEN	6059	7	119
12756	MONDAY	EVEN	6032	2	119
12757	MONDAY	EVEN	6033	2	119
11771	TUESDAY	ODD	5502	1	61
11772	TUESDAY	EVEN	5502	1	61
11773	TUESDAY	ODD	5601	2	66
11774	TUESDAY	EVEN	5601	2	66
11775	TUESDAY	ODD	5633	3	74
11776	TUESDAY	ODD	5634	3	74
11777	TUESDAY	EVEN	5633	3	74
11778	TUESDAY	EVEN	5634	3	74
11779	WEDNESDAY	ODD	5631	1	59
11780	WEDNESDAY	ODD	5632	1	59
11781	WEDNESDAY	EVEN	5631	1	59
11782	WEDNESDAY	EVEN	5632	1	59
11783	WEDNESDAY	ODD	5635	2	59
11784	WEDNESDAY	ODD	5636	2	59
11785	WEDNESDAY	EVEN	5637	2	59
11786	WEDNESDAY	EVEN	5638	2	59
11787	THURSDAY	ODD	5627	2	58
11788	THURSDAY	EVEN	5627	2	58
11789	THURSDAY	ODD	5630	3	60
11790	THURSDAY	EVEN	5630	3	60
11791	THURSDAY	ODD	5629	4	54
11792	FRIDAY	ODD	5628	3	120
11793	FRIDAY	EVEN	5628	3	120
11799	TUESDAY	ODD	5498	1	61
11800	TUESDAY	EVEN	5498	1	61
11801	TUESDAY	ODD	5640	2	51
11802	TUESDAY	EVEN	5640	2	51
11805	THURSDAY	ODD	5602	2	66
11806	THURSDAY	EVEN	5602	2	66
11807	THURSDAY	ODD	5639	3	66
11808	THURSDAY	EVEN	5639	3	66
11809	FRIDAY	ODD	5490	4	52
11810	FRIDAY	EVEN	5490	4	52
11811	MONDAY	ODD	5674	2	64
11812	MONDAY	EVEN	5674	2	64
11813	MONDAY	ODD	5668	3	65
11814	MONDAY	ODD	5669	3	65
11815	MONDAY	ODD	5670	3	65
11816	MONDAY	ODD	5671	3	65
11817	MONDAY	ODD	5672	3	65
11818	MONDAY	ODD	5673	3	65
11819	MONDAY	EVEN	5668	3	65
11820	MONDAY	EVEN	5669	3	65
11821	MONDAY	EVEN	5670	3	65
11822	MONDAY	EVEN	5671	3	65
11823	MONDAY	EVEN	5672	3	65
11824	MONDAY	EVEN	5673	3	65
11825	MONDAY	ODD	5727	4	52
11826	MONDAY	ODD	5710	7	68
11827	MONDAY	ODD	5711	7	68
11828	MONDAY	ODD	5712	7	68
11829	MONDAY	ODD	5713	7	68
11830	MONDAY	ODD	5714	7	68
11831	MONDAY	ODD	5715	7	68
11832	MONDAY	EVEN	5710	7	68
11833	MONDAY	EVEN	5711	7	68
11769	MONDAY	ODD	5618	2	61
11770	MONDAY	EVEN	5618	2	61
11754	TUESDAY	ODD	5497	2	58
11755	TUESDAY	EVEN	5497	2	58
11834	MONDAY	EVEN	5712	7	68
11864	TUESDAY	ODD	5716	7	52
11865	TUESDAY	EVEN	5716	7	52
11868	WEDNESDAY	ODD	5641	2	74
11869	WEDNESDAY	ODD	5642	2	74
11870	WEDNESDAY	ODD	5643	2	74
11871	WEDNESDAY	ODD	5644	2	74
11872	WEDNESDAY	ODD	5645	2	74
11876	WEDNESDAY	EVEN	5644	2	74
11877	WEDNESDAY	EVEN	5645	2	74
11878	WEDNESDAY	ODD	5727	3	120
11888	THURSDAY	EVEN	5686	3	68
11889	THURSDAY	EVEN	5687	3	68
11890	THURSDAY	EVEN	5688	3	68
12727	THURSDAY	ODD	6062	7	119
12728	THURSDAY	ODD	6063	7	119
12729	THURSDAY	ODD	6064	7	119
12733	THURSDAY	ODD	6065	8	119
12734	THURSDAY	ODD	6066	8	119
12735	THURSDAY	ODD	6067	8	119
12764	MONDAY	EVEN	6034	3	119
12766	MONDAY	ODD	6034	4	119
12767	MONDAY	ODD	6035	4	119
11835	MONDAY	EVEN	5713	7	68
11836	MONDAY	EVEN	5714	7	68
11837	MONDAY	EVEN	5715	7	68
11843	TUESDAY	EVEN	5722	1	68
11844	TUESDAY	EVEN	5723	1	68
11845	TUESDAY	EVEN	5724	1	68
11846	TUESDAY	EVEN	5725	1	68
11847	TUESDAY	EVEN	5726	1	68
11862	TUESDAY	ODD	5689	4	54
11863	TUESDAY	EVEN	5689	4	54
11879	THURSDAY	ODD	5689	1	57
11891	THURSDAY	ODD	5680	3	68
11892	THURSDAY	ODD	5681	3	68
11893	THURSDAY	ODD	5682	3	68
11894	THURSDAY	ODD	5683	3	68
11895	THURSDAY	ODD	5684	3	68
11896	THURSDAY	ODD	5685	3	68
11897	THURSDAY	ODD	5686	3	68
11898	THURSDAY	ODD	5687	3	68
11899	THURSDAY	ODD	5688	3	68
12730	THURSDAY	EVEN	6062	7	119
12731	THURSDAY	EVEN	6063	7	119
12732	THURSDAY	EVEN	6064	7	119
12765	MONDAY	EVEN	6035	3	119
12770	THURSDAY	ODD	6032	2	119
12771	THURSDAY	ODD	6033	2	119
12773	WEDNESDAY	ODD	6069	4	119
12774	WEDNESDAY	ODD	6070	4	119
12781	WEDNESDAY	EVEN	6068	7	119
12782	WEDNESDAY	EVEN	6069	7	119
12783	WEDNESDAY	EVEN	6070	7	119
12784	THURSDAY	ODD	6071	2	119
12785	THURSDAY	ODD	6072	2	119
12786	THURSDAY	ODD	6073	2	119
12790	THURSDAY	ODD	6068	3	119
12791	THURSDAY	ODD	6069	3	119
12792	THURSDAY	ODD	6070	3	119
12796	THURSDAY	ODD	6071	4	119
12797	THURSDAY	ODD	6072	4	119
12798	THURSDAY	ODD	6073	4	119
12799	THURSDAY	EVEN	6071	4	119
12800	THURSDAY	EVEN	6072	4	119
12801	THURSDAY	EVEN	6073	4	119
11838	TUESDAY	ODD	5746	1	68
11839	TUESDAY	ODD	5747	1	68
11840	TUESDAY	ODD	5748	1	68
11841	TUESDAY	ODD	5749	1	68
11842	TUESDAY	ODD	5750	1	68
11848	TUESDAY	ODD	5662	2	65
11849	TUESDAY	ODD	5663	2	65
11850	TUESDAY	ODD	5664	2	65
11851	TUESDAY	ODD	5665	2	65
11852	TUESDAY	ODD	5666	2	65
11853	TUESDAY	ODD	5667	2	65
11854	TUESDAY	EVEN	5698	2	65
11855	TUESDAY	EVEN	5699	2	65
11856	TUESDAY	EVEN	5700	2	65
11857	TUESDAY	EVEN	5701	2	65
11858	TUESDAY	EVEN	5702	2	65
11859	TUESDAY	EVEN	5703	2	65
11860	TUESDAY	ODD	5503	3	58
11861	TUESDAY	EVEN	5503	3	58
11866	WEDNESDAY	ODD	5704	1	52
11867	WEDNESDAY	EVEN	5704	1	52
11873	WEDNESDAY	EVEN	5641	2	74
11874	WEDNESDAY	EVEN	5642	2	74
11875	WEDNESDAY	EVEN	5643	2	74
11880	THURSDAY	ODD	5646	2	60
11881	THURSDAY	EVEN	5646	2	60
11882	THURSDAY	EVEN	5680	3	68
11883	THURSDAY	EVEN	5681	3	68
11884	THURSDAY	EVEN	5682	3	68
11885	THURSDAY	EVEN	5683	3	68
11886	THURSDAY	EVEN	5684	3	68
11887	THURSDAY	EVEN	5685	3	68
12736	WEDNESDAY	ODD	5742	4	52
12739	THURSDAY	EVEN	5692	1	58
12768	MONDAY	EVEN	6032	4	119
12769	MONDAY	EVEN	6033	4	119
11910	THURSDAY	ODD	5761	7	64
11911	THURSDAY	ODD	5762	7	64
11912	THURSDAY	ODD	5763	7	64
11913	THURSDAY	ODD	5764	7	64
11914	THURSDAY	ODD	5765	7	64
11915	THURSDAY	EVEN	5761	7	64
11916	THURSDAY	EVEN	5762	7	64
11917	THURSDAY	EVEN	5763	7	64
11918	THURSDAY	EVEN	5764	7	64
11919	THURSDAY	EVEN	5765	7	64
11920	FRIDAY	ODD	5751	1	64
11921	FRIDAY	EVEN	5751	1	64
11922	FRIDAY	ODD	5656	2	120
11923	FRIDAY	EVEN	5656	2	120
11924	FRIDAY	ODD	5741	3	56
11925	FRIDAY	EVEN	5741	3	56
11926	FRIDAY	ODD	5732	7	119
11927	FRIDAY	ODD	5733	7	119
11928	FRIDAY	ODD	5734	7	119
11929	FRIDAY	ODD	5735	7	119
11930	FRIDAY	ODD	5736	7	119
11931	FRIDAY	ODD	5737	7	119
11932	FRIDAY	ODD	5738	7	119
11933	FRIDAY	ODD	5739	7	119
11934	FRIDAY	ODD	5740	7	119
11935	FRIDAY	EVEN	5732	7	119
11936	FRIDAY	EVEN	5733	7	119
11937	FRIDAY	EVEN	5734	7	119
11938	FRIDAY	EVEN	5735	7	119
11939	FRIDAY	EVEN	5736	7	119
11940	FRIDAY	EVEN	5737	7	119
11941	FRIDAY	EVEN	5738	7	119
11942	FRIDAY	EVEN	5739	7	119
11943	FRIDAY	EVEN	5740	7	119
11944	MONDAY	ODD	5752	2	55
11945	MONDAY	EVEN	5752	2	55
11946	MONDAY	ODD	5728	4	52
11949	TUESDAY	ODD	5690	4	54
11950	TUESDAY	EVEN	5690	4	54
11951	TUESDAY	ODD	5717	7	52
11952	TUESDAY	EVEN	5717	7	52
11947	TUESDAY	ODD	5504	3	61
11948	TUESDAY	EVEN	5504	3	61
11953	WEDNESDAY	ODD	5705	1	52
11954	WEDNESDAY	EVEN	5705	1	52
11955	WEDNESDAY	ODD	5728	3	120
11956	THURSDAY	ODD	5690	1	57
11957	THURSDAY	ODD	5675	2	52
11958	THURSDAY	EVEN	5675	2	52
11959	FRIDAY	ODD	5657	1	120
11960	FRIDAY	EVEN	5657	1	120
11961	FRIDAY	ODD	5648	2	60
11962	FRIDAY	EVEN	5648	2	60
11965	MONDAY	ODD	5658	1	55
11966	MONDAY	EVEN	5658	1	55
11967	MONDAY	ODD	5729	2	52
11968	MONDAY	ODD	5730	2	52
11969	MONDAY	ODD	5731	2	52
11970	MONDAY	EVEN	5729	2	52
11971	MONDAY	EVEN	5730	2	52
11972	MONDAY	EVEN	5731	2	52
11973	MONDAY	ODD	5753	4	55
11974	MONDAY	EVEN	5753	4	55
11975	TUESDAY	ODD	5505	3	61
11976	TUESDAY	EVEN	5505	3	61
11977	TUESDAY	ODD	5706	4	55
11978	TUESDAY	EVEN	5706	4	55
11979	WEDNESDAY	ODD	5691	1	57
11980	WEDNESDAY	ODD	5692	1	57
11981	WEDNESDAY	ODD	5693	1	57
11985	WEDNESDAY	ODD	5647	3	52
11986	WEDNESDAY	EVEN	5647	3	52
11988	WEDNESDAY	EVEN	5743	4	52
11995	FRIDAY	EVEN	5676	2	56
12737	WEDNESDAY	EVEN	5742	4	52
12772	WEDNESDAY	ODD	6068	4	119
12775	WEDNESDAY	EVEN	6068	4	119
12776	WEDNESDAY	EVEN	6069	4	119
12777	WEDNESDAY	EVEN	6070	4	119
11987	WEDNESDAY	ODD	5743	4	52
12738	THURSDAY	EVEN	5691	1	58
12740	FRIDAY	ODD	5744	3	56
12741	FRIDAY	EVEN	5744	3	56
12747	TUESDAY	ODD	6000	3	52
12778	WEDNESDAY	ODD	6068	7	119
12779	WEDNESDAY	ODD	6069	7	119
12780	WEDNESDAY	ODD	6070	7	119
12787	THURSDAY	EVEN	6068	2	119
12788	THURSDAY	EVEN	6069	2	119
12789	THURSDAY	EVEN	6070	2	119
12793	THURSDAY	EVEN	6071	3	119
12794	THURSDAY	EVEN	6072	3	119
12795	THURSDAY	EVEN	6073	3	119
11989	THURSDAY	ODD	5691	1	58
11990	THURSDAY	ODD	5692	1	58
11991	THURSDAY	ODD	5693	1	58
11992	THURSDAY	ODD	5718	2	55
11993	THURSDAY	EVEN	5718	2	55
11994	FRIDAY	ODD	5676	2	56
11996	MONDAY	ODD	5677	1	64
11997	MONDAY	EVEN	5677	1	64
11998	MONDAY	ODD	5754	4	55
11999	MONDAY	EVEN	5754	4	55
12000	TUESDAY	ODD	5506	3	51
12001	TUESDAY	EVEN	5506	3	51
12002	TUESDAY	ODD	5707	4	55
12003	TUESDAY	EVEN	5707	4	55
12004	WEDNESDAY	ODD	5649	3	60
12005	WEDNESDAY	EVEN	5649	3	60
12006	THURSDAY	ODD	5719	2	55
12007	THURSDAY	EVEN	5719	2	55
12008	FRIDAY	ODD	5659	2	64
12009	FRIDAY	EVEN	5659	2	64
12010	MONDAY	ODD	5678	1	64
12011	MONDAY	EVEN	5678	1	64
12012	TUESDAY	ODD	5507	3	51
12013	TUESDAY	EVEN	5507	3	51
12014	TUESDAY	ODD	5708	4	55
12015	WEDNESDAY	ODD	5650	3	60
12016	WEDNESDAY	ODD	5745	4	52
12017	FRIDAY	ODD	5755	1	64
12018	FRIDAY	EVEN	5755	1	64
12019	FRIDAY	ODD	5660	2	64
12020	FRIDAY	EVEN	5660	2	64
12021	TUESDAY	EVEN	5708	4	55
12022	WEDNESDAY	EVEN	5650	3	60
12023	WEDNESDAY	EVEN	5745	4	52
12024	TUESDAY	ODD	5508	4	61
12025	TUESDAY	EVEN	5508	4	61
12026	WEDNESDAY	ODD	5694	2	54
12027	WEDNESDAY	ODD	5695	2	54
12028	WEDNESDAY	ODD	5696	2	54
12029	WEDNESDAY	ODD	5697	2	54
12030	WEDNESDAY	EVEN	5694	2	54
12031	WEDNESDAY	EVEN	5695	2	54
12032	WEDNESDAY	EVEN	5696	2	54
12033	WEDNESDAY	EVEN	5697	2	54
12034	THURSDAY	EVEN	5694	1	54
12035	THURSDAY	EVEN	5695	1	54
12036	THURSDAY	EVEN	5696	1	54
12037	THURSDAY	EVEN	5697	1	54
12742	TUESDAY	ODD	5806	1	52
12745	TUESDAY	ODD	6001	1	60
12746	TUESDAY	EVEN	6001	1	60
12046	MONDAY	ODD	5782	3	64
12047	MONDAY	EVEN	5798	3	56
12048	MONDAY	EVEN	5782	4	64
12063	WEDNESDAY	ODD	5766	1	54
12064	WEDNESDAY	ODD	5767	1	54
12065	WEDNESDAY	ODD	5768	1	54
12066	WEDNESDAY	ODD	5769	1	54
12067	WEDNESDAY	EVEN	5766	1	54
12068	WEDNESDAY	EVEN	5767	1	54
12069	WEDNESDAY	EVEN	5768	1	54
12070	WEDNESDAY	EVEN	5769	1	54
12071	WEDNESDAY	ODD	5802	3	54
12072	WEDNESDAY	ODD	5803	3	54
12073	WEDNESDAY	ODD	5804	3	54
12074	WEDNESDAY	ODD	5805	3	54
12075	WEDNESDAY	EVEN	5802	3	54
12076	WEDNESDAY	EVEN	5803	3	54
12077	WEDNESDAY	EVEN	5804	3	54
12078	WEDNESDAY	EVEN	5805	3	54
12079	THURSDAY	ODD	5786	2	54
12080	THURSDAY	ODD	5787	2	54
12081	THURSDAY	ODD	5788	2	54
12082	THURSDAY	ODD	5789	2	54
12083	THURSDAY	EVEN	5786	2	54
12084	THURSDAY	EVEN	5787	2	54
12085	THURSDAY	EVEN	5788	2	54
12086	THURSDAY	EVEN	5789	2	54
12087	FRIDAY	ODD	5774	4	119
12088	FRIDAY	EVEN	5774	4	119
12089	MONDAY	ODD	5799	3	56
12090	MONDAY	EVEN	5783	3	64
12091	MONDAY	ODD	5783	4	64
12092	TUESDAY	ODD	5509	4	61
12093	TUESDAY	EVEN	5509	4	61
12094	TUESDAY	EVEN	5807	7	60
12095	THURSDAY	ODD	5791	1	56
12096	FRIDAY	ODD	5775	4	119
12097	FRIDAY	EVEN	5775	4	119
12100	MONDAY	ODD	5784	4	64
12743	TUESDAY	EVEN	5790	1	56
12744	TUESDAY	ODD	5793	1	56
12748	TUESDAY	EVEN	6000	3	52
12098	MONDAY	ODD	5800	3	56
12099	MONDAY	EVEN	5784	3	64
12153	WEDNESDAY	ODD	5816	3	121
12155	WEDNESDAY	EVEN	5816	3	121
12103	TUESDAY	EVEN	5808	7	60
12104	THURSDAY	ODD	5792	1	56
12105	THURSDAY	ODD	5772	4	55
12106	THURSDAY	ODD	5773	4	55
12107	THURSDAY	EVEN	5772	4	55
12108	THURSDAY	EVEN	5773	4	55
12109	FRIDAY	ODD	5776	3	119
12110	FRIDAY	EVEN	5776	3	119
12111	MONDAY	ODD	5785	1	60
12112	MONDAY	EVEN	5785	1	60
12157	WEDNESDAY	EVEN	5814	4	121
12116	TUESDAY	ODD	5801	4	56
12117	TUESDAY	EVEN	5809	4	56
12118	FRIDAY	ODD	5777	3	119
12119	FRIDAY	EVEN	5777	3	119
12120	MONDAY	ODD	5453	3	52
12121	MONDAY	EVEN	5453	3	52
12122	THURSDAY	EVEN	5606	3	55
12123	FRIDAY	EVEN	5606	4	64
12124	TUESDAY	EVEN	5607	4	64
12125	WEDNESDAY	ODD	5489	2	52
12126	WEDNESDAY	EVEN	5489	2	52
12127	MONDAY	ODD	5821	2	108
12128	MONDAY	EVEN	5820	2	108
12129	MONDAY	ODD	5812	3	58
12130	MONDAY	EVEN	5812	3	58
12131	MONDAY	ODD	5813	4	120
12132	MONDAY	EVEN	5813	4	120
12133	TUESDAY	ODD	5661	1	120
12134	TUESDAY	EVEN	5661	1	120
12135	TUESDAY	ODD	5819	3	60
12136	TUESDAY	EVEN	5819	3	60
12139	WEDNESDAY	ODD	5823	1	55
12140	WEDNESDAY	EVEN	5823	1	55
12141	WEDNESDAY	ODD	5824	2	65
12142	WEDNESDAY	ODD	5825	2	65
12143	WEDNESDAY	ODD	5826	2	65
12144	WEDNESDAY	ODD	5827	2	65
12145	WEDNESDAY	ODD	5828	2	65
12146	WEDNESDAY	ODD	5829	2	65
12147	WEDNESDAY	EVEN	5824	2	65
12148	WEDNESDAY	EVEN	5825	2	65
12149	WEDNESDAY	EVEN	5826	2	65
12150	WEDNESDAY	EVEN	5827	2	65
12151	WEDNESDAY	EVEN	5828	2	65
12152	WEDNESDAY	EVEN	5829	2	65
12159	THURSDAY	ODD	5811	1	60
12160	THURSDAY	EVEN	5811	1	60
12161	THURSDAY	ODD	5810	2	58
12162	THURSDAY	EVEN	5810	2	58
12163	THURSDAY	ODD	5818	3	53
12164	THURSDAY	EVEN	5818	3	53
12165	WEDNESDAY	ODD	5565	7	72
12166	WEDNESDAY	EVEN	5565	7	72
12167	MONDAY	ODD	5835	1	52
12168	MONDAY	EVEN	5835	1	52
12169	MONDAY	ODD	5834	2	58
12170	MONDAY	EVEN	5834	2	58
12171	TUESDAY	ODD	5841	2	54
12172	TUESDAY	EVEN	5841	2	54
12173	TUESDAY	ODD	5832	3	54
12174	TUESDAY	EVEN	5832	3	54
12175	WEDNESDAY	ODD	5830	1	58
12176	WEDNESDAY	EVEN	5830	1	58
12177	WEDNESDAY	ODD	5833	2	57
12178	WEDNESDAY	EVEN	5833	2	57
12181	THURSDAY	ODD	5840	1	54
12182	THURSDAY	ODD	5838	2	59
12183	THURSDAY	ODD	5839	2	59
12184	THURSDAY	EVEN	5838	2	59
12185	THURSDAY	EVEN	5839	2	59
12186	THURSDAY	EVEN	5831	3	51
12187	MONDAY	ODD	5846	1	66
12188	MONDAY	EVEN	5846	1	66
12189	MONDAY	ODD	5847	2	66
12190	MONDAY	EVEN	5847	2	66
12191	MONDAY	ODD	5679	4	56
12192	MONDAY	EVEN	5679	4	56
12193	TUESDAY	ODD	5844	1	67
12194	TUESDAY	EVEN	5844	1	67
12195	TUESDAY	ODD	5844	2	67
12196	TUESDAY	ODD	5850	3	54
12197	TUESDAY	EVEN	5850	3	54
12200	WEDNESDAY	EVEN	5843	1	66
12201	WEDNESDAY	ODD	5846	1	66
12202	WEDNESDAY	EVEN	5851	2	57
12204	WEDNESDAY	EVEN	5847	3	59
12205	WEDNESDAY	ODD	5851	2	57
12206	THURSDAY	ODD	5848	1	67
12207	THURSDAY	EVEN	5848	1	67
12208	THURSDAY	ODD	5849	2	51
12209	THURSDAY	EVEN	5849	2	51
12210	THURSDAY	ODD	5848	3	51
12211	WEDNESDAY	ODD	5843	3	66
12212	FRIDAY	ODD	5842	1	67
12213	FRIDAY	ODD	5845	2	67
12214	FRIDAY	EVEN	5845	2	67
12215	FRIDAY	EVEN	5842	1	67
12216	MONDAY	ODD	5889	1	56
12217	MONDAY	EVEN	5889	1	56
12218	MONDAY	ODD	5900	2	56
12219	MONDAY	ODD	5901	2	56
12220	MONDAY	ODD	5902	2	56
12221	MONDAY	EVEN	5900	2	56
12222	MONDAY	EVEN	5901	2	56
12223	MONDAY	EVEN	5902	2	56
12224	MONDAY	ODD	5904	3	53
12225	MONDAY	ODD	5905	3	53
12226	MONDAY	ODD	5906	3	53
12227	MONDAY	ODD	5907	3	53
12228	MONDAY	EVEN	5908	3	53
12229	MONDAY	EVEN	5909	3	53
12230	MONDAY	EVEN	5910	3	53
12231	MONDAY	EVEN	5911	3	53
12232	MONDAY	ODD	5877	4	53
12233	MONDAY	ODD	5878	4	53
12234	MONDAY	ODD	5879	4	53
12235	MONDAY	ODD	5880	4	53
12236	MONDAY	EVEN	5877	4	53
12237	MONDAY	EVEN	5878	4	53
12238	MONDAY	EVEN	5879	4	53
12239	MONDAY	EVEN	5880	4	53
12240	TUESDAY	ODD	5865	1	55
12241	TUESDAY	EVEN	5865	1	55
12242	TUESDAY	ODD	5852	2	74
12243	TUESDAY	ODD	5853	2	74
12244	TUESDAY	ODD	5854	2	74
12245	TUESDAY	ODD	5855	2	74
12247	TUESDAY	EVEN	5852	2	74
12248	TUESDAY	EVEN	5853	2	74
12249	TUESDAY	EVEN	5854	2	74
12250	TUESDAY	EVEN	5855	2	74
12252	TUESDAY	ODD	5869	3	65
12253	TUESDAY	ODD	5870	3	65
12254	TUESDAY	ODD	5871	3	65
12255	TUESDAY	ODD	5872	3	65
12256	TUESDAY	EVEN	5857	3	59
12257	TUESDAY	ODD	5923	4	65
12258	TUESDAY	ODD	5924	4	65
12259	TUESDAY	ODD	5925	4	65
12260	TUESDAY	ODD	5926	4	65
12261	TUESDAY	EVEN	5923	4	65
12262	TUESDAY	EVEN	5924	4	65
12263	TUESDAY	EVEN	5925	4	65
12264	TUESDAY	EVEN	5926	4	65
12265	WEDNESDAY	ODD	5912	1	60
12266	WEDNESDAY	ODD	5873	3	64
12267	WEDNESDAY	EVEN	5873	3	64
12268	WEDNESDAY	ODD	5920	4	67
12269	WEDNESDAY	EVEN	5920	4	67
12270	WEDNESDAY	ODD	5921	7	67
12271	WEDNESDAY	ODD	5922	7	67
12272	WEDNESDAY	EVEN	5921	7	67
12273	WEDNESDAY	EVEN	5922	7	67
12274	THURSDAY	ODD	5896	1	53
12275	THURSDAY	ODD	5897	1	53
12276	THURSDAY	ODD	5898	1	53
12277	THURSDAY	ODD	5899	1	53
12278	THURSDAY	EVEN	5896	1	53
12279	THURSDAY	EVEN	5897	1	53
12280	THURSDAY	EVEN	5898	1	53
12281	THURSDAY	EVEN	5899	1	53
12282	THURSDAY	ODD	5881	3	52
12283	THURSDAY	EVEN	5881	3	52
12302	FRIDAY	ODD	5861	2	65
12284	THURSDAY	ODD	5756	4	67
12285	THURSDAY	ODD	5757	4	67
12286	THURSDAY	ODD	5758	4	67
12287	THURSDAY	ODD	5759	4	67
12288	THURSDAY	ODD	5760	4	67
12289	THURSDAY	EVEN	5756	4	67
12290	THURSDAY	EVEN	5757	4	67
12291	THURSDAY	EVEN	5758	4	67
12292	THURSDAY	EVEN	5759	4	67
12293	THURSDAY	EVEN	5760	4	67
12294	THURSDAY	ODD	5916	4	53
12295	THURSDAY	ODD	5917	4	53
12296	THURSDAY	EVEN	5916	4	53
12297	THURSDAY	EVEN	5917	4	53
12298	THURSDAY	ODD	5918	7	52
12299	THURSDAY	ODD	5919	7	52
12300	THURSDAY	EVEN	5918	7	52
12301	THURSDAY	EVEN	5919	7	52
12303	FRIDAY	ODD	5862	2	65
12304	FRIDAY	ODD	5863	2	65
12305	FRIDAY	ODD	5864	2	65
12306	FRIDAY	EVEN	5861	2	65
12307	FRIDAY	EVEN	5862	2	65
12308	FRIDAY	EVEN	5863	2	65
12309	FRIDAY	EVEN	5864	2	65
12310	FRIDAY	ODD	5885	3	61
12311	FRIDAY	EVEN	5885	3	61
12312	MONDAY	ODD	5882	7	120
12313	MONDAY	EVEN	5882	7	120
12318	WEDNESDAY	EVEN	5913	1	60
12319	WEDNESDAY	ODD	5890	3	55
12320	WEDNESDAY	EVEN	5890	3	55
12321	THURSDAY	ODD	5858	2	61
12322	THURSDAY	ODD	5874	3	120
12323	THURSDAY	EVEN	5874	3	120
12324	FRIDAY	ODD	5866	1	56
12325	FRIDAY	EVEN	5866	1	56
12326	FRIDAY	ODD	5886	3	57
12327	FRIDAY	EVEN	5886	3	57
12328	MONDAY	ODD	5883	7	120
12329	MONDAY	EVEN	5883	7	120
12330	TUESDAY	EVEN	5914	1	52
12331	TUESDAY	EVEN	5915	1	52
12332	TUESDAY	EVEN	5859	3	65
12333	TUESDAY	EVEN	5860	3	65
12334	TUESDAY	ODD	5930	7	55
12335	TUESDAY	EVEN	5930	7	55
12336	THURSDAY	ODD	5927	4	60
12337	THURSDAY	ODD	5928	4	60
12338	WEDNESDAY	ODD	5929	1	55
12339	WEDNESDAY	EVEN	5929	1	55
12340	WEDNESDAY	ODD	5867	3	56
12341	WEDNESDAY	EVEN	5867	3	56
12342	THURSDAY	ODD	5875	2	64
12343	THURSDAY	EVEN	5875	2	64
12344	THURSDAY	EVEN	5927	4	60
12345	THURSDAY	EVEN	5928	4	60
12346	FRIDAY	ODD	5887	3	61
12347	FRIDAY	EVEN	5887	3	61
12348	MONDAY	ODD	5903	1	120
12349	MONDAY	EVEN	5903	1	120
12350	MONDAY	ODD	5892	2	120
12351	MONDAY	EVEN	5892	2	120
12352	TUESDAY	ODD	5931	7	55
12353	TUESDAY	EVEN	5931	7	55
12354	WEDNESDAY	ODD	5868	3	56
12355	WEDNESDAY	EVEN	5868	3	56
12356	THURSDAY	ODD	5876	2	64
12357	THURSDAY	EVEN	5876	2	64
12358	THURSDAY	ODD	5884	3	52
12359	THURSDAY	EVEN	5884	3	52
12360	FRIDAY	ODD	5888	3	57
12361	FRIDAY	EVEN	5888	3	57
12362	WEDNESDAY	ODD	5932	4	67
12363	WEDNESDAY	EVEN	5932	4	67
12364	MONDAY	ODD	5937	3	57
12365	MONDAY	ODD	5938	3	57
12366	MONDAY	EVEN	5937	3	57
12367	MONDAY	EVEN	5938	3	57
12368	MONDAY	ODD	5939	4	54
12369	MONDAY	ODD	5940	4	54
12370	MONDAY	EVEN	5941	4	54
12371	MONDAY	EVEN	5942	4	54
12372	TUESDAY	ODD	5949	2	64
12373	TUESDAY	EVEN	5949	2	64
12374	TUESDAY	ODD	5945	3	64
12375	TUESDAY	EVEN	5945	3	64
12376	WEDNESDAY	ODD	5935	1	120
12377	WEDNESDAY	EVEN	5935	1	120
12378	WEDNESDAY	ODD	5933	2	58
12379	WEDNESDAY	ODD	5934	2	58
12380	WEDNESDAY	EVEN	5933	2	58
12381	WEDNESDAY	EVEN	5934	2	58
12382	WEDNESDAY	ODD	5943	3	61
12383	WEDNESDAY	ODD	5944	3	61
12384	WEDNESDAY	EVEN	5943	3	61
12385	WEDNESDAY	EVEN	5944	3	61
12386	THURSDAY	ODD	5953	1	55
12387	THURSDAY	ODD	5954	1	55
12388	THURSDAY	EVEN	5953	1	55
12389	THURSDAY	EVEN	5954	1	55
12390	THURSDAY	ODD	5951	2	57
12391	THURSDAY	ODD	5952	2	57
12392	THURSDAY	EVEN	5941	2	57
12393	THURSDAY	EVEN	5942	2	57
12394	THURSDAY	ODD	5947	3	57
12395	THURSDAY	ODD	5948	3	57
12396	THURSDAY	EVEN	5947	3	57
12397	THURSDAY	EVEN	5948	3	57
12398	FRIDAY	ODD	5961	1	119
12399	FRIDAY	ODD	5962	1	119
12400	FRIDAY	EVEN	5961	1	119
12401	FRIDAY	EVEN	5962	1	119
12402	FRIDAY	ODD	5959	2	119
12403	FRIDAY	ODD	5960	2	119
12404	FRIDAY	EVEN	5955	2	119
12405	FRIDAY	EVEN	5956	2	119
12406	FRIDAY	ODD	5955	3	119
12407	FRIDAY	ODD	5956	3	119
12408	FRIDAY	EVEN	5957	3	119
12409	FRIDAY	EVEN	5958	3	119
12410	FRIDAY	ODD	5957	4	119
12411	FRIDAY	ODD	5958	4	119
12412	TUESDAY	ODD	5950	1	64
12413	TUESDAY	EVEN	5950	1	64
12414	TUESDAY	ODD	5936	2	120
12415	TUESDAY	EVEN	5936	2	120
12416	WEDNESDAY	ODD	5946	4	120
12417	WEDNESDAY	EVEN	5946	4	120
12418	MONDAY	ODD	5984	1	57
12419	MONDAY	ODD	5985	1	57
12420	MONDAY	EVEN	5984	1	57
12421	MONDAY	EVEN	5985	1	57
12425	MONDAY	ODD	5966	2	67
12426	MONDAY	EVEN	5966	2	67
12435	TUESDAY	ODD	5975	3	66
12436	TUESDAY	EVEN	5965	3	65
12437	TUESDAY	ODD	5974	4	66
12438	TUESDAY	EVEN	5974	4	66
12439	WEDNESDAY	ODD	5895	1	55
12440	WEDNESDAY	EVEN	5895	1	55
12449	THURSDAY	ODD	5972	1	51
12450	THURSDAY	EVEN	5972	1	51
12451	MONDAY	ODD	5998	2	53
12452	MONDAY	ODD	5999	2	53
12453	MONDAY	EVEN	5998	2	53
12454	MONDAY	EVEN	5999	2	53
12455	TUESDAY	ODD	5995	2	54
12456	TUESDAY	EVEN	5995	2	54
12457	TUESDAY	ODD	5990	4	53
12458	TUESDAY	ODD	5991	4	53
12459	TUESDAY	EVEN	5992	4	53
12460	TUESDAY	EVEN	5993	4	53
12461	FRIDAY	ODD	5992	2	59
12462	FRIDAY	ODD	5993	2	59
12463	FRIDAY	ODD	5997	1	59
12464	FRIDAY	EVEN	5997	1	59
12466	WEDNESDAY	EVEN	5979	3	74
12467	WEDNESDAY	EVEN	5980	3	74
12468	WEDNESDAY	EVEN	5981	3	74
12470	THURSDAY	ODD	5964	2	59
12471	THURSDAY	EVEN	5964	2	59
12472	THURSDAY	ODD	5994	1	54
12473	THURSDAY	ODD	5986	4	65
12474	THURSDAY	ODD	5987	4	65
12475	THURSDAY	EVEN	5986	4	65
12476	THURSDAY	EVEN	5987	4	65
12477	THURSDAY	ODD	5988	7	120
12478	THURSDAY	EVEN	5988	7	120
12481	FRIDAY	EVEN	5996	2	59
12482	MONDAY	ODD	6004	3	120
12483	MONDAY	EVEN	6004	3	120
12486	TUESDAY	ODD	6003	2	60
12487	TUESDAY	EVEN	6002	2	67
12488	MONDAY	ODD	5989	4	60
12489	MONDAY	EVEN	5989	4	60
12492	THURSDAY	EVEN	6006	1	56
12493	THURSDAY	EVEN	6005	2	108
12494	FRIDAY	EVEN	6007	2	51
12495	FRIDAY	ODD	6008	1	52
12496	FRIDAY	EVEN	6004	1	52
12497	MONDAY	ODD	6009	1	119
12498	MONDAY	ODD	6010	1	119
12499	MONDAY	EVEN	6009	1	119
12500	MONDAY	EVEN	6010	1	119
12501	MONDAY	ODD	6016	3	119
12502	MONDAY	EVEN	6016	3	119
12503	MONDAY	ODD	6015	4	119
12504	MONDAY	EVEN	6015	4	119
12505	WEDNESDAY	ODD	6009	3	119
12506	WEDNESDAY	ODD	6010	3	119
12507	WEDNESDAY	EVEN	6009	3	119
12508	WEDNESDAY	EVEN	6010	3	119
12517	FRIDAY	ODD	6017	1	119
12518	FRIDAY	ODD	6018	1	119
12519	FRIDAY	EVEN	6009	1	119
12520	FRIDAY	EVEN	6010	1	119
12521	FRIDAY	ODD	6019	2	119
12522	FRIDAY	ODD	6020	2	119
12523	FRIDAY	EVEN	6017	2	119
12524	FRIDAY	EVEN	6018	2	119
12525	FRIDAY	ODD	6015	3	119
12526	FRIDAY	EVEN	6015	3	119
12527	TUESDAY	ODD	6013	1	119
12528	TUESDAY	ODD	6014	1	119
12529	TUESDAY	EVEN	6013	1	119
12530	TUESDAY	EVEN	6014	1	119
12531	TUESDAY	ODD	6013	2	119
12532	TUESDAY	ODD	6014	2	119
12533	TUESDAY	EVEN	6011	2	119
12534	TUESDAY	EVEN	6012	2	119
12535	TUESDAY	ODD	6011	3	119
12536	TUESDAY	ODD	6012	3	119
12537	FRIDAY	ODD	6016	4	119
12538	FRIDAY	EVEN	6016	4	119
12547	MONDAY	ODD	6023	1	119
12548	MONDAY	EVEN	6023	1	119
12549	MONDAY	ODD	6023	2	119
12550	MONDAY	EVEN	6023	2	119
12553	TUESDAY	ODD	6021	7	119
12554	TUESDAY	EVEN	6021	7	119
12555	TUESDAY	ODD	6022	8	119
12556	TUESDAY	EVEN	6022	8	119
12559	WEDNESDAY	ODD	6023	2	119
12560	WEDNESDAY	EVEN	6023	2	119
12561	WEDNESDAY	ODD	6023	3	119
12562	WEDNESDAY	EVEN	6022	3	119
12563	THURSDAY	ODD	6021	1	119
12564	THURSDAY	EVEN	6021	1	119
12565	TUESDAY	ODD	6027	1	119
12566	TUESDAY	EVEN	6027	1	119
12567	TUESDAY	ODD	6026	2	119
12568	TUESDAY	EVEN	6026	2	119
12569	TUESDAY	ODD	6026	3	119
12570	WEDNESDAY	ODD	6030	1	119
12571	WEDNESDAY	ODD	6031	1	119
12572	WEDNESDAY	EVEN	6030	1	119
12573	WEDNESDAY	EVEN	6031	1	119
12574	WEDNESDAY	ODD	6030	2	119
12575	WEDNESDAY	ODD	6031	2	119
12576	WEDNESDAY	EVEN	6028	2	119
12577	WEDNESDAY	EVEN	6029	2	119
12578	THURSDAY	ODD	6028	3	119
12579	THURSDAY	ODD	6029	3	119
12580	THURSDAY	EVEN	6028	3	119
12581	THURSDAY	EVEN	6029	3	119
12582	THURSDAY	ODD	6030	4	119
12583	THURSDAY	ODD	6031	4	119
12584	THURSDAY	EVEN	6028	4	119
12585	THURSDAY	EVEN	6029	4	119
12596	FRIDAY	EVEN	6034	3	119
12597	FRIDAY	EVEN	6035	3	119
12598	THURSDAY	ODD	6037	7	119
12599	TUESDAY	ODD	6037	2	119
12600	TUESDAY	EVEN	6036	2	119
12601	THURSDAY	EVEN	6037	7	119
12604	FRIDAY	EVEN	6032	4	119
12605	FRIDAY	EVEN	6033	4	119
12610	MONDAY	ODD	6042	4	119
12611	MONDAY	EVEN	6042	4	119
12612	MONDAY	ODD	6043	7	119
12613	MONDAY	EVEN	6043	7	119
12614	TUESDAY	ODD	6038	3	119
12615	TUESDAY	EVEN	6038	3	119
12616	TUESDAY	ODD	6039	4	119
12617	TUESDAY	EVEN	6039	4	119
12618	WEDNESDAY	ODD	6040	7	119
12619	WEDNESDAY	EVEN	6040	7	119
12620	WEDNESDAY	ODD	6039	3	119
12621	WEDNESDAY	EVEN	6039	2	119
12622	WEDNESDAY	ODD	6038	2	119
12623	WEDNESDAY	EVEN	6038	3	119
12624	THURSDAY	ODD	6042	1	119
12625	THURSDAY	EVEN	6042	1	119
12626	THURSDAY	ODD	6043	2	119
12627	THURSDAY	EVEN	6043	2	119
12628	FRIDAY	ODD	6040	1	119
12629	FRIDAY	EVEN	6040	1	119
12630	FRIDAY	ODD	6041	2	119
12631	FRIDAY	EVEN	6041	2	119
12632	FRIDAY	ODD	6041	3	119
12633	FRIDAY	EVEN	6041	3	119
12634	WEDNESDAY	ODD	5631	3	53
12635	WEDNESDAY	ODD	5632	3	53
12636	WEDNESDAY	EVEN	5631	3	53
12637	WEDNESDAY	EVEN	5632	3	53
12638	FRIDAY	ODD	5631	2	74
12639	FRIDAY	ODD	5632	2	74
12640	FRIDAY	EVEN	5631	2	74
12641	FRIDAY	EVEN	5632	2	74
12642	MONDAY	ODD	5973	3	67
12643	MONDAY	EVEN	5966	3	67
12644	MONDAY	ODD	5967	4	67
12645	MONDAY	EVEN	5967	4	67
12646	MONDAY	ODD	5639	4	66
12647	MONDAY	EVEN	5639	4	66
12648	MONDAY	ODD	5778	2	65
12649	MONDAY	ODD	5779	2	65
12650	MONDAY	ODD	5780	2	65
12651	MONDAY	ODD	5781	2	65
12652	MONDAY	EVEN	5778	2	65
12653	MONDAY	EVEN	5779	2	65
12654	MONDAY	EVEN	5780	2	65
12655	MONDAY	EVEN	5781	2	65
12656	MONDAY	ODD	6045	2	61
12657	MONDAY	EVEN	6045	2	61
12658	MONDAY	ODD	6044	3	59
12659	MONDAY	EVEN	6044	3	59
12660	TUESDAY	ODD	5720	7	52
12661	TUESDAY	EVEN	5720	7	52
12662	TUESDAY	ODD	5721	7	52
12663	TUESDAY	EVEN	5721	7	52
12664	TUESDAY	ODD	5794	2	53
12665	TUESDAY	ODD	5795	2	53
12666	TUESDAY	ODD	5796	2	53
12667	TUESDAY	ODD	5797	2	53
12668	TUESDAY	EVEN	5794	2	53
12669	TUESDAY	EVEN	5795	2	53
12670	TUESDAY	EVEN	5796	2	53
12671	TUESDAY	EVEN	5797	2	53
12672	TUESDAY	ODD	5511	3	57
12673	TUESDAY	EVEN	5511	3	57
12674	TUESDAY	ODD	5510	3	57
12675	TUESDAY	EVEN	5510	3	57
12676	TUESDAY	ODD	5770	3	55
12677	TUESDAY	ODD	5771	3	55
12678	TUESDAY	EVEN	5770	3	55
12679	TUESDAY	EVEN	5771	3	55
12680	TUESDAY	ODD	5856	2	74
12681	TUESDAY	EVEN	5856	2	74
12682	WEDNESDAY	EVEN	5970	7	66
12683	WEDNESDAY	EVEN	5971	7	66
12684	TUESDAY	ODD	5496	2	59
12685	TUESDAY	ODD	6046	7	51
12686	TUESDAY	ODD	6047	7	51
12687	TUESDAY	ODD	6048	7	51
12688	TUESDAY	ODD	6049	7	51
12689	TUESDAY	ODD	6050	7	51
12690	TUESDAY	ODD	6051	7	51
12691	TUESDAY	EVEN	6046	7	51
12692	TUESDAY	EVEN	6047	7	51
12693	TUESDAY	EVEN	6048	7	51
12694	TUESDAY	EVEN	6049	7	51
12695	TUESDAY	EVEN	6050	7	51
12696	TUESDAY	EVEN	6051	7	51
\.


--
-- Data for Name: semester_day; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.semester_day (semester_id, day) FROM stdin;
57	WEDNESDAY
57	MONDAY
57	THURSDAY
57	FRIDAY
57	TUESDAY
\.


--
-- Data for Name: semester_group; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.semester_group (semester_id, group_id) FROM stdin;
57	56
57	84
57	37
57	43
57	33
57	28
57	66
57	71
57	95
57	52
57	40
57	94
57	30
57	49
57	41
57	59
57	98
57	27
57	62
57	87
57	58
57	50
57	42
57	55
57	106
57	29
57	105
57	5
57	65
57	61
57	45
57	26
57	38
57	53
57	31
57	103
57	104
57	64
57	39
57	102
57	36
57	85
57	57
57	67
57	46
57	70
57	51
57	72
57	93
57	44
57	86
57	73
57	63
57	54
57	100
57	60
57	68
\.


--
-- Data for Name: semester_period; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.semester_period (semester_id, period_id) FROM stdin;
57	1
57	2
57	3
57	4
57	7
57	8
\.


--
-- Data for Name: semesters; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.semesters (id, current_semester, description, disable, end_day, start_day, year, default_semester) FROM stdin;
53	f	2	f	2022-05-19	2022-02-01	2022	f
57	t	1 семестр 24/25	f	2024-12-13	2024-08-12	2024	t
\.


--
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.students (id, name, patronymic, surname, group_id, user_id) FROM stdin;
\.


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.subjects (id, disable, name) FROM stdin;
7	t	Pain
10	t	IOS
1	t	Computer Science
4	t	Node.js
3	t	Бекенд
2	t	Фронтенд
169	f	Українська  мова (за професійним спрямуванням)
15	f	Програмування
14	f	Алгебра і геометрія
13	f	Фізичне виховання
18	f	Іноземна мова
65	f	Вибрані розділи математичної фізики
170	f	Архітектура комп'ютерів
17	f	Дискретна математика
57	f	Диференціальна геометрія
114	f	Суч.ймовірн.задачі оптим.керув.та їх реалізація на ПК
32	f	Технології програмування на Java
58	f	Комплексний аналіз
86	f	Математична логіка
89	f	Мат.статистика з елементами теорії випадкових процесів
79	f	Методика викладання інформатики в початковій школі
33	f	Моделювання жорстких систем
93	f	Основи криптології
62	f	Основи медичний знань
67	f	Платформи корпоративних інформаційних систем
48	f	Програмування мовою Python
52	f	Психологія (загальна, вікова, педагогічна)
35	f	Сучасні СУБД
257	f	Актуальні питання історії та культури України
22	f	Лінійна алгебра
24	f	Аналітична геометрія
25	f	Вступ до спеціальності
27	f	Операційні системи
28	f	Професійна іноземна мова
30	f	Теорія ймовірностей та математична статистика
31	f	Теорія програмування
36	f	Теорія алгоритмів
37	f	Основи теорії систем
39	f	Числові методи
40	f	Основи інтернет-технологгій
41	f	Математична теорія ризиків
42	f	Комп'ютерна математика
43	f	Іноземна мова (за професійним спрямуванням)
44	f	Алгоритми і структури даних
45	f	Диференціальні рівняння
46	f	Об'єктно-орієнтоване програмування
77	f	Технології програмування мовою Python
50	f	Комп'ютерні мережі
51	f	Прикладний функціональний аналіз
54	f	Математичний аналіз2
16	f	Математичний аналіз1
55	f	Математичний аналіз
56	f	Алгебра і теорія чисел
60	f	Рівняння математичної фізики
61	f	Елементарна математика і методика викладання математики
63	f	Методика викладання математики
64	f	Методика викладання інформатики
66	f	Методи оптимізації та дослідження операцій
68	f	Проектування програмних систем
69	f	Системи та методи прийняття рішень
72	f	Теорія керування
73	f	Системний аналіз та теорія прийняття рішень
74	f	Випадкові процеси
75	f	Методи оптимізації
76	f	Основи математичного моделювання та системного аналізу
80	f	Інформаційно-комунікаційні технології в освіті
59	f	Теорія міри та інтеграла
83	f	Методи обчислень
84	f	Методика впровадження дослідних робіт з інформатики
92	f	Топологічні векторні простори
178	f	Обчислювальні методи
179	f	Філософія
82	f	Методика розв'язування олімп. задач з ІТ
94	f	Науковий семінар
99	f	Маг.семінар "Сучасні інформаційні технології"
102	f	Основи наукових досліджень
103	f	Математичний аналіз*
106	f	Інф.системи і техн.створення та управління проектами
107	f	Математичне моделювання динамічних систем і процесів
108	f	Мережеві інформаційні технології
109	f	Обробка структурованих та нестрктурованих даних BigData
110	f	Системи штучного інтелекту
111	f	Програмні засоби управління проектами
116	f	Розробка професійного програмного забезпечення
119	f	Системи і методи захисту інформації
122	f	Технології викладання математики у закладах освіти
123	f	Теорія функцій багатьох змінних
171	f	Математична логіка та теорія алгоритмів
128	f	Диференц.моделі соціальних та природничих процесів
129	f	Зображення геометричних фігур у просторі
78	f	Frontend-розробка Web-додатків
132	f	Англійська мова
133	f	Німецька мова
134	f	Французька мова
100	f	Філософія освіти і науки
173	f	Архітектура обчислювальних систем
174	f	Пакети прикладних програм
175	f	Олімпіадні задачі з інформаційних технологій
124	f	Інноваційні технології навчання в сучасній школі
81	f	Хмарні технології в освіті
130	f	Конфліктно-керовані процеси та нелінійні моделі
97	f	Інтелектуальна власність в ІТ-галузі
96	f	Комунікації та теорії конфліктів
117	t	Методи Data Science
105	f	Педагогіка і психологія вищої школи
95	f	Охорона праці в ІТ-галузі
113	f	Інтелектуальні системи прийняття рішень
118	f	Розробка крос-платформених додатків
258	f	Використання MS Excel y BigData
101	f	Охорона праці в галузі та цивільний захист
131	f	Системи та методи захисту інформації
115	f	Технології розробки розподілених баз даних
181	f	Поглиблена 3D графіка
182	f	Інформаційні технології менеджменту
183	f	Бібліотеки мови Python
184	f	Бази даних та знань
49	f	Громадське здоров'я та медицина порятунку
185	f	Програмування у Visual Studio NET
186	f	Математичне моделювання еволюційних процесів
188	f	Педагогіка з основами педмайстерності
189	f	Комп'ютерні мережі та Інтернет
190	f	Програмно-педагогічні засоби навчання
191	f	Векторна та растрова графіка
192	f	Обчислювальна геометрія
193	f	Топологія
196	f	Захист інформації
197	f	Платформи корпоративних інформ.систем
198	f	Програмування та підтримка Веб-застосунків
199	f	Системне програмування
201	f	Основи інформаційної безпеки
202	f	Теорія інформації та кодування
203	f	Серверна мова РНР
204	f	Контроль якості та тестування програмного забезпечення
205	f	Web-дизайн
207	f	Інтерпретована динамічна візуальна мова програмування
208	f	Функціональний аналіз
209	f	Нестандартні задачі математики та методи їх розв'язання
71	f	Комунікаційні технології в управлінні проектами
211	f	Загальна теорія функцій
212	f	Сучасні інформаційні технології
213	f	Теорія ймовірностей
194	f	Обробка зображень та мультимедія
214	f	Інтелектуальні інформаційні системи
215	f	Аналіз даних
218	f	Розробка комп'ютерних ігор
219	f	Актуарна математика
220	f	Теорія компіляції
221	f	Математичне моделювання природничих процесів
222	f	Варіаційне числення і методи оптимізації
223	f	Управління навчальними процесами
224	f	Базові алгоритми олімпіадних задач з інформатики
225	f	Методика розв'язування олімпіадних задач з математики
226	f	Інформаційні технології у підготовці дидакт.матеріалів
228	f	Основи геометрії
230	f	Методологія та організація наукових досліджень
231	f	Багатопроцесорні машини та техн.паралельного прогр.
232	f	Маркетингові комунікації в інформаційному суспільстві
233	f	Методика викладання комп.наук у вищій школі
235	f	Комунікаційні технології аналітичних систем
236	f	Інтелект.системи прийняття рішень
237	f	Системи машинного навчання
238	f	Програмні засоби в системному аналізі
187	f	Розробка UI/UX дизайну
239	f	Технології паралельного програмування
240	f	Моделювання соціальних та кризових явищ
243	f	Розробка мобільних додатків для ОС Android
244	f	Java-технології в клієнт-серверних системах
245	f	Паралельне програмування
246	f	Магістерський семінар 1
248	f	Задачі з параметрами
249	f	Сучасні технології в дистанційній освіті
251	f	Класифікація методів розв'язування олімпіадних задач
253	f	Методика викладання математики у закладах вищої освіти
254	f	Теорія наближень
255	f	Комунікаційні техн.в управлінні проектами
241	f	Сучасні клієнтські Web-технології
19	t	Актуальні питання історії та кул.України
259	f	Алгебра і геометрія*
260	f	Лінійна алгебра*
261	f	Диференціальні рівняння.
262	f	Ств.веб-додатків з вик.фреймворку Django мови Python
264	f	Основи інклюзивної освіти
217	f	Розробка програмних додатків для мобільних пристроїв
112	f	Сіткове планування
267	f	Історія математики
268	f	Задачі прикладного характеру
85	f	Геометричні перетворення
269	f	Стереометрія в задачах
271	f	Олімпіадні задачі з алгебри і теорії чисел
272	f	Прогнозування в системному аналізі
274	f	Методи DataScience
277	f	Партнерство і професійна комунікація вчителя
278	f	Технології викладання інформатики у закладах освіти
200	f	Математичні моделі макро- і мікроекономіки
242	f	Комп'ютерне моделювання еколого-економ.систем
176	f	Обчислювальна геометрія та комп'ютерна графіка
276	f	Інклюзивна педагогіка
234	f	Моделювання соціального-економічних та еколог.процесів
265	f	Вибрані питання Ріманової геометрії
206	f	Методика соціально-виховної роботи в сучасних умовах
279	f	Розподілені інформаційно-аналітичні системи
281	f	Практика особистої та ділової комунікації іноземною мовою
288	f	Ознайомлювальна практика
290	f	Математична логіка та теорія алгоритмів*
291	f	Архітектура ПК
293	f	3D графіка та моделювання
294	f	ІТ та онлайн сервіси в професійній діяльності вчителя*
295	f	Векторні гратки
296	f	Прикладні алгоритми теорії чисел
297	f	Професійно зорієнтована практика
298	f	Предметний практикум
299	f	Навчально-педагогічна практика
300	f	Професійно зорієнтована практика з елементами програмування
301	f	Інтелектуальний аналіз даних та моделювання кризових явищ
302	f	Інформаційні системи і  технології створення та управління проектами
303	f	Інформаційні системи та технології в системному аналізі
304	f	Технології Blockechain та прогнозування фінансових ризиків
305	f	Бізнес аналіз в ІТ-проектах
306	f	Математична майстерня
307	f	Web-розробка з використанням фреймворків
308	f	Адміністрування навчальних систем
309	f	Мережні інформаційні та освітні системи
310	f	Особливості розв'язування олімп.задач з інформатики та ІТ
311	f	Лідерство та основи партнерської взаємодії в освітньому процесі
312	f	Математичні студії (особливості викладання інформатики у початк.та середній НУШ
313	f	STEM-практики в освіті
314	f	Принципи та методи навчання інформатики в закладах освіти
315	f	Методика навчання математики в закладах освіти
316	f	Геометричні та комбінаторні олімпіадні задачі
317	f	Польська мова для професійного спілкування
318	f	Методика організації позаурочної роботи з математики
319	f	Методика розв'язування олімпіадних задач з інформатики
320	f	Комп'ютерні технології у тестуванні
321	f	Інформаційні технології у підготовці дидактичних матеріалів
322	f	Чинники успішного працевлаштування
323	f	Python для Data Science
324	f	Бази даних у навчальному процесі
325	f	Створення веб-додатків з використанням фреймворку Django мови Python
326	f	Бази даних та інформаційні системи
70	f	Інформаційні системи обліку та логістика
328	f	Комп'ютерне моделювання жорстких процесів та систем
329	f	Основи штучного інтелекту
330	f	Фреймворки JavaScript
327	f	Здоров'язбережувальні технології та медицина порятунку
332	f	Здоров'язбережувальні технології та домедична допомога
333	f	Хмарні технології
334	f	Елементи теорії чисел у ЗЗСО
335	f	Вибрані питання геометрії (основна школа)
336	f	Комунікативні технології в управлінні проектами
337	f	Прикладний статистичний аналіз з використанням Python
338	f	Елементи теорії випадкових процесів
339	f	Основи DevOps
340	f	Тренінг професійного розвитку вчителя
341	f	Практикум з тригонометрії
342	f	Математична статистика з елементами теорії випадкових процесів
343	f	Штучний інтелект та аналітика BigData
344	f	Технології навчання математики та інформатики в закладах освіти
345	f	Інформаційно-комунікаційні, хмарні технології в освіті
346	f	Професійна іншомовна комунікація
348	f	Класифікація та методи розв'язування задач з параметрами
349	f	Вибрані питання алгебри та початків аналізу
350	f	Технології розробки програмно забезпечення
351	f	Вибрані питання інформатики
352	f	Інформатична STEM освіта
353	f	Медіаграмотність
354	f	Професійна комунікація та управління конфліктами
355	f	Теоретичні основи прикладних досліджень
356	f	Технології розробки та проектування ІС екологічного моніторингу
359	f	Організація наукової роботи учнів з математики та інформатики в НУШ
360	f	Сучасні проблеми інформатики
361	f	Web-технології та web-програмування
362	f	Нереляційні бази даних
363	f	Практикум з розв'язування задач шкільного курсу математики (основна школа)
364	f	Програмні засоби навчання у освітньому процесі
365	f	Вибрані питання шкільного курсу математики
366	f	Математичне та комп'ютерне моделювання
367	f	Інтегровані уроки, особливості викладання
368	f	Геометрія мас
369	f	Математичні методи в системах штучного інтелекту та нейронних мереж
370	f	Метод.особливості викладання інформатики в НУШ
371	f	Мережеві інформаційні та освітні системи
372	f	Релігієзнавство
373	f	Латинська мова та основи наукової термінології
374	f	Власний бізнес : реєстрація, облік, оподаткування
375	f	Інтернет-літературна творчість: види і жанри
379	f	Нечітка логіка в інтелектуальних системах
380	f	Web-розробка на Ruby on Rails
292	f	Фінансова математика
377	f	Багатопроцесорні машини та техн.парал.прогр.
381	f	Системи оцінювання здобувачів освіти в сучасній школі
53	f	Основи інформаційних систем та технологій
382	f	Методика позакласної роботи з інформатики
331	f	Управління ІТ проектами
383	f	C# та NET: Розробка програмного забезпечення
384	f	Перші типи топологічних векторних просторів
385	f	Система комп'ютерної математики Maxima
386	f	Системи та методи прийняття рішень в соціальних та економічних системах
387	f	Методи і засоби викладання фахових дисциплін та наукових досліджень
388	f	Середовище блочного програмування
389	f	Управління навчальними проектами
390	f	Фінансова грамотність
\.


--
-- Data for Name: teachers; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.teachers (id, disable, name, patronymic, "position", surname, user_id, department_id) FROM stdin;
102	f	Наталія	Михайлівна	доцент	Попович	\N	\N
19	f	Ігор	Дмитрович	асистент	Скутар	\N	\N
21	f	Володимир	Васильович	професор	Михайлюк	\N	\N
23	f	Тарас	Іванович	доцент	Звоздецький	\N	\N
26	f	Василь	Володимирович	доцент	Нестеренко	\N	\N
7	t	Олександр	Петровичd	Професор	Рурський	44	\N
28	f	Олена	Георгіївна	асистент	Фотій	\N	\N
30	f	Ігор	Михайлович	професор	Черевко	\N	\N
31	f	Наталія	Іллівна	асистент	Фонарюк	\N	\N
32	f	Тоня	Михайлівна	доцент	Фратавчан	\N	\N
34	f	Лариса	Андріївна	доцент	Піддубна	\N	\N
36	f	Ігор	Валерійович	доцент	Юрченко	\N	\N
5	t	Дмитро	Святославович	Юніті	Савостьянов	13	\N
40	f	Василь	Йосипович	доцент	Кушнірчук	\N	\N
41	f	Тетяна	Петрівна	доцент	Караванова	\N	\N
42	f	Андрій	Богданович	асистент	Дорош	\N	\N
43	f	Руслана	Степанівна	доцент	Колісник	\N	\N
44	f	Вадим	Ілліч	доцент	Мироник	\N	\N
45	f	Вікторія	Сергіївна	асистент	Лучко	\N	\N
46	f	Віра	Степанівна	доцент	Сікора	\N	\N
47	f	Наталія	Михайлівна	асистент	Шевчук	\N	\N
48	f	Ольга	Василівна	професор	Мартинюк	\N	\N
49	f	Світлана	Богданівна	доцент	Боднарук	\N	\N
50	f	Жана	Ілінічна	асистент	Довгей	\N	\N
52	f	Микола	Петрович	доцент	Філіпчук	\N	\N
3	t	Денисs	Павлович	Помічник	Чікар	8	\N
108	f	Владислав	Антонович	професор	Літовченко	\N	\N
66	f	Галина	Василівна	доцент	Мельник	\N	\N
67	f	Богдан	Дмитрович	доцент	Шепетюк	\N	\N
70	f	Олександр	Васильович	доцент	Матвій	\N	\N
71	f	Тетяна	Миколаївна	доцент	Сопронюк	\N	\N
37	f	Іван	Іванович	професор	Клевчук	\N	\N
96	f	Аліна	Андріївна	асистент	Плегуца	\N	\N
4	t	Anton	Petrovych	Cool	Shevchuk	38	\N
11	t	Tetiana	Tanasiivna	teacher	Vykliuk	48	\N
10	t	Макійaaaaaa	Іванович	Сейморв	Джудуж	\N	\N
1	t	Бамбіно	Брусте	Професор	Діно	14	\N
6	t	Дмитро	Васильович	Помічник	Колодюк	21	\N
145	f	Інна	Владиславівна	доцент	Ковальчук	\N	\N
106	f	Тетяна	Іванівна	доцент	Радзиняк	\N	\N
101	t	Валентина	Візіторівна	професор	Балахтар	\N	\N
60	f	Іван	Михайлович	асистент	Данилюк	\N	\N
63	f	Світлана	Анатоліївна	асистент	Іліка	\N	\N
72	f	Лідія	Миколаївна	асистент	Сергєєва	\N	\N
73	f	Тетяна	Іванівна	доцент	Готинчан	\N	\N
77	f	Володимир	Миколайович	доцент	Лучко	\N	\N
78	f	Олег	Михайлович	доцент	Ленюк	\N	\N
75	f	Анастасія	Олександрівна	асистент	Юрійчук	\N	\N
79	f	Лілія	Михайлівна	доцент	Мельничук	\N	\N
80	f	Микола	Юрійович	асистент	Горбатенко	\N	\N
61	f	Андрій	Сергійович	доцент	Перцов	\N	\N
81	f	Василь	Григорович	доцент	Маценко	\N	\N
33	f	Галина	Петрівна	доцент	Івасюк	\N	1
35	f	Галина	Савеліївна	доцент	Пасічник	\N	\N
65	f	Ярослав	Йосипович	професор	Бігун	\N	\N
64	f	Ірина	Вікторівна	доцент	Дорошенко	\N	\N
22	f	Олена	Олексіївна	професор	Карлова	\N	\N
82	f	Галина	Михайлівна	доцент	Перун	\N	\N
83	f	Іван	Васильович	професор	Житарюк	\N	\N
111	f	Оксана	Любомирівна	доцент	Даскалюк	\N	\N
97	f	Викладач	Викладач	асистент	Викладач	\N	\N
85	f	Олена	Миколаївна	асистент	Гусак	\N	\N
90	f	Ірина	Олександрівна	асистент	Захарчук	\N	\N
99	t	Василь	Сергійович	асистент	Мельник	\N	\N
98	t	Ольга	Сергіївна	доцент	Шестобуз	\N	\N
105	f	Денис	Павлович	асистент	Онипа	\N	\N
107	f	Дмитро	Валерійович	асистент	Шкільнюк	\N	\N
87	f	Лілія	Василівна	асистент	Маковійчук	\N	\N
149	f	Наталя	Олександрівна	асистент	Мельничук	\N	\N
91	f	Тетяна	Василівна	доцент	Тоненчук	\N	\N
94	f	Оксана	Євгенівна	доцент	Гордійчук	\N	\N
76	f	Світлана	Сільвестрівна	доцент	Доскач	\N	\N
162	f	Оксана	Мирославівна	асистент	Яцько	\N	6
54	t	Олександр	Олександрович	асистент	Блажевський	\N	\N
166	f	Ігор	Володимирович	доцент	Малик	\N	\N
88	f	Мирослава 	Миколаївна	асистент	Шенько	\N	\N
168	f	Михайло	Михайлович	професор	Попович	\N	\N
62	f	Наталія	Вікторівна	асистент	Романенко	\N	4
183	t	Викладач	Викладач	асистент	Викладач	\N	\N
184	f	Ганна	Павлівна	доцент	Бигар	\N	\N
185	f	Юрій	Віталійович	асистент	Луцюк	\N	\N
189	f	Василь	Сергійович	асистент	Мельник	\N	\N
190	f	Іннеса	Володимирівна	доцент	Краснокутська	\N	\N
191	f	Наталія	Іванівна	доцент	Кучумова 	\N	\N
194	f	Богдан	Олегович	асистент	Яшан	\N	\N
195	f	Ганна	Петрівна	асистент	Вережак	\N	\N
198	f	Сергій	Васильович	доцент	Мартинюк 	\N	\N
199	f	Галина 	Михайлівна	асистент	Унгурян	\N	\N
200	f	Лариса	Василівна	доцент	Мафтин	\N	\N
204	f	Наталя	Сергіївна	асистент	Правіцка 	\N	\N
203	f	Василь	Михайлович	асистент	Косован	\N	\N
205	f	Маріан	Філаретович	професор	Бирка	\N	\N
161	f	Наталія	Василівна	асистент	Цинтар	\N	\N
210	f	Тетяна	Анатоліївна	асистент	Равлюк	\N	\N
216	f	Володимир	Сергійович	доцент	Кшевецький	\N	\N
218	f	Галина	Степанівна	асистент	Артеменко 	\N	\N
219	f	Ольга	Іванівна	асистент	Луган	\N	\N
221	f	Роман	Вікторович	асистент	Івасюк	\N	\N
53	f	Олена	Василівна	доцент	Мудра	\N	\N
226	f	Світлана	Борисівна	асистент	Бортник 	\N	\N
220	f	Мар'яна	Петрівна	асистент	Ривак	\N	\N
207	t	Іван	Дмитрович	професор	Пукальський 	\N	\N
230	f	Роман	Іванович	професор	Петришин	\N	\N
231	f	Людмила	Вікторівна	доцент	Романів	\N	\N
232	f	Іван	Дмитрович	професор	Пукальський 	\N	\N
233	f	Василь	Михайлович	асистент	Косован*	\N	\N
187	f	Анна	Миколаївна	асистент	Кричун	\N	\N
234	f	Володимир	Володимирович	доцент	Білоус	\N	\N
\.


--
-- Data for Name: temporary_schedule; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.temporary_schedule (id, date, grouped, lessontype, subject_for_site, vacation, group_id, period_id, room_id, semester_id, subject_id, teacher_id, notification, schedule_id, link_to_meeting) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.users (id, email, password, role, token) FROM stdin;
11	test41@test.com	$2a$10$JY/bzDg4cY6Am1R1RPkk2.JieH0DRKSjQ1FwAUt9BMSnIp/H4bNzC	ROLE_USER	33dd9cb6-75db-4222-b036-66f235a787c1
12	test50@test.com	$2a$10$.RGmFapkahytT9xtgnJspOUmzeVRyXtrHtxY1hdybyNSX7U33XrPK	ROLE_USER	f6abe608-6381-4f87-b9c8-139ec5892be5
15	test410@test.com	$2a$10$bpJDasyJxm.ltw5ZMZYZHe0hmddKKAqvYP4CQMzRkZYaL.2jionQG	ROLE_USER	a6b56362-6170-4d5b-a1d8-1a7067a75c69
17	das@mail.com	$2a$10$.kRighywghveMzRXAPC.r.muVm5jh.sZb5nhlm871LF2.oqV.9fZ6	ROLE_USER	918b5320-81c2-4883-819c-bf1fdc44ba94
1	folf_test@test.com	$2a$10$a/wpHr7KA8.gvk8kmOvIr.wCK2mZUp0Jv46MzIoVW4Y/PYMS/pmcC	ROLE_MANAGER	\N
3	Fedir_@i.ua	$2a$10$a/wpHr7KA8.gvk8kmOvIr.wCK2mZUp0Jv46MzIoVW4Y/PYMS/pmcC	ROLE_MANAGER	\N
9	test4@test.com	$2a$10$fwBnMzbASCdAHaeiwlNji.Y9EnitJevRdHOrwIEYjlBbPBl7sq4ea	ROLE_TEACHER	0bbb3631-be44-4bc2-930e-4d377c4da9ff
20	oleksandrkravets1995@gmail.com	$2a$10$PgvbsX9gmvBDcXcWcU0Ak.RcluITm77XQCrsvZZsHMGlA4nY3wFye	ROLE_MANAGER	\N
6	test@test.com	$2a$10$J7mqEk43IlKMZD72NqaYi.IcCi/fNFYqpjNyed/aVpiQCr17.cIVe	ROLE_USER	3bf11b95-3771-4533-9fa5-0311e2fea7d8
22	aaaaasdfcvgtbhj7ku@gmail.com	adsfdvgftjhgn	ROLE_USER	\N
23	noname@gmail.com	adsfdvgftjhgn	ROLE_USER	\N
25	noname2@gmail.com	adsfdvgftjhgn	ROLE_USER	\N
2	vasja.mazuryk@gmail.com	$2a$04$SpUhTZ/SjkDQop/Zvx1.seftJdqvOploGce/wau247zQhpEvKtz9.	ROLE_MANAGER	\N
26	Fedir_@email.ua	$2a$10$KxihjeqGUUUoEf7WrOEjbu77C8VTfEWK5kDnDVNkGkKA8C1fZ2QZK	ROLE_USER	d906f12c-4a7d-478f-9fd5-08e57efac2ad
32	test4021312312312312@test.com	$2a$10$hqtQdFER6EXsDsbLaWw6g.e92lGob99jwImkLSNCMlVrE0LAbRFYO	ROLE_USER	3625ca8c-d2b0-49fa-a35c-a9896f5b69ee
10	test40@test.com	$2a$10$HrN7h.UlANnxyNlgvHQ7eOKI4RGWoqfzCiAt4RLq649rsSLsSNaGq	ROLE_TEACHER	5ae335bc-cc26-491e-a366-cc532e892a7c
4	aaaaqewdf@gmail.com	string	ROLE_USER	\N
19	aaaaqewdfaaa@gmail.com	string	ROLE_USER	\N
18	degvtawsfdgnf@gmail.com	string	ROLE_USER	\N
28	jowiti1173@emailhost99.com	$2a$10$0c/pG/8U/yjhFNBniCyYHOAas4gOF.O9b8ZJTsDEvjn4xQ338J3M6	ROLE_USER	\N
34	oleksandrkravets1995123213312@gmail.com	$2a$10$x38zos8srXPYtM1HrkRVtOzWf9lRQKmmLvzRccf9A7/6TiZAd87WO	ROLE_USER	d5d9cf02-0b8e-4a17-b223-67d492f3e5ff
30	aaaassssssasqewdf@gmail.com	string	ROLE_USER	\N
29	aaaasssssaasasqewdf@gmail.com	string	ROLE_USER	\N
33	mitrobaz91@gmail.com	$2a$10$AkdUxFiC.NUS7nC1S4wrh.5HOU8s5Hqev2ZVvNlhvxrU6GKCrrgui	ROLE_USER	\N
35	toxa13.01@ukr.net	$2a$10$gGqAlAo4jXtdUw6fQHFsDuy19lDz9fcnEfQ4JCkzTd/ucs61zJPpu	ROLE_USER	dedf6dc2-d603-4605-987e-c30fb27475f0
36	toxa13.02@ukr.net	$2a$10$n42piLaPdPXrjztMBqkaJurcKRRD0yZodW.S282aY1vS3GbKtgqhS	ROLE_USER	893b2551-8610-49d3-9613-d8652a31da65
27	aaaaaa@gmail.com	aaaavregtdrfhberb	ROLE_USER	\N
37	sdfsdvsdvdv@gmail.com	stringsssss	ROLE_USER	\N
8	test_user	$2a$04$SpUhTZ/SjkDQop/Zvx1.seftJdqvOploGce/wau247zQhpEvKtz9.	ROLE_TEACHER	\N
42	test540123@test.com	$2a$10$gj3wgw2LcEBqEZlvWj1TO.F4lW0UZ9Hmp2Wi2jdWiD3uk2HDAkHQW	ROLE_USER	c6d151b1-8535-4fd5-933e-1a2c69099656
43	gafowe1087@coalamails.com	$2a$10$8hKpi/Vj5vMwqdVPcSVArOMlXw/L7lz/QWXYGgMHsooiqEG5G177G	ROLE_TEACHER	\N
50	notice.board1221@gmail.com	$2a$10$U1QB090zQBtbWKVb0dBLT.E1Y9KH1tddOcfAYLUZHvx/Q1aWs1IkK	ROLE_USER	\N
40	stringsds@gmail.com	stringsdsd	ROLE_USER	\N
45	stringsds111@gmail.com	stringsdsd	ROLE_USER	\N
47	stringsdcfervedb@gmail.com	string	ROLE_USER	\N
46	stringaasasq@gmail.com	string	ROLE_USER	\N
49	stringasdfvsrg@gmail.com	$2a$10$/gCJFc6ithNWbZuj9EGFSO1Wb2hJCQP.EJhS.ettiCTFTpxYLeNXO	ROLE_USER	8cfb8c81-4025-457c-881b-8cf2193838e3
44	toxa13.00@ukr.net	$2a$10$WQT0t7ql5JkRoEqG7D7jMeRqjbtyAwLkBKHiz7Ect.X/FSQTfVWHO	ROLE_USER	\N
13	test45@test.com	$2a$10$zmLW/J700eouFqK3f9BThep2ca0caPFRDrEPEijInUSD/ngIbqxCC	ROLE_USER	c496655b-37e2-40fd-8661-7decaecf631b
38	mnepohuinanickname@gmail.com	$2a$10$5fbAftld306o4Ug84Pe6IOTYoW9ITGTgosP6Otvj4YCMKKbZ5SpTe	ROLE_USER	\N
48	tanya.vykliuk@gmail.com	$2a$10$rrFW0heVYunJFJwfLvggl.VresUzyJKZgc79.MRrfGB6XwitjLQKe	ROLE_USER	\N
14	test80@test.com	$2a$10$x7KDBNenz3PLeaXdYjXyFuHL/9GRmMpVzrqh1AZ9NUyyokCpEQysS	ROLE_USER	14fe6942-85da-49cb-a14e-3b743820e36e
21	aaaa@gmail.com	$2a$04$zpA2SNu7WAjToGz5C6ZKKOCwYnOHpMQ1bEisxfwWtMTM3jJMugAkq	ROLE_USER	\N
7	i.masliuchenko@chnu.edu.ua	$2a$04$zpA2SNu7WAjToGz5C6ZKKOCwYnOHpMQ1bEisxfwWtMTM3jJMugAkq	ROLE_MANAGER	\N
16	petrofediuk004@gmail.com	$2a$04$zpA2SNu7WAjToGz5C6ZKKOCwYnOHpMQ1bEisxfwWtMTM3jJMugAkq	ROLE_TEACHER	\N
65	ivankozmulyak@gmail.com	$2a$10$yg9fyW242kM.Rz0tLa8LReYaQzskLOElilC.vonvxHU1yMIsKyFWy	ROLE_USER	fe814151-62a7-4745-96e5-34e29b45c52d
66	herasymchuk.anastasiia@chnu.edu.ua	$2a$10$5LAQW.cXwh6TkZncy9p8C.3DkOOM3WDquvfnliDYjdOTB0cMBpV8a	ROLE_USER	26dd3055-0639-474f-8a4a-be37edfd4e6f
68	admin@gmail.com	$2a$10$o.Q3V2u2TcRgMlup2E3m3OhQrK2jOuRhV5H3iBs5AEK6Oh1BSmy4G	ROLE_USER	b8b09edc-d141-4317-bd29-a01a08ba1694
67	offic6e@chnu.edu.ua	$2a$10$34kt/1Zt4SdxZCSg8tv8oei53REQgH6qZ/TDGU.7O19i61anT7yiK	ROLE_USER	d731d3df-30b0-422f-8cae-4551df03a216
73	gerasymchuk88888888@gmail.com	A&vbSdvSeук4му%ца349ІВмк432ем0!Qfdruevvb	ROLE_USER	\N
64	kondrserg1@gmail.com	$2a$10$VGyx651t21jGGx0aVVKK4uFvyV6nl6NYu4LJQJkWB5YUobrlF4zRu	ROLE_MANAGER	\N
78	yashchemskyio@gmail.com	A&vbSdvSeук4му%ца349ІВмк432ем0!Qfdruevvb	ROLE_USER	\N
77	ivan.demianchuk@kpk-lp.com.ua	A&vbSdvSeук4му%ца349ІВмк432ем0!Qfdruevvb	ROLE_USER	\N
79	akr1sdevelop@gmail.com	A&vbSdvSeук4му%ца349ІВмк432ем0!Qfdruevvb	ROLE_USER	\N
80	viktoriia.kosovan@gmail.com	A&vbSdvSeук4му%ца349ІВмк432ем0!Qfdruevvb	ROLE_USER	\N
85	see4.whoami@gmail.com	$2a$10$e7a8dxs8J.qSu8W9RYsjte67pe88mQ2M9afe.sQ24M36zFpQo3XO.	ROLE_USER	21037a99-4201-4d20-bb2a-2b80a98b09fd
86	popesku.andrii@chnu.edu.ua	$2a$10$nW2BHhowDif8kwqan8X7guIroo4HojI991q1m0AzV2hVeaEnegAbW	ROLE_USER	f08b31a5-70e9-4589-9504-2cf7876e9c16
87	andepopeskua@gmail.com	$2a$10$adiz0bLpDW4du5Yitken3ePrfzFMW126t1pNZk3KPNNVYBldiK2ui	ROLE_USER	7021a42b-89d3-4121-b52e-2dc635781432
88	kolyabolabolya678@gmail.com	$2a$10$yz1O3cvhbw0eiaJf0rHsBOOKmS86gSJQ2bBeHb2XazKE8nhZsxlsq	ROLE_USER	0581d8c7-43a3-44b7-82c5-6cf15704051d
89	vlasenko.yuliia@gmail.com	$2a$10$VPVZyQ0CmmEEVUj6Sa1jrO9qt/BfHYu0QHCdr1HccVRSZNgo44hnu	ROLE_USER	7650966d-1cdf-4b45-9c29-8ece717c0480
90	jbegou26@gmail.com	$2a$10$9MX6ywespCWLu1y6P1pCjOjUWGHP1vQh3OX1KQEk5KPbfPSwWRoXS	ROLE_USER	7edb4ebd-2512-4821-a1fe-b79046981a7a
91	ivanunik@icloud.com	$2a$10$7aJ1AwH.ILE5.iQ4r/eBQeWDFAibWnorZCYX.QmAHLJWgpcIUq4Ke	ROLE_USER	77f43337-b34b-4189-8629-8435b0dbac78
92	shevtsova19931993@gmail.com	$2a$10$RS09YnzR1rtz.X51hsaScOgsTCTck59nh..aVLtreJDQU1mr9sea.	ROLE_USER	ee446e90-cefa-43a9-9665-2ce0c91486b1
93	23elina94@gmail.com	$2a$10$dcdCx8wkhmzSMwteuAYEOe4m.cZ/dlcBKjxOYr7YBdqKy/T4cYfZ6	ROLE_USER	5114b366-fa07-4fcc-8a15-b3df3e473780
94	marianchuk.maksym@chnu.edu.ua	$2a$10$7EBkrJgfNqeSf/7ZazjLI.WI.KqpAP51oMzk718cqFBQG.HJPVrd6	ROLE_USER	a5580d13-a819-4d35-8e4f-2548dc912b65
\.


--
-- Name: department_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.department_id_seq', 16, true);


--
-- Name: groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.groups_id_seq', 106, true);


--
-- Name: lessons_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.lessons_id_seq', 6073, true);


--
-- Name: periods_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.periods_id_seq', 9, true);


--
-- Name: room_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.room_types_id_seq', 9, true);


--
-- Name: rooms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.rooms_id_seq', 123, true);


--
-- Name: schedules_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.schedules_id_seq', 12801, true);


--
-- Name: semesters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.semesters_id_seq', 57, true);


--
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.students_id_seq', 12, true);


--
-- Name: subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.subjects_id_seq', 390, true);


--
-- Name: teachers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.teachers_id_seq', 234, true);


--
-- Name: temporary_schedule_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.temporary_schedule_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 94, true);


--
-- Name: databasechangeloglock databasechangeloglock_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.databasechangeloglock
    ADD CONSTRAINT databasechangeloglock_pkey PRIMARY KEY (id);


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: lessons lessons_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT lessons_pkey PRIMARY KEY (id);


--
-- Name: periods periods_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.periods
    ADD CONSTRAINT periods_pkey PRIMARY KEY (id);


--
-- Name: room_types room_types_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.room_types
    ADD CONSTRAINT room_types_pkey PRIMARY KEY (id);


--
-- Name: rooms rooms_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_pkey PRIMARY KEY (id);


--
-- Name: schedules schedules_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT schedules_pkey PRIMARY KEY (id);


--
-- Name: semester_group semester_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_group
    ADD CONSTRAINT semester_group_pkey PRIMARY KEY (semester_id, group_id);


--
-- Name: semester_period semester_period_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_period
    ADD CONSTRAINT semester_period_pkey PRIMARY KEY (semester_id, period_id);


--
-- Name: semesters semesters_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semesters
    ADD CONSTRAINT semesters_pkey PRIMARY KEY (id);


--
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (id);


--
-- Name: teachers teachers_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT teachers_pkey PRIMARY KEY (id);


--
-- Name: temporary_schedule temporary_schedule_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT temporary_schedule_pkey PRIMARY KEY (id);


--
-- Name: users uk_6dotkott2kjsp8vw4d0m25fb7; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT uk_6dotkott2kjsp8vw4d0m25fb7 UNIQUE (email);


--
-- Name: subjects uk_aodt3utnw0lsov4k9ta88dbpr; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT uk_aodt3utnw0lsov4k9ta88dbpr UNIQUE (name);


--
-- Name: periods uk_bgj9vbqf54b7iryxqu895bggh; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.periods
    ADD CONSTRAINT uk_bgj9vbqf54b7iryxqu895bggh UNIQUE (name);


--
-- Name: department uk_biw7tevwc07g3iutlbmkes0cm; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.department
    ADD CONSTRAINT uk_biw7tevwc07g3iutlbmkes0cm UNIQUE (name);


--
-- Name: groups uk_ct3jhny5hfe6uj2osyn8a4p83; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT uk_ct3jhny5hfe6uj2osyn8a4p83 UNIQUE (title);


--
-- Name: room_types uk_gunh6313ruq1dghti9p00529u; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.room_types
    ADD CONSTRAINT uk_gunh6313ruq1dghti9p00529u UNIQUE (description);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: schedules fk34r5t4jexlcas19pleifb8ihv; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT fk34r5t4jexlcas19pleifb8ihv FOREIGN KEY (room_id) REFERENCES public.rooms(id);


--
-- Name: semester_day fk36f17dewxqjhb23rhlmc7slk3; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_day
    ADD CONSTRAINT fk36f17dewxqjhb23rhlmc7slk3 FOREIGN KEY (semester_id) REFERENCES public.semesters(id);


--
-- Name: temporary_schedule fk3hid2313ah5gjqqye9d3eik2g; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT fk3hid2313ah5gjqqye9d3eik2g FOREIGN KEY (room_id) REFERENCES public.rooms(id);


--
-- Name: schedules fk4g2p59v3jm7hk6a9ufdufy8ie; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT fk4g2p59v3jm7hk6a9ufdufy8ie FOREIGN KEY (period_id) REFERENCES public.periods(id);


--
-- Name: semester_group fk4j15tivie8ttfhl0s7x3o3syv; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_group
    ADD CONSTRAINT fk4j15tivie8ttfhl0s7x3o3syv FOREIGN KEY (semester_id) REFERENCES public.semesters(id);


--
-- Name: schedules fk7f954gltrwny6pe4see76kpw8; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schedules
    ADD CONSTRAINT fk7f954gltrwny6pe4see76kpw8 FOREIGN KEY (lesson_id) REFERENCES public.lessons(id);


--
-- Name: semester_period fk94poii1rmjhoevjx7bsymtbtd; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_period
    ADD CONSTRAINT fk94poii1rmjhoevjx7bsymtbtd FOREIGN KEY (semester_id) REFERENCES public.semesters(id);


--
-- Name: temporary_schedule fka1bsm9fsuxn5t098i2cb7nncu; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT fka1bsm9fsuxn5t098i2cb7nncu FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: temporary_schedule fkaqmj2bajc0ud8wproqn4843pk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT fkaqmj2bajc0ud8wproqn4843pk FOREIGN KEY (semester_id) REFERENCES public.semesters(id);


--
-- Name: lessons fkbr76cuebuufbbltujpfq04tto; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT fkbr76cuebuufbbltujpfq04tto FOREIGN KEY (teacher_id) REFERENCES public.teachers(id);


--
-- Name: lessons fke94a0k21xpi7glv89af90lwjv; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT fke94a0k21xpi7glv89af90lwjv FOREIGN KEY (subject_id) REFERENCES public.subjects(id);


--
-- Name: rooms fkh9m2n1paq5hmd3u0klfl7wsfv; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT fkh9m2n1paq5hmd3u0klfl7wsfv FOREIGN KEY (room_type_id) REFERENCES public.room_types(id);


--
-- Name: lessons fkil1jt6gri8x6yfaa3ijf7d6d9; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT fkil1jt6gri8x6yfaa3ijf7d6d9 FOREIGN KEY (semester_id) REFERENCES public.semesters(id);


--
-- Name: teachers fkl19hwymwn2ra2gwwty5trvyas; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.teachers
    ADD CONSTRAINT fkl19hwymwn2ra2gwwty5trvyas FOREIGN KEY (department_id) REFERENCES public.department(id);


--
-- Name: semester_period fkm237asf73ugk3vvw47aq266kl; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_period
    ADD CONSTRAINT fkm237asf73ugk3vvw47aq266kl FOREIGN KEY (period_id) REFERENCES public.periods(id);


--
-- Name: students fkmsev1nou0j86spuk5jrv19mss; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT fkmsev1nou0j86spuk5jrv19mss FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: temporary_schedule fko7tild8vhrqlodd3oaf8acvyw; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT fko7tild8vhrqlodd3oaf8acvyw FOREIGN KEY (teacher_id) REFERENCES public.teachers(id);


--
-- Name: semester_group fkpf19s66cmi8qpqc0iaeigbrhh; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.semester_group
    ADD CONSTRAINT fkpf19s66cmi8qpqc0iaeigbrhh FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: temporary_schedule fkqn6ufkok0nhqdkn46ctqckb76; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT fkqn6ufkok0nhqdkn46ctqckb76 FOREIGN KEY (subject_id) REFERENCES public.subjects(id);


--
-- Name: temporary_schedule fkr76lbhlv0di8ix7iviixs0p4g; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temporary_schedule
    ADD CONSTRAINT fkr76lbhlv0di8ix7iviixs0p4g FOREIGN KEY (period_id) REFERENCES public.periods(id);


--
-- Name: lessons fktdolsaotaqlwxbxwaxt00kimk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.lessons
    ADD CONSTRAINT fktdolsaotaqlwxbxwaxt00kimk FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: students user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: -
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

