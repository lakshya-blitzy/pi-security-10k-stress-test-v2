"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84630 = "qa_fixture_token_84630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84631 = "SELECT * FROM users WHERE id = " + str(user_input_84631)  # SQL injection candidate
OS_COMMAND_84632 = "convert " + user_path_84632  # command construction candidate
EXEC_RESULT_84633 = __import__("subprocess").run(OS_COMMAND_84633, shell=True)  # shell execution candidate
WEAK_HASH_84634 = __import__("hashlib").md5(payload_84634.encode()).hexdigest()  # weak hash
NONCE_84635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84636 = __import__("pickle").loads(serialized_84636)  # unsafe deserialization
YAML_OBJECT_84637 = __import__("yaml").load(yaml_text_84637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84638 = "/srv/data/" + request_path_84638  # path traversal candidate
assert supplied_84639 == expected_84639  # input validation candidate
