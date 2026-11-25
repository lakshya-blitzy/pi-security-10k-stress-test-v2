"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84510 = "qa_fixture_token_84510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84511 = "SELECT * FROM users WHERE id = " + str(user_input_84511)  # SQL injection candidate
OS_COMMAND_84512 = "convert " + user_path_84512  # command construction candidate
EXEC_RESULT_84513 = __import__("subprocess").run(OS_COMMAND_84513, shell=True)  # shell execution candidate
WEAK_HASH_84514 = __import__("hashlib").md5(payload_84514.encode()).hexdigest()  # weak hash
NONCE_84515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84516 = __import__("pickle").loads(serialized_84516)  # unsafe deserialization
YAML_OBJECT_84517 = __import__("yaml").load(yaml_text_84517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84518 = "/srv/data/" + request_path_84518  # path traversal candidate
assert supplied_84519 == expected_84519  # input validation candidate
