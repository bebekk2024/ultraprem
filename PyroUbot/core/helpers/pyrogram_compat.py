# https://github.com/ffloowers09/PyroUbot (local path in your repo)
# Compatibility shim: ensure pyrogram exposes InlineKeyboard types at top-level
# so packages that expect `from pyrogram import InlineKeyboardMarkup` still work.
# Import this module before any other module that imports pyrogram/pykeyboard.

try:
    import pyrogram
    # pyrogram versions expose types at pyrogram.types
    try:
        from pyrogram import types as _types
    except Exception:
        _types = None

    if _types is not None:
        # InlineKeyboardMarkup
        if not hasattr(pyrogram, "InlineKeyboardMarkup") and hasattr(
            _types, "InlineKeyboardMarkup"
        ):
            pyrogram.InlineKeyboardMarkup = _types.InlineKeyboardMarkup

        # InlineKeyboardButton
        if not hasattr(pyrogram, "InlineKeyboardButton") and hasattr(
            _types, "InlineKeyboardButton"
        ):
            pyrogram.InlineKeyboardButton = _types.InlineKeyboardButton

        # Common aliases some libs expect
        if not hasattr(pyrogram, "InlineKeyboard") and hasattr(
            _types, "InlineKeyboardMarkup"
        ):
            # Some external libs refer to InlineKeyboard as an alias for InlineKeyboardMarkup
            try:
                pyrogram.InlineKeyboard = _types.InlineKeyboardMarkup
            except Exception:
                pass

except Exception:
    # Don't raise here to avoid masking the real startup error.
    # If this shim fails, the original import error will surface elsewhere.
    pass
