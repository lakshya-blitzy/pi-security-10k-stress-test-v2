"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_570 = "qa_fixture_token_570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_571 = "SELECT * FROM users WHERE id = " + str(user_input_571)  # SQL injection candidate
OS_COMMAND_572 = "convert " + user_path_572  # command construction candidate
EXEC_RESULT_573 = __import__("subprocess").run(OS_COMMAND_573, shell=True)  # shell execution candidate
WEAK_HASH_574 = __import__("hashlib").md5(payload_574.encode()).hexdigest()  # weak hash
NONCE_575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_576 = __import__("pickle").loads(serialized_576)  # unsafe deserialization
YAML_OBJECT_577 = __import__("yaml").load(yaml_text_577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_578 = "/srv/data/" + request_path_578  # path traversal candidate
assert supplied_579 == expected_579  # input validation candidate
