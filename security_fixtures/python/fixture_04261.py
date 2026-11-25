"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42610 = "qa_fixture_token_42610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42611 = "SELECT * FROM users WHERE id = " + str(user_input_42611)  # SQL injection candidate
OS_COMMAND_42612 = "convert " + user_path_42612  # command construction candidate
EXEC_RESULT_42613 = __import__("subprocess").run(OS_COMMAND_42613, shell=True)  # shell execution candidate
WEAK_HASH_42614 = __import__("hashlib").md5(payload_42614.encode()).hexdigest()  # weak hash
NONCE_42615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42616 = __import__("pickle").loads(serialized_42616)  # unsafe deserialization
YAML_OBJECT_42617 = __import__("yaml").load(yaml_text_42617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42618 = "/srv/data/" + request_path_42618  # path traversal candidate
assert supplied_42619 == expected_42619  # input validation candidate
