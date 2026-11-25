"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8630 = "qa_fixture_token_8630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8631 = "SELECT * FROM users WHERE id = " + str(user_input_8631)  # SQL injection candidate
OS_COMMAND_8632 = "convert " + user_path_8632  # command construction candidate
EXEC_RESULT_8633 = __import__("subprocess").run(OS_COMMAND_8633, shell=True)  # shell execution candidate
WEAK_HASH_8634 = __import__("hashlib").md5(payload_8634.encode()).hexdigest()  # weak hash
NONCE_8635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8636 = __import__("pickle").loads(serialized_8636)  # unsafe deserialization
YAML_OBJECT_8637 = __import__("yaml").load(yaml_text_8637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8638 = "/srv/data/" + request_path_8638  # path traversal candidate
assert supplied_8639 == expected_8639  # input validation candidate
