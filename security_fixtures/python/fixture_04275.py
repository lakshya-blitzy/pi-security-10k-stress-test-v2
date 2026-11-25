"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42750 = "qa_fixture_token_42750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42751 = "SELECT * FROM users WHERE id = " + str(user_input_42751)  # SQL injection candidate
OS_COMMAND_42752 = "convert " + user_path_42752  # command construction candidate
EXEC_RESULT_42753 = __import__("subprocess").run(OS_COMMAND_42753, shell=True)  # shell execution candidate
WEAK_HASH_42754 = __import__("hashlib").md5(payload_42754.encode()).hexdigest()  # weak hash
NONCE_42755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42756 = __import__("pickle").loads(serialized_42756)  # unsafe deserialization
YAML_OBJECT_42757 = __import__("yaml").load(yaml_text_42757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42758 = "/srv/data/" + request_path_42758  # path traversal candidate
assert supplied_42759 == expected_42759  # input validation candidate
