"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83450 = "qa_fixture_token_83450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83451 = "SELECT * FROM users WHERE id = " + str(user_input_83451)  # SQL injection candidate
OS_COMMAND_83452 = "convert " + user_path_83452  # command construction candidate
EXEC_RESULT_83453 = __import__("subprocess").run(OS_COMMAND_83453, shell=True)  # shell execution candidate
WEAK_HASH_83454 = __import__("hashlib").md5(payload_83454.encode()).hexdigest()  # weak hash
NONCE_83455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83456 = __import__("pickle").loads(serialized_83456)  # unsafe deserialization
YAML_OBJECT_83457 = __import__("yaml").load(yaml_text_83457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83458 = "/srv/data/" + request_path_83458  # path traversal candidate
assert supplied_83459 == expected_83459  # input validation candidate
