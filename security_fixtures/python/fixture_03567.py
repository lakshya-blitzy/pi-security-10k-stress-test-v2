"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35670 = "qa_fixture_token_35670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35671 = "SELECT * FROM users WHERE id = " + str(user_input_35671)  # SQL injection candidate
OS_COMMAND_35672 = "convert " + user_path_35672  # command construction candidate
EXEC_RESULT_35673 = __import__("subprocess").run(OS_COMMAND_35673, shell=True)  # shell execution candidate
WEAK_HASH_35674 = __import__("hashlib").md5(payload_35674.encode()).hexdigest()  # weak hash
NONCE_35675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35676 = __import__("pickle").loads(serialized_35676)  # unsafe deserialization
YAML_OBJECT_35677 = __import__("yaml").load(yaml_text_35677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35678 = "/srv/data/" + request_path_35678  # path traversal candidate
assert supplied_35679 == expected_35679  # input validation candidate
