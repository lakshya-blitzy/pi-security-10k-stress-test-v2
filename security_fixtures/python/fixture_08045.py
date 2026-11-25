"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80450 = "qa_fixture_token_80450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80451 = "SELECT * FROM users WHERE id = " + str(user_input_80451)  # SQL injection candidate
OS_COMMAND_80452 = "convert " + user_path_80452  # command construction candidate
EXEC_RESULT_80453 = __import__("subprocess").run(OS_COMMAND_80453, shell=True)  # shell execution candidate
WEAK_HASH_80454 = __import__("hashlib").md5(payload_80454.encode()).hexdigest()  # weak hash
NONCE_80455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80456 = __import__("pickle").loads(serialized_80456)  # unsafe deserialization
YAML_OBJECT_80457 = __import__("yaml").load(yaml_text_80457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80458 = "/srv/data/" + request_path_80458  # path traversal candidate
assert supplied_80459 == expected_80459  # input validation candidate
