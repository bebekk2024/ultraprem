"""
Compatibility shim for pyrogram types.

Place this file at: PyroUbot/core/helpers/pyrogram_compat.py

This module will try to map common keyboard-related classes from pyrogram.types
onto the top-level pyrogram module, so third-party libs that do
`from pyrogram import InlineKeyboardMarkup` or `from pyrogram import ReplyKeyboardMarkup`
will not fail.
"""
from __future__ import annotations

import importlib
import sys
import warnings
from typing import Dict

def _apply_mappings():
    try:
        pyrogram = importlib.import_module("pyrogram")
    except Exception:
        # pyrogram not installed; nothing to do
        return

    # Try to import pyrogram.types (newer pyrograms expose types here)
    _types = None
    try:
        _types = importlib.import_module("pyrogram.types")
    except Exception:
        _types = None

    # Mapping: top-level name (what external libs import) -> attribute name in pyrogram.types
    mappings: Dict[str, str] = {
        # Inline keyboards
        "InlineKeyboardMarkup": "InlineKeyboardMarkup",
        "InlineKeyboardButton": "InlineKeyboardButton",
        "InlineKeyboard": "InlineKeyboardMarkup",  # some libs expect this alias

        # Reply keyboards
        "ReplyKeyboardMarkup": "ReplyKeyboardMarkup",
        "ReplyKeyboardButton": "ReplyKeyboardButton",
        "KeyboardButton": "KeyboardButton",
        "KeyboardButtonRow": "KeyboardButtonRow",

        # Other common names (add as needed)
        "ForceReply": "ForceReply",
        "ReplyKeyboardRemove": "ReplyKeyboardRemove",
    }

    if _types is not None:
        for top_name, type_name in mappings.items():
            try:
                if not hasattr(pyrogram, top_name):
                    attr = getattr(_types, type_name, None)
                    if attr is not None:
                        setattr(pyrogram, top_name, attr)
            except Exception as exc:
                warnings.warn(f"pyrogram_compat: failed to map {top_name}: {exc}")

    # Some packages import specific classes directly from submodules, e.g.:
    #   from pyrogram.types import InlineKeyboardButton
    # That will work normally if pyrogram.types exists; we don't overwrite that.
    # But some packages do `from pyrogram import InlineKeyboardMarkup` which expects
    # the attribute on top-level pyrogram module — mapping above handles that.

# Run mapping at import time
_apply_mappings()
