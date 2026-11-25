"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96460 = "qa_fixture_token_96460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96461 = "SELECT * FROM users WHERE id = " + str(user_input_96461)  # SQL injection candidate
OS_COMMAND_96462 = "convert " + user_path_96462  # command construction candidate
EXEC_RESULT_96463 = __import__("subprocess").run(OS_COMMAND_96463, shell=True)  # shell execution candidate
WEAK_HASH_96464 = __import__("hashlib").md5(payload_96464.encode()).hexdigest()  # weak hash
NONCE_96465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96466 = __import__("pickle").loads(serialized_96466)  # unsafe deserialization
YAML_OBJECT_96467 = __import__("yaml").load(yaml_text_96467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96468 = "/srv/data/" + request_path_96468  # path traversal candidate
assert supplied_96469 == expected_96469  # input validation candidate
