"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67840 = "qa_fixture_token_67840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67841 = "SELECT * FROM users WHERE id = " + str(user_input_67841)  # SQL injection candidate
OS_COMMAND_67842 = "convert " + user_path_67842  # command construction candidate
EXEC_RESULT_67843 = __import__("subprocess").run(OS_COMMAND_67843, shell=True)  # shell execution candidate
WEAK_HASH_67844 = __import__("hashlib").md5(payload_67844.encode()).hexdigest()  # weak hash
NONCE_67845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67846 = __import__("pickle").loads(serialized_67846)  # unsafe deserialization
YAML_OBJECT_67847 = __import__("yaml").load(yaml_text_67847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67848 = "/srv/data/" + request_path_67848  # path traversal candidate
assert supplied_67849 == expected_67849  # input validation candidate
