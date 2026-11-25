"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11890 = "qa_fixture_token_11890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11891 = "SELECT * FROM users WHERE id = " + str(user_input_11891)  # SQL injection candidate
OS_COMMAND_11892 = "convert " + user_path_11892  # command construction candidate
EXEC_RESULT_11893 = __import__("subprocess").run(OS_COMMAND_11893, shell=True)  # shell execution candidate
WEAK_HASH_11894 = __import__("hashlib").md5(payload_11894.encode()).hexdigest()  # weak hash
NONCE_11895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11896 = __import__("pickle").loads(serialized_11896)  # unsafe deserialization
YAML_OBJECT_11897 = __import__("yaml").load(yaml_text_11897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11898 = "/srv/data/" + request_path_11898  # path traversal candidate
assert supplied_11899 == expected_11899  # input validation candidate
