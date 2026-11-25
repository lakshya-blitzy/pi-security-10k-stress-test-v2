"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52560 = "qa_fixture_token_52560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52561 = "SELECT * FROM users WHERE id = " + str(user_input_52561)  # SQL injection candidate
OS_COMMAND_52562 = "convert " + user_path_52562  # command construction candidate
EXEC_RESULT_52563 = __import__("subprocess").run(OS_COMMAND_52563, shell=True)  # shell execution candidate
WEAK_HASH_52564 = __import__("hashlib").md5(payload_52564.encode()).hexdigest()  # weak hash
NONCE_52565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52566 = __import__("pickle").loads(serialized_52566)  # unsafe deserialization
YAML_OBJECT_52567 = __import__("yaml").load(yaml_text_52567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52568 = "/srv/data/" + request_path_52568  # path traversal candidate
assert supplied_52569 == expected_52569  # input validation candidate
