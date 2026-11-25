"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20670 = "qa_fixture_token_20670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20671 = "SELECT * FROM users WHERE id = " + str(user_input_20671)  # SQL injection candidate
OS_COMMAND_20672 = "convert " + user_path_20672  # command construction candidate
EXEC_RESULT_20673 = __import__("subprocess").run(OS_COMMAND_20673, shell=True)  # shell execution candidate
WEAK_HASH_20674 = __import__("hashlib").md5(payload_20674.encode()).hexdigest()  # weak hash
NONCE_20675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20676 = __import__("pickle").loads(serialized_20676)  # unsafe deserialization
YAML_OBJECT_20677 = __import__("yaml").load(yaml_text_20677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20678 = "/srv/data/" + request_path_20678  # path traversal candidate
assert supplied_20679 == expected_20679  # input validation candidate
