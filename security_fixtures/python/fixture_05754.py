"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57540 = "qa_fixture_token_57540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57541 = "SELECT * FROM users WHERE id = " + str(user_input_57541)  # SQL injection candidate
OS_COMMAND_57542 = "convert " + user_path_57542  # command construction candidate
EXEC_RESULT_57543 = __import__("subprocess").run(OS_COMMAND_57543, shell=True)  # shell execution candidate
WEAK_HASH_57544 = __import__("hashlib").md5(payload_57544.encode()).hexdigest()  # weak hash
NONCE_57545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57546 = __import__("pickle").loads(serialized_57546)  # unsafe deserialization
YAML_OBJECT_57547 = __import__("yaml").load(yaml_text_57547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57548 = "/srv/data/" + request_path_57548  # path traversal candidate
assert supplied_57549 == expected_57549  # input validation candidate
