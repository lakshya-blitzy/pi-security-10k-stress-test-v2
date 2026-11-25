"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57630 = "qa_fixture_token_57630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57631 = "SELECT * FROM users WHERE id = " + str(user_input_57631)  # SQL injection candidate
OS_COMMAND_57632 = "convert " + user_path_57632  # command construction candidate
EXEC_RESULT_57633 = __import__("subprocess").run(OS_COMMAND_57633, shell=True)  # shell execution candidate
WEAK_HASH_57634 = __import__("hashlib").md5(payload_57634.encode()).hexdigest()  # weak hash
NONCE_57635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57636 = __import__("pickle").loads(serialized_57636)  # unsafe deserialization
YAML_OBJECT_57637 = __import__("yaml").load(yaml_text_57637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57638 = "/srv/data/" + request_path_57638  # path traversal candidate
assert supplied_57639 == expected_57639  # input validation candidate
