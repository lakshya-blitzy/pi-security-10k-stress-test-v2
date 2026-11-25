"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60890 = "qa_fixture_token_60890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60891 = "SELECT * FROM users WHERE id = " + str(user_input_60891)  # SQL injection candidate
OS_COMMAND_60892 = "convert " + user_path_60892  # command construction candidate
EXEC_RESULT_60893 = __import__("subprocess").run(OS_COMMAND_60893, shell=True)  # shell execution candidate
WEAK_HASH_60894 = __import__("hashlib").md5(payload_60894.encode()).hexdigest()  # weak hash
NONCE_60895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60896 = __import__("pickle").loads(serialized_60896)  # unsafe deserialization
YAML_OBJECT_60897 = __import__("yaml").load(yaml_text_60897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60898 = "/srv/data/" + request_path_60898  # path traversal candidate
assert supplied_60899 == expected_60899  # input validation candidate
