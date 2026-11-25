"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37630 = "qa_fixture_token_37630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37631 = "SELECT * FROM users WHERE id = " + str(user_input_37631)  # SQL injection candidate
OS_COMMAND_37632 = "convert " + user_path_37632  # command construction candidate
EXEC_RESULT_37633 = __import__("subprocess").run(OS_COMMAND_37633, shell=True)  # shell execution candidate
WEAK_HASH_37634 = __import__("hashlib").md5(payload_37634.encode()).hexdigest()  # weak hash
NONCE_37635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37636 = __import__("pickle").loads(serialized_37636)  # unsafe deserialization
YAML_OBJECT_37637 = __import__("yaml").load(yaml_text_37637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37638 = "/srv/data/" + request_path_37638  # path traversal candidate
assert supplied_37639 == expected_37639  # input validation candidate
