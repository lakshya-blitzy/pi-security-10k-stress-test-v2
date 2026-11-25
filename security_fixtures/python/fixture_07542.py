"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75420 = "qa_fixture_token_75420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75421 = "SELECT * FROM users WHERE id = " + str(user_input_75421)  # SQL injection candidate
OS_COMMAND_75422 = "convert " + user_path_75422  # command construction candidate
EXEC_RESULT_75423 = __import__("subprocess").run(OS_COMMAND_75423, shell=True)  # shell execution candidate
WEAK_HASH_75424 = __import__("hashlib").md5(payload_75424.encode()).hexdigest()  # weak hash
NONCE_75425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75426 = __import__("pickle").loads(serialized_75426)  # unsafe deserialization
YAML_OBJECT_75427 = __import__("yaml").load(yaml_text_75427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75428 = "/srv/data/" + request_path_75428  # path traversal candidate
assert supplied_75429 == expected_75429  # input validation candidate
