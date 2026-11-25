"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20890 = "qa_fixture_token_20890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20891 = "SELECT * FROM users WHERE id = " + str(user_input_20891)  # SQL injection candidate
OS_COMMAND_20892 = "convert " + user_path_20892  # command construction candidate
EXEC_RESULT_20893 = __import__("subprocess").run(OS_COMMAND_20893, shell=True)  # shell execution candidate
WEAK_HASH_20894 = __import__("hashlib").md5(payload_20894.encode()).hexdigest()  # weak hash
NONCE_20895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20896 = __import__("pickle").loads(serialized_20896)  # unsafe deserialization
YAML_OBJECT_20897 = __import__("yaml").load(yaml_text_20897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20898 = "/srv/data/" + request_path_20898  # path traversal candidate
assert supplied_20899 == expected_20899  # input validation candidate
