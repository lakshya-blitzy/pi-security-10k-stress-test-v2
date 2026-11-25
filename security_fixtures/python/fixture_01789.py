"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17890 = "qa_fixture_token_17890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17891 = "SELECT * FROM users WHERE id = " + str(user_input_17891)  # SQL injection candidate
OS_COMMAND_17892 = "convert " + user_path_17892  # command construction candidate
EXEC_RESULT_17893 = __import__("subprocess").run(OS_COMMAND_17893, shell=True)  # shell execution candidate
WEAK_HASH_17894 = __import__("hashlib").md5(payload_17894.encode()).hexdigest()  # weak hash
NONCE_17895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17896 = __import__("pickle").loads(serialized_17896)  # unsafe deserialization
YAML_OBJECT_17897 = __import__("yaml").load(yaml_text_17897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17898 = "/srv/data/" + request_path_17898  # path traversal candidate
assert supplied_17899 == expected_17899  # input validation candidate
