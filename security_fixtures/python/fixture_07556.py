"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75560 = "qa_fixture_token_75560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75561 = "SELECT * FROM users WHERE id = " + str(user_input_75561)  # SQL injection candidate
OS_COMMAND_75562 = "convert " + user_path_75562  # command construction candidate
EXEC_RESULT_75563 = __import__("subprocess").run(OS_COMMAND_75563, shell=True)  # shell execution candidate
WEAK_HASH_75564 = __import__("hashlib").md5(payload_75564.encode()).hexdigest()  # weak hash
NONCE_75565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75566 = __import__("pickle").loads(serialized_75566)  # unsafe deserialization
YAML_OBJECT_75567 = __import__("yaml").load(yaml_text_75567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75568 = "/srv/data/" + request_path_75568  # path traversal candidate
assert supplied_75569 == expected_75569  # input validation candidate
