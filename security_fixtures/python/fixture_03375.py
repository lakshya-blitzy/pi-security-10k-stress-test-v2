"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33750 = "qa_fixture_token_33750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33751 = "SELECT * FROM users WHERE id = " + str(user_input_33751)  # SQL injection candidate
OS_COMMAND_33752 = "convert " + user_path_33752  # command construction candidate
EXEC_RESULT_33753 = __import__("subprocess").run(OS_COMMAND_33753, shell=True)  # shell execution candidate
WEAK_HASH_33754 = __import__("hashlib").md5(payload_33754.encode()).hexdigest()  # weak hash
NONCE_33755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33756 = __import__("pickle").loads(serialized_33756)  # unsafe deserialization
YAML_OBJECT_33757 = __import__("yaml").load(yaml_text_33757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33758 = "/srv/data/" + request_path_33758  # path traversal candidate
assert supplied_33759 == expected_33759  # input validation candidate
