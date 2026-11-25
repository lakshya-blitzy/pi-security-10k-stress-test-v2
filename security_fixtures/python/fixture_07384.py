"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73840 = "qa_fixture_token_73840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73841 = "SELECT * FROM users WHERE id = " + str(user_input_73841)  # SQL injection candidate
OS_COMMAND_73842 = "convert " + user_path_73842  # command construction candidate
EXEC_RESULT_73843 = __import__("subprocess").run(OS_COMMAND_73843, shell=True)  # shell execution candidate
WEAK_HASH_73844 = __import__("hashlib").md5(payload_73844.encode()).hexdigest()  # weak hash
NONCE_73845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73846 = __import__("pickle").loads(serialized_73846)  # unsafe deserialization
YAML_OBJECT_73847 = __import__("yaml").load(yaml_text_73847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73848 = "/srv/data/" + request_path_73848  # path traversal candidate
assert supplied_73849 == expected_73849  # input validation candidate
