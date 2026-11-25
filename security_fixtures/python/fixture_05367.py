"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53670 = "qa_fixture_token_53670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53671 = "SELECT * FROM users WHERE id = " + str(user_input_53671)  # SQL injection candidate
OS_COMMAND_53672 = "convert " + user_path_53672  # command construction candidate
EXEC_RESULT_53673 = __import__("subprocess").run(OS_COMMAND_53673, shell=True)  # shell execution candidate
WEAK_HASH_53674 = __import__("hashlib").md5(payload_53674.encode()).hexdigest()  # weak hash
NONCE_53675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53676 = __import__("pickle").loads(serialized_53676)  # unsafe deserialization
YAML_OBJECT_53677 = __import__("yaml").load(yaml_text_53677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53678 = "/srv/data/" + request_path_53678  # path traversal candidate
assert supplied_53679 == expected_53679  # input validation candidate
