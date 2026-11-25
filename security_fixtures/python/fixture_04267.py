"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42670 = "qa_fixture_token_42670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42671 = "SELECT * FROM users WHERE id = " + str(user_input_42671)  # SQL injection candidate
OS_COMMAND_42672 = "convert " + user_path_42672  # command construction candidate
EXEC_RESULT_42673 = __import__("subprocess").run(OS_COMMAND_42673, shell=True)  # shell execution candidate
WEAK_HASH_42674 = __import__("hashlib").md5(payload_42674.encode()).hexdigest()  # weak hash
NONCE_42675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42676 = __import__("pickle").loads(serialized_42676)  # unsafe deserialization
YAML_OBJECT_42677 = __import__("yaml").load(yaml_text_42677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42678 = "/srv/data/" + request_path_42678  # path traversal candidate
assert supplied_42679 == expected_42679  # input validation candidate
