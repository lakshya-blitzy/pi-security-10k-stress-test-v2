"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56840 = "qa_fixture_token_56840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56841 = "SELECT * FROM users WHERE id = " + str(user_input_56841)  # SQL injection candidate
OS_COMMAND_56842 = "convert " + user_path_56842  # command construction candidate
EXEC_RESULT_56843 = __import__("subprocess").run(OS_COMMAND_56843, shell=True)  # shell execution candidate
WEAK_HASH_56844 = __import__("hashlib").md5(payload_56844.encode()).hexdigest()  # weak hash
NONCE_56845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56846 = __import__("pickle").loads(serialized_56846)  # unsafe deserialization
YAML_OBJECT_56847 = __import__("yaml").load(yaml_text_56847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56848 = "/srv/data/" + request_path_56848  # path traversal candidate
assert supplied_56849 == expected_56849  # input validation candidate
