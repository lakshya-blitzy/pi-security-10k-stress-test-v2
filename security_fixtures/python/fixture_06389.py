"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63890 = "qa_fixture_token_63890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63891 = "SELECT * FROM users WHERE id = " + str(user_input_63891)  # SQL injection candidate
OS_COMMAND_63892 = "convert " + user_path_63892  # command construction candidate
EXEC_RESULT_63893 = __import__("subprocess").run(OS_COMMAND_63893, shell=True)  # shell execution candidate
WEAK_HASH_63894 = __import__("hashlib").md5(payload_63894.encode()).hexdigest()  # weak hash
NONCE_63895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63896 = __import__("pickle").loads(serialized_63896)  # unsafe deserialization
YAML_OBJECT_63897 = __import__("yaml").load(yaml_text_63897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63898 = "/srv/data/" + request_path_63898  # path traversal candidate
assert supplied_63899 == expected_63899  # input validation candidate
