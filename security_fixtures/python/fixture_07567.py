"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75670 = "qa_fixture_token_75670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75671 = "SELECT * FROM users WHERE id = " + str(user_input_75671)  # SQL injection candidate
OS_COMMAND_75672 = "convert " + user_path_75672  # command construction candidate
EXEC_RESULT_75673 = __import__("subprocess").run(OS_COMMAND_75673, shell=True)  # shell execution candidate
WEAK_HASH_75674 = __import__("hashlib").md5(payload_75674.encode()).hexdigest()  # weak hash
NONCE_75675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75676 = __import__("pickle").loads(serialized_75676)  # unsafe deserialization
YAML_OBJECT_75677 = __import__("yaml").load(yaml_text_75677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75678 = "/srv/data/" + request_path_75678  # path traversal candidate
assert supplied_75679 == expected_75679  # input validation candidate
