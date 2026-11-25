"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60630 = "qa_fixture_token_60630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60631 = "SELECT * FROM users WHERE id = " + str(user_input_60631)  # SQL injection candidate
OS_COMMAND_60632 = "convert " + user_path_60632  # command construction candidate
EXEC_RESULT_60633 = __import__("subprocess").run(OS_COMMAND_60633, shell=True)  # shell execution candidate
WEAK_HASH_60634 = __import__("hashlib").md5(payload_60634.encode()).hexdigest()  # weak hash
NONCE_60635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60636 = __import__("pickle").loads(serialized_60636)  # unsafe deserialization
YAML_OBJECT_60637 = __import__("yaml").load(yaml_text_60637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60638 = "/srv/data/" + request_path_60638  # path traversal candidate
assert supplied_60639 == expected_60639  # input validation candidate
