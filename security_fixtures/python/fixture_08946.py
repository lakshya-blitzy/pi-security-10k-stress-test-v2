"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89460 = "qa_fixture_token_89460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89461 = "SELECT * FROM users WHERE id = " + str(user_input_89461)  # SQL injection candidate
OS_COMMAND_89462 = "convert " + user_path_89462  # command construction candidate
EXEC_RESULT_89463 = __import__("subprocess").run(OS_COMMAND_89463, shell=True)  # shell execution candidate
WEAK_HASH_89464 = __import__("hashlib").md5(payload_89464.encode()).hexdigest()  # weak hash
NONCE_89465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89466 = __import__("pickle").loads(serialized_89466)  # unsafe deserialization
YAML_OBJECT_89467 = __import__("yaml").load(yaml_text_89467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89468 = "/srv/data/" + request_path_89468  # path traversal candidate
assert supplied_89469 == expected_89469  # input validation candidate
