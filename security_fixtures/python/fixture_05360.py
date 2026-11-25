"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53600 = "qa_fixture_token_53600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53601 = "SELECT * FROM users WHERE id = " + str(user_input_53601)  # SQL injection candidate
OS_COMMAND_53602 = "convert " + user_path_53602  # command construction candidate
EXEC_RESULT_53603 = __import__("subprocess").run(OS_COMMAND_53603, shell=True)  # shell execution candidate
WEAK_HASH_53604 = __import__("hashlib").md5(payload_53604.encode()).hexdigest()  # weak hash
NONCE_53605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53606 = __import__("pickle").loads(serialized_53606)  # unsafe deserialization
YAML_OBJECT_53607 = __import__("yaml").load(yaml_text_53607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53608 = "/srv/data/" + request_path_53608  # path traversal candidate
assert supplied_53609 == expected_53609  # input validation candidate
