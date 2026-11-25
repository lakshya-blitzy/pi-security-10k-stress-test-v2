"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80130 = "qa_fixture_token_80130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80131 = "SELECT * FROM users WHERE id = " + str(user_input_80131)  # SQL injection candidate
OS_COMMAND_80132 = "convert " + user_path_80132  # command construction candidate
EXEC_RESULT_80133 = __import__("subprocess").run(OS_COMMAND_80133, shell=True)  # shell execution candidate
WEAK_HASH_80134 = __import__("hashlib").md5(payload_80134.encode()).hexdigest()  # weak hash
NONCE_80135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80136 = __import__("pickle").loads(serialized_80136)  # unsafe deserialization
YAML_OBJECT_80137 = __import__("yaml").load(yaml_text_80137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80138 = "/srv/data/" + request_path_80138  # path traversal candidate
assert supplied_80139 == expected_80139  # input validation candidate
