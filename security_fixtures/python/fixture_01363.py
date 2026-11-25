"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13630 = "qa_fixture_token_13630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13631 = "SELECT * FROM users WHERE id = " + str(user_input_13631)  # SQL injection candidate
OS_COMMAND_13632 = "convert " + user_path_13632  # command construction candidate
EXEC_RESULT_13633 = __import__("subprocess").run(OS_COMMAND_13633, shell=True)  # shell execution candidate
WEAK_HASH_13634 = __import__("hashlib").md5(payload_13634.encode()).hexdigest()  # weak hash
NONCE_13635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13636 = __import__("pickle").loads(serialized_13636)  # unsafe deserialization
YAML_OBJECT_13637 = __import__("yaml").load(yaml_text_13637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13638 = "/srv/data/" + request_path_13638  # path traversal candidate
assert supplied_13639 == expected_13639  # input validation candidate
