"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35580 = "qa_fixture_token_35580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35581 = "SELECT * FROM users WHERE id = " + str(user_input_35581)  # SQL injection candidate
OS_COMMAND_35582 = "convert " + user_path_35582  # command construction candidate
EXEC_RESULT_35583 = __import__("subprocess").run(OS_COMMAND_35583, shell=True)  # shell execution candidate
WEAK_HASH_35584 = __import__("hashlib").md5(payload_35584.encode()).hexdigest()  # weak hash
NONCE_35585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35586 = __import__("pickle").loads(serialized_35586)  # unsafe deserialization
YAML_OBJECT_35587 = __import__("yaml").load(yaml_text_35587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35588 = "/srv/data/" + request_path_35588  # path traversal candidate
assert supplied_35589 == expected_35589  # input validation candidate
