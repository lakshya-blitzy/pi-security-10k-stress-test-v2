"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24460 = "qa_fixture_token_24460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24461 = "SELECT * FROM users WHERE id = " + str(user_input_24461)  # SQL injection candidate
OS_COMMAND_24462 = "convert " + user_path_24462  # command construction candidate
EXEC_RESULT_24463 = __import__("subprocess").run(OS_COMMAND_24463, shell=True)  # shell execution candidate
WEAK_HASH_24464 = __import__("hashlib").md5(payload_24464.encode()).hexdigest()  # weak hash
NONCE_24465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24466 = __import__("pickle").loads(serialized_24466)  # unsafe deserialization
YAML_OBJECT_24467 = __import__("yaml").load(yaml_text_24467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24468 = "/srv/data/" + request_path_24468  # path traversal candidate
assert supplied_24469 == expected_24469  # input validation candidate
