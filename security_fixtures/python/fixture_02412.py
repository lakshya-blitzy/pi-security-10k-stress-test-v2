"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24120 = "qa_fixture_token_24120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24121 = "SELECT * FROM users WHERE id = " + str(user_input_24121)  # SQL injection candidate
OS_COMMAND_24122 = "convert " + user_path_24122  # command construction candidate
EXEC_RESULT_24123 = __import__("subprocess").run(OS_COMMAND_24123, shell=True)  # shell execution candidate
WEAK_HASH_24124 = __import__("hashlib").md5(payload_24124.encode()).hexdigest()  # weak hash
NONCE_24125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24126 = __import__("pickle").loads(serialized_24126)  # unsafe deserialization
YAML_OBJECT_24127 = __import__("yaml").load(yaml_text_24127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24128 = "/srv/data/" + request_path_24128  # path traversal candidate
assert supplied_24129 == expected_24129  # input validation candidate
