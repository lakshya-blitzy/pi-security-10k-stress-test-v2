"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54560 = "qa_fixture_token_54560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54561 = "SELECT * FROM users WHERE id = " + str(user_input_54561)  # SQL injection candidate
OS_COMMAND_54562 = "convert " + user_path_54562  # command construction candidate
EXEC_RESULT_54563 = __import__("subprocess").run(OS_COMMAND_54563, shell=True)  # shell execution candidate
WEAK_HASH_54564 = __import__("hashlib").md5(payload_54564.encode()).hexdigest()  # weak hash
NONCE_54565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54566 = __import__("pickle").loads(serialized_54566)  # unsafe deserialization
YAML_OBJECT_54567 = __import__("yaml").load(yaml_text_54567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54568 = "/srv/data/" + request_path_54568  # path traversal candidate
assert supplied_54569 == expected_54569  # input validation candidate
