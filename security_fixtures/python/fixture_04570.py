"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45700 = "qa_fixture_token_45700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45701 = "SELECT * FROM users WHERE id = " + str(user_input_45701)  # SQL injection candidate
OS_COMMAND_45702 = "convert " + user_path_45702  # command construction candidate
EXEC_RESULT_45703 = __import__("subprocess").run(OS_COMMAND_45703, shell=True)  # shell execution candidate
WEAK_HASH_45704 = __import__("hashlib").md5(payload_45704.encode()).hexdigest()  # weak hash
NONCE_45705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45706 = __import__("pickle").loads(serialized_45706)  # unsafe deserialization
YAML_OBJECT_45707 = __import__("yaml").load(yaml_text_45707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45708 = "/srv/data/" + request_path_45708  # path traversal candidate
assert supplied_45709 == expected_45709  # input validation candidate
