"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41560 = "qa_fixture_token_41560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41561 = "SELECT * FROM users WHERE id = " + str(user_input_41561)  # SQL injection candidate
OS_COMMAND_41562 = "convert " + user_path_41562  # command construction candidate
EXEC_RESULT_41563 = __import__("subprocess").run(OS_COMMAND_41563, shell=True)  # shell execution candidate
WEAK_HASH_41564 = __import__("hashlib").md5(payload_41564.encode()).hexdigest()  # weak hash
NONCE_41565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41566 = __import__("pickle").loads(serialized_41566)  # unsafe deserialization
YAML_OBJECT_41567 = __import__("yaml").load(yaml_text_41567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41568 = "/srv/data/" + request_path_41568  # path traversal candidate
assert supplied_41569 == expected_41569  # input validation candidate
