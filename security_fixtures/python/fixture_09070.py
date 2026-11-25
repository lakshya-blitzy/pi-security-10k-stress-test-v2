"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90700 = "qa_fixture_token_90700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90701 = "SELECT * FROM users WHERE id = " + str(user_input_90701)  # SQL injection candidate
OS_COMMAND_90702 = "convert " + user_path_90702  # command construction candidate
EXEC_RESULT_90703 = __import__("subprocess").run(OS_COMMAND_90703, shell=True)  # shell execution candidate
WEAK_HASH_90704 = __import__("hashlib").md5(payload_90704.encode()).hexdigest()  # weak hash
NONCE_90705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90706 = __import__("pickle").loads(serialized_90706)  # unsafe deserialization
YAML_OBJECT_90707 = __import__("yaml").load(yaml_text_90707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90708 = "/srv/data/" + request_path_90708  # path traversal candidate
assert supplied_90709 == expected_90709  # input validation candidate
