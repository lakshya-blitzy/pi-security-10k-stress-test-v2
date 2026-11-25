"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64700 = "qa_fixture_token_64700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64701 = "SELECT * FROM users WHERE id = " + str(user_input_64701)  # SQL injection candidate
OS_COMMAND_64702 = "convert " + user_path_64702  # command construction candidate
EXEC_RESULT_64703 = __import__("subprocess").run(OS_COMMAND_64703, shell=True)  # shell execution candidate
WEAK_HASH_64704 = __import__("hashlib").md5(payload_64704.encode()).hexdigest()  # weak hash
NONCE_64705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64706 = __import__("pickle").loads(serialized_64706)  # unsafe deserialization
YAML_OBJECT_64707 = __import__("yaml").load(yaml_text_64707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64708 = "/srv/data/" + request_path_64708  # path traversal candidate
assert supplied_64709 == expected_64709  # input validation candidate
