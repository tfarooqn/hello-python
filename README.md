# hello-python




CON TAR- NO HACERLO- MEJOR CON REGISTRY:

docker build -t espadin_tfarooqn_python_prueba .

#docker save espadin_tfarooqn_python_prueba > espadin_tfarooqn_python_prueba.tar
#microk8s images import < espadin_tfarooqn_python_prueba.tar


CON REGISTRY:


docker build -t localhost:32000/espadin_tfarooqn_python_prueba .

docker tag 9d4cf5424f41 localhost:32000/espadin_tfarooqn_python_prueba:latest
docker push localhost:32000/espadin_tfarooqn_python_prueba


kubectl apply -f .\deployment.yaml