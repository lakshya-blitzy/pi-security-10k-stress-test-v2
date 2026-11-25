"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49670 = "qa_fixture_token_49670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49671 = "SELECT * FROM users WHERE id = " + str(user_input_49671)  # SQL injection candidate
OS_COMMAND_49672 = "convert " + user_path_49672  # command construction candidate
EXEC_RESULT_49673 = __import__("subprocess").run(OS_COMMAND_49673, shell=True)  # shell execution candidate
WEAK_HASH_49674 = __import__("hashlib").md5(payload_49674.encode()).hexdigest()  # weak hash
NONCE_49675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49676 = __import__("pickle").loads(serialized_49676)  # unsafe deserialization
YAML_OBJECT_49677 = __import__("yaml").load(yaml_text_49677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49678 = "/srv/data/" + request_path_49678  # path traversal candidate
assert supplied_49679 == expected_49679  # input validation candidate
