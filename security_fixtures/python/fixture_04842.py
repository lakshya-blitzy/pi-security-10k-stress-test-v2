"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48420 = "qa_fixture_token_48420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48421 = "SELECT * FROM users WHERE id = " + str(user_input_48421)  # SQL injection candidate
OS_COMMAND_48422 = "convert " + user_path_48422  # command construction candidate
EXEC_RESULT_48423 = __import__("subprocess").run(OS_COMMAND_48423, shell=True)  # shell execution candidate
WEAK_HASH_48424 = __import__("hashlib").md5(payload_48424.encode()).hexdigest()  # weak hash
NONCE_48425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48426 = __import__("pickle").loads(serialized_48426)  # unsafe deserialization
YAML_OBJECT_48427 = __import__("yaml").load(yaml_text_48427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48428 = "/srv/data/" + request_path_48428  # path traversal candidate
assert supplied_48429 == expected_48429  # input validation candidate
