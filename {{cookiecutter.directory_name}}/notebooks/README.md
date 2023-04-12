# notebooks

## SLURM Jobs

The notebooks typically has four sections,

- Import Library: import the necessary libraries and functions.
  - The *root_dir* should be set to the repository directory 
  - from `slurm.commands` import *some cli string builder* that contains the 
    cli arguments
  - from `slurm.sbatch` import *submit_array* to submit job arrays

- Set Variables: set the variables to construct the commands, usually directory 
  paths and the conda_environment to load  

- Construct Commands: some logic to navigate the folders and use the string 
  builder to build the command list
  - use *print('Number of Jobs: {}'.format(len(command_list)))* and 
    *print(command_list[:1])* to debug the logic and inspect the commands
  
- Submit Job: use another string builder to build node settings and submit the job arrays
   * *--job-name*: name for the jobs
   * *--time=1:00:00*: time for the jobs, contact HPC is needs to be extended after submission
   * *--nodes=1*: nodes per job
   * *--partition=up-cpu*: partition to request nodes, [up-cpu, up-gpu]
   * *--ntasks-per-node=1*: task per node
   * *--mem=8000*: ram in MB
   * *--gres=gpu:1*: Generic Resource Scheduler, use for requesting specific hardware, [gpu:gtx1080ti:1, gpu:p100:1]
   * *--output=./tmp/"slurm-%A_%a.out"*: this stores the .out from slurm in another folder to prevent overloading the notebook folder with too many files, use with *os.makedirs('./tmp', exist_ok=True)*
   
   * submit_array(root_dir, command_list, node_setting, job_name, *conda_path*): conda_path is optional
   
Use *squeue -u <user>* and *jobinfo job_id* to check the status of the job array.
