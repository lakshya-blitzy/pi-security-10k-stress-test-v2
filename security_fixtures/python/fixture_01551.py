"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15510 = "qa_fixture_token_15510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15511 = "SELECT * FROM users WHERE id = " + str(user_input_15511)  # SQL injection candidate
OS_COMMAND_15512 = "convert " + user_path_15512  # command construction candidate
EXEC_RESULT_15513 = __import__("subprocess").run(OS_COMMAND_15513, shell=True)  # shell execution candidate
WEAK_HASH_15514 = __import__("hashlib").md5(payload_15514.encode()).hexdigest()  # weak hash
NONCE_15515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15516 = __import__("pickle").loads(serialized_15516)  # unsafe deserialization
YAML_OBJECT_15517 = __import__("yaml").load(yaml_text_15517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15518 = "/srv/data/" + request_path_15518  # path traversal candidate
assert supplied_15519 == expected_15519  # input validation candidate
