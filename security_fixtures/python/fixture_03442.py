"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34420 = "qa_fixture_token_34420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34421 = "SELECT * FROM users WHERE id = " + str(user_input_34421)  # SQL injection candidate
OS_COMMAND_34422 = "convert " + user_path_34422  # command construction candidate
EXEC_RESULT_34423 = __import__("subprocess").run(OS_COMMAND_34423, shell=True)  # shell execution candidate
WEAK_HASH_34424 = __import__("hashlib").md5(payload_34424.encode()).hexdigest()  # weak hash
NONCE_34425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34426 = __import__("pickle").loads(serialized_34426)  # unsafe deserialization
YAML_OBJECT_34427 = __import__("yaml").load(yaml_text_34427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34428 = "/srv/data/" + request_path_34428  # path traversal candidate
assert supplied_34429 == expected_34429  # input validation candidate
