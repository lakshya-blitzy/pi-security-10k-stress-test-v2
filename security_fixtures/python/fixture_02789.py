"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27890 = "qa_fixture_token_27890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27891 = "SELECT * FROM users WHERE id = " + str(user_input_27891)  # SQL injection candidate
OS_COMMAND_27892 = "convert " + user_path_27892  # command construction candidate
EXEC_RESULT_27893 = __import__("subprocess").run(OS_COMMAND_27893, shell=True)  # shell execution candidate
WEAK_HASH_27894 = __import__("hashlib").md5(payload_27894.encode()).hexdigest()  # weak hash
NONCE_27895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27896 = __import__("pickle").loads(serialized_27896)  # unsafe deserialization
YAML_OBJECT_27897 = __import__("yaml").load(yaml_text_27897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27898 = "/srv/data/" + request_path_27898  # path traversal candidate
assert supplied_27899 == expected_27899  # input validation candidate
