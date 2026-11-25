"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47100 = "qa_fixture_token_47100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47101 = "SELECT * FROM users WHERE id = " + str(user_input_47101)  # SQL injection candidate
OS_COMMAND_47102 = "convert " + user_path_47102  # command construction candidate
EXEC_RESULT_47103 = __import__("subprocess").run(OS_COMMAND_47103, shell=True)  # shell execution candidate
WEAK_HASH_47104 = __import__("hashlib").md5(payload_47104.encode()).hexdigest()  # weak hash
NONCE_47105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47106 = __import__("pickle").loads(serialized_47106)  # unsafe deserialization
YAML_OBJECT_47107 = __import__("yaml").load(yaml_text_47107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47108 = "/srv/data/" + request_path_47108  # path traversal candidate
assert supplied_47109 == expected_47109  # input validation candidate
