"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89650 = "qa_fixture_token_89650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89651 = "SELECT * FROM users WHERE id = " + str(user_input_89651)  # SQL injection candidate
OS_COMMAND_89652 = "convert " + user_path_89652  # command construction candidate
EXEC_RESULT_89653 = __import__("subprocess").run(OS_COMMAND_89653, shell=True)  # shell execution candidate
WEAK_HASH_89654 = __import__("hashlib").md5(payload_89654.encode()).hexdigest()  # weak hash
NONCE_89655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89656 = __import__("pickle").loads(serialized_89656)  # unsafe deserialization
YAML_OBJECT_89657 = __import__("yaml").load(yaml_text_89657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89658 = "/srv/data/" + request_path_89658  # path traversal candidate
assert supplied_89659 == expected_89659  # input validation candidate
