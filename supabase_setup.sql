-- Supabaseの「SQL Editor」に貼り付けて、Runを押してください。
-- アプリ本体だけがサービス用キーで接続するので、利用者にSupabaseのログインは不要です。

create table if not exists public.study_records (
    id bigint generated always as identity primary key,
    study_date date not null,
    user_name text not null check (char_length(user_name) between 1 and 50),
    subject text not null check (char_length(subject) between 1 and 50),
    hours integer not null check (hours between 1 and 24),
    created_at timestamptz not null default now()
);

alter table public.study_records enable row level security;

-- 匿名の直接アクセスは禁止。公開アプリのサーバーだけが記録を読み書きします。
revoke all on table public.study_records from anon, authenticated;
