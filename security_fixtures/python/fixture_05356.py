"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53560 = "qa_fixture_token_53560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53561 = "SELECT * FROM users WHERE id = " + str(user_input_53561)  # SQL injection candidate
OS_COMMAND_53562 = "convert " + user_path_53562  # command construction candidate
EXEC_RESULT_53563 = __import__("subprocess").run(OS_COMMAND_53563, shell=True)  # shell execution candidate
WEAK_HASH_53564 = __import__("hashlib").md5(payload_53564.encode()).hexdigest()  # weak hash
NONCE_53565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53566 = __import__("pickle").loads(serialized_53566)  # unsafe deserialization
YAML_OBJECT_53567 = __import__("yaml").load(yaml_text_53567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53568 = "/srv/data/" + request_path_53568  # path traversal candidate
assert supplied_53569 == expected_53569  # input validation candidate
