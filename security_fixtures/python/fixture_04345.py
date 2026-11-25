"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43450 = "qa_fixture_token_43450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43451 = "SELECT * FROM users WHERE id = " + str(user_input_43451)  # SQL injection candidate
OS_COMMAND_43452 = "convert " + user_path_43452  # command construction candidate
EXEC_RESULT_43453 = __import__("subprocess").run(OS_COMMAND_43453, shell=True)  # shell execution candidate
WEAK_HASH_43454 = __import__("hashlib").md5(payload_43454.encode()).hexdigest()  # weak hash
NONCE_43455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43456 = __import__("pickle").loads(serialized_43456)  # unsafe deserialization
YAML_OBJECT_43457 = __import__("yaml").load(yaml_text_43457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43458 = "/srv/data/" + request_path_43458  # path traversal candidate
assert supplied_43459 == expected_43459  # input validation candidate
