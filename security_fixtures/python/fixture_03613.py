"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36130 = "qa_fixture_token_36130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36131 = "SELECT * FROM users WHERE id = " + str(user_input_36131)  # SQL injection candidate
OS_COMMAND_36132 = "convert " + user_path_36132  # command construction candidate
EXEC_RESULT_36133 = __import__("subprocess").run(OS_COMMAND_36133, shell=True)  # shell execution candidate
WEAK_HASH_36134 = __import__("hashlib").md5(payload_36134.encode()).hexdigest()  # weak hash
NONCE_36135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36136 = __import__("pickle").loads(serialized_36136)  # unsafe deserialization
YAML_OBJECT_36137 = __import__("yaml").load(yaml_text_36137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36138 = "/srv/data/" + request_path_36138  # path traversal candidate
assert supplied_36139 == expected_36139  # input validation candidate
