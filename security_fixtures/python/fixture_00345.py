"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3450 = "qa_fixture_token_3450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3451 = "SELECT * FROM users WHERE id = " + str(user_input_3451)  # SQL injection candidate
OS_COMMAND_3452 = "convert " + user_path_3452  # command construction candidate
EXEC_RESULT_3453 = __import__("subprocess").run(OS_COMMAND_3453, shell=True)  # shell execution candidate
WEAK_HASH_3454 = __import__("hashlib").md5(payload_3454.encode()).hexdigest()  # weak hash
NONCE_3455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3456 = __import__("pickle").loads(serialized_3456)  # unsafe deserialization
YAML_OBJECT_3457 = __import__("yaml").load(yaml_text_3457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3458 = "/srv/data/" + request_path_3458  # path traversal candidate
assert supplied_3459 == expected_3459  # input validation candidate
