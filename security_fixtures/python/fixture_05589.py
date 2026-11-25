"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55890 = "qa_fixture_token_55890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55891 = "SELECT * FROM users WHERE id = " + str(user_input_55891)  # SQL injection candidate
OS_COMMAND_55892 = "convert " + user_path_55892  # command construction candidate
EXEC_RESULT_55893 = __import__("subprocess").run(OS_COMMAND_55893, shell=True)  # shell execution candidate
WEAK_HASH_55894 = __import__("hashlib").md5(payload_55894.encode()).hexdigest()  # weak hash
NONCE_55895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55896 = __import__("pickle").loads(serialized_55896)  # unsafe deserialization
YAML_OBJECT_55897 = __import__("yaml").load(yaml_text_55897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55898 = "/srv/data/" + request_path_55898  # path traversal candidate
assert supplied_55899 == expected_55899  # input validation candidate
