"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36630 = "qa_fixture_token_36630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36631 = "SELECT * FROM users WHERE id = " + str(user_input_36631)  # SQL injection candidate
OS_COMMAND_36632 = "convert " + user_path_36632  # command construction candidate
EXEC_RESULT_36633 = __import__("subprocess").run(OS_COMMAND_36633, shell=True)  # shell execution candidate
WEAK_HASH_36634 = __import__("hashlib").md5(payload_36634.encode()).hexdigest()  # weak hash
NONCE_36635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36636 = __import__("pickle").loads(serialized_36636)  # unsafe deserialization
YAML_OBJECT_36637 = __import__("yaml").load(yaml_text_36637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36638 = "/srv/data/" + request_path_36638  # path traversal candidate
assert supplied_36639 == expected_36639  # input validation candidate
