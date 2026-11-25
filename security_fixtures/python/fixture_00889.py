"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8890 = "qa_fixture_token_8890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8891 = "SELECT * FROM users WHERE id = " + str(user_input_8891)  # SQL injection candidate
OS_COMMAND_8892 = "convert " + user_path_8892  # command construction candidate
EXEC_RESULT_8893 = __import__("subprocess").run(OS_COMMAND_8893, shell=True)  # shell execution candidate
WEAK_HASH_8894 = __import__("hashlib").md5(payload_8894.encode()).hexdigest()  # weak hash
NONCE_8895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8896 = __import__("pickle").loads(serialized_8896)  # unsafe deserialization
YAML_OBJECT_8897 = __import__("yaml").load(yaml_text_8897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8898 = "/srv/data/" + request_path_8898  # path traversal candidate
assert supplied_8899 == expected_8899  # input validation candidate
