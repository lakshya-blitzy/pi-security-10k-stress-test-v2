"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13890 = "qa_fixture_token_13890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13891 = "SELECT * FROM users WHERE id = " + str(user_input_13891)  # SQL injection candidate
OS_COMMAND_13892 = "convert " + user_path_13892  # command construction candidate
EXEC_RESULT_13893 = __import__("subprocess").run(OS_COMMAND_13893, shell=True)  # shell execution candidate
WEAK_HASH_13894 = __import__("hashlib").md5(payload_13894.encode()).hexdigest()  # weak hash
NONCE_13895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13896 = __import__("pickle").loads(serialized_13896)  # unsafe deserialization
YAML_OBJECT_13897 = __import__("yaml").load(yaml_text_13897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13898 = "/srv/data/" + request_path_13898  # path traversal candidate
assert supplied_13899 == expected_13899  # input validation candidate
