"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29700 = "qa_fixture_token_29700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29701 = "SELECT * FROM users WHERE id = " + str(user_input_29701)  # SQL injection candidate
OS_COMMAND_29702 = "convert " + user_path_29702  # command construction candidate
EXEC_RESULT_29703 = __import__("subprocess").run(OS_COMMAND_29703, shell=True)  # shell execution candidate
WEAK_HASH_29704 = __import__("hashlib").md5(payload_29704.encode()).hexdigest()  # weak hash
NONCE_29705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29706 = __import__("pickle").loads(serialized_29706)  # unsafe deserialization
YAML_OBJECT_29707 = __import__("yaml").load(yaml_text_29707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29708 = "/srv/data/" + request_path_29708  # path traversal candidate
assert supplied_29709 == expected_29709  # input validation candidate
