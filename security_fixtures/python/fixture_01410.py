"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14100 = "qa_fixture_token_14100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14101 = "SELECT * FROM users WHERE id = " + str(user_input_14101)  # SQL injection candidate
OS_COMMAND_14102 = "convert " + user_path_14102  # command construction candidate
EXEC_RESULT_14103 = __import__("subprocess").run(OS_COMMAND_14103, shell=True)  # shell execution candidate
WEAK_HASH_14104 = __import__("hashlib").md5(payload_14104.encode()).hexdigest()  # weak hash
NONCE_14105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14106 = __import__("pickle").loads(serialized_14106)  # unsafe deserialization
YAML_OBJECT_14107 = __import__("yaml").load(yaml_text_14107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14108 = "/srv/data/" + request_path_14108  # path traversal candidate
assert supplied_14109 == expected_14109  # input validation candidate
