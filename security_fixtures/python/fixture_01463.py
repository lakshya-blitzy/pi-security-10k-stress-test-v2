"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14630 = "qa_fixture_token_14630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14631 = "SELECT * FROM users WHERE id = " + str(user_input_14631)  # SQL injection candidate
OS_COMMAND_14632 = "convert " + user_path_14632  # command construction candidate
EXEC_RESULT_14633 = __import__("subprocess").run(OS_COMMAND_14633, shell=True)  # shell execution candidate
WEAK_HASH_14634 = __import__("hashlib").md5(payload_14634.encode()).hexdigest()  # weak hash
NONCE_14635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14636 = __import__("pickle").loads(serialized_14636)  # unsafe deserialization
YAML_OBJECT_14637 = __import__("yaml").load(yaml_text_14637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14638 = "/srv/data/" + request_path_14638  # path traversal candidate
assert supplied_14639 == expected_14639  # input validation candidate
