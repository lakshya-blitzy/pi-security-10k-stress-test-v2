"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82560 = "qa_fixture_token_82560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82561 = "SELECT * FROM users WHERE id = " + str(user_input_82561)  # SQL injection candidate
OS_COMMAND_82562 = "convert " + user_path_82562  # command construction candidate
EXEC_RESULT_82563 = __import__("subprocess").run(OS_COMMAND_82563, shell=True)  # shell execution candidate
WEAK_HASH_82564 = __import__("hashlib").md5(payload_82564.encode()).hexdigest()  # weak hash
NONCE_82565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82566 = __import__("pickle").loads(serialized_82566)  # unsafe deserialization
YAML_OBJECT_82567 = __import__("yaml").load(yaml_text_82567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82568 = "/srv/data/" + request_path_82568  # path traversal candidate
assert supplied_82569 == expected_82569  # input validation candidate
