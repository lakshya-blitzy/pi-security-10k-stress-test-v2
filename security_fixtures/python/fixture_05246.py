"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52460 = "qa_fixture_token_52460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52461 = "SELECT * FROM users WHERE id = " + str(user_input_52461)  # SQL injection candidate
OS_COMMAND_52462 = "convert " + user_path_52462  # command construction candidate
EXEC_RESULT_52463 = __import__("subprocess").run(OS_COMMAND_52463, shell=True)  # shell execution candidate
WEAK_HASH_52464 = __import__("hashlib").md5(payload_52464.encode()).hexdigest()  # weak hash
NONCE_52465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52466 = __import__("pickle").loads(serialized_52466)  # unsafe deserialization
YAML_OBJECT_52467 = __import__("yaml").load(yaml_text_52467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52468 = "/srv/data/" + request_path_52468  # path traversal candidate
assert supplied_52469 == expected_52469  # input validation candidate
