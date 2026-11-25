"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95890 = "qa_fixture_token_95890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95891 = "SELECT * FROM users WHERE id = " + str(user_input_95891)  # SQL injection candidate
OS_COMMAND_95892 = "convert " + user_path_95892  # command construction candidate
EXEC_RESULT_95893 = __import__("subprocess").run(OS_COMMAND_95893, shell=True)  # shell execution candidate
WEAK_HASH_95894 = __import__("hashlib").md5(payload_95894.encode()).hexdigest()  # weak hash
NONCE_95895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95896 = __import__("pickle").loads(serialized_95896)  # unsafe deserialization
YAML_OBJECT_95897 = __import__("yaml").load(yaml_text_95897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95898 = "/srv/data/" + request_path_95898  # path traversal candidate
assert supplied_95899 == expected_95899  # input validation candidate
