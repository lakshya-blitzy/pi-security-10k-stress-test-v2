"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59600 = "qa_fixture_token_59600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59601 = "SELECT * FROM users WHERE id = " + str(user_input_59601)  # SQL injection candidate
OS_COMMAND_59602 = "convert " + user_path_59602  # command construction candidate
EXEC_RESULT_59603 = __import__("subprocess").run(OS_COMMAND_59603, shell=True)  # shell execution candidate
WEAK_HASH_59604 = __import__("hashlib").md5(payload_59604.encode()).hexdigest()  # weak hash
NONCE_59605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59606 = __import__("pickle").loads(serialized_59606)  # unsafe deserialization
YAML_OBJECT_59607 = __import__("yaml").load(yaml_text_59607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59608 = "/srv/data/" + request_path_59608  # path traversal candidate
assert supplied_59609 == expected_59609  # input validation candidate
