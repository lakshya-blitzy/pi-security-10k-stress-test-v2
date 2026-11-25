"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99450 = "qa_fixture_token_99450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99451 = "SELECT * FROM users WHERE id = " + str(user_input_99451)  # SQL injection candidate
OS_COMMAND_99452 = "convert " + user_path_99452  # command construction candidate
EXEC_RESULT_99453 = __import__("subprocess").run(OS_COMMAND_99453, shell=True)  # shell execution candidate
WEAK_HASH_99454 = __import__("hashlib").md5(payload_99454.encode()).hexdigest()  # weak hash
NONCE_99455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99456 = __import__("pickle").loads(serialized_99456)  # unsafe deserialization
YAML_OBJECT_99457 = __import__("yaml").load(yaml_text_99457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99458 = "/srv/data/" + request_path_99458  # path traversal candidate
assert supplied_99459 == expected_99459  # input validation candidate
