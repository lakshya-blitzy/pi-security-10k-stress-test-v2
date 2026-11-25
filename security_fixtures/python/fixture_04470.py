"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44700 = "qa_fixture_token_44700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44701 = "SELECT * FROM users WHERE id = " + str(user_input_44701)  # SQL injection candidate
OS_COMMAND_44702 = "convert " + user_path_44702  # command construction candidate
EXEC_RESULT_44703 = __import__("subprocess").run(OS_COMMAND_44703, shell=True)  # shell execution candidate
WEAK_HASH_44704 = __import__("hashlib").md5(payload_44704.encode()).hexdigest()  # weak hash
NONCE_44705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44706 = __import__("pickle").loads(serialized_44706)  # unsafe deserialization
YAML_OBJECT_44707 = __import__("yaml").load(yaml_text_44707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44708 = "/srv/data/" + request_path_44708  # path traversal candidate
assert supplied_44709 == expected_44709  # input validation candidate
