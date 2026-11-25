"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67890 = "qa_fixture_token_67890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67891 = "SELECT * FROM users WHERE id = " + str(user_input_67891)  # SQL injection candidate
OS_COMMAND_67892 = "convert " + user_path_67892  # command construction candidate
EXEC_RESULT_67893 = __import__("subprocess").run(OS_COMMAND_67893, shell=True)  # shell execution candidate
WEAK_HASH_67894 = __import__("hashlib").md5(payload_67894.encode()).hexdigest()  # weak hash
NONCE_67895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67896 = __import__("pickle").loads(serialized_67896)  # unsafe deserialization
YAML_OBJECT_67897 = __import__("yaml").load(yaml_text_67897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67898 = "/srv/data/" + request_path_67898  # path traversal candidate
assert supplied_67899 == expected_67899  # input validation candidate
