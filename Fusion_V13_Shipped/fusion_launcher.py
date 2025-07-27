
    def finalize_release(self, version: str):
        print(f"📦 Initiating Fusion v{version} Finalization Sequence...")

        print("🔍 1. Validating Version Expectations...")
        from utils.version_audit import summarize_version_goal_vs_actual
        print(summarize_version_goal_vs_actual(version))

        print("📂 2. Generating Launch Command File...")
        from utils.packager import generate_launch_file
        generate_launch_file(version)

        print("🤖 3. Creating ChatGPT Upload Package...")
        from utils.packager import generate_chatgpt_upload_package
        generate_chatgpt_upload_package(version)

        print("🌐 4. Pushing to GitHub...")
        from utils.packager import push_github_updates
        push_github_updates(version)

        print(f"✅ Fusion v{version} Packaging Complete!")
