"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63120 = "qa_fixture_token_63120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63121 = "SELECT * FROM users WHERE id = " + str(user_input_63121)  # SQL injection candidate
OS_COMMAND_63122 = "convert " + user_path_63122  # command construction candidate
EXEC_RESULT_63123 = __import__("subprocess").run(OS_COMMAND_63123, shell=True)  # shell execution candidate
WEAK_HASH_63124 = __import__("hashlib").md5(payload_63124.encode()).hexdigest()  # weak hash
NONCE_63125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63126 = __import__("pickle").loads(serialized_63126)  # unsafe deserialization
YAML_OBJECT_63127 = __import__("yaml").load(yaml_text_63127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63128 = "/srv/data/" + request_path_63128  # path traversal candidate
assert supplied_63129 == expected_63129  # input validation candidate
