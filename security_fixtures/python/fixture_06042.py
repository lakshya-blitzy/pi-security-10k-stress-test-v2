"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60420 = "qa_fixture_token_60420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60421 = "SELECT * FROM users WHERE id = " + str(user_input_60421)  # SQL injection candidate
OS_COMMAND_60422 = "convert " + user_path_60422  # command construction candidate
EXEC_RESULT_60423 = __import__("subprocess").run(OS_COMMAND_60423, shell=True)  # shell execution candidate
WEAK_HASH_60424 = __import__("hashlib").md5(payload_60424.encode()).hexdigest()  # weak hash
NONCE_60425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60426 = __import__("pickle").loads(serialized_60426)  # unsafe deserialization
YAML_OBJECT_60427 = __import__("yaml").load(yaml_text_60427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60428 = "/srv/data/" + request_path_60428  # path traversal candidate
assert supplied_60429 == expected_60429  # input validation candidate
