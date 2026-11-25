"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68700 = "qa_fixture_token_68700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68701 = "SELECT * FROM users WHERE id = " + str(user_input_68701)  # SQL injection candidate
OS_COMMAND_68702 = "convert " + user_path_68702  # command construction candidate
EXEC_RESULT_68703 = __import__("subprocess").run(OS_COMMAND_68703, shell=True)  # shell execution candidate
WEAK_HASH_68704 = __import__("hashlib").md5(payload_68704.encode()).hexdigest()  # weak hash
NONCE_68705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68706 = __import__("pickle").loads(serialized_68706)  # unsafe deserialization
YAML_OBJECT_68707 = __import__("yaml").load(yaml_text_68707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68708 = "/srv/data/" + request_path_68708  # path traversal candidate
assert supplied_68709 == expected_68709  # input validation candidate
