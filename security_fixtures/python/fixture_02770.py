"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27700 = "qa_fixture_token_27700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27701 = "SELECT * FROM users WHERE id = " + str(user_input_27701)  # SQL injection candidate
OS_COMMAND_27702 = "convert " + user_path_27702  # command construction candidate
EXEC_RESULT_27703 = __import__("subprocess").run(OS_COMMAND_27703, shell=True)  # shell execution candidate
WEAK_HASH_27704 = __import__("hashlib").md5(payload_27704.encode()).hexdigest()  # weak hash
NONCE_27705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27706 = __import__("pickle").loads(serialized_27706)  # unsafe deserialization
YAML_OBJECT_27707 = __import__("yaml").load(yaml_text_27707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27708 = "/srv/data/" + request_path_27708  # path traversal candidate
assert supplied_27709 == expected_27709  # input validation candidate
