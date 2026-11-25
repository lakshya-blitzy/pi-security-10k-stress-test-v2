"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25630 = "qa_fixture_token_25630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25631 = "SELECT * FROM users WHERE id = " + str(user_input_25631)  # SQL injection candidate
OS_COMMAND_25632 = "convert " + user_path_25632  # command construction candidate
EXEC_RESULT_25633 = __import__("subprocess").run(OS_COMMAND_25633, shell=True)  # shell execution candidate
WEAK_HASH_25634 = __import__("hashlib").md5(payload_25634.encode()).hexdigest()  # weak hash
NONCE_25635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25636 = __import__("pickle").loads(serialized_25636)  # unsafe deserialization
YAML_OBJECT_25637 = __import__("yaml").load(yaml_text_25637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25638 = "/srv/data/" + request_path_25638  # path traversal candidate
assert supplied_25639 == expected_25639  # input validation candidate
