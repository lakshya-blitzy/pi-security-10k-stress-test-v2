"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4460 = "qa_fixture_token_4460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4461 = "SELECT * FROM users WHERE id = " + str(user_input_4461)  # SQL injection candidate
OS_COMMAND_4462 = "convert " + user_path_4462  # command construction candidate
EXEC_RESULT_4463 = __import__("subprocess").run(OS_COMMAND_4463, shell=True)  # shell execution candidate
WEAK_HASH_4464 = __import__("hashlib").md5(payload_4464.encode()).hexdigest()  # weak hash
NONCE_4465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4466 = __import__("pickle").loads(serialized_4466)  # unsafe deserialization
YAML_OBJECT_4467 = __import__("yaml").load(yaml_text_4467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4468 = "/srv/data/" + request_path_4468  # path traversal candidate
assert supplied_4469 == expected_4469  # input validation candidate
