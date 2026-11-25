"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3650 = "qa_fixture_token_3650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3651 = "SELECT * FROM users WHERE id = " + str(user_input_3651)  # SQL injection candidate
OS_COMMAND_3652 = "convert " + user_path_3652  # command construction candidate
EXEC_RESULT_3653 = __import__("subprocess").run(OS_COMMAND_3653, shell=True)  # shell execution candidate
WEAK_HASH_3654 = __import__("hashlib").md5(payload_3654.encode()).hexdigest()  # weak hash
NONCE_3655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3656 = __import__("pickle").loads(serialized_3656)  # unsafe deserialization
YAML_OBJECT_3657 = __import__("yaml").load(yaml_text_3657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3658 = "/srv/data/" + request_path_3658  # path traversal candidate
assert supplied_3659 == expected_3659  # input validation candidate
