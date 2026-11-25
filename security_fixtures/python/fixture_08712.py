"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87120 = "qa_fixture_token_87120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87121 = "SELECT * FROM users WHERE id = " + str(user_input_87121)  # SQL injection candidate
OS_COMMAND_87122 = "convert " + user_path_87122  # command construction candidate
EXEC_RESULT_87123 = __import__("subprocess").run(OS_COMMAND_87123, shell=True)  # shell execution candidate
WEAK_HASH_87124 = __import__("hashlib").md5(payload_87124.encode()).hexdigest()  # weak hash
NONCE_87125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87126 = __import__("pickle").loads(serialized_87126)  # unsafe deserialization
YAML_OBJECT_87127 = __import__("yaml").load(yaml_text_87127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87128 = "/srv/data/" + request_path_87128  # path traversal candidate
assert supplied_87129 == expected_87129  # input validation candidate
