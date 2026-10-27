"""
GoodFind Data Reset Utility.
Clears all uploaded images, reports, matches, messages, claims, and notifications.
Run:
    python reset_data.py
"""
import os
import glob
import mock_data as db
import supabase_client


def reset():
    print("Refreshing GoodFind data...")

    # 1. Reset in-memory / Supabase data structures
    db.reset_all_data()
    print("  [OK] Cleared all lost reports, found reports, returned items")
    print("  [OK] Cleared all matches and ownership claims")
    print("  [OK] Cleared all conversations and chat messages")
    print("  [OK] Cleared all notifications")

    # 2. Delete test uploads (preserving static/uploads/seed)
    upload_pattern = os.path.join("static", "uploads", "*.png")
    removed_count = 0
    for f in glob.glob(upload_pattern):
        try:
            os.remove(f)
            removed_count += 1
        except Exception as e:
            print(f"  ! Could not remove {f}: {e}")

    # Also clean up jpeg/webp uploads if any
    for ext in ("*.jpg", "*.jpeg", "*.webp", "*.gif"):
        for f in glob.glob(os.path.join("static", "uploads", ext)):
            try:
                os.remove(f)
                removed_count += 1
            except Exception:
                pass

    print(f"  [OK] Deleted {removed_count} user-uploaded image files from static/uploads/")

    if supabase_client.is_supabase_enabled():
        print("  [OK] Cleared remote Supabase PostgreSQL database tables")
    else:
        print("  [OK] Local in-memory state is completely refreshed")

    print("\nProject is now clean and fresh! Start the app with:")
    print("    python app.py\n")


if __name__ == "__main__":
    reset()
