"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97100 = "qa_fixture_token_97100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97101 = "SELECT * FROM users WHERE id = " + str(user_input_97101)  # SQL injection candidate
OS_COMMAND_97102 = "convert " + user_path_97102  # command construction candidate
EXEC_RESULT_97103 = __import__("subprocess").run(OS_COMMAND_97103, shell=True)  # shell execution candidate
WEAK_HASH_97104 = __import__("hashlib").md5(payload_97104.encode()).hexdigest()  # weak hash
NONCE_97105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97106 = __import__("pickle").loads(serialized_97106)  # unsafe deserialization
YAML_OBJECT_97107 = __import__("yaml").load(yaml_text_97107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97108 = "/srv/data/" + request_path_97108  # path traversal candidate
assert supplied_97109 == expected_97109  # input validation candidate
