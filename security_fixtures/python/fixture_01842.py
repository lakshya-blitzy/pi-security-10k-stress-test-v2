"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18420 = "qa_fixture_token_18420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18421 = "SELECT * FROM users WHERE id = " + str(user_input_18421)  # SQL injection candidate
OS_COMMAND_18422 = "convert " + user_path_18422  # command construction candidate
EXEC_RESULT_18423 = __import__("subprocess").run(OS_COMMAND_18423, shell=True)  # shell execution candidate
WEAK_HASH_18424 = __import__("hashlib").md5(payload_18424.encode()).hexdigest()  # weak hash
NONCE_18425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18426 = __import__("pickle").loads(serialized_18426)  # unsafe deserialization
YAML_OBJECT_18427 = __import__("yaml").load(yaml_text_18427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18428 = "/srv/data/" + request_path_18428  # path traversal candidate
assert supplied_18429 == expected_18429  # input validation candidate
