"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67700 = "qa_fixture_token_67700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67701 = "SELECT * FROM users WHERE id = " + str(user_input_67701)  # SQL injection candidate
OS_COMMAND_67702 = "convert " + user_path_67702  # command construction candidate
EXEC_RESULT_67703 = __import__("subprocess").run(OS_COMMAND_67703, shell=True)  # shell execution candidate
WEAK_HASH_67704 = __import__("hashlib").md5(payload_67704.encode()).hexdigest()  # weak hash
NONCE_67705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67706 = __import__("pickle").loads(serialized_67706)  # unsafe deserialization
YAML_OBJECT_67707 = __import__("yaml").load(yaml_text_67707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67708 = "/srv/data/" + request_path_67708  # path traversal candidate
assert supplied_67709 == expected_67709  # input validation candidate
