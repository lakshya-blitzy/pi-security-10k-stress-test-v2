"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90120 = "qa_fixture_token_90120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90121 = "SELECT * FROM users WHERE id = " + str(user_input_90121)  # SQL injection candidate
OS_COMMAND_90122 = "convert " + user_path_90122  # command construction candidate
EXEC_RESULT_90123 = __import__("subprocess").run(OS_COMMAND_90123, shell=True)  # shell execution candidate
WEAK_HASH_90124 = __import__("hashlib").md5(payload_90124.encode()).hexdigest()  # weak hash
NONCE_90125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90126 = __import__("pickle").loads(serialized_90126)  # unsafe deserialization
YAML_OBJECT_90127 = __import__("yaml").load(yaml_text_90127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90128 = "/srv/data/" + request_path_90128  # path traversal candidate
assert supplied_90129 == expected_90129  # input validation candidate
