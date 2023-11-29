import os
import shutil

def replicate_folder(directory,original_name,replica_name):
    if os.path.isdir(directory):
        # Check if the current directory contains subdirectories
        subdirectories = [subdir for subdir in os.listdir(directory) if os.path.isdir(os.path.join(directory, subdir))]
        print(subdirectories)
        for subdirs in subdirectories:
            #print(os.listdir(directory))
            if original_name in subdirs:
                abc_path = os.path.join(directory, subdirs)
                cde_path = os.path.join(directory, str(subdirs).replace(original_name,replica_name))
                if not os.path.exists(cde_path):
                    shutil.copytree(abc_path, cde_path)
                    print(f"Replicated "+original_name+" as "+replica_name+" in {subdirs}")
                    print(os.listdir(cde_path))
                    for filenames in os.listdir(cde_path):
                        if ".cs" in filenames:
                            print(filenames)
                            os.rename(os.path.join(cde_path,filenames), os.path.join(cde_path,str(filenames).replace(original_name,replica_name)))
                            # Replace content of the .cs file if it contains the original name
                            with open(os.path.join(cde_path,str(filenames).replace(original_name,replica_name)), 'r') as cs_file:
                                cs_content = cs_file.read()
                                cs_content = cs_content.replace(original_name, replica_name)

                            with open(os.path.join(cde_path,str(filenames).replace(original_name,replica_name)), 'w') as cs_file:
                                cs_file.write(cs_content)
    
        for filenames in os.listdir(directory):
            if ".cs" in filenames and original_name in filenames and original_name not in directory:
                print(filenames)
                shutil.copy2(os.path.join(directory,filenames), os.path.join(directory,str(filenames).replace(original_name,replica_name)))
                # Replace content of the .cs file if it contains the original name
                with open(os.path.join(directory,str(filenames).replace(original_name,replica_name)), 'r') as cs_file:
                    cs_content = cs_file.read()
                    cs_content = cs_content.replace(original_name, replica_name)

                with open(os.path.join(directory,str(filenames).replace(original_name,replica_name)), 'w') as cs_file:
                    cs_file.write(cs_content)

        

        for subdir in subdirectories:
            # Recursively call the function on subdirectories
            replicate_folder(os.path.join(directory, subdir),original_name,replica_name)
root_folder="C:\\Users\\admin\\source\\repos\\shopfloor\\src\\services\\business\\master\\"
#request_folder="C:\\Users\\admin\\source\\repos\\develope\\src\\services\\business\\master\\Shopfloor.Master.Api\\Consumers\\Requests\\"
request_folder = "C:\\Users\\admin\\source\\repos\\shopfloor\\src\\shareds\\Shopfloor.EventBus\\Models\\"
original_name="PurchaseUOM"
replica_name="UOM"
#C:\Users\admin\source\repos\develope\src\shareds\Shopfloor.EventBus\Models
replicate_folder(root_folder,original_name,replica_name)
replicate_folder(request_folder,original_name,replica_name)