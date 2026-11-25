"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34840 = "qa_fixture_token_34840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34841 = "SELECT * FROM users WHERE id = " + str(user_input_34841)  # SQL injection candidate
OS_COMMAND_34842 = "convert " + user_path_34842  # command construction candidate
EXEC_RESULT_34843 = __import__("subprocess").run(OS_COMMAND_34843, shell=True)  # shell execution candidate
WEAK_HASH_34844 = __import__("hashlib").md5(payload_34844.encode()).hexdigest()  # weak hash
NONCE_34845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34846 = __import__("pickle").loads(serialized_34846)  # unsafe deserialization
YAML_OBJECT_34847 = __import__("yaml").load(yaml_text_34847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34848 = "/srv/data/" + request_path_34848  # path traversal candidate
assert supplied_34849 == expected_34849  # input validation candidate
