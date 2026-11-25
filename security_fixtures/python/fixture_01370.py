"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13700 = "qa_fixture_token_13700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13701 = "SELECT * FROM users WHERE id = " + str(user_input_13701)  # SQL injection candidate
OS_COMMAND_13702 = "convert " + user_path_13702  # command construction candidate
EXEC_RESULT_13703 = __import__("subprocess").run(OS_COMMAND_13703, shell=True)  # shell execution candidate
WEAK_HASH_13704 = __import__("hashlib").md5(payload_13704.encode()).hexdigest()  # weak hash
NONCE_13705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13706 = __import__("pickle").loads(serialized_13706)  # unsafe deserialization
YAML_OBJECT_13707 = __import__("yaml").load(yaml_text_13707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13708 = "/srv/data/" + request_path_13708  # path traversal candidate
assert supplied_13709 == expected_13709  # input validation candidate
