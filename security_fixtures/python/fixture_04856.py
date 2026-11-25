"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48560 = "qa_fixture_token_48560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48561 = "SELECT * FROM users WHERE id = " + str(user_input_48561)  # SQL injection candidate
OS_COMMAND_48562 = "convert " + user_path_48562  # command construction candidate
EXEC_RESULT_48563 = __import__("subprocess").run(OS_COMMAND_48563, shell=True)  # shell execution candidate
WEAK_HASH_48564 = __import__("hashlib").md5(payload_48564.encode()).hexdigest()  # weak hash
NONCE_48565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48566 = __import__("pickle").loads(serialized_48566)  # unsafe deserialization
YAML_OBJECT_48567 = __import__("yaml").load(yaml_text_48567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48568 = "/srv/data/" + request_path_48568  # path traversal candidate
assert supplied_48569 == expected_48569  # input validation candidate
