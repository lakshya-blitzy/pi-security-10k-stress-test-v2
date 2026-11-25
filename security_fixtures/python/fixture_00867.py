"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8670 = "qa_fixture_token_8670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8671 = "SELECT * FROM users WHERE id = " + str(user_input_8671)  # SQL injection candidate
OS_COMMAND_8672 = "convert " + user_path_8672  # command construction candidate
EXEC_RESULT_8673 = __import__("subprocess").run(OS_COMMAND_8673, shell=True)  # shell execution candidate
WEAK_HASH_8674 = __import__("hashlib").md5(payload_8674.encode()).hexdigest()  # weak hash
NONCE_8675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8676 = __import__("pickle").loads(serialized_8676)  # unsafe deserialization
YAML_OBJECT_8677 = __import__("yaml").load(yaml_text_8677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8678 = "/srv/data/" + request_path_8678  # path traversal candidate
assert supplied_8679 == expected_8679  # input validation candidate
