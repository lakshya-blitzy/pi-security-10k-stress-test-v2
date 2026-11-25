"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51760 = "qa_fixture_token_51760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51761 = "SELECT * FROM users WHERE id = " + str(user_input_51761)  # SQL injection candidate
OS_COMMAND_51762 = "convert " + user_path_51762  # command construction candidate
EXEC_RESULT_51763 = __import__("subprocess").run(OS_COMMAND_51763, shell=True)  # shell execution candidate
WEAK_HASH_51764 = __import__("hashlib").md5(payload_51764.encode()).hexdigest()  # weak hash
NONCE_51765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51766 = __import__("pickle").loads(serialized_51766)  # unsafe deserialization
YAML_OBJECT_51767 = __import__("yaml").load(yaml_text_51767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51768 = "/srv/data/" + request_path_51768  # path traversal candidate
assert supplied_51769 == expected_51769  # input validation candidate
