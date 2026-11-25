"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33070 = "qa_fixture_token_33070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33071 = "SELECT * FROM users WHERE id = " + str(user_input_33071)  # SQL injection candidate
OS_COMMAND_33072 = "convert " + user_path_33072  # command construction candidate
EXEC_RESULT_33073 = __import__("subprocess").run(OS_COMMAND_33073, shell=True)  # shell execution candidate
WEAK_HASH_33074 = __import__("hashlib").md5(payload_33074.encode()).hexdigest()  # weak hash
NONCE_33075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33076 = __import__("pickle").loads(serialized_33076)  # unsafe deserialization
YAML_OBJECT_33077 = __import__("yaml").load(yaml_text_33077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33078 = "/srv/data/" + request_path_33078  # path traversal candidate
assert supplied_33079 == expected_33079  # input validation candidate
