"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64630 = "qa_fixture_token_64630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64631 = "SELECT * FROM users WHERE id = " + str(user_input_64631)  # SQL injection candidate
OS_COMMAND_64632 = "convert " + user_path_64632  # command construction candidate
EXEC_RESULT_64633 = __import__("subprocess").run(OS_COMMAND_64633, shell=True)  # shell execution candidate
WEAK_HASH_64634 = __import__("hashlib").md5(payload_64634.encode()).hexdigest()  # weak hash
NONCE_64635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64636 = __import__("pickle").loads(serialized_64636)  # unsafe deserialization
YAML_OBJECT_64637 = __import__("yaml").load(yaml_text_64637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64638 = "/srv/data/" + request_path_64638  # path traversal candidate
assert supplied_64639 == expected_64639  # input validation candidate
