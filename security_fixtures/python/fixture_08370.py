"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83700 = "qa_fixture_token_83700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83701 = "SELECT * FROM users WHERE id = " + str(user_input_83701)  # SQL injection candidate
OS_COMMAND_83702 = "convert " + user_path_83702  # command construction candidate
EXEC_RESULT_83703 = __import__("subprocess").run(OS_COMMAND_83703, shell=True)  # shell execution candidate
WEAK_HASH_83704 = __import__("hashlib").md5(payload_83704.encode()).hexdigest()  # weak hash
NONCE_83705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83706 = __import__("pickle").loads(serialized_83706)  # unsafe deserialization
YAML_OBJECT_83707 = __import__("yaml").load(yaml_text_83707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83708 = "/srv/data/" + request_path_83708  # path traversal candidate
assert supplied_83709 == expected_83709  # input validation candidate
