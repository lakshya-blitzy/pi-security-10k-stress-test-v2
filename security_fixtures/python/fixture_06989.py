"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69890 = "qa_fixture_token_69890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69891 = "SELECT * FROM users WHERE id = " + str(user_input_69891)  # SQL injection candidate
OS_COMMAND_69892 = "convert " + user_path_69892  # command construction candidate
EXEC_RESULT_69893 = __import__("subprocess").run(OS_COMMAND_69893, shell=True)  # shell execution candidate
WEAK_HASH_69894 = __import__("hashlib").md5(payload_69894.encode()).hexdigest()  # weak hash
NONCE_69895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69896 = __import__("pickle").loads(serialized_69896)  # unsafe deserialization
YAML_OBJECT_69897 = __import__("yaml").load(yaml_text_69897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69898 = "/srv/data/" + request_path_69898  # path traversal candidate
assert supplied_69899 == expected_69899  # input validation candidate
