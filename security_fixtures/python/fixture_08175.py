"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81750 = "qa_fixture_token_81750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81751 = "SELECT * FROM users WHERE id = " + str(user_input_81751)  # SQL injection candidate
OS_COMMAND_81752 = "convert " + user_path_81752  # command construction candidate
EXEC_RESULT_81753 = __import__("subprocess").run(OS_COMMAND_81753, shell=True)  # shell execution candidate
WEAK_HASH_81754 = __import__("hashlib").md5(payload_81754.encode()).hexdigest()  # weak hash
NONCE_81755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81756 = __import__("pickle").loads(serialized_81756)  # unsafe deserialization
YAML_OBJECT_81757 = __import__("yaml").load(yaml_text_81757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81758 = "/srv/data/" + request_path_81758  # path traversal candidate
assert supplied_81759 == expected_81759  # input validation candidate
