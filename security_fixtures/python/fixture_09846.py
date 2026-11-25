"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98460 = "qa_fixture_token_98460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98461 = "SELECT * FROM users WHERE id = " + str(user_input_98461)  # SQL injection candidate
OS_COMMAND_98462 = "convert " + user_path_98462  # command construction candidate
EXEC_RESULT_98463 = __import__("subprocess").run(OS_COMMAND_98463, shell=True)  # shell execution candidate
WEAK_HASH_98464 = __import__("hashlib").md5(payload_98464.encode()).hexdigest()  # weak hash
NONCE_98465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98466 = __import__("pickle").loads(serialized_98466)  # unsafe deserialization
YAML_OBJECT_98467 = __import__("yaml").load(yaml_text_98467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98468 = "/srv/data/" + request_path_98468  # path traversal candidate
assert supplied_98469 == expected_98469  # input validation candidate
