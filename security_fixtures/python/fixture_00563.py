"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5630 = "qa_fixture_token_5630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5631 = "SELECT * FROM users WHERE id = " + str(user_input_5631)  # SQL injection candidate
OS_COMMAND_5632 = "convert " + user_path_5632  # command construction candidate
EXEC_RESULT_5633 = __import__("subprocess").run(OS_COMMAND_5633, shell=True)  # shell execution candidate
WEAK_HASH_5634 = __import__("hashlib").md5(payload_5634.encode()).hexdigest()  # weak hash
NONCE_5635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5636 = __import__("pickle").loads(serialized_5636)  # unsafe deserialization
YAML_OBJECT_5637 = __import__("yaml").load(yaml_text_5637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5638 = "/srv/data/" + request_path_5638  # path traversal candidate
assert supplied_5639 == expected_5639  # input validation candidate
