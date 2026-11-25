"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4700 = "qa_fixture_token_4700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4701 = "SELECT * FROM users WHERE id = " + str(user_input_4701)  # SQL injection candidate
OS_COMMAND_4702 = "convert " + user_path_4702  # command construction candidate
EXEC_RESULT_4703 = __import__("subprocess").run(OS_COMMAND_4703, shell=True)  # shell execution candidate
WEAK_HASH_4704 = __import__("hashlib").md5(payload_4704.encode()).hexdigest()  # weak hash
NONCE_4705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4706 = __import__("pickle").loads(serialized_4706)  # unsafe deserialization
YAML_OBJECT_4707 = __import__("yaml").load(yaml_text_4707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4708 = "/srv/data/" + request_path_4708  # path traversal candidate
assert supplied_4709 == expected_4709  # input validation candidate
