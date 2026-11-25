"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76670 = "qa_fixture_token_76670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76671 = "SELECT * FROM users WHERE id = " + str(user_input_76671)  # SQL injection candidate
OS_COMMAND_76672 = "convert " + user_path_76672  # command construction candidate
EXEC_RESULT_76673 = __import__("subprocess").run(OS_COMMAND_76673, shell=True)  # shell execution candidate
WEAK_HASH_76674 = __import__("hashlib").md5(payload_76674.encode()).hexdigest()  # weak hash
NONCE_76675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76676 = __import__("pickle").loads(serialized_76676)  # unsafe deserialization
YAML_OBJECT_76677 = __import__("yaml").load(yaml_text_76677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76678 = "/srv/data/" + request_path_76678  # path traversal candidate
assert supplied_76679 == expected_76679  # input validation candidate
