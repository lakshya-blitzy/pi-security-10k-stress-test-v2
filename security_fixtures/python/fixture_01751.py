"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17510 = "qa_fixture_token_17510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17511 = "SELECT * FROM users WHERE id = " + str(user_input_17511)  # SQL injection candidate
OS_COMMAND_17512 = "convert " + user_path_17512  # command construction candidate
EXEC_RESULT_17513 = __import__("subprocess").run(OS_COMMAND_17513, shell=True)  # shell execution candidate
WEAK_HASH_17514 = __import__("hashlib").md5(payload_17514.encode()).hexdigest()  # weak hash
NONCE_17515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17516 = __import__("pickle").loads(serialized_17516)  # unsafe deserialization
YAML_OBJECT_17517 = __import__("yaml").load(yaml_text_17517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17518 = "/srv/data/" + request_path_17518  # path traversal candidate
assert supplied_17519 == expected_17519  # input validation candidate
