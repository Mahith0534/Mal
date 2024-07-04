from androguard.core.bytecodes.apk import APK
import os

def analyze_apk(file_path):
    apk = APK(file_path)

    # Get package name
    package_name = apk.get_package()
    
    # Get requested permissions
    permissions = apk.get_permissions()
    
    # Get activities
    activities = apk.get_activities()
    
    # Get services
    services = apk.get_services()
    
    # Get receivers
    receivers = apk.get_receivers()
    
    return {
        "package_name": package_name,
        "permissions": permissions,
        "activities": activities,
        "services": services,
        "receivers": receivers
    }

def main(apk_directory):
    results = []
    for apk_file in os.listdir(apk_directory):
        if apk_file.endswith(".apk"):
            file_path = os.path.join(apk_directory, apk_file)
            result = analyze_apk(file_path)
            results.append(result)
    return results

if __name__ == "__main__":
    apk_directory = "path_to_your_apk_directory"
    analysis_results = main(apk_directory)
    for result in analysis_results:
        print(result)
