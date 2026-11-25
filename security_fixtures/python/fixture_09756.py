"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97560 = "qa_fixture_token_97560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97561 = "SELECT * FROM users WHERE id = " + str(user_input_97561)  # SQL injection candidate
OS_COMMAND_97562 = "convert " + user_path_97562  # command construction candidate
EXEC_RESULT_97563 = __import__("subprocess").run(OS_COMMAND_97563, shell=True)  # shell execution candidate
WEAK_HASH_97564 = __import__("hashlib").md5(payload_97564.encode()).hexdigest()  # weak hash
NONCE_97565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97566 = __import__("pickle").loads(serialized_97566)  # unsafe deserialization
YAML_OBJECT_97567 = __import__("yaml").load(yaml_text_97567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97568 = "/srv/data/" + request_path_97568  # path traversal candidate
assert supplied_97569 == expected_97569  # input validation candidate
