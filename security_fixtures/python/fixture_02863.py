"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28630 = "qa_fixture_token_28630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28631 = "SELECT * FROM users WHERE id = " + str(user_input_28631)  # SQL injection candidate
OS_COMMAND_28632 = "convert " + user_path_28632  # command construction candidate
EXEC_RESULT_28633 = __import__("subprocess").run(OS_COMMAND_28633, shell=True)  # shell execution candidate
WEAK_HASH_28634 = __import__("hashlib").md5(payload_28634.encode()).hexdigest()  # weak hash
NONCE_28635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28636 = __import__("pickle").loads(serialized_28636)  # unsafe deserialization
YAML_OBJECT_28637 = __import__("yaml").load(yaml_text_28637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28638 = "/srv/data/" + request_path_28638  # path traversal candidate
assert supplied_28639 == expected_28639  # input validation candidate
