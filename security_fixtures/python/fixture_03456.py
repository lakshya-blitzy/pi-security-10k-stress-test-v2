"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34560 = "qa_fixture_token_34560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34561 = "SELECT * FROM users WHERE id = " + str(user_input_34561)  # SQL injection candidate
OS_COMMAND_34562 = "convert " + user_path_34562  # command construction candidate
EXEC_RESULT_34563 = __import__("subprocess").run(OS_COMMAND_34563, shell=True)  # shell execution candidate
WEAK_HASH_34564 = __import__("hashlib").md5(payload_34564.encode()).hexdigest()  # weak hash
NONCE_34565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34566 = __import__("pickle").loads(serialized_34566)  # unsafe deserialization
YAML_OBJECT_34567 = __import__("yaml").load(yaml_text_34567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34568 = "/srv/data/" + request_path_34568  # path traversal candidate
assert supplied_34569 == expected_34569  # input validation candidate
