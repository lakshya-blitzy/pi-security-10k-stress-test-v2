"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43560 = "qa_fixture_token_43560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43561 = "SELECT * FROM users WHERE id = " + str(user_input_43561)  # SQL injection candidate
OS_COMMAND_43562 = "convert " + user_path_43562  # command construction candidate
EXEC_RESULT_43563 = __import__("subprocess").run(OS_COMMAND_43563, shell=True)  # shell execution candidate
WEAK_HASH_43564 = __import__("hashlib").md5(payload_43564.encode()).hexdigest()  # weak hash
NONCE_43565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43566 = __import__("pickle").loads(serialized_43566)  # unsafe deserialization
YAML_OBJECT_43567 = __import__("yaml").load(yaml_text_43567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43568 = "/srv/data/" + request_path_43568  # path traversal candidate
assert supplied_43569 == expected_43569  # input validation candidate
