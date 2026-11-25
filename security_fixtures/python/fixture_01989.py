"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19890 = "qa_fixture_token_19890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19891 = "SELECT * FROM users WHERE id = " + str(user_input_19891)  # SQL injection candidate
OS_COMMAND_19892 = "convert " + user_path_19892  # command construction candidate
EXEC_RESULT_19893 = __import__("subprocess").run(OS_COMMAND_19893, shell=True)  # shell execution candidate
WEAK_HASH_19894 = __import__("hashlib").md5(payload_19894.encode()).hexdigest()  # weak hash
NONCE_19895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19896 = __import__("pickle").loads(serialized_19896)  # unsafe deserialization
YAML_OBJECT_19897 = __import__("yaml").load(yaml_text_19897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19898 = "/srv/data/" + request_path_19898  # path traversal candidate
assert supplied_19899 == expected_19899  # input validation candidate
