#=================================================================
# DROP TABLE public.account_account;
# DROP SEQUENCE public.openacademy_course_id_seq
CREATE SEQUENCE public.openacademy_course_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE public.openacademy_course_id_seq
  OWNER TO openpg;

CREATE TABLE public.openacademy_course
(
  id integer NOT NULL DEFAULT nextval('openacademy_course_id_seq'::regclass),
  name character(20),
  description character varying(50),
  CONSTRAINT id_course PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.openacademy_course
  OWNER TO openpg;