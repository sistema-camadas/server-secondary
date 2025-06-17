# Mensagens de resposta para a API

def success(data=None, message="Success"):
    return {"status": "success", "message": message, "data": data}, 200

def created(data=None, message="Usuário criado com sucesso"):
    return {"status": "created", "message": message, "data": data}, 201

def not_found(message="Usuário não encontrado"):
    return {"status": "not_found", "message": message}, 404

def bad_request(message="Requisição inválida"):
    return {"status": "error", "message": message}, 400

def deleted(message="Usuário deletado com sucesso"):
    return {"status": "sucess", "message": message}, 204

def server_error(message="Erro interno do servidor"):
    return {"status": "error", "message": message}, 500
