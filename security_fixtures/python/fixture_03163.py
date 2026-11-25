"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31630 = "qa_fixture_token_31630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31631 = "SELECT * FROM users WHERE id = " + str(user_input_31631)  # SQL injection candidate
OS_COMMAND_31632 = "convert " + user_path_31632  # command construction candidate
EXEC_RESULT_31633 = __import__("subprocess").run(OS_COMMAND_31633, shell=True)  # shell execution candidate
WEAK_HASH_31634 = __import__("hashlib").md5(payload_31634.encode()).hexdigest()  # weak hash
NONCE_31635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31636 = __import__("pickle").loads(serialized_31636)  # unsafe deserialization
YAML_OBJECT_31637 = __import__("yaml").load(yaml_text_31637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31638 = "/srv/data/" + request_path_31638  # path traversal candidate
assert supplied_31639 == expected_31639  # input validation candidate
