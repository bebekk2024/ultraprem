"""
Compatibility shim for pyrogram types.

Some third-party packages (e.g. pykeyboard) do `from pyrogram import InlineKeyboardMarkup`
or `from pyrogram import ReplyKeyboardMarkup`. Newer pyrogram versions expose these
classes under `pyrogram.types` only. Import this module before any import that may
trigger pykeyboard/pyrogram imports so the top-level names exist.

Place this file in: PyroUbot/core/helpers/pyrogram_compat.py
and ensure other helper modules import it first (see inline.py sample).
"""
import warnings

try:
    import pyrogram
    try:
        from pyrogram import types as _types
    except Exception:
        _types = None

    if _types is not None:
        # Mapping table: top-level name -> attribute name in pyrogram.types
        _mappings = {
            "InlineKeyboardMarkup": "InlineKeyboardMarkup",
            "InlineKeyboardButton": "InlineKeyboardButton",
            "InlineKeyboard": "InlineKeyboardMarkup",  # some libs expect InlineKeyboard alias
            "ReplyKeyboardMarkup": "ReplyKeyboardMarkup",
            "ReplyKeyboardButton": "ReplyKeyboardButton",
            "KeyboardButton": "KeyboardButton",
            "KeyboardButtonRow": "KeyboardButtonRow",
        }

        for top_name, type_name in _mappings.items():
            try:
                if not hasattr(pyrogram, top_name) and hasattr(_types, type_name):
                    setattr(pyrogram, top_name, getattr(_types, type_name))
            except Exception as _exc:
                # Keep going if a single mapping fails
                warnings.warn(
                    f"pyrogram_compat: failed to map {top_name} -> {type_name}: {_exc}"
                )
except Exception:
    # If anything goes wrong, don't block startup here; let the real import error surface.
    pass
