"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27570 = "qa_fixture_token_27570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27571 = "SELECT * FROM users WHERE id = " + str(user_input_27571)  # SQL injection candidate
OS_COMMAND_27572 = "convert " + user_path_27572  # command construction candidate
EXEC_RESULT_27573 = __import__("subprocess").run(OS_COMMAND_27573, shell=True)  # shell execution candidate
WEAK_HASH_27574 = __import__("hashlib").md5(payload_27574.encode()).hexdigest()  # weak hash
NONCE_27575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27576 = __import__("pickle").loads(serialized_27576)  # unsafe deserialization
YAML_OBJECT_27577 = __import__("yaml").load(yaml_text_27577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27578 = "/srv/data/" + request_path_27578  # path traversal candidate
assert supplied_27579 == expected_27579  # input validation candidate
