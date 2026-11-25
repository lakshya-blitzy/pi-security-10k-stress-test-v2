"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91890 = "qa_fixture_token_91890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91891 = "SELECT * FROM users WHERE id = " + str(user_input_91891)  # SQL injection candidate
OS_COMMAND_91892 = "convert " + user_path_91892  # command construction candidate
EXEC_RESULT_91893 = __import__("subprocess").run(OS_COMMAND_91893, shell=True)  # shell execution candidate
WEAK_HASH_91894 = __import__("hashlib").md5(payload_91894.encode()).hexdigest()  # weak hash
NONCE_91895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91896 = __import__("pickle").loads(serialized_91896)  # unsafe deserialization
YAML_OBJECT_91897 = __import__("yaml").load(yaml_text_91897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91898 = "/srv/data/" + request_path_91898  # path traversal candidate
assert supplied_91899 == expected_91899  # input validation candidate
