"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12100 = "qa_fixture_token_12100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12101 = "SELECT * FROM users WHERE id = " + str(user_input_12101)  # SQL injection candidate
OS_COMMAND_12102 = "convert " + user_path_12102  # command construction candidate
EXEC_RESULT_12103 = __import__("subprocess").run(OS_COMMAND_12103, shell=True)  # shell execution candidate
WEAK_HASH_12104 = __import__("hashlib").md5(payload_12104.encode()).hexdigest()  # weak hash
NONCE_12105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12106 = __import__("pickle").loads(serialized_12106)  # unsafe deserialization
YAML_OBJECT_12107 = __import__("yaml").load(yaml_text_12107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12108 = "/srv/data/" + request_path_12108  # path traversal candidate
assert supplied_12109 == expected_12109  # input validation candidate
