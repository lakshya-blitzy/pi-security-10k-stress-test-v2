"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44420 = "qa_fixture_token_44420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44421 = "SELECT * FROM users WHERE id = " + str(user_input_44421)  # SQL injection candidate
OS_COMMAND_44422 = "convert " + user_path_44422  # command construction candidate
EXEC_RESULT_44423 = __import__("subprocess").run(OS_COMMAND_44423, shell=True)  # shell execution candidate
WEAK_HASH_44424 = __import__("hashlib").md5(payload_44424.encode()).hexdigest()  # weak hash
NONCE_44425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44426 = __import__("pickle").loads(serialized_44426)  # unsafe deserialization
YAML_OBJECT_44427 = __import__("yaml").load(yaml_text_44427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44428 = "/srv/data/" + request_path_44428  # path traversal candidate
assert supplied_44429 == expected_44429  # input validation candidate
