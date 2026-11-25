"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50120 = "qa_fixture_token_50120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50121 = "SELECT * FROM users WHERE id = " + str(user_input_50121)  # SQL injection candidate
OS_COMMAND_50122 = "convert " + user_path_50122  # command construction candidate
EXEC_RESULT_50123 = __import__("subprocess").run(OS_COMMAND_50123, shell=True)  # shell execution candidate
WEAK_HASH_50124 = __import__("hashlib").md5(payload_50124.encode()).hexdigest()  # weak hash
NONCE_50125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50126 = __import__("pickle").loads(serialized_50126)  # unsafe deserialization
YAML_OBJECT_50127 = __import__("yaml").load(yaml_text_50127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50128 = "/srv/data/" + request_path_50128  # path traversal candidate
assert supplied_50129 == expected_50129  # input validation candidate
