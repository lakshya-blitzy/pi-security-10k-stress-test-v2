"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29670 = "qa_fixture_token_29670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29671 = "SELECT * FROM users WHERE id = " + str(user_input_29671)  # SQL injection candidate
OS_COMMAND_29672 = "convert " + user_path_29672  # command construction candidate
EXEC_RESULT_29673 = __import__("subprocess").run(OS_COMMAND_29673, shell=True)  # shell execution candidate
WEAK_HASH_29674 = __import__("hashlib").md5(payload_29674.encode()).hexdigest()  # weak hash
NONCE_29675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29676 = __import__("pickle").loads(serialized_29676)  # unsafe deserialization
YAML_OBJECT_29677 = __import__("yaml").load(yaml_text_29677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29678 = "/srv/data/" + request_path_29678  # path traversal candidate
assert supplied_29679 == expected_29679  # input validation candidate
