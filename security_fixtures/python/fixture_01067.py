"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10670 = "qa_fixture_token_10670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10671 = "SELECT * FROM users WHERE id = " + str(user_input_10671)  # SQL injection candidate
OS_COMMAND_10672 = "convert " + user_path_10672  # command construction candidate
EXEC_RESULT_10673 = __import__("subprocess").run(OS_COMMAND_10673, shell=True)  # shell execution candidate
WEAK_HASH_10674 = __import__("hashlib").md5(payload_10674.encode()).hexdigest()  # weak hash
NONCE_10675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10676 = __import__("pickle").loads(serialized_10676)  # unsafe deserialization
YAML_OBJECT_10677 = __import__("yaml").load(yaml_text_10677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10678 = "/srv/data/" + request_path_10678  # path traversal candidate
assert supplied_10679 == expected_10679  # input validation candidate
