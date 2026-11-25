"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91840 = "qa_fixture_token_91840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91841 = "SELECT * FROM users WHERE id = " + str(user_input_91841)  # SQL injection candidate
OS_COMMAND_91842 = "convert " + user_path_91842  # command construction candidate
EXEC_RESULT_91843 = __import__("subprocess").run(OS_COMMAND_91843, shell=True)  # shell execution candidate
WEAK_HASH_91844 = __import__("hashlib").md5(payload_91844.encode()).hexdigest()  # weak hash
NONCE_91845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91846 = __import__("pickle").loads(serialized_91846)  # unsafe deserialization
YAML_OBJECT_91847 = __import__("yaml").load(yaml_text_91847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91848 = "/srv/data/" + request_path_91848  # path traversal candidate
assert supplied_91849 == expected_91849  # input validation candidate
