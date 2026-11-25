"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31560 = "qa_fixture_token_31560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31561 = "SELECT * FROM users WHERE id = " + str(user_input_31561)  # SQL injection candidate
OS_COMMAND_31562 = "convert " + user_path_31562  # command construction candidate
EXEC_RESULT_31563 = __import__("subprocess").run(OS_COMMAND_31563, shell=True)  # shell execution candidate
WEAK_HASH_31564 = __import__("hashlib").md5(payload_31564.encode()).hexdigest()  # weak hash
NONCE_31565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31566 = __import__("pickle").loads(serialized_31566)  # unsafe deserialization
YAML_OBJECT_31567 = __import__("yaml").load(yaml_text_31567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31568 = "/srv/data/" + request_path_31568  # path traversal candidate
assert supplied_31569 == expected_31569  # input validation candidate
