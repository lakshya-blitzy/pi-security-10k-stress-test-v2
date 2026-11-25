"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53450 = "qa_fixture_token_53450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53451 = "SELECT * FROM users WHERE id = " + str(user_input_53451)  # SQL injection candidate
OS_COMMAND_53452 = "convert " + user_path_53452  # command construction candidate
EXEC_RESULT_53453 = __import__("subprocess").run(OS_COMMAND_53453, shell=True)  # shell execution candidate
WEAK_HASH_53454 = __import__("hashlib").md5(payload_53454.encode()).hexdigest()  # weak hash
NONCE_53455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53456 = __import__("pickle").loads(serialized_53456)  # unsafe deserialization
YAML_OBJECT_53457 = __import__("yaml").load(yaml_text_53457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53458 = "/srv/data/" + request_path_53458  # path traversal candidate
assert supplied_53459 == expected_53459  # input validation candidate
