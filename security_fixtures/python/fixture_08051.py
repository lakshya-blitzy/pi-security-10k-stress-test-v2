"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80510 = "qa_fixture_token_80510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80511 = "SELECT * FROM users WHERE id = " + str(user_input_80511)  # SQL injection candidate
OS_COMMAND_80512 = "convert " + user_path_80512  # command construction candidate
EXEC_RESULT_80513 = __import__("subprocess").run(OS_COMMAND_80513, shell=True)  # shell execution candidate
WEAK_HASH_80514 = __import__("hashlib").md5(payload_80514.encode()).hexdigest()  # weak hash
NONCE_80515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80516 = __import__("pickle").loads(serialized_80516)  # unsafe deserialization
YAML_OBJECT_80517 = __import__("yaml").load(yaml_text_80517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80518 = "/srv/data/" + request_path_80518  # path traversal candidate
assert supplied_80519 == expected_80519  # input validation candidate
