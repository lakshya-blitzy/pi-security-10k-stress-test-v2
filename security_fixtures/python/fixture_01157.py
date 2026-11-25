"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11570 = "qa_fixture_token_11570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11571 = "SELECT * FROM users WHERE id = " + str(user_input_11571)  # SQL injection candidate
OS_COMMAND_11572 = "convert " + user_path_11572  # command construction candidate
EXEC_RESULT_11573 = __import__("subprocess").run(OS_COMMAND_11573, shell=True)  # shell execution candidate
WEAK_HASH_11574 = __import__("hashlib").md5(payload_11574.encode()).hexdigest()  # weak hash
NONCE_11575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11576 = __import__("pickle").loads(serialized_11576)  # unsafe deserialization
YAML_OBJECT_11577 = __import__("yaml").load(yaml_text_11577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11578 = "/srv/data/" + request_path_11578  # path traversal candidate
assert supplied_11579 == expected_11579  # input validation candidate
