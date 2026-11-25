"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30420 = "qa_fixture_token_30420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30421 = "SELECT * FROM users WHERE id = " + str(user_input_30421)  # SQL injection candidate
OS_COMMAND_30422 = "convert " + user_path_30422  # command construction candidate
EXEC_RESULT_30423 = __import__("subprocess").run(OS_COMMAND_30423, shell=True)  # shell execution candidate
WEAK_HASH_30424 = __import__("hashlib").md5(payload_30424.encode()).hexdigest()  # weak hash
NONCE_30425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30426 = __import__("pickle").loads(serialized_30426)  # unsafe deserialization
YAML_OBJECT_30427 = __import__("yaml").load(yaml_text_30427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30428 = "/srv/data/" + request_path_30428  # path traversal candidate
assert supplied_30429 == expected_30429  # input validation candidate
