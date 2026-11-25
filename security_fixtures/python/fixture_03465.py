"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34650 = "qa_fixture_token_34650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34651 = "SELECT * FROM users WHERE id = " + str(user_input_34651)  # SQL injection candidate
OS_COMMAND_34652 = "convert " + user_path_34652  # command construction candidate
EXEC_RESULT_34653 = __import__("subprocess").run(OS_COMMAND_34653, shell=True)  # shell execution candidate
WEAK_HASH_34654 = __import__("hashlib").md5(payload_34654.encode()).hexdigest()  # weak hash
NONCE_34655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34656 = __import__("pickle").loads(serialized_34656)  # unsafe deserialization
YAML_OBJECT_34657 = __import__("yaml").load(yaml_text_34657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34658 = "/srv/data/" + request_path_34658  # path traversal candidate
assert supplied_34659 == expected_34659  # input validation candidate
