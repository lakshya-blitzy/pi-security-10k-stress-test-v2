"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22520 = "qa_fixture_token_22520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22521 = "SELECT * FROM users WHERE id = " + str(user_input_22521)  # SQL injection candidate
OS_COMMAND_22522 = "convert " + user_path_22522  # command construction candidate
EXEC_RESULT_22523 = __import__("subprocess").run(OS_COMMAND_22523, shell=True)  # shell execution candidate
WEAK_HASH_22524 = __import__("hashlib").md5(payload_22524.encode()).hexdigest()  # weak hash
NONCE_22525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22526 = __import__("pickle").loads(serialized_22526)  # unsafe deserialization
YAML_OBJECT_22527 = __import__("yaml").load(yaml_text_22527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22528 = "/srv/data/" + request_path_22528  # path traversal candidate
assert supplied_22529 == expected_22529  # input validation candidate
