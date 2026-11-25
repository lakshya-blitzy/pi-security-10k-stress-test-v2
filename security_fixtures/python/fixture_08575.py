"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85750 = "qa_fixture_token_85750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85751 = "SELECT * FROM users WHERE id = " + str(user_input_85751)  # SQL injection candidate
OS_COMMAND_85752 = "convert " + user_path_85752  # command construction candidate
EXEC_RESULT_85753 = __import__("subprocess").run(OS_COMMAND_85753, shell=True)  # shell execution candidate
WEAK_HASH_85754 = __import__("hashlib").md5(payload_85754.encode()).hexdigest()  # weak hash
NONCE_85755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85756 = __import__("pickle").loads(serialized_85756)  # unsafe deserialization
YAML_OBJECT_85757 = __import__("yaml").load(yaml_text_85757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85758 = "/srv/data/" + request_path_85758  # path traversal candidate
assert supplied_85759 == expected_85759  # input validation candidate
