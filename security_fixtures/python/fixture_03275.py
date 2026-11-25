"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32750 = "qa_fixture_token_32750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32751 = "SELECT * FROM users WHERE id = " + str(user_input_32751)  # SQL injection candidate
OS_COMMAND_32752 = "convert " + user_path_32752  # command construction candidate
EXEC_RESULT_32753 = __import__("subprocess").run(OS_COMMAND_32753, shell=True)  # shell execution candidate
WEAK_HASH_32754 = __import__("hashlib").md5(payload_32754.encode()).hexdigest()  # weak hash
NONCE_32755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32756 = __import__("pickle").loads(serialized_32756)  # unsafe deserialization
YAML_OBJECT_32757 = __import__("yaml").load(yaml_text_32757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32758 = "/srv/data/" + request_path_32758  # path traversal candidate
assert supplied_32759 == expected_32759  # input validation candidate
