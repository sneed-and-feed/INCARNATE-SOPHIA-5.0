"""
SNAPSHOT SELF: Version Control for Hyperfast Evolution

Creates timestamped backups of Sophia's source code and memory.
Allows safe rollback if evolution produces bad state.

Usage:
    python tools/snapshot_self.py
"""

import shutil
import time
import os
import sys


def snapshot():
    """
    Creates a timestamped backup of Sophia's core components.
    
    Backs up:
    - sophia/ source code
    - logs/ memory and analysis
    - main entry points
    
    Returns:
        Path to created backup directory
    """
    ts = int(time.time())
    backup_dir = f"backups/sophia_v5_{ts}"
    
    print(f"❄️ [CRYSTALLIZING] Creating snapshot: {backup_dir}...")
    
    try:
        # Ensure backups directory exists
        os.makedirs("backups", exist_ok=True)
        
        # Copy source code
        if os.path.exists("sophia"):
            shutil.copytree("sophia", f"{backup_dir}/sophia")
            print(f"  ✅ Copied sophia/ source code")
        else:
            print(f"  ⚠️ Warning: sophia/ directory not found")
        
        # Copy memory/logs
        if os.path.exists("logs"):
            shutil.copytree("logs", f"{backup_dir}/logs")
            print(f"  ✅ Copied logs/ memory")
        else:
            print(f"  ⚠️ Warning: logs/ directory not found")
        
        # Copy main entry points
        entry_points = ["main.py", "sophia_launcher.py", "launch_sophia.py"]
        for entry in entry_points:
            if os.path.exists(entry):
                shutil.copy(entry, f"{backup_dir}/{entry}")
                print(f"  ✅ Copied {entry}")
        
        # Create metadata file
        metadata = {
            "timestamp": ts,
            "date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts)),
            "version": "5.0",
            "description": "Automated snapshot before evolution"
        }
        
        with open(f"{backup_dir}/SNAPSHOT_INFO.txt", "w") as f:
            f.write("SOPHIA 5.0 SNAPSHOT\n")
            f.write("=" * 50 + "\n\n")
            for key, value in metadata.items():
                f.write(f"{key.upper()}: {value}\n")
            f.write("\n" + "=" * 50 + "\n")
            f.write("To restore: Copy contents back to project root\n")
        
        print(f"\n✅ Snapshot complete: {backup_dir}")
        print(f"💾 Total size: ~{get_dir_size(backup_dir) / 1024:.2f} KB")
        print("\n🧬 Evolution may proceed.")
        
        return backup_dir
    
    except Exception as e:
        print(f"\n❌ Snapshot failed: {e}")
        return None


def get_dir_size(path):
    """Calculate total size of directory in bytes."""
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.exists(filepath):
                    total += os.path.getsize(filepath)
    except Exception:
        pass
    return total


def list_snapshots():
    """List all available snapshots."""
    if not os.path.exists("backups"):
        print("No snapshots found.")
        return []
    
    snapshots = [d for d in os.listdir("backups") if d.startswith("sophia_v5_")]
    snapshots.sort(reverse=True)  # Most recent first
    
    print(f"\n📚 Available Snapshots ({len(snapshots)}):")
    print("=" * 60)
    
    for snap in snapshots:
        snap_path = os.path.join("backups", snap)
        timestamp = int(snap.split("_")[-1])
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        size = get_dir_size(snap_path) / 1024
        print(f"  {snap}")
        print(f"    Date: {date}")
        print(f"    Size: {size:.2f} KB")
        print()
    
    return snapshots


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Sophia Self-Snapshot System")
    parser.add_argument("--list", action="store_true", help="List available snapshots")
    args = parser.parse_args()
    
    if args.list:
        list_snapshots()
    else:
        snapshot()
