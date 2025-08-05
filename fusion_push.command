#!/bin/bash

# Fusion v14 Auto-Push Script
# Commits and pushes to GitHub with timestamp
# Works from any location by finding the correct Fusion v14 directory

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get current timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo -e "${BLUE}🚀 Fusion v14 Auto-Push Script${NC}"
echo -e "${BLUE}Timestamp: ${TIMESTAMP}${NC}"
echo ""

# Find the Fusion v14 directory
FUSION_DIR=""
POSSIBLE_PATHS=(
    "/Users/soheil/Desktop/Fusion_v14"
    "/Users/soheil/Desktop/Fusion_v14_Desktop"
    "/Users/soheil/fusion_v13"
    "$(pwd)"
)

for path in "${POSSIBLE_PATHS[@]}"; do
    if [ -d "$path" ] && [ -f "$path/fusion.py" ] && [ -d "$path/.git" ]; then
        FUSION_DIR="$path"
        break
    fi
done

if [ -z "$FUSION_DIR" ]; then
    echo -e "${RED}❌ Error: Could not find Fusion v14 directory${NC}"
    echo "Please ensure you're running this from a Fusion v14 directory with git repository"
    echo "Expected locations:"
    for path in "${POSSIBLE_PATHS[@]}"; do
        echo "  - $path"
    done
    exit 1
fi

echo -e "${BLUE}📍 Found Fusion v14 directory: $FUSION_DIR${NC}"

# Change to the Fusion v14 directory
cd "$FUSION_DIR"
echo -e "${BLUE}📁 Changed to directory: $(pwd)${NC}"

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}❌ Error: Not in a git repository${NC}"
    echo "Directory: $(pwd)"
    echo "Please ensure this is a git repository"
    exit 1
fi

# Check if there are any changes to commit
if git diff-index --quiet HEAD --; then
    echo -e "${YELLOW}⚠️ No changes to commit${NC}"
    echo "Working directory is clean"
    echo -e "${GREEN}✅ Fusion v14 is up to date!${NC}"
    exit 0
fi

# Get the current branch
CURRENT_BRANCH=$(git branch --show-current)
echo -e "${BLUE}Current branch: ${CURRENT_BRANCH}${NC}"

# Get list of changed files
CHANGED_FILES=$(git diff --name-only)
echo -e "${BLUE}Changed files:${NC}"
echo "$CHANGED_FILES" | sed 's/^/  - /'

echo ""

# Stage all changes
echo -e "${BLUE}📦 Staging changes...${NC}"
git add .

# Create commit message with timestamp
COMMIT_MESSAGE="Fusion v14 update - $TIMESTAMP

Auto-commit from Fusion v14 system
- Timestamp: $TIMESTAMP
- Branch: $CURRENT_BRANCH
- Changed files: $(echo "$CHANGED_FILES" | wc -l | tr -d ' ')
- Directory: $FUSION_DIR"

echo -e "${BLUE}💾 Creating commit...${NC}"
echo -e "${BLUE}Commit message:${NC}"
echo "$COMMIT_MESSAGE"
echo ""

# Commit the changes
git commit -m "$COMMIT_MESSAGE"

# Get the commit hash
COMMIT_HASH=$(git rev-parse HEAD)
echo -e "${GREEN}✅ Commit created: ${COMMIT_HASH:0:8}${NC}"

# Check if remote exists
if git remote get-url origin > /dev/null 2>&1; then
    echo -e "${BLUE}🌐 Pushing to remote...${NC}"
    
    # Push to remote
    if git push origin "$CURRENT_BRANCH"; then
        echo -e "${GREEN}✅ Successfully pushed to remote${NC}"
        echo -e "${GREEN}Branch: $CURRENT_BRANCH${NC}"
        echo -e "${GREEN}Commit: ${COMMIT_HASH:0:8}${NC}"
        echo -e "${GREEN}Repository: $(git remote get-url origin)${NC}"
    else
        echo -e "${RED}❌ Failed to push to remote${NC}"
        echo "You may need to:"
        echo "  - Set up remote: git remote add origin <repository-url>"
        echo "  - Configure credentials"
        echo "  - Pull latest changes first"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️ No remote repository configured${NC}"
    echo "To set up remote:"
    echo "  git remote add origin <repository-url>"
    echo "  git push -u origin $CURRENT_BRANCH"
fi

echo ""
echo -e "${GREEN}🎉 Fusion v14 auto-push completed successfully!${NC}"
echo -e "${BLUE}Timestamp: $TIMESTAMP${NC}"
echo -e "${BLUE}Directory: $FUSION_DIR${NC}" 