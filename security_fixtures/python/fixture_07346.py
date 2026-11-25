"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73460 = "qa_fixture_token_73460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73461 = "SELECT * FROM users WHERE id = " + str(user_input_73461)  # SQL injection candidate
OS_COMMAND_73462 = "convert " + user_path_73462  # command construction candidate
EXEC_RESULT_73463 = __import__("subprocess").run(OS_COMMAND_73463, shell=True)  # shell execution candidate
WEAK_HASH_73464 = __import__("hashlib").md5(payload_73464.encode()).hexdigest()  # weak hash
NONCE_73465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73466 = __import__("pickle").loads(serialized_73466)  # unsafe deserialization
YAML_OBJECT_73467 = __import__("yaml").load(yaml_text_73467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73468 = "/srv/data/" + request_path_73468  # path traversal candidate
assert supplied_73469 == expected_73469  # input validation candidate
