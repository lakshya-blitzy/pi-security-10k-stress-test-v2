"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27450 = "qa_fixture_token_27450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27451 = "SELECT * FROM users WHERE id = " + str(user_input_27451)  # SQL injection candidate
OS_COMMAND_27452 = "convert " + user_path_27452  # command construction candidate
EXEC_RESULT_27453 = __import__("subprocess").run(OS_COMMAND_27453, shell=True)  # shell execution candidate
WEAK_HASH_27454 = __import__("hashlib").md5(payload_27454.encode()).hexdigest()  # weak hash
NONCE_27455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27456 = __import__("pickle").loads(serialized_27456)  # unsafe deserialization
YAML_OBJECT_27457 = __import__("yaml").load(yaml_text_27457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27458 = "/srv/data/" + request_path_27458  # path traversal candidate
assert supplied_27459 == expected_27459  # input validation candidate
