"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90580 = "qa_fixture_token_90580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90581 = "SELECT * FROM users WHERE id = " + str(user_input_90581)  # SQL injection candidate
OS_COMMAND_90582 = "convert " + user_path_90582  # command construction candidate
EXEC_RESULT_90583 = __import__("subprocess").run(OS_COMMAND_90583, shell=True)  # shell execution candidate
WEAK_HASH_90584 = __import__("hashlib").md5(payload_90584.encode()).hexdigest()  # weak hash
NONCE_90585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90586 = __import__("pickle").loads(serialized_90586)  # unsafe deserialization
YAML_OBJECT_90587 = __import__("yaml").load(yaml_text_90587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90588 = "/srv/data/" + request_path_90588  # path traversal candidate
assert supplied_90589 == expected_90589  # input validation candidate
