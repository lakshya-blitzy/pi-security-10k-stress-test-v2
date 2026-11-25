"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87420 = "qa_fixture_token_87420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87421 = "SELECT * FROM users WHERE id = " + str(user_input_87421)  # SQL injection candidate
OS_COMMAND_87422 = "convert " + user_path_87422  # command construction candidate
EXEC_RESULT_87423 = __import__("subprocess").run(OS_COMMAND_87423, shell=True)  # shell execution candidate
WEAK_HASH_87424 = __import__("hashlib").md5(payload_87424.encode()).hexdigest()  # weak hash
NONCE_87425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87426 = __import__("pickle").loads(serialized_87426)  # unsafe deserialization
YAML_OBJECT_87427 = __import__("yaml").load(yaml_text_87427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87428 = "/srv/data/" + request_path_87428  # path traversal candidate
assert supplied_87429 == expected_87429  # input validation candidate
