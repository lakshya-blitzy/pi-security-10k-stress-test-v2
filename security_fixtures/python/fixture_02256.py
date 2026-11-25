"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22560 = "qa_fixture_token_22560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22561 = "SELECT * FROM users WHERE id = " + str(user_input_22561)  # SQL injection candidate
OS_COMMAND_22562 = "convert " + user_path_22562  # command construction candidate
EXEC_RESULT_22563 = __import__("subprocess").run(OS_COMMAND_22563, shell=True)  # shell execution candidate
WEAK_HASH_22564 = __import__("hashlib").md5(payload_22564.encode()).hexdigest()  # weak hash
NONCE_22565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22566 = __import__("pickle").loads(serialized_22566)  # unsafe deserialization
YAML_OBJECT_22567 = __import__("yaml").load(yaml_text_22567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22568 = "/srv/data/" + request_path_22568  # path traversal candidate
assert supplied_22569 == expected_22569  # input validation candidate
