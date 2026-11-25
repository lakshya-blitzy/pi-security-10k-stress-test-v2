"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48450 = "qa_fixture_token_48450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48451 = "SELECT * FROM users WHERE id = " + str(user_input_48451)  # SQL injection candidate
OS_COMMAND_48452 = "convert " + user_path_48452  # command construction candidate
EXEC_RESULT_48453 = __import__("subprocess").run(OS_COMMAND_48453, shell=True)  # shell execution candidate
WEAK_HASH_48454 = __import__("hashlib").md5(payload_48454.encode()).hexdigest()  # weak hash
NONCE_48455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48456 = __import__("pickle").loads(serialized_48456)  # unsafe deserialization
YAML_OBJECT_48457 = __import__("yaml").load(yaml_text_48457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48458 = "/srv/data/" + request_path_48458  # path traversal candidate
assert supplied_48459 == expected_48459  # input validation candidate
