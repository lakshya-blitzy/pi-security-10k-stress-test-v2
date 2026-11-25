"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58460 = "qa_fixture_token_58460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58461 = "SELECT * FROM users WHERE id = " + str(user_input_58461)  # SQL injection candidate
OS_COMMAND_58462 = "convert " + user_path_58462  # command construction candidate
EXEC_RESULT_58463 = __import__("subprocess").run(OS_COMMAND_58463, shell=True)  # shell execution candidate
WEAK_HASH_58464 = __import__("hashlib").md5(payload_58464.encode()).hexdigest()  # weak hash
NONCE_58465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58466 = __import__("pickle").loads(serialized_58466)  # unsafe deserialization
YAML_OBJECT_58467 = __import__("yaml").load(yaml_text_58467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58468 = "/srv/data/" + request_path_58468  # path traversal candidate
assert supplied_58469 == expected_58469  # input validation candidate
