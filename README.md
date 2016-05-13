# DS-GA1004 Project
NYC Taxi and Citibike Analysis
Team member: Sida Ye, Xingye Zhang, Kaiwen Liu

Instruction(refer to [Tuan-Anh Hoang-Vu](http://bigdata.poly.edu/~tuananh/))
-----------
1. Create an Amazon EMR cluster with the following configuration (the bootstrap action is very important -- please pay attention to that):

        * Logging: Enabled (remember to input your S3 bucket to store log file)
        * Bootstrap action: This is a very important step because the sample scripts 
        make use of python rtree library, but Amazon AMI 3.3.1 does not have rtree installed.
        * Use advanced option in cluster configuraiton
        Click 'Add bootstrap action' -> Custom action -> Configure and add -> 
        Put the following in 'S3 location': rtree.sh
        * Don't add any step at this point

2. Clone this repository and upload the shapefile(.shp) to your bucket on S3.
        *shp file
        *rtree.sh
        *shapefile.py
        
3. To run neighborhoods script: Add the following streaming step to your cluster with the following information:

        Replace username with your own path in S3:
        * Mapper: s3://username/mapper.py
        * Reducer: s3://username/reducer.py
        * Input: s3://username/data
        * Output: s3://username/output
        * Arguments: -files s3://username/mapper.py,s3://username/reducer.py,s3://username/shapefile.py,s3://username/NYC.shp,s3://username/NYC.prj,s3://username/NYC.shx,s3://username/NYC.dbf
              
4. Remember to terminate cluster after use.

Reference:
======

[Huy T. Vo](http://serv.cusp.nyu.edu/~hvo/)

Contributors
============

[Tuan-Anh Hoang-Vu](http://bigdata.poly.edu/~tuananh/)






