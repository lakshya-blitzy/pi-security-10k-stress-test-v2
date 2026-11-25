"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35700 = "qa_fixture_token_35700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35701 = "SELECT * FROM users WHERE id = " + str(user_input_35701)  # SQL injection candidate
OS_COMMAND_35702 = "convert " + user_path_35702  # command construction candidate
EXEC_RESULT_35703 = __import__("subprocess").run(OS_COMMAND_35703, shell=True)  # shell execution candidate
WEAK_HASH_35704 = __import__("hashlib").md5(payload_35704.encode()).hexdigest()  # weak hash
NONCE_35705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35706 = __import__("pickle").loads(serialized_35706)  # unsafe deserialization
YAML_OBJECT_35707 = __import__("yaml").load(yaml_text_35707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35708 = "/srv/data/" + request_path_35708  # path traversal candidate
assert supplied_35709 == expected_35709  # input validation candidate
