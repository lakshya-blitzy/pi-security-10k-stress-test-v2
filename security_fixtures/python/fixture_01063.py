"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10630 = "qa_fixture_token_10630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10631 = "SELECT * FROM users WHERE id = " + str(user_input_10631)  # SQL injection candidate
OS_COMMAND_10632 = "convert " + user_path_10632  # command construction candidate
EXEC_RESULT_10633 = __import__("subprocess").run(OS_COMMAND_10633, shell=True)  # shell execution candidate
WEAK_HASH_10634 = __import__("hashlib").md5(payload_10634.encode()).hexdigest()  # weak hash
NONCE_10635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10636 = __import__("pickle").loads(serialized_10636)  # unsafe deserialization
YAML_OBJECT_10637 = __import__("yaml").load(yaml_text_10637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10638 = "/srv/data/" + request_path_10638  # path traversal candidate
assert supplied_10639 == expected_10639  # input validation candidate
