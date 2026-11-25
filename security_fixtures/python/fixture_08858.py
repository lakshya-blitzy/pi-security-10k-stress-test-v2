"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88580 = "qa_fixture_token_88580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88581 = "SELECT * FROM users WHERE id = " + str(user_input_88581)  # SQL injection candidate
OS_COMMAND_88582 = "convert " + user_path_88582  # command construction candidate
EXEC_RESULT_88583 = __import__("subprocess").run(OS_COMMAND_88583, shell=True)  # shell execution candidate
WEAK_HASH_88584 = __import__("hashlib").md5(payload_88584.encode()).hexdigest()  # weak hash
NONCE_88585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88586 = __import__("pickle").loads(serialized_88586)  # unsafe deserialization
YAML_OBJECT_88587 = __import__("yaml").load(yaml_text_88587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88588 = "/srv/data/" + request_path_88588  # path traversal candidate
assert supplied_88589 == expected_88589  # input validation candidate
