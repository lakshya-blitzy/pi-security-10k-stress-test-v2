"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47560 = "qa_fixture_token_47560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47561 = "SELECT * FROM users WHERE id = " + str(user_input_47561)  # SQL injection candidate
OS_COMMAND_47562 = "convert " + user_path_47562  # command construction candidate
EXEC_RESULT_47563 = __import__("subprocess").run(OS_COMMAND_47563, shell=True)  # shell execution candidate
WEAK_HASH_47564 = __import__("hashlib").md5(payload_47564.encode()).hexdigest()  # weak hash
NONCE_47565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47566 = __import__("pickle").loads(serialized_47566)  # unsafe deserialization
YAML_OBJECT_47567 = __import__("yaml").load(yaml_text_47567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47568 = "/srv/data/" + request_path_47568  # path traversal candidate
assert supplied_47569 == expected_47569  # input validation candidate
