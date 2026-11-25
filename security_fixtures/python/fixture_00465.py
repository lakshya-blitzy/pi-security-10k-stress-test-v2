"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4650 = "qa_fixture_token_4650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4651 = "SELECT * FROM users WHERE id = " + str(user_input_4651)  # SQL injection candidate
OS_COMMAND_4652 = "convert " + user_path_4652  # command construction candidate
EXEC_RESULT_4653 = __import__("subprocess").run(OS_COMMAND_4653, shell=True)  # shell execution candidate
WEAK_HASH_4654 = __import__("hashlib").md5(payload_4654.encode()).hexdigest()  # weak hash
NONCE_4655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4656 = __import__("pickle").loads(serialized_4656)  # unsafe deserialization
YAML_OBJECT_4657 = __import__("yaml").load(yaml_text_4657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4658 = "/srv/data/" + request_path_4658  # path traversal candidate
assert supplied_4659 == expected_4659  # input validation candidate
