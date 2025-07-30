# Fusion Launcher Usage Guide

## 🚀 How to Use the Portable Fusion Launcher

### **Step 1: Copy to Your Project Directory**
```bash
# Navigate to your project directory
cd /path/to/your/project

# Copy the launcher to your project
cp ~/Desktop/fusion_launcher.command .

# Make it executable
chmod +x fusion_launcher.command
```

### **Step 2: Run the Launcher**
```bash
# Run from within your project directory
./fusion_launcher.command
```

### **Step 3: Verify Installation**
```bash
# Check that Fusion files were installed
ls -la | grep -E "(fusion|master_prompt|agents|tools)"

# Test Fusion
python3 fusion.py --help
```

## 📁 What Gets Installed

### **Core Files:**
- `fusion.py` - Main Fusion system
- `agents_combined.py` - All agents
- `tools_combined.py` - All tools
- `execution_orchestrator_v14.py` - Execution engine
- `fusion_context.py` - Context management
- `memory_system.py` - Memory system

### **Additional Dependencies:**
- `autocritique_loop.py` - Auto-critique system
- `task_classifier_agent.py` - Task classifier
- `voice_modulation_engine.py` - Voice modulation

### **Master Prompts:**
- `master_prompt_main.md` - Complete version (34,993 chars)
- `master_prompt_8000.md` - ChatGPT version (6,284 chars)

### **Configuration:**
- `.fusion.json` - Configuration file
- `README.md` - Documentation

## 🎯 Usage Examples

### **For Cursor Projects:**
```bash
# In your Cursor project
cd ~/Desktop/MyCursorProject
cp ~/Desktop/fusion_launcher.command .
./fusion_launcher.command

# Now use Fusion in your project
python3 fusion.py run vp_design "Design a user interface"
```

### **For New Projects:**
```bash
# Create new project
mkdir my_new_project
cd my_new_project

# Install Fusion
cp ~/Desktop/fusion_launcher.command .
./fusion_launcher.command

# Start using Fusion
python3 fusion.py pipeline "Create a design system"
```

## ⚠️ Important Notes

### **Run from Project Directory:**
- The launcher must be run **from within** your project directory
- It installs files in the **current directory** where you run it
- Don't run it from your home directory unless you want Fusion there

### **Check Installation:**
- Look for Fusion files in your project directory after running
- If you don't see files, make sure you're in the right directory
- The launcher shows what directory it's installing to

### **Portable:**
- Copy `fusion_launcher.command` to any project
- Each project gets its own copy of Fusion
- No conflicts between projects

## 🔧 Troubleshooting

### **No Files Appear:**
1. Check you're in the right directory
2. Make sure the launcher is executable: `chmod +x fusion_launcher.command`
3. Check the output shows the correct installation directory

### **Permission Errors:**
```bash
chmod +x fusion_launcher.command
```

### **GitHub Issues:**
- The launcher pulls from GitHub, so internet connection is required
- If GitHub is down, the launcher will show an error

## 🎯 Quick Start

```bash
# 1. Go to your project
cd /path/to/your/project

# 2. Copy launcher
cp ~/Desktop/fusion_launcher.command .

# 3. Make executable
chmod +x fusion_launcher.command

# 4. Run installer
./fusion_launcher.command

# 5. Use Fusion
python3 fusion.py run vp_design "your design task"
``` 