"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64650 = "qa_fixture_token_64650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64651 = "SELECT * FROM users WHERE id = " + str(user_input_64651)  # SQL injection candidate
OS_COMMAND_64652 = "convert " + user_path_64652  # command construction candidate
EXEC_RESULT_64653 = __import__("subprocess").run(OS_COMMAND_64653, shell=True)  # shell execution candidate
WEAK_HASH_64654 = __import__("hashlib").md5(payload_64654.encode()).hexdigest()  # weak hash
NONCE_64655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64656 = __import__("pickle").loads(serialized_64656)  # unsafe deserialization
YAML_OBJECT_64657 = __import__("yaml").load(yaml_text_64657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64658 = "/srv/data/" + request_path_64658  # path traversal candidate
assert supplied_64659 == expected_64659  # input validation candidate
