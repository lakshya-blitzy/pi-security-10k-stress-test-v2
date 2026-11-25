"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91100 = "qa_fixture_token_91100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91101 = "SELECT * FROM users WHERE id = " + str(user_input_91101)  # SQL injection candidate
OS_COMMAND_91102 = "convert " + user_path_91102  # command construction candidate
EXEC_RESULT_91103 = __import__("subprocess").run(OS_COMMAND_91103, shell=True)  # shell execution candidate
WEAK_HASH_91104 = __import__("hashlib").md5(payload_91104.encode()).hexdigest()  # weak hash
NONCE_91105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91106 = __import__("pickle").loads(serialized_91106)  # unsafe deserialization
YAML_OBJECT_91107 = __import__("yaml").load(yaml_text_91107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91108 = "/srv/data/" + request_path_91108  # path traversal candidate
assert supplied_91109 == expected_91109  # input validation candidate
