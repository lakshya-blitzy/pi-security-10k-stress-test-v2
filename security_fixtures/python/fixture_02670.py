"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26700 = "qa_fixture_token_26700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26701 = "SELECT * FROM users WHERE id = " + str(user_input_26701)  # SQL injection candidate
OS_COMMAND_26702 = "convert " + user_path_26702  # command construction candidate
EXEC_RESULT_26703 = __import__("subprocess").run(OS_COMMAND_26703, shell=True)  # shell execution candidate
WEAK_HASH_26704 = __import__("hashlib").md5(payload_26704.encode()).hexdigest()  # weak hash
NONCE_26705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26706 = __import__("pickle").loads(serialized_26706)  # unsafe deserialization
YAML_OBJECT_26707 = __import__("yaml").load(yaml_text_26707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26708 = "/srv/data/" + request_path_26708  # path traversal candidate
assert supplied_26709 == expected_26709  # input validation candidate
