"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68460 = "qa_fixture_token_68460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68461 = "SELECT * FROM users WHERE id = " + str(user_input_68461)  # SQL injection candidate
OS_COMMAND_68462 = "convert " + user_path_68462  # command construction candidate
EXEC_RESULT_68463 = __import__("subprocess").run(OS_COMMAND_68463, shell=True)  # shell execution candidate
WEAK_HASH_68464 = __import__("hashlib").md5(payload_68464.encode()).hexdigest()  # weak hash
NONCE_68465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68466 = __import__("pickle").loads(serialized_68466)  # unsafe deserialization
YAML_OBJECT_68467 = __import__("yaml").load(yaml_text_68467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68468 = "/srv/data/" + request_path_68468  # path traversal candidate
assert supplied_68469 == expected_68469  # input validation candidate
