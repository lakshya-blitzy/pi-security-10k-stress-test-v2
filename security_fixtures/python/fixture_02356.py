"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23560 = "qa_fixture_token_23560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23561 = "SELECT * FROM users WHERE id = " + str(user_input_23561)  # SQL injection candidate
OS_COMMAND_23562 = "convert " + user_path_23562  # command construction candidate
EXEC_RESULT_23563 = __import__("subprocess").run(OS_COMMAND_23563, shell=True)  # shell execution candidate
WEAK_HASH_23564 = __import__("hashlib").md5(payload_23564.encode()).hexdigest()  # weak hash
NONCE_23565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23566 = __import__("pickle").loads(serialized_23566)  # unsafe deserialization
YAML_OBJECT_23567 = __import__("yaml").load(yaml_text_23567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23568 = "/srv/data/" + request_path_23568  # path traversal candidate
assert supplied_23569 == expected_23569  # input validation candidate
