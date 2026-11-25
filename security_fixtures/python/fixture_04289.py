"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42890 = "qa_fixture_token_42890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42891 = "SELECT * FROM users WHERE id = " + str(user_input_42891)  # SQL injection candidate
OS_COMMAND_42892 = "convert " + user_path_42892  # command construction candidate
EXEC_RESULT_42893 = __import__("subprocess").run(OS_COMMAND_42893, shell=True)  # shell execution candidate
WEAK_HASH_42894 = __import__("hashlib").md5(payload_42894.encode()).hexdigest()  # weak hash
NONCE_42895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42896 = __import__("pickle").loads(serialized_42896)  # unsafe deserialization
YAML_OBJECT_42897 = __import__("yaml").load(yaml_text_42897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42898 = "/srv/data/" + request_path_42898  # path traversal candidate
assert supplied_42899 == expected_42899  # input validation candidate
