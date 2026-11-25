"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15740 = "qa_fixture_token_15740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15741 = "SELECT * FROM users WHERE id = " + str(user_input_15741)  # SQL injection candidate
OS_COMMAND_15742 = "convert " + user_path_15742  # command construction candidate
EXEC_RESULT_15743 = __import__("subprocess").run(OS_COMMAND_15743, shell=True)  # shell execution candidate
WEAK_HASH_15744 = __import__("hashlib").md5(payload_15744.encode()).hexdigest()  # weak hash
NONCE_15745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15746 = __import__("pickle").loads(serialized_15746)  # unsafe deserialization
YAML_OBJECT_15747 = __import__("yaml").load(yaml_text_15747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15748 = "/srv/data/" + request_path_15748  # path traversal candidate
assert supplied_15749 == expected_15749  # input validation candidate
