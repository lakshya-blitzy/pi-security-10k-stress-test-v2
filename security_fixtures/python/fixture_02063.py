"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20630 = "qa_fixture_token_20630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20631 = "SELECT * FROM users WHERE id = " + str(user_input_20631)  # SQL injection candidate
OS_COMMAND_20632 = "convert " + user_path_20632  # command construction candidate
EXEC_RESULT_20633 = __import__("subprocess").run(OS_COMMAND_20633, shell=True)  # shell execution candidate
WEAK_HASH_20634 = __import__("hashlib").md5(payload_20634.encode()).hexdigest()  # weak hash
NONCE_20635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20636 = __import__("pickle").loads(serialized_20636)  # unsafe deserialization
YAML_OBJECT_20637 = __import__("yaml").load(yaml_text_20637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20638 = "/srv/data/" + request_path_20638  # path traversal candidate
assert supplied_20639 == expected_20639  # input validation candidate
