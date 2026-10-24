"""
Hatırlatıcılar — Windows sürümü.

Microsoft To-Do hatırlatıcıları Windows üzerinden tarayıcıda yönetilir.
"""

from __future__ import annotations

import webbrowser


def get_reminders(query: str = "upcoming", limit: int = 8, list_name: str = "") -> str:
    webbrowser.open("https://to-do.microsoft.com/tasks")
    return (
        "Microsoft To-Do tarayıcıda açıldı."
    )


def add_reminder(
    title: str,
    due_iso: str = "",
    notes: str = "",
    list_name: str = "",
    priority: str = "",
    all_day: bool = False,
) -> str:
    webbrowser.open("https://to-do.microsoft.com/tasks")
    return (
        f"Microsoft To-Do tarayıcıda açıldı — '{title}' hatırlatıcısını oradan ekleyebilirsin."
    )
