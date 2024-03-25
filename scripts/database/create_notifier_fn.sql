\c app_db

CREATE OR REPLACE FUNCTION notify_users_change() RETURNS TRIGGER AS $$
BEGIN
  PERFORM pg_notify('users_changes', TG_OP || ':' || NULL::text);
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;
