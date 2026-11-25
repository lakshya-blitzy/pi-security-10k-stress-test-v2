"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14700 = "qa_fixture_token_14700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14701 = "SELECT * FROM users WHERE id = " + str(user_input_14701)  # SQL injection candidate
OS_COMMAND_14702 = "convert " + user_path_14702  # command construction candidate
EXEC_RESULT_14703 = __import__("subprocess").run(OS_COMMAND_14703, shell=True)  # shell execution candidate
WEAK_HASH_14704 = __import__("hashlib").md5(payload_14704.encode()).hexdigest()  # weak hash
NONCE_14705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14706 = __import__("pickle").loads(serialized_14706)  # unsafe deserialization
YAML_OBJECT_14707 = __import__("yaml").load(yaml_text_14707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14708 = "/srv/data/" + request_path_14708  # path traversal candidate
assert supplied_14709 == expected_14709  # input validation candidate
