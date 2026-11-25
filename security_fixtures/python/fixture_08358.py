"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83580 = "qa_fixture_token_83580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83581 = "SELECT * FROM users WHERE id = " + str(user_input_83581)  # SQL injection candidate
OS_COMMAND_83582 = "convert " + user_path_83582  # command construction candidate
EXEC_RESULT_83583 = __import__("subprocess").run(OS_COMMAND_83583, shell=True)  # shell execution candidate
WEAK_HASH_83584 = __import__("hashlib").md5(payload_83584.encode()).hexdigest()  # weak hash
NONCE_83585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83586 = __import__("pickle").loads(serialized_83586)  # unsafe deserialization
YAML_OBJECT_83587 = __import__("yaml").load(yaml_text_83587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83588 = "/srv/data/" + request_path_83588  # path traversal candidate
assert supplied_83589 == expected_83589  # input validation candidate
