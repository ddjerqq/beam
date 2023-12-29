CREATE TABLE IF NOT EXISTS webhook
(
    id        INTEGER NOT NULL
        CONSTRAINT webhook_pk
            PRIMARY KEY,
    secret   TEXT    NOT NULL,
    owner_id INTEGER NOT NULL
        CONSTRAINT webhook_discord_user_id_fk
            REFERENCES discord_user (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
);

CREATE UNIQUE INDEX IF NOT EXISTS webhook_id_uindex
    ON webhook (id);

CREATE UNIQUE INDEX IF NOT EXISTS webhook_secret_uindex
    ON webhook (secret);


CREATE TABLE IF NOT EXISTS video
(
    id                TEXT NOT NULL
        CONSTRAINT video_pk
            PRIMARY KEY,
    create_time       INTEGER NOT NULL,
    cover_image_url   TEXT    NOT NULL,
    share_url         TEXT    NOT NULL,
    video_description TEXT    NOT NULL,
    duration          INTEGER NOT NULL,
    height            INTEGER NOT NULL,
    width             INTEGER NOT NULL,
    title             TEXT    NOT NULL,
    embed_html        TEXT    NOT NULL,
    embed_link        TEXT    NOT NULL,
    like_count        INTEGER NOT NULL,
    comment_count     INTEGER NOT NULL,
    share_count       INTEGER NOT NULL,
    view_count        INTEGER NOT NULL,

    -- TODO need info about author here
    --  waiting for the app to get verified.
    --  will set up the bot in the meantime tho.

    acknowledged      INTEGER NOT NULL DEFAULT 0
);

CREATE UNIQUE INDEX IF NOT EXISTS video_id_uindex
    ON video (id);


CREATE TABLE IF NOT EXISTS discord_user
(
    id          INTEGER NOT NULL
        CONSTRAINT discord_user_pk
            PRIMARY KEY,
    username    TEXT    NOT NULL,
    avatar_hash TEXT    NOT NULL,
    tiktok_id   TEXT    NOT NULL
        CONSTRAINT discord_user_tiktok_user_union_id_fk
            REFERENCES tiktok_user (union_id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
);

CREATE UNIQUE INDEX IF NOT EXISTS discord_user_id_uindex
    ON discord_user (id);


-- need user.info.(basic|profile|stats) intents
CREATE TABLE IF NOT EXISTS tiktok_user
(
    union_id           TEXT NOT NULL
        CONSTRAINT tiktok_user_pk
            PRIMARY KEY,
    open_id            TEXT    NOT NULL,
    avatar_url         TEXT    NOT NULL,
    avatar_url_100     TEXT    NOT NULL,
    avatar_large_url   TEXT    NOT NULL,
    display_name       TEXT    NOT NULL,
    bio_description    TEXT    NOT NULL,
    profile_deep_link  TEXT    NOT NULL,
    is_verified        INTEGER NOT NULL,
    follower_count     INTEGER NOT NULL,
    following_count    INTEGER NOT NULL,
    likes_count        INTEGER NOT NULL,
    video_count        INTEGER NOT NULL,
    last_updated       INTEGER NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS tiktok_user_open_id_uindex
    ON tiktok_user (open_id);

CREATE UNIQUE INDEX IF NOT EXISTS tiktok_user_union_id_uindex
    ON tiktok_user (union_id);
