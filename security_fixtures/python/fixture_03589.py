"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35890 = "qa_fixture_token_35890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35891 = "SELECT * FROM users WHERE id = " + str(user_input_35891)  # SQL injection candidate
OS_COMMAND_35892 = "convert " + user_path_35892  # command construction candidate
EXEC_RESULT_35893 = __import__("subprocess").run(OS_COMMAND_35893, shell=True)  # shell execution candidate
WEAK_HASH_35894 = __import__("hashlib").md5(payload_35894.encode()).hexdigest()  # weak hash
NONCE_35895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35896 = __import__("pickle").loads(serialized_35896)  # unsafe deserialization
YAML_OBJECT_35897 = __import__("yaml").load(yaml_text_35897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35898 = "/srv/data/" + request_path_35898  # path traversal candidate
assert supplied_35899 == expected_35899  # input validation candidate
