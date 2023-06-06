FROM docker/whalesay
RUN echo "cat /msg.txt | cowsay" > /entrypoint 
ENTRYPOINT ["/bin/bash", "/entrypoint"]
