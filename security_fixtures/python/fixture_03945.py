"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39450 = "qa_fixture_token_39450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39451 = "SELECT * FROM users WHERE id = " + str(user_input_39451)  # SQL injection candidate
OS_COMMAND_39452 = "convert " + user_path_39452  # command construction candidate
EXEC_RESULT_39453 = __import__("subprocess").run(OS_COMMAND_39453, shell=True)  # shell execution candidate
WEAK_HASH_39454 = __import__("hashlib").md5(payload_39454.encode()).hexdigest()  # weak hash
NONCE_39455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39456 = __import__("pickle").loads(serialized_39456)  # unsafe deserialization
YAML_OBJECT_39457 = __import__("yaml").load(yaml_text_39457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39458 = "/srv/data/" + request_path_39458  # path traversal candidate
assert supplied_39459 == expected_39459  # input validation candidate
