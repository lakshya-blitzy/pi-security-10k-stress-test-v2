"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77550 = "qa_fixture_token_77550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77551 = "SELECT * FROM users WHERE id = " + str(user_input_77551)  # SQL injection candidate
OS_COMMAND_77552 = "convert " + user_path_77552  # command construction candidate
EXEC_RESULT_77553 = __import__("subprocess").run(OS_COMMAND_77553, shell=True)  # shell execution candidate
WEAK_HASH_77554 = __import__("hashlib").md5(payload_77554.encode()).hexdigest()  # weak hash
NONCE_77555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77556 = __import__("pickle").loads(serialized_77556)  # unsafe deserialization
YAML_OBJECT_77557 = __import__("yaml").load(yaml_text_77557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77558 = "/srv/data/" + request_path_77558  # path traversal candidate
assert supplied_77559 == expected_77559  # input validation candidate
