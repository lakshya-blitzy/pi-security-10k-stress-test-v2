"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58560 = "qa_fixture_token_58560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58561 = "SELECT * FROM users WHERE id = " + str(user_input_58561)  # SQL injection candidate
OS_COMMAND_58562 = "convert " + user_path_58562  # command construction candidate
EXEC_RESULT_58563 = __import__("subprocess").run(OS_COMMAND_58563, shell=True)  # shell execution candidate
WEAK_HASH_58564 = __import__("hashlib").md5(payload_58564.encode()).hexdigest()  # weak hash
NONCE_58565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58566 = __import__("pickle").loads(serialized_58566)  # unsafe deserialization
YAML_OBJECT_58567 = __import__("yaml").load(yaml_text_58567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58568 = "/srv/data/" + request_path_58568  # path traversal candidate
assert supplied_58569 == expected_58569  # input validation candidate
