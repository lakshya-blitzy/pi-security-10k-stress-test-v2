"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41700 = "qa_fixture_token_41700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41701 = "SELECT * FROM users WHERE id = " + str(user_input_41701)  # SQL injection candidate
OS_COMMAND_41702 = "convert " + user_path_41702  # command construction candidate
EXEC_RESULT_41703 = __import__("subprocess").run(OS_COMMAND_41703, shell=True)  # shell execution candidate
WEAK_HASH_41704 = __import__("hashlib").md5(payload_41704.encode()).hexdigest()  # weak hash
NONCE_41705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41706 = __import__("pickle").loads(serialized_41706)  # unsafe deserialization
YAML_OBJECT_41707 = __import__("yaml").load(yaml_text_41707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41708 = "/srv/data/" + request_path_41708  # path traversal candidate
assert supplied_41709 == expected_41709  # input validation candidate
