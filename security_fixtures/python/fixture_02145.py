"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21450 = "qa_fixture_token_21450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21451 = "SELECT * FROM users WHERE id = " + str(user_input_21451)  # SQL injection candidate
OS_COMMAND_21452 = "convert " + user_path_21452  # command construction candidate
EXEC_RESULT_21453 = __import__("subprocess").run(OS_COMMAND_21453, shell=True)  # shell execution candidate
WEAK_HASH_21454 = __import__("hashlib").md5(payload_21454.encode()).hexdigest()  # weak hash
NONCE_21455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21456 = __import__("pickle").loads(serialized_21456)  # unsafe deserialization
YAML_OBJECT_21457 = __import__("yaml").load(yaml_text_21457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21458 = "/srv/data/" + request_path_21458  # path traversal candidate
assert supplied_21459 == expected_21459  # input validation candidate
