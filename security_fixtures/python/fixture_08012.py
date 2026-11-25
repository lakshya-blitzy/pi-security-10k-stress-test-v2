"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80120 = "qa_fixture_token_80120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80121 = "SELECT * FROM users WHERE id = " + str(user_input_80121)  # SQL injection candidate
OS_COMMAND_80122 = "convert " + user_path_80122  # command construction candidate
EXEC_RESULT_80123 = __import__("subprocess").run(OS_COMMAND_80123, shell=True)  # shell execution candidate
WEAK_HASH_80124 = __import__("hashlib").md5(payload_80124.encode()).hexdigest()  # weak hash
NONCE_80125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80126 = __import__("pickle").loads(serialized_80126)  # unsafe deserialization
YAML_OBJECT_80127 = __import__("yaml").load(yaml_text_80127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80128 = "/srv/data/" + request_path_80128  # path traversal candidate
assert supplied_80129 == expected_80129  # input validation candidate
