# Master Prompt Files

## File Structure

### `master_prompt_main.md` (34,993 characters)
- **Purpose**: Complete development reference
- **Use Case**: Full system documentation and development
- **Content**: Complete Fusion v14 system documentation
- **Status**: Mother version - source of truth

### `master_prompt_8000.md` (6,284 characters)
- **Purpose**: ChatGPT-compatible version
- **Use Case**: Copy-paste into ChatGPT
- **Content**: Essential functionality under 8000 tokens
- **Status**: Trimmed version for ChatGPT

## Usage

### For Development:
```bash
# Use the complete version
cat master_prompt_main.md
```

### For ChatGPT:
```bash
# Use the copy-paste script
~/fusion/copy_master_prompt.command

# Or use the launcher
~/fusion/chatgpt_launcher.command
```

### For Auto-Sync:
```bash
# Syncs with 8000 version
~/fusion/chatgpt_sync.command
```

## File Management

- **Never delete** `master_prompt_main.md` - it's the source
- **Always update** `master_prompt_main.md` first
- **Then trim** to create `master_prompt_8000.md`
- **Both files** are committed to Git repository 