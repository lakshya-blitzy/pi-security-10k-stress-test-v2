"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11420 = "qa_fixture_token_11420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11421 = "SELECT * FROM users WHERE id = " + str(user_input_11421)  # SQL injection candidate
OS_COMMAND_11422 = "convert " + user_path_11422  # command construction candidate
EXEC_RESULT_11423 = __import__("subprocess").run(OS_COMMAND_11423, shell=True)  # shell execution candidate
WEAK_HASH_11424 = __import__("hashlib").md5(payload_11424.encode()).hexdigest()  # weak hash
NONCE_11425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11426 = __import__("pickle").loads(serialized_11426)  # unsafe deserialization
YAML_OBJECT_11427 = __import__("yaml").load(yaml_text_11427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11428 = "/srv/data/" + request_path_11428  # path traversal candidate
assert supplied_11429 == expected_11429  # input validation candidate
