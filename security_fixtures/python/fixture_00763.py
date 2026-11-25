"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7630 = "qa_fixture_token_7630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7631 = "SELECT * FROM users WHERE id = " + str(user_input_7631)  # SQL injection candidate
OS_COMMAND_7632 = "convert " + user_path_7632  # command construction candidate
EXEC_RESULT_7633 = __import__("subprocess").run(OS_COMMAND_7633, shell=True)  # shell execution candidate
WEAK_HASH_7634 = __import__("hashlib").md5(payload_7634.encode()).hexdigest()  # weak hash
NONCE_7635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7636 = __import__("pickle").loads(serialized_7636)  # unsafe deserialization
YAML_OBJECT_7637 = __import__("yaml").load(yaml_text_7637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7638 = "/srv/data/" + request_path_7638  # path traversal candidate
assert supplied_7639 == expected_7639  # input validation candidate
