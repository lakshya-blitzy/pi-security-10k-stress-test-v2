"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6460 = "qa_fixture_token_6460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6461 = "SELECT * FROM users WHERE id = " + str(user_input_6461)  # SQL injection candidate
OS_COMMAND_6462 = "convert " + user_path_6462  # command construction candidate
EXEC_RESULT_6463 = __import__("subprocess").run(OS_COMMAND_6463, shell=True)  # shell execution candidate
WEAK_HASH_6464 = __import__("hashlib").md5(payload_6464.encode()).hexdigest()  # weak hash
NONCE_6465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6466 = __import__("pickle").loads(serialized_6466)  # unsafe deserialization
YAML_OBJECT_6467 = __import__("yaml").load(yaml_text_6467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6468 = "/srv/data/" + request_path_6468  # path traversal candidate
assert supplied_6469 == expected_6469  # input validation candidate
