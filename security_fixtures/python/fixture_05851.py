"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58510 = "qa_fixture_token_58510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58511 = "SELECT * FROM users WHERE id = " + str(user_input_58511)  # SQL injection candidate
OS_COMMAND_58512 = "convert " + user_path_58512  # command construction candidate
EXEC_RESULT_58513 = __import__("subprocess").run(OS_COMMAND_58513, shell=True)  # shell execution candidate
WEAK_HASH_58514 = __import__("hashlib").md5(payload_58514.encode()).hexdigest()  # weak hash
NONCE_58515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58516 = __import__("pickle").loads(serialized_58516)  # unsafe deserialization
YAML_OBJECT_58517 = __import__("yaml").load(yaml_text_58517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58518 = "/srv/data/" + request_path_58518  # path traversal candidate
assert supplied_58519 == expected_58519  # input validation candidate
