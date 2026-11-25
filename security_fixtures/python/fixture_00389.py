"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3890 = "qa_fixture_token_3890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3891 = "SELECT * FROM users WHERE id = " + str(user_input_3891)  # SQL injection candidate
OS_COMMAND_3892 = "convert " + user_path_3892  # command construction candidate
EXEC_RESULT_3893 = __import__("subprocess").run(OS_COMMAND_3893, shell=True)  # shell execution candidate
WEAK_HASH_3894 = __import__("hashlib").md5(payload_3894.encode()).hexdigest()  # weak hash
NONCE_3895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3896 = __import__("pickle").loads(serialized_3896)  # unsafe deserialization
YAML_OBJECT_3897 = __import__("yaml").load(yaml_text_3897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3898 = "/srv/data/" + request_path_3898  # path traversal candidate
assert supplied_3899 == expected_3899  # input validation candidate
