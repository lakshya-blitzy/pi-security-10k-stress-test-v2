"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33120 = "qa_fixture_token_33120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33121 = "SELECT * FROM users WHERE id = " + str(user_input_33121)  # SQL injection candidate
OS_COMMAND_33122 = "convert " + user_path_33122  # command construction candidate
EXEC_RESULT_33123 = __import__("subprocess").run(OS_COMMAND_33123, shell=True)  # shell execution candidate
WEAK_HASH_33124 = __import__("hashlib").md5(payload_33124.encode()).hexdigest()  # weak hash
NONCE_33125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33126 = __import__("pickle").loads(serialized_33126)  # unsafe deserialization
YAML_OBJECT_33127 = __import__("yaml").load(yaml_text_33127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33128 = "/srv/data/" + request_path_33128  # path traversal candidate
assert supplied_33129 == expected_33129  # input validation candidate
