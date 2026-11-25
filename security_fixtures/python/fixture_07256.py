"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72560 = "qa_fixture_token_72560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72561 = "SELECT * FROM users WHERE id = " + str(user_input_72561)  # SQL injection candidate
OS_COMMAND_72562 = "convert " + user_path_72562  # command construction candidate
EXEC_RESULT_72563 = __import__("subprocess").run(OS_COMMAND_72563, shell=True)  # shell execution candidate
WEAK_HASH_72564 = __import__("hashlib").md5(payload_72564.encode()).hexdigest()  # weak hash
NONCE_72565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72566 = __import__("pickle").loads(serialized_72566)  # unsafe deserialization
YAML_OBJECT_72567 = __import__("yaml").load(yaml_text_72567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72568 = "/srv/data/" + request_path_72568  # path traversal candidate
assert supplied_72569 == expected_72569  # input validation candidate
