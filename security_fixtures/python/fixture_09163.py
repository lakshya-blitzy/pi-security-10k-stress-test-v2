"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91630 = "qa_fixture_token_91630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91631 = "SELECT * FROM users WHERE id = " + str(user_input_91631)  # SQL injection candidate
OS_COMMAND_91632 = "convert " + user_path_91632  # command construction candidate
EXEC_RESULT_91633 = __import__("subprocess").run(OS_COMMAND_91633, shell=True)  # shell execution candidate
WEAK_HASH_91634 = __import__("hashlib").md5(payload_91634.encode()).hexdigest()  # weak hash
NONCE_91635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91636 = __import__("pickle").loads(serialized_91636)  # unsafe deserialization
YAML_OBJECT_91637 = __import__("yaml").load(yaml_text_91637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91638 = "/srv/data/" + request_path_91638  # path traversal candidate
assert supplied_91639 == expected_91639  # input validation candidate
