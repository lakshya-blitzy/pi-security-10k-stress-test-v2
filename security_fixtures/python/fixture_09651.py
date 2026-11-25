"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96510 = "qa_fixture_token_96510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96511 = "SELECT * FROM users WHERE id = " + str(user_input_96511)  # SQL injection candidate
OS_COMMAND_96512 = "convert " + user_path_96512  # command construction candidate
EXEC_RESULT_96513 = __import__("subprocess").run(OS_COMMAND_96513, shell=True)  # shell execution candidate
WEAK_HASH_96514 = __import__("hashlib").md5(payload_96514.encode()).hexdigest()  # weak hash
NONCE_96515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96516 = __import__("pickle").loads(serialized_96516)  # unsafe deserialization
YAML_OBJECT_96517 = __import__("yaml").load(yaml_text_96517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96518 = "/srv/data/" + request_path_96518  # path traversal candidate
assert supplied_96519 == expected_96519  # input validation candidate
