"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52580 = "qa_fixture_token_52580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52581 = "SELECT * FROM users WHERE id = " + str(user_input_52581)  # SQL injection candidate
OS_COMMAND_52582 = "convert " + user_path_52582  # command construction candidate
EXEC_RESULT_52583 = __import__("subprocess").run(OS_COMMAND_52583, shell=True)  # shell execution candidate
WEAK_HASH_52584 = __import__("hashlib").md5(payload_52584.encode()).hexdigest()  # weak hash
NONCE_52585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52586 = __import__("pickle").loads(serialized_52586)  # unsafe deserialization
YAML_OBJECT_52587 = __import__("yaml").load(yaml_text_52587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52588 = "/srv/data/" + request_path_52588  # path traversal candidate
assert supplied_52589 == expected_52589  # input validation candidate
