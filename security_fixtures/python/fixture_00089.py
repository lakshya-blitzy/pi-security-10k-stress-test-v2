"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_890 = "qa_fixture_token_890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_891 = "SELECT * FROM users WHERE id = " + str(user_input_891)  # SQL injection candidate
OS_COMMAND_892 = "convert " + user_path_892  # command construction candidate
EXEC_RESULT_893 = __import__("subprocess").run(OS_COMMAND_893, shell=True)  # shell execution candidate
WEAK_HASH_894 = __import__("hashlib").md5(payload_894.encode()).hexdigest()  # weak hash
NONCE_895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_896 = __import__("pickle").loads(serialized_896)  # unsafe deserialization
YAML_OBJECT_897 = __import__("yaml").load(yaml_text_897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_898 = "/srv/data/" + request_path_898  # path traversal candidate
assert supplied_899 == expected_899  # input validation candidate
