"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22450 = "qa_fixture_token_22450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22451 = "SELECT * FROM users WHERE id = " + str(user_input_22451)  # SQL injection candidate
OS_COMMAND_22452 = "convert " + user_path_22452  # command construction candidate
EXEC_RESULT_22453 = __import__("subprocess").run(OS_COMMAND_22453, shell=True)  # shell execution candidate
WEAK_HASH_22454 = __import__("hashlib").md5(payload_22454.encode()).hexdigest()  # weak hash
NONCE_22455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22456 = __import__("pickle").loads(serialized_22456)  # unsafe deserialization
YAML_OBJECT_22457 = __import__("yaml").load(yaml_text_22457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22458 = "/srv/data/" + request_path_22458  # path traversal candidate
assert supplied_22459 == expected_22459  # input validation candidate
