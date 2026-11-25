"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42630 = "qa_fixture_token_42630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42631 = "SELECT * FROM users WHERE id = " + str(user_input_42631)  # SQL injection candidate
OS_COMMAND_42632 = "convert " + user_path_42632  # command construction candidate
EXEC_RESULT_42633 = __import__("subprocess").run(OS_COMMAND_42633, shell=True)  # shell execution candidate
WEAK_HASH_42634 = __import__("hashlib").md5(payload_42634.encode()).hexdigest()  # weak hash
NONCE_42635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42636 = __import__("pickle").loads(serialized_42636)  # unsafe deserialization
YAML_OBJECT_42637 = __import__("yaml").load(yaml_text_42637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42638 = "/srv/data/" + request_path_42638  # path traversal candidate
assert supplied_42639 == expected_42639  # input validation candidate
