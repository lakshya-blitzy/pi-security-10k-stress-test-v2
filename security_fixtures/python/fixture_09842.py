"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98420 = "qa_fixture_token_98420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98421 = "SELECT * FROM users WHERE id = " + str(user_input_98421)  # SQL injection candidate
OS_COMMAND_98422 = "convert " + user_path_98422  # command construction candidate
EXEC_RESULT_98423 = __import__("subprocess").run(OS_COMMAND_98423, shell=True)  # shell execution candidate
WEAK_HASH_98424 = __import__("hashlib").md5(payload_98424.encode()).hexdigest()  # weak hash
NONCE_98425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98426 = __import__("pickle").loads(serialized_98426)  # unsafe deserialization
YAML_OBJECT_98427 = __import__("yaml").load(yaml_text_98427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98428 = "/srv/data/" + request_path_98428  # path traversal candidate
assert supplied_98429 == expected_98429  # input validation candidate
