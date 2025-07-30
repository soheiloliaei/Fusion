# Master Prompt Rules - ALWAYS MAINTAIN BOTH VERSIONS

## 🚨 CRITICAL RULE: Always Include Both Versions

### Required Files:
1. **`master_prompt_main.md`** - Complete version (34,993 chars)
2. **`master_prompt_8000.md`** - ChatGPT version (6,284 chars)

### Git Repository Structure:
```
~/fusion/
├── master_prompt/
│   ├── master_prompt_main.md    # ✅ ALWAYS COMMIT
│   ├── master_prompt_8000.md    # ✅ ALWAYS COMMIT
│   └── README.md               # ✅ ALWAYS COMMIT
└── ChatGPT_Upload_v14.3/
    ├── master_prompt_main.md    # ✅ ALWAYS COMMIT
    ├── master_prompt_8000.md    # ✅ ALWAYS COMMIT
    └── ... (other files)
```

## 📋 Workflow Rules:

### 1. Development Workflow:
- **Always edit** `master_prompt_main.md` first
- **Then create** `master_prompt_8000.md` from the main version
- **Never delete** either file

### 2. Git Commit Rules:
```bash
# ALWAYS commit both files
git add master_prompt/master_prompt_main.md
git add master_prompt/master_prompt_8000.md
git add ChatGPT_Upload_v14.3/master_prompt_main.md
git add ChatGPT_Upload_v14.3/master_prompt_8000.md
```

### 3. Sync Script Rules:
- **chatgpt_sync.command** must copy BOTH files
- **fusion_launcher.command** must copy BOTH files
- **Never overwrite** one with the other

### 4. File Naming Rules:
- **Main version**: `master_prompt_main.md`
- **ChatGPT version**: `master_prompt_8000.md`
- **Never use**: `master_prompt.md` (ambiguous)

## 🔄 Update Process:

### When Updating Master Prompt:
1. Edit `master_prompt_main.md`
2. Create `master_prompt_8000.md` (trimmed version)
3. Update sync scripts to use new file names
4. Commit ALL files to git
5. Push to GitHub

### Verification Checklist:
- [ ] `master_prompt_main.md` exists and is complete
- [ ] `master_prompt_8000.md` exists and is under 8000 tokens
- [ ] Both files are in git repository
- [ ] Both files are in ChatGPT_Upload_v14.3/
- [ ] Sync scripts reference correct file names

## 🚨 NEVER ALLOW:
- Only one master prompt file in repository
- Ambiguous file names like `master_prompt.md`
- Missing files in ChatGPT upload folder
- Sync scripts that don't include both versions

## ✅ ALWAYS ENSURE:
- Both versions are committed to git
- Both versions are in ChatGPT upload folder
- Clear file naming convention
- Updated sync scripts
- GitHub shows both files

---

**This rule is CRITICAL for maintaining the dual-version master prompt system.** 