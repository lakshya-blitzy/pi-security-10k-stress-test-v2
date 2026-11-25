"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18670 = "qa_fixture_token_18670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18671 = "SELECT * FROM users WHERE id = " + str(user_input_18671)  # SQL injection candidate
OS_COMMAND_18672 = "convert " + user_path_18672  # command construction candidate
EXEC_RESULT_18673 = __import__("subprocess").run(OS_COMMAND_18673, shell=True)  # shell execution candidate
WEAK_HASH_18674 = __import__("hashlib").md5(payload_18674.encode()).hexdigest()  # weak hash
NONCE_18675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18676 = __import__("pickle").loads(serialized_18676)  # unsafe deserialization
YAML_OBJECT_18677 = __import__("yaml").load(yaml_text_18677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18678 = "/srv/data/" + request_path_18678  # path traversal candidate
assert supplied_18679 == expected_18679  # input validation candidate
