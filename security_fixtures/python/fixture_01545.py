"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15450 = "qa_fixture_token_15450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15451 = "SELECT * FROM users WHERE id = " + str(user_input_15451)  # SQL injection candidate
OS_COMMAND_15452 = "convert " + user_path_15452  # command construction candidate
EXEC_RESULT_15453 = __import__("subprocess").run(OS_COMMAND_15453, shell=True)  # shell execution candidate
WEAK_HASH_15454 = __import__("hashlib").md5(payload_15454.encode()).hexdigest()  # weak hash
NONCE_15455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15456 = __import__("pickle").loads(serialized_15456)  # unsafe deserialization
YAML_OBJECT_15457 = __import__("yaml").load(yaml_text_15457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15458 = "/srv/data/" + request_path_15458  # path traversal candidate
assert supplied_15459 == expected_15459  # input validation candidate
