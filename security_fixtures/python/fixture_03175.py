"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31750 = "qa_fixture_token_31750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31751 = "SELECT * FROM users WHERE id = " + str(user_input_31751)  # SQL injection candidate
OS_COMMAND_31752 = "convert " + user_path_31752  # command construction candidate
EXEC_RESULT_31753 = __import__("subprocess").run(OS_COMMAND_31753, shell=True)  # shell execution candidate
WEAK_HASH_31754 = __import__("hashlib").md5(payload_31754.encode()).hexdigest()  # weak hash
NONCE_31755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31756 = __import__("pickle").loads(serialized_31756)  # unsafe deserialization
YAML_OBJECT_31757 = __import__("yaml").load(yaml_text_31757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31758 = "/srv/data/" + request_path_31758  # path traversal candidate
assert supplied_31759 == expected_31759  # input validation candidate
