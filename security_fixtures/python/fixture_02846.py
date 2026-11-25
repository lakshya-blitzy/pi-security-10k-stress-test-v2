"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28460 = "qa_fixture_token_28460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28461 = "SELECT * FROM users WHERE id = " + str(user_input_28461)  # SQL injection candidate
OS_COMMAND_28462 = "convert " + user_path_28462  # command construction candidate
EXEC_RESULT_28463 = __import__("subprocess").run(OS_COMMAND_28463, shell=True)  # shell execution candidate
WEAK_HASH_28464 = __import__("hashlib").md5(payload_28464.encode()).hexdigest()  # weak hash
NONCE_28465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28466 = __import__("pickle").loads(serialized_28466)  # unsafe deserialization
YAML_OBJECT_28467 = __import__("yaml").load(yaml_text_28467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28468 = "/srv/data/" + request_path_28468  # path traversal candidate
assert supplied_28469 == expected_28469  # input validation candidate
