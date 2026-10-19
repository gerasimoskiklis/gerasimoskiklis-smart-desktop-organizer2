import os
import shutil

def smart_organize_desktop():
    # 1. Εντοπίζουμε το Desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # 2. Ορίζουμε τον κεντρικό φάκελο ταξινόμησης
    main_archive = os.path.join(desktop_path, "Smart_Desktop_Organized")
    
    # Ορισμός των έξυπνων κατηγοριών (υποφακέλοι)
    categories = {
        "1_Projects_Code": ["python", "bot", "project", "app", "code", "script", "web", "html", "py"],
        "2_Media_Photos": ["photo", "image", "jpg", "png", "jpeg", "img", "screenshot", "video", "mp4"],
        "3_Documents_Work": ["doc", "pdf", "txt", "excel", "xlsx", "csv", "work", "εγγραφα", "σημειωσεις"],
        "4_General_Archive": [] # Εδώ καταλήγουν οτιδήποτε άλλο δεν ταιριάζει παραπάνω
    }

    # Δημιουργία των φακέλων κατηγοριών αν δεν υπάρχουν
    for cat_name in categories.keys():
        cat_path = os.path.join(main_archive, cat_name)
        if not os.path.exists(cat_path):
            os.makedirs(cat_path)

    # 3. ΕΞΑΙΡΕΣΕΙΣ: Φάκελοι που δεν πειράζουμε ποτέ (τρέχοντα ενεργά εργαλεία)
    protected_items = [
        "Smart_Desktop_Organized",
        "Gerrybot",
        "my_python_project",
        "file_organizer",
        "Projects"
    ]

    print("Ξεκινάει η έξυπνη ταξινόμηση της Επιφάνειας Εργασίας...")

    moved_count = 0
    for filename in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, filename)

        # Ελέγχουμε αν είναι φάκελος και δεν προστατεύεται
        if os.path.isdir(item_path) and filename not in protected_items:
            
            # Αποφασίζουμε κατηγορία με βάση το όνομα του φακέλου (σε πεζά για ευκολία)
            folder_name_lower = filename.lower()
            assigned_category = "4_General_Archive" # Default κατηγορία

            for cat_name, keywords in categories.items():
                if cat_name == "4_General_Archive":
                    continue
                # Αν κάποια λέξη-κλειδί περιέχεται στο όνομα του φακέλου
                if any(kw in folder_name_lower for kw in keywords):
                    assigned_category = cat_name
                    break

            # Ορίζουμε την τελική διαδρομή μετακίνησης
            destination_dir = os.path.join(main_archive, assigned_category)
            destination_path = os.path.join(destination_dir, filename)

            # Αν υπάρχει ήδη ίδιος φάκελος, προσθέτουμε διακριτικό
            if os.path.exists(destination_path):
                filename = f"{filename}_dup"
                destination_path = os.path.join(destination_dir, filename)

            # Μετακίνηση
            shutil.move(item_path, destination_path)
            print(f"[{assigned_category}] Μετακινήθηκε: {filename}")
            moved_count += 1

    print(f"\nΗ ταξινόμηση ολοκληρώθηκε! Τακτοποιήθηκαν συνολικά {moved_count} φάκελοι.")

if __name__ == "__main__":
    smart_organize_desktop()
