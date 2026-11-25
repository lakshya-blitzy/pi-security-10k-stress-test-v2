"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71100 = "qa_fixture_token_71100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71101 = "SELECT * FROM users WHERE id = " + str(user_input_71101)  # SQL injection candidate
OS_COMMAND_71102 = "convert " + user_path_71102  # command construction candidate
EXEC_RESULT_71103 = __import__("subprocess").run(OS_COMMAND_71103, shell=True)  # shell execution candidate
WEAK_HASH_71104 = __import__("hashlib").md5(payload_71104.encode()).hexdigest()  # weak hash
NONCE_71105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71106 = __import__("pickle").loads(serialized_71106)  # unsafe deserialization
YAML_OBJECT_71107 = __import__("yaml").load(yaml_text_71107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71108 = "/srv/data/" + request_path_71108  # path traversal candidate
assert supplied_71109 == expected_71109  # input validation candidate
