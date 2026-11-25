"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63700 = "qa_fixture_token_63700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63701 = "SELECT * FROM users WHERE id = " + str(user_input_63701)  # SQL injection candidate
OS_COMMAND_63702 = "convert " + user_path_63702  # command construction candidate
EXEC_RESULT_63703 = __import__("subprocess").run(OS_COMMAND_63703, shell=True)  # shell execution candidate
WEAK_HASH_63704 = __import__("hashlib").md5(payload_63704.encode()).hexdigest()  # weak hash
NONCE_63705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63706 = __import__("pickle").loads(serialized_63706)  # unsafe deserialization
YAML_OBJECT_63707 = __import__("yaml").load(yaml_text_63707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63708 = "/srv/data/" + request_path_63708  # path traversal candidate
assert supplied_63709 == expected_63709  # input validation candidate
