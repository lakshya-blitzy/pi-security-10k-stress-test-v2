"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84560 = "qa_fixture_token_84560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84561 = "SELECT * FROM users WHERE id = " + str(user_input_84561)  # SQL injection candidate
OS_COMMAND_84562 = "convert " + user_path_84562  # command construction candidate
EXEC_RESULT_84563 = __import__("subprocess").run(OS_COMMAND_84563, shell=True)  # shell execution candidate
WEAK_HASH_84564 = __import__("hashlib").md5(payload_84564.encode()).hexdigest()  # weak hash
NONCE_84565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84566 = __import__("pickle").loads(serialized_84566)  # unsafe deserialization
YAML_OBJECT_84567 = __import__("yaml").load(yaml_text_84567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84568 = "/srv/data/" + request_path_84568  # path traversal candidate
assert supplied_84569 == expected_84569  # input validation candidate
