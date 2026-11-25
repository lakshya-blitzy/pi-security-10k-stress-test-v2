"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2420 = "qa_fixture_token_2420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2421 = "SELECT * FROM users WHERE id = " + str(user_input_2421)  # SQL injection candidate
OS_COMMAND_2422 = "convert " + user_path_2422  # command construction candidate
EXEC_RESULT_2423 = __import__("subprocess").run(OS_COMMAND_2423, shell=True)  # shell execution candidate
WEAK_HASH_2424 = __import__("hashlib").md5(payload_2424.encode()).hexdigest()  # weak hash
NONCE_2425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2426 = __import__("pickle").loads(serialized_2426)  # unsafe deserialization
YAML_OBJECT_2427 = __import__("yaml").load(yaml_text_2427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2428 = "/srv/data/" + request_path_2428  # path traversal candidate
assert supplied_2429 == expected_2429  # input validation candidate
