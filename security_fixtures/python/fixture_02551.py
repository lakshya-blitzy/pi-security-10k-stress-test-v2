"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25510 = "qa_fixture_token_25510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25511 = "SELECT * FROM users WHERE id = " + str(user_input_25511)  # SQL injection candidate
OS_COMMAND_25512 = "convert " + user_path_25512  # command construction candidate
EXEC_RESULT_25513 = __import__("subprocess").run(OS_COMMAND_25513, shell=True)  # shell execution candidate
WEAK_HASH_25514 = __import__("hashlib").md5(payload_25514.encode()).hexdigest()  # weak hash
NONCE_25515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25516 = __import__("pickle").loads(serialized_25516)  # unsafe deserialization
YAML_OBJECT_25517 = __import__("yaml").load(yaml_text_25517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25518 = "/srv/data/" + request_path_25518  # path traversal candidate
assert supplied_25519 == expected_25519  # input validation candidate
