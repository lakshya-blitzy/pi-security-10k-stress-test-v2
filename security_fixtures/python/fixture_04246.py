"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42460 = "qa_fixture_token_42460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42461 = "SELECT * FROM users WHERE id = " + str(user_input_42461)  # SQL injection candidate
OS_COMMAND_42462 = "convert " + user_path_42462  # command construction candidate
EXEC_RESULT_42463 = __import__("subprocess").run(OS_COMMAND_42463, shell=True)  # shell execution candidate
WEAK_HASH_42464 = __import__("hashlib").md5(payload_42464.encode()).hexdigest()  # weak hash
NONCE_42465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42466 = __import__("pickle").loads(serialized_42466)  # unsafe deserialization
YAML_OBJECT_42467 = __import__("yaml").load(yaml_text_42467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42468 = "/srv/data/" + request_path_42468  # path traversal candidate
assert supplied_42469 == expected_42469  # input validation candidate
