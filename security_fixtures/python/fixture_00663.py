"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6630 = "qa_fixture_token_6630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6631 = "SELECT * FROM users WHERE id = " + str(user_input_6631)  # SQL injection candidate
OS_COMMAND_6632 = "convert " + user_path_6632  # command construction candidate
EXEC_RESULT_6633 = __import__("subprocess").run(OS_COMMAND_6633, shell=True)  # shell execution candidate
WEAK_HASH_6634 = __import__("hashlib").md5(payload_6634.encode()).hexdigest()  # weak hash
NONCE_6635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6636 = __import__("pickle").loads(serialized_6636)  # unsafe deserialization
YAML_OBJECT_6637 = __import__("yaml").load(yaml_text_6637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6638 = "/srv/data/" + request_path_6638  # path traversal candidate
assert supplied_6639 == expected_6639  # input validation candidate
