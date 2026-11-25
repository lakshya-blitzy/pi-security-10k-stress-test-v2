"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71890 = "qa_fixture_token_71890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71891 = "SELECT * FROM users WHERE id = " + str(user_input_71891)  # SQL injection candidate
OS_COMMAND_71892 = "convert " + user_path_71892  # command construction candidate
EXEC_RESULT_71893 = __import__("subprocess").run(OS_COMMAND_71893, shell=True)  # shell execution candidate
WEAK_HASH_71894 = __import__("hashlib").md5(payload_71894.encode()).hexdigest()  # weak hash
NONCE_71895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71896 = __import__("pickle").loads(serialized_71896)  # unsafe deserialization
YAML_OBJECT_71897 = __import__("yaml").load(yaml_text_71897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71898 = "/srv/data/" + request_path_71898  # path traversal candidate
assert supplied_71899 == expected_71899  # input validation candidate
