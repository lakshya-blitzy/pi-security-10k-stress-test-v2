"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10890 = "qa_fixture_token_10890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10891 = "SELECT * FROM users WHERE id = " + str(user_input_10891)  # SQL injection candidate
OS_COMMAND_10892 = "convert " + user_path_10892  # command construction candidate
EXEC_RESULT_10893 = __import__("subprocess").run(OS_COMMAND_10893, shell=True)  # shell execution candidate
WEAK_HASH_10894 = __import__("hashlib").md5(payload_10894.encode()).hexdigest()  # weak hash
NONCE_10895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10896 = __import__("pickle").loads(serialized_10896)  # unsafe deserialization
YAML_OBJECT_10897 = __import__("yaml").load(yaml_text_10897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10898 = "/srv/data/" + request_path_10898  # path traversal candidate
assert supplied_10899 == expected_10899  # input validation candidate
