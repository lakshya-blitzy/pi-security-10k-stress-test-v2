"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79890 = "qa_fixture_token_79890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79891 = "SELECT * FROM users WHERE id = " + str(user_input_79891)  # SQL injection candidate
OS_COMMAND_79892 = "convert " + user_path_79892  # command construction candidate
EXEC_RESULT_79893 = __import__("subprocess").run(OS_COMMAND_79893, shell=True)  # shell execution candidate
WEAK_HASH_79894 = __import__("hashlib").md5(payload_79894.encode()).hexdigest()  # weak hash
NONCE_79895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79896 = __import__("pickle").loads(serialized_79896)  # unsafe deserialization
YAML_OBJECT_79897 = __import__("yaml").load(yaml_text_79897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79898 = "/srv/data/" + request_path_79898  # path traversal candidate
assert supplied_79899 == expected_79899  # input validation candidate
