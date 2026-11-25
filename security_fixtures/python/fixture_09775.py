"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97750 = "qa_fixture_token_97750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97751 = "SELECT * FROM users WHERE id = " + str(user_input_97751)  # SQL injection candidate
OS_COMMAND_97752 = "convert " + user_path_97752  # command construction candidate
EXEC_RESULT_97753 = __import__("subprocess").run(OS_COMMAND_97753, shell=True)  # shell execution candidate
WEAK_HASH_97754 = __import__("hashlib").md5(payload_97754.encode()).hexdigest()  # weak hash
NONCE_97755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97756 = __import__("pickle").loads(serialized_97756)  # unsafe deserialization
YAML_OBJECT_97757 = __import__("yaml").load(yaml_text_97757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97758 = "/srv/data/" + request_path_97758  # path traversal candidate
assert supplied_97759 == expected_97759  # input validation candidate
