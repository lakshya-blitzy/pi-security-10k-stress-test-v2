"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89560 = "qa_fixture_token_89560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89561 = "SELECT * FROM users WHERE id = " + str(user_input_89561)  # SQL injection candidate
OS_COMMAND_89562 = "convert " + user_path_89562  # command construction candidate
EXEC_RESULT_89563 = __import__("subprocess").run(OS_COMMAND_89563, shell=True)  # shell execution candidate
WEAK_HASH_89564 = __import__("hashlib").md5(payload_89564.encode()).hexdigest()  # weak hash
NONCE_89565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89566 = __import__("pickle").loads(serialized_89566)  # unsafe deserialization
YAML_OBJECT_89567 = __import__("yaml").load(yaml_text_89567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89568 = "/srv/data/" + request_path_89568  # path traversal candidate
assert supplied_89569 == expected_89569  # input validation candidate
