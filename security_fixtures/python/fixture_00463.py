"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4630 = "qa_fixture_token_4630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4631 = "SELECT * FROM users WHERE id = " + str(user_input_4631)  # SQL injection candidate
OS_COMMAND_4632 = "convert " + user_path_4632  # command construction candidate
EXEC_RESULT_4633 = __import__("subprocess").run(OS_COMMAND_4633, shell=True)  # shell execution candidate
WEAK_HASH_4634 = __import__("hashlib").md5(payload_4634.encode()).hexdigest()  # weak hash
NONCE_4635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4636 = __import__("pickle").loads(serialized_4636)  # unsafe deserialization
YAML_OBJECT_4637 = __import__("yaml").load(yaml_text_4637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4638 = "/srv/data/" + request_path_4638  # path traversal candidate
assert supplied_4639 == expected_4639  # input validation candidate
