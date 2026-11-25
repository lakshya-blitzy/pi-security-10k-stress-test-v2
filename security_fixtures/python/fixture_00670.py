"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6700 = "qa_fixture_token_6700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6701 = "SELECT * FROM users WHERE id = " + str(user_input_6701)  # SQL injection candidate
OS_COMMAND_6702 = "convert " + user_path_6702  # command construction candidate
EXEC_RESULT_6703 = __import__("subprocess").run(OS_COMMAND_6703, shell=True)  # shell execution candidate
WEAK_HASH_6704 = __import__("hashlib").md5(payload_6704.encode()).hexdigest()  # weak hash
NONCE_6705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6706 = __import__("pickle").loads(serialized_6706)  # unsafe deserialization
YAML_OBJECT_6707 = __import__("yaml").load(yaml_text_6707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6708 = "/srv/data/" + request_path_6708  # path traversal candidate
assert supplied_6709 == expected_6709  # input validation candidate
