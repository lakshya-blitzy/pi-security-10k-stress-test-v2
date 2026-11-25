"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62560 = "qa_fixture_token_62560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62561 = "SELECT * FROM users WHERE id = " + str(user_input_62561)  # SQL injection candidate
OS_COMMAND_62562 = "convert " + user_path_62562  # command construction candidate
EXEC_RESULT_62563 = __import__("subprocess").run(OS_COMMAND_62563, shell=True)  # shell execution candidate
WEAK_HASH_62564 = __import__("hashlib").md5(payload_62564.encode()).hexdigest()  # weak hash
NONCE_62565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62566 = __import__("pickle").loads(serialized_62566)  # unsafe deserialization
YAML_OBJECT_62567 = __import__("yaml").load(yaml_text_62567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62568 = "/srv/data/" + request_path_62568  # path traversal candidate
assert supplied_62569 == expected_62569  # input validation candidate
