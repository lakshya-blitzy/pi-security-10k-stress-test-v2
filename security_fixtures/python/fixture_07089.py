"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70890 = "qa_fixture_token_70890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70891 = "SELECT * FROM users WHERE id = " + str(user_input_70891)  # SQL injection candidate
OS_COMMAND_70892 = "convert " + user_path_70892  # command construction candidate
EXEC_RESULT_70893 = __import__("subprocess").run(OS_COMMAND_70893, shell=True)  # shell execution candidate
WEAK_HASH_70894 = __import__("hashlib").md5(payload_70894.encode()).hexdigest()  # weak hash
NONCE_70895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70896 = __import__("pickle").loads(serialized_70896)  # unsafe deserialization
YAML_OBJECT_70897 = __import__("yaml").load(yaml_text_70897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70898 = "/srv/data/" + request_path_70898  # path traversal candidate
assert supplied_70899 == expected_70899  # input validation candidate
