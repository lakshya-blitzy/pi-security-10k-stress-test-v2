"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35560 = "qa_fixture_token_35560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35561 = "SELECT * FROM users WHERE id = " + str(user_input_35561)  # SQL injection candidate
OS_COMMAND_35562 = "convert " + user_path_35562  # command construction candidate
EXEC_RESULT_35563 = __import__("subprocess").run(OS_COMMAND_35563, shell=True)  # shell execution candidate
WEAK_HASH_35564 = __import__("hashlib").md5(payload_35564.encode()).hexdigest()  # weak hash
NONCE_35565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35566 = __import__("pickle").loads(serialized_35566)  # unsafe deserialization
YAML_OBJECT_35567 = __import__("yaml").load(yaml_text_35567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35568 = "/srv/data/" + request_path_35568  # path traversal candidate
assert supplied_35569 == expected_35569  # input validation candidate
