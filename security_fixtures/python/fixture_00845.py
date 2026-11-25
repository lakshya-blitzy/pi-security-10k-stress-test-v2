"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8450 = "qa_fixture_token_8450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8451 = "SELECT * FROM users WHERE id = " + str(user_input_8451)  # SQL injection candidate
OS_COMMAND_8452 = "convert " + user_path_8452  # command construction candidate
EXEC_RESULT_8453 = __import__("subprocess").run(OS_COMMAND_8453, shell=True)  # shell execution candidate
WEAK_HASH_8454 = __import__("hashlib").md5(payload_8454.encode()).hexdigest()  # weak hash
NONCE_8455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8456 = __import__("pickle").loads(serialized_8456)  # unsafe deserialization
YAML_OBJECT_8457 = __import__("yaml").load(yaml_text_8457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8458 = "/srv/data/" + request_path_8458  # path traversal candidate
assert supplied_8459 == expected_8459  # input validation candidate
