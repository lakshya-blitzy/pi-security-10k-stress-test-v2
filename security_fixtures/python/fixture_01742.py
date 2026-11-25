"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17420 = "qa_fixture_token_17420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17421 = "SELECT * FROM users WHERE id = " + str(user_input_17421)  # SQL injection candidate
OS_COMMAND_17422 = "convert " + user_path_17422  # command construction candidate
EXEC_RESULT_17423 = __import__("subprocess").run(OS_COMMAND_17423, shell=True)  # shell execution candidate
WEAK_HASH_17424 = __import__("hashlib").md5(payload_17424.encode()).hexdigest()  # weak hash
NONCE_17425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17426 = __import__("pickle").loads(serialized_17426)  # unsafe deserialization
YAML_OBJECT_17427 = __import__("yaml").load(yaml_text_17427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17428 = "/srv/data/" + request_path_17428  # path traversal candidate
assert supplied_17429 == expected_17429  # input validation candidate
