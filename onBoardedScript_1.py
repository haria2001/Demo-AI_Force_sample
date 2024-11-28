import os
import re
import time  
import json               
import time
import shutil
import openai
import logging
import traceback
from pathlib import Path


PROMPT_CODE_MIG_DEP = """You are an expert in C plus plus and JAVA  programming language. Analyze the below c plus plus  code very carefully  and  find the dependencies while you need to migrate this code to JAVA. Respond back with only the name of the dependencies that are required to be taken care while migrating to JAVA code. Do not migrate the code , only mention the dependencies.
"""

PROMPT_CODE_MIG_2JAVA = """You are an expert in migrating  C plus plus to JAVA  programming language. You are required to provide the migrated code in Java from cplus plus project file. You are here given the overall list of dependencies from project point of view and given one individual cplus plus file from the project. Analyze the below cplus plus  code carefully and migrate the code to Java. While migrating to JAVA code consider the following points.
1.Appropriate Java libraries are used in Java code corresponding to C++ libraries.
2.Suitable data structure in JAVA corresponding to C++ data structure.
3.Namespaves in C++ properly converted to package in JAVA.
4.Pointer in C++ are converted to equivalent code in Java.
5.Callback function in C++ are converted to equivalent code in Java.  
6.Use ConcurrentHashMap wherever applicable for safe concurrent access.
7.Take care of appropriate synchronization mechanisms from C++ to Java equivalents.
8.Use ExecutorService framework for managing thread pools whenever applicable.
9.Take care of appropriate java’s garbage collection, runtime optimizations.
10.Use appropriate Java testing frameworks like JUnit or TestNG for unit and integration tests by replacing C++ testing frameworks wherever applicable.
11. Each java file should have exactly one public class.
12. Test files should be in separate folder.
13. Package name should be according to the project structure.
14. Ensure the migrated Java code should be Java8 or higher.
15. Provide the relevant comment for the generated code.
16. Abstract class from C++  should be taken care while migarating it to Java.
17. Use SLF4J or Apache common logging for logging related pupose.
"""

PROMPT_CODE_MIG_GUIDELINES_ON_CODE_UPDATE = """ Make sure to take care the following Guide Lines while updating the code on review comment.
1.Appropriate Java libraries are used in Java code corresponding to C++ libraries.
2.Suitable data structure in JAVA corresponding to C++ data structure.
3.Namespaves in C++ properly converted to package in JAVA.
4.Pointer in C++ are converted to equivalent code in Java.
5.Callback function in C++ are converted to equivalent code in Java.  
6.Use ConcurrentHashMap wherever applicable for safe concurrent access.
7.Take care of appropriate synchronization mechanisms from C++ to Java equivalents.
8.Use ExecutorService framework for managing thread pools whenever applicable.
9.Take care of appropriate java’s garbage collection, runtime optimizations.
10.Use appropriate Java testing frameworks like JUnit or TestNG for unit and integration tests by replacing C++ testing frameworks wherever applicable.
11. Each java file should have exactly one public class.
12. Test files should be in separate folder.
13. Package name should be according to the project structure.
14. Ensure the migrated Java code should be Java8 or higher.
15. Provide the relevant comment for the generated code.
16. Abstract class from C++  should be taken care while migarating it to Java.
17. Use SLF4J or Apache common logging for logging related pupose.
"""
PROMPT_CODE_MIG_CREATE_POM_FILE="""You are an expert in creating a Maven project for Java files. Create a pom.xml required for Maven project by carefully scanning all information given below. While creating the pom.xml file ,mention all the external dependencies mentioned in the following java files. """



PROMPT_CODE_MIG_GUIDELINES_ON_CODE_UPDATE_ADDITIONAL = """\n\n Make sure to take care the following Guide Lines while updating the code on review comment which are specific to project.
1.Create a controller class, service class and repository class.
2.Controller class should invoke the service class methods.
3.Service class should invoke the repository class methods.
4.Repository class should invoke the database calls.
5.It should have consistent service package and service classes.
6.SQL queries should be in repository classes only.
7.Must ensure to include Annotations and autowiring features wherever applicable.
8.Models and Entities should be clearly prepared.
"""

PROMPT_CODE_MIG_GUIDELINES_ON_CODE_UPDATE_ADDITIONAL_OLD = """\n\n Make sure to take care the following Guide Lines while updating the code on review comment which are specific to project.
1. Avoid creating nested class.
2. Avoid the use of static in the class.
2. Avoid referring storage from controller class .Refer the storage class from service class only if available.
4. Add repository Classes wherever required.
5. It should have consistent service package and service classes.
6. SQL queries should be in repository classes only.
7. Must ensure to include Annotations and autowiring features wherever applicable.
8. Models and Entities should be clearly prepared. 
"""


PROMPT_CODE_MIG_CREATE_FOLDER="""You are an expert in creating a Maven project for Java files. Create a suitable project folder required for Maven project by carefully scanning all information given below. The folder structure must be provided in Json format only. Also make sure to keep test files in respective test folder only."""

PROMPT_CODE_MIG_SRC = """
{source_file}
"""

PROMPT_CODE_MIG_DISPLAY_FOLDER="""You are an expert in creating a Maven project for Java files.  Following is folder structure for the project in a json format. You need to display the folder structure.
"""


PROMPT_CODE_MIG_CREATE_APPLICATION_PROP="""You are an expert in JAVA  programming language. You are given below some JAVA code snipet from different java files from a project. Analyze the below  code very carefully  and create an application properties file.
"""

PROMPT_CODE_MIG_REVIEW_COMMENT="""You are an expert in JAVA  programming language. Migrated JAVA code from C plus plus code is given  below. Analyze the below  code carefully and provide the review comments. Only provide the clear and crisp review comment and do not provide any java code. Also provide the quality of the code with the range of 1 to 10 where 1 is least quality and 10 is highest quality.
"""
PROMPT_CODE_MIG_UPDATE_CODE_ON_REVIEW="""You are an expert in JAVA  programming language. You are given a review comment for a java file and the corresponding java file below. You need to take care of the review comment and re-write the improved version of the java code. Please provide only the improved version of the java code after review comment incorporated.
"""


# creater logger with file handler


#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
#logger.addHandler(logging.FileHandler("log.txt"))

           

class pocOnCodeMigration:
    def __init__(self):
        return None

    def llmHandler(self,file_content,prompts):
        try:    
            import openai
            openai.api_type = "azure"
            openai.api_base = "https://aiforce-openai.openai.azure.com/"
            openai.api_version = "2023-03-15-preview"
            openai.api_key = "5a60e1c154fa4563b37ca14a4a6c5a0f"
            deployment_name="gpt-4o"
            if prompts=="PROMPT_CODE_MIG_DEP" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_DEP
                GeneratedPrompt2 = PROMPT_CODE_MIG_SRC.format(source_file=file_content)    
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2            
            elif prompts=="PROMPT_CODE_MIG_2JAVA" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_2JAVA  
                GeneratedPrompt2 = PROMPT_CODE_MIG_SRC.format(source_file=file_content)    
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2            
            elif prompts=="PROMPT_CODE_MIG_CREATE_POM_FILE" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_CREATE_POM_FILE  
                GeneratedPrompt2 = file_content  
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2 
            elif prompts=="PROMPT_CODE_MIG_CREATE_FOLDER" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_CREATE_FOLDER  
                GeneratedPrompt2 = file_content  
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2
            elif prompts=="PROMPT_CODE_MIG_REVIEW_COMMENT" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_REVIEW_COMMENT  
                GeneratedPrompt2 = file_content  
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2            
            elif prompts=="PROMPT_CODE_MIG_UPDATE_CODE_ON_REVIEW" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_UPDATE_CODE_ON_REVIEW  
                GeneratedPrompt2 = file_content  
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2            

            elif prompts=="PROMPT_CODE_MIG_DISPLAY_FOLDER" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_DISPLAY_FOLDER  
                GeneratedPrompt2 = file_content  
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2           

            elif prompts=="PROMPT_CODE_MIG_CREATE_APPLICATION_PROP" :
                GeneratedPrompt1 = PROMPT_CODE_MIG_CREATE_APPLICATION_PROP  
                GeneratedPrompt2 = file_content  
                GeneratedPrompt=GeneratedPrompt1+GeneratedPrompt2           

            message_text = [{"role":"system","content":"You are a Expertise Full Stack Software Engineer."},{"role":"user","content":GeneratedPrompt}]
            response = openai.ChatCompletion.create(engine=deployment_name, messages = message_text,temperature=0.7,max_tokens=4096,top_p=0.95,frequency_penalty=0,   presence_penalty=0,stop=None)
            response = response.choices[0]["message"]["content"]
            response1=response
            return response1
        except Exception as e:
            print("Encountered exception. {0}".format(e))
            return 0

    def startJavaMigrationPOC(self,inpfld,output_dirpath):        
        try:
            import os
            import time  
            import pandas as pd
            cwd = os.getcwd()
            rootpath=os.path.join(cwd, inpfld) 
            global_all_dependencies_from_cpp=""
            print("\n DEP Gen [Started]")
            for root, dirs, files in os.walk(rootpath):
                for name in files:
                    if name.endswith(".cpp") or name.endswith(".cc") or name.endswith(".hpp") or name.endswith(".h"):
                        try:
                            fileName=os.path.join(root, name) 
                            with open(fileName, 'r') as file:
                                file_content = file.read()
                            prompts="PROMPT_CODE_MIG_DEP"
                            response=self.llmHandler(file_content,prompts)
                            global_all_dependencies_from_cpp=global_all_dependencies_from_cpp+response
                        except Exception as e:
                            print("Encountered exception. {0}".format(e))
            print("\n DEP Gen [Ends]")                            
            print("\n Java Gen 1st Level [Started]")            
            classNameOnly=""
            for root, dirs, files in os.walk(rootpath):
                for name in files:
                    if name.endswith(".cpp") or name.endswith(".cc"):
                        try:
                            fileName=os.path.join(root, name) 
                            with open(fileName, 'r') as file:
                                file_content = file.read()
                                prompts="PROMPT_CODE_MIG_2JAVA"
                                #print("\n classNameOnly ",classNameOnly)
                                file_content=global_all_dependencies_from_cpp+"\nDonot use any of the following public class name while migrating the cplus plus code to Java code\n"+classNameOnly+"\n The original cplus plus file follows."+ file_content
                                response1=self.llmHandler(file_content,prompts)
                                start = '```java'
                                end = '```'
                                s = response1
                                response1=(s.split(start))[1].split(end)[0]
                                import re
                                pattern = r'public class ([A-Za-z0-9_]+)'
                                class_names = re.findall(pattern, response1)
                                for class_name in class_names:
                                    javaFileName1=class_name+".java"
                                    classNameOnly=classNameOnly+"public class  "+class_name+"{  }"+" "
                                    javaFileName=os.path.join(cwd, javaFileName1)
                                    javaFileName=os.path.join(output_dirpath, javaFileName1)                        

                                if os.path.isfile(javaFileName) :
                                    print("\n File already exist--(L1)->",javaFileName)
                                    continue 
                                    
                                f = open(javaFileName, "w")
                                f.write(response1)
                                f.close()                            
                        except Exception as e:
                            print("Encountered exception. {0}".format(e))
            print("\n Java Gen 1st Level [Ends]")                   
            return (global_all_dependencies_from_cpp)
        except Exception as e:
            print("Encountered exception. {0}".format(e))
            return 0


    def create_folders(self,structure, parent_dir='', input_path=''):
        try:
            if not parent_dir:
                parent_dir = os.getcwd()
            for folder_name, substructure in structure.items():
                path = os.path.join(parent_dir, folder_name)
                if (path.endswith(".java")):
                    file_name = os.path.basename(path)  
                    dir_name=os.path.dirname(path)
                    srcfileName=os.path.join(input_path, file_name)            
                    shutil.copy(srcfileName, parent_dir)
                elif (path.endswith(".xml")):
                    file_name = os.path.basename(path)
                    dir_name=os.path.dirname(path)
                    srcfileName=os.path.join(input_path, file_name)           
                    #shutil.move(srcfileName, parent_dir)
                    shutil.copy(srcfileName, parent_dir)                    
                else :
                    if not os.path.exists(path):
                        os.makedirs(path)
                if isinstance(substructure, dict):
                    self.create_folders(substructure, path, input_path)
        except Exception as e:
            print("Encountered exception. {0}".format(e))
            return 0


    def del_tmpfile(self, folder):
        try:    
            import os
            path = os.getcwd()            
            cwd = folder
            listofFiles=os.listdir(cwd)
            for filename in listofFiles:
                if (filename.endswith(".java")):
                    filename1 = os.path.join(path,folder)
                    filename1 = os.path.join(filename1,filename)                    
                    command="del    "+filename1
                    os.system(command)                    
            return 0
        except Exception as e:
            print("Encountered exception. {0}".format(e))
            return 0

    def startAgenticReview(self,outpfld,global_all_dependencies_from_cpp):        
        try:
            import os
            all_dep_list=""
            llm_responses = ''
            dir_response = ''
            pom_response = ''            
            cwd = outpfld
            listofFiles=os.listdir(cwd)
            print("\n Agentic Review [Started]")             
            #print("\n list of java files ---",listofFiles)
            global_all_dependencies_from_java=""
            all_classes=""
            all_package=""            
            classNameOnly=""
            for name in listofFiles:
                if name.endswith(".java"):
                    try:
                        javaFile = os.path.join(cwd,name.split('.')[0]+".java")
                        javaOrgFile = os.path.join(cwd,name.split('.')[0]+"_org.java")                      
############################################################################################                        
                        with open(javaFile, 'r') as file:
                            jfile_content = file.read()
                        file.close()
                        prompts="PROMPT_CODE_MIG_REVIEW_COMMENT"
                        review_content=self.llmHandler(jfile_content,prompts)
           
                        file_content="\n The following is the the review comment \n"+review_content+"\n"+PROMPT_CODE_MIG_GUIDELINES_ON_CODE_UPDATE+PROMPT_CODE_MIG_GUIDELINES_ON_CODE_UPDATE_ADDITIONAL+"\n Also donot use any of the following public class name while providing the updated Java code\n"+classNameOnly+"\n"+"\nThe following is the java file \n"+jfile_content
                        prompts="PROMPT_CODE_MIG_UPDATE_CODE_ON_REVIEW"
                        response1=self.llmHandler(file_content,prompts)
                        start = '```java'
                        end = '```'
                        s = response1
                        response1=(s.split(start))[1].split(end)[0]
                      
#####################################################################################3
                        #f = open(javaOrgFile, "w")
                        #f.write(jfile_content)
                        #f.close() 
######################################################################################
                        import re
                        pattern = r'public class ([A-Za-z0-9_]+)'
                        class_names = re.findall(pattern, response1)
                        for class_name in class_names:
                            global_all_dependencies_from_java=global_all_dependencies_from_java+"public class  "+class_name+"{  }"+" "
                            all_classes=all_classes+"public class  "+class_name+"{  }"+" "
                            classNameOnly=classNameOnly+"\n"+"public class  "+class_name+"{  }"+" "
                            javaFileName1=class_name+".java"
                            javaFileName=os.path.join(cwd, javaFileName1)
                        pattern = r'import ([A-Za-z0-9.;_]+)'
                        importall = re.findall(pattern, response1)
                        for importall in importall:
                            global_all_dependencies_from_java=global_all_dependencies_from_java+importall
                        pattern = r'package ([A-Za-z0-9.;_]+)'
                        packageall = re.findall(pattern, response1)
                        for packageall in packageall:
                            all_package=all_package+"\n"+"package "+packageall+"\n"+"public class  "+class_name+"{  }"+" "
                        llm_responses=llm_responses+"\n File Name :"+javaFileName1+"\n"+response1
                        f = open(javaFileName, "w")
                        f.write(response1)
                        f.close()                            
                    except Exception as e:
                        print("Encountered exception. {0}".format(e))
            print("\nAgentic Review [Ends]")
            prompts="PROMPT_CODE_MIG_CREATE_POM_FILE"
            response=self.llmHandler(global_all_dependencies_from_java,prompts)
            response = response.replace(' .', '.').strip()
            start = '```xml'
            end = '```'
            s = response
            response=(s.split(start))[1].split(end)[0]          
            filename1 = os.path.join(outpfld,"pom.xml")
            f = open(filename1, "w")            
            f.write(response)
            f.close()
            pom_response=response
            prompts="PROMPT_CODE_MIG_CREATE_FOLDER"
            response=self.llmHandler(all_package,prompts)
            response = response.replace(' .', '.').strip()         
            start = '```json'
            end = '```'
            s = response
            response=(s.split(start))[1].split(end)[0]
            import json               
            json_str = json.loads(response)
            json_str = {outpfld: json_str}            
            self.create_folders(json_str,input_path=outpfld )            
            
            prompts="PROMPT_CODE_MIG_DISPLAY_FOLDER"
            response=self.llmHandler(response,prompts)
            response = response.replace(' .', '.').strip()
            start = '```'
            end = '```'
            s = response
            response=(s.split(start))[1].split(end)[0]            
            dir_response=response
            self.del_tmpfile(outpfld)
            print("\n\n Migration is almost Completed at folder\n\n",outpfld)
            return pom_response, dir_response, llm_responses
        except Exception as e:
            print("Encountered exception. {0}".format(e))
            return 0

    def CreateApplicationProp(self,inpfld):        
        try:
            import os
            import time  
            import pandas as pd
            cwd = os.getcwd()
            rootpath=os.path.join(cwd, inpfld) 
            global_all_dependencies_from_java=""
            all_classes=""
            classNameOnly=""
            all_package=""
            print("\n CreateApplicationProp  [Started]")
            for root, dirs, files in os.walk(rootpath):
                for name in files:
                    if name.endswith(".java") :
                        try:
                            fileName=os.path.join(root, name) 
                            with open(fileName, 'r') as file:
                                response1 = file.read()
                            import re
                            pattern = r'public class ([A-Za-z0-9_]+)'
                            class_names = re.findall(pattern, response1)
                            for class_name in class_names:
                                global_all_dependencies_from_java=global_all_dependencies_from_java+"public class  "+class_name+"{  }"+" "
                                all_classes=all_classes+"public class  "+class_name+"{  }"+" "
                                classNameOnly=classNameOnly+"\n"+"public class  "+class_name+"{  }"+" "
                                javaFileName1=class_name+".java"
                                javaFileName=os.path.join(cwd, javaFileName1)
                            pattern = r'import ([A-Za-z0-9.;_]+)'
                            importall = re.findall(pattern, response1)
                            for importall in importall:
                                global_all_dependencies_from_java=global_all_dependencies_from_java+importall
                            pattern = r'package ([A-Za-z0-9.;_]+)'
                            packageall = re.findall(pattern, response1)
                            for packageall in packageall:
                                all_package=all_package+"\n"+"package "+packageall+"\n"+"public class  "+class_name+"{  }"+" "
                        except Exception as e:
                            print("Encountered exception. {0}".format(e))


            prompts="PROMPT_CODE_MIG_CREATE_APPLICATION_PROP"            
            response=self.llmHandler(global_all_dependencies_from_java+all_package,prompts)
            response = response.replace(' .', '.').strip()
            start = '```properties'
            end = '```'
            s = response
            response=(s.split(start))[1].split(end)[0]                        
         
            appPropFileName=os.path.join(inpfld, "application.properties")            
            f = open(appPropFileName, "w")
            f.write(response)
            f.close()                                        
            print("\n CreateApplicationProp [Ends]") 
            return response            
        except Exception as e:
            print("Encountered exception. {0}".format(e))
            return 'error',e,''



def run_usecase(usecase_name, form_data, exec_id, job_name, model_name, *args, **kwargs):
    input_dirpath = os.path.join("assets", "UploadedData", usecase_name, job_name)
    output_dirpath = os.path.join("assets", "Result", usecase_name, job_name)
    os.makedirs(output_dirpath, exist_ok=True) # ensure output dir is created
    logger.info(f"Input dir: {input_dirpath}")
    logger.info(f"Output dir: {output_dirpath}")
    pocObj = pocOnCodeMigration()    
    response = pocObj.startJavaMigrationPOC(input_dirpath, output_dirpath)
    pom_response, dir_response, llm_responses = pocObj.startAgenticReview(output_dirpath)  
    logger.info(f"Code Migration Done")
    response = f"{pom_response}\n{dir_response}\n{llm_responses}\n"
    append_execution_result(f"Code Migration Done", "Source file: CPP", response)
    ####[System defined]. save_execution_summary has to be called at end of execution
    save_execution_summary(
        job_name=job_name,
        model_name=model_name,
        prompt_tokens=0,
        total_tokens=0,
        numof_files=0,
        )
    logger.info(f"Execution summary saved")
    return {"status": "success", "msg": "Success"}


import argparse
def main():
    parser = argparse.ArgumentParser(description='POC On C++ to JAVA CodeMigration')
    parser.add_argument('-i', '--inputFolder', required=True, type=str, help='input file folder') 
    parser.add_argument('-o', '--ouputFolder', required=True, type=str, help='output file folder')     
    args = parser.parse_args()    
    inpfld=args.inputFolder
    outpfld=args.ouputFolder    
    import os
    os.makedirs(outpfld, exist_ok=True) # ensure output dir is created          
    t1=time.time()
    pocObj = pocOnCodeMigration()    
    global_all_dependencies_from_cpp=pocObj.startJavaMigrationPOC(inpfld,outpfld)
    pom_response, dir_response, llm_responses=pocObj.startAgenticReview(outpfld,global_all_dependencies_from_cpp) 
    appProp=pocObj.CreateApplicationProp(outpfld)        
    t2=time.time()  
    print("\n time taken --->",t2-t1)
if __name__ == "__main__":
    main()