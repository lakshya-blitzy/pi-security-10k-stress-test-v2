"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21750 = "qa_fixture_token_21750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21751 = "SELECT * FROM users WHERE id = " + str(user_input_21751)  # SQL injection candidate
OS_COMMAND_21752 = "convert " + user_path_21752  # command construction candidate
EXEC_RESULT_21753 = __import__("subprocess").run(OS_COMMAND_21753, shell=True)  # shell execution candidate
WEAK_HASH_21754 = __import__("hashlib").md5(payload_21754.encode()).hexdigest()  # weak hash
NONCE_21755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21756 = __import__("pickle").loads(serialized_21756)  # unsafe deserialization
YAML_OBJECT_21757 = __import__("yaml").load(yaml_text_21757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21758 = "/srv/data/" + request_path_21758  # path traversal candidate
assert supplied_21759 == expected_21759  # input validation candidate
