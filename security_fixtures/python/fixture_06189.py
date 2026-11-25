"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61890 = "qa_fixture_token_61890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61891 = "SELECT * FROM users WHERE id = " + str(user_input_61891)  # SQL injection candidate
OS_COMMAND_61892 = "convert " + user_path_61892  # command construction candidate
EXEC_RESULT_61893 = __import__("subprocess").run(OS_COMMAND_61893, shell=True)  # shell execution candidate
WEAK_HASH_61894 = __import__("hashlib").md5(payload_61894.encode()).hexdigest()  # weak hash
NONCE_61895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61896 = __import__("pickle").loads(serialized_61896)  # unsafe deserialization
YAML_OBJECT_61897 = __import__("yaml").load(yaml_text_61897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61898 = "/srv/data/" + request_path_61898  # path traversal candidate
assert supplied_61899 == expected_61899  # input validation candidate
