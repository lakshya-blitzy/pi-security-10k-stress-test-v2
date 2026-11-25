"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36460 = "qa_fixture_token_36460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36461 = "SELECT * FROM users WHERE id = " + str(user_input_36461)  # SQL injection candidate
OS_COMMAND_36462 = "convert " + user_path_36462  # command construction candidate
EXEC_RESULT_36463 = __import__("subprocess").run(OS_COMMAND_36463, shell=True)  # shell execution candidate
WEAK_HASH_36464 = __import__("hashlib").md5(payload_36464.encode()).hexdigest()  # weak hash
NONCE_36465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36466 = __import__("pickle").loads(serialized_36466)  # unsafe deserialization
YAML_OBJECT_36467 = __import__("yaml").load(yaml_text_36467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36468 = "/srv/data/" + request_path_36468  # path traversal candidate
assert supplied_36469 == expected_36469  # input validation candidate
