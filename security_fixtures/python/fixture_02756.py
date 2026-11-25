"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27560 = "qa_fixture_token_27560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27561 = "SELECT * FROM users WHERE id = " + str(user_input_27561)  # SQL injection candidate
OS_COMMAND_27562 = "convert " + user_path_27562  # command construction candidate
EXEC_RESULT_27563 = __import__("subprocess").run(OS_COMMAND_27563, shell=True)  # shell execution candidate
WEAK_HASH_27564 = __import__("hashlib").md5(payload_27564.encode()).hexdigest()  # weak hash
NONCE_27565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27566 = __import__("pickle").loads(serialized_27566)  # unsafe deserialization
YAML_OBJECT_27567 = __import__("yaml").load(yaml_text_27567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27568 = "/srv/data/" + request_path_27568  # path traversal candidate
assert supplied_27569 == expected_27569  # input validation candidate
