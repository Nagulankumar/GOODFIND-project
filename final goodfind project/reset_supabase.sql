-- GoodFind — Refresh / Clear Data Script
-- Run this in your Supabase SQL Editor to wipe all user reports, matches, messages, and claims
-- while keeping the organization setup intact.

truncate table
    messages,
    conversations,
    ownership_claims,
    matches,
    lost_reports,
    found_reports,
    notifications
cascade;

-- If you also want to remove test users (except the default admin):
-- delete from users where role != 'admin';
