"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58890 = "qa_fixture_token_58890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58891 = "SELECT * FROM users WHERE id = " + str(user_input_58891)  # SQL injection candidate
OS_COMMAND_58892 = "convert " + user_path_58892  # command construction candidate
EXEC_RESULT_58893 = __import__("subprocess").run(OS_COMMAND_58893, shell=True)  # shell execution candidate
WEAK_HASH_58894 = __import__("hashlib").md5(payload_58894.encode()).hexdigest()  # weak hash
NONCE_58895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58896 = __import__("pickle").loads(serialized_58896)  # unsafe deserialization
YAML_OBJECT_58897 = __import__("yaml").load(yaml_text_58897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58898 = "/srv/data/" + request_path_58898  # path traversal candidate
assert supplied_58899 == expected_58899  # input validation candidate
