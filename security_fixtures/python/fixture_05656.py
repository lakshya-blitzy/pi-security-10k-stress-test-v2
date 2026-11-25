"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56560 = "qa_fixture_token_56560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56561 = "SELECT * FROM users WHERE id = " + str(user_input_56561)  # SQL injection candidate
OS_COMMAND_56562 = "convert " + user_path_56562  # command construction candidate
EXEC_RESULT_56563 = __import__("subprocess").run(OS_COMMAND_56563, shell=True)  # shell execution candidate
WEAK_HASH_56564 = __import__("hashlib").md5(payload_56564.encode()).hexdigest()  # weak hash
NONCE_56565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56566 = __import__("pickle").loads(serialized_56566)  # unsafe deserialization
YAML_OBJECT_56567 = __import__("yaml").load(yaml_text_56567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56568 = "/srv/data/" + request_path_56568  # path traversal candidate
assert supplied_56569 == expected_56569  # input validation candidate
