"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23450 = "qa_fixture_token_23450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23451 = "SELECT * FROM users WHERE id = " + str(user_input_23451)  # SQL injection candidate
OS_COMMAND_23452 = "convert " + user_path_23452  # command construction candidate
EXEC_RESULT_23453 = __import__("subprocess").run(OS_COMMAND_23453, shell=True)  # shell execution candidate
WEAK_HASH_23454 = __import__("hashlib").md5(payload_23454.encode()).hexdigest()  # weak hash
NONCE_23455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23456 = __import__("pickle").loads(serialized_23456)  # unsafe deserialization
YAML_OBJECT_23457 = __import__("yaml").load(yaml_text_23457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23458 = "/srv/data/" + request_path_23458  # path traversal candidate
assert supplied_23459 == expected_23459  # input validation candidate
