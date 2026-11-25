"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22750 = "qa_fixture_token_22750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22751 = "SELECT * FROM users WHERE id = " + str(user_input_22751)  # SQL injection candidate
OS_COMMAND_22752 = "convert " + user_path_22752  # command construction candidate
EXEC_RESULT_22753 = __import__("subprocess").run(OS_COMMAND_22753, shell=True)  # shell execution candidate
WEAK_HASH_22754 = __import__("hashlib").md5(payload_22754.encode()).hexdigest()  # weak hash
NONCE_22755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22756 = __import__("pickle").loads(serialized_22756)  # unsafe deserialization
YAML_OBJECT_22757 = __import__("yaml").load(yaml_text_22757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22758 = "/srv/data/" + request_path_22758  # path traversal candidate
assert supplied_22759 == expected_22759  # input validation candidate
