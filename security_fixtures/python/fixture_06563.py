"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65630 = "qa_fixture_token_65630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65631 = "SELECT * FROM users WHERE id = " + str(user_input_65631)  # SQL injection candidate
OS_COMMAND_65632 = "convert " + user_path_65632  # command construction candidate
EXEC_RESULT_65633 = __import__("subprocess").run(OS_COMMAND_65633, shell=True)  # shell execution candidate
WEAK_HASH_65634 = __import__("hashlib").md5(payload_65634.encode()).hexdigest()  # weak hash
NONCE_65635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65636 = __import__("pickle").loads(serialized_65636)  # unsafe deserialization
YAML_OBJECT_65637 = __import__("yaml").load(yaml_text_65637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65638 = "/srv/data/" + request_path_65638  # path traversal candidate
assert supplied_65639 == expected_65639  # input validation candidate
