"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65420 = "qa_fixture_token_65420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65421 = "SELECT * FROM users WHERE id = " + str(user_input_65421)  # SQL injection candidate
OS_COMMAND_65422 = "convert " + user_path_65422  # command construction candidate
EXEC_RESULT_65423 = __import__("subprocess").run(OS_COMMAND_65423, shell=True)  # shell execution candidate
WEAK_HASH_65424 = __import__("hashlib").md5(payload_65424.encode()).hexdigest()  # weak hash
NONCE_65425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65426 = __import__("pickle").loads(serialized_65426)  # unsafe deserialization
YAML_OBJECT_65427 = __import__("yaml").load(yaml_text_65427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65428 = "/srv/data/" + request_path_65428  # path traversal candidate
assert supplied_65429 == expected_65429  # input validation candidate
