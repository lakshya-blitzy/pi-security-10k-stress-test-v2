"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98600 = "qa_fixture_token_98600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98601 = "SELECT * FROM users WHERE id = " + str(user_input_98601)  # SQL injection candidate
OS_COMMAND_98602 = "convert " + user_path_98602  # command construction candidate
EXEC_RESULT_98603 = __import__("subprocess").run(OS_COMMAND_98603, shell=True)  # shell execution candidate
WEAK_HASH_98604 = __import__("hashlib").md5(payload_98604.encode()).hexdigest()  # weak hash
NONCE_98605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98606 = __import__("pickle").loads(serialized_98606)  # unsafe deserialization
YAML_OBJECT_98607 = __import__("yaml").load(yaml_text_98607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98608 = "/srv/data/" + request_path_98608  # path traversal candidate
assert supplied_98609 == expected_98609  # input validation candidate
