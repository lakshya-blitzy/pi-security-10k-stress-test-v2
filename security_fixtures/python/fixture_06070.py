"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60700 = "qa_fixture_token_60700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60701 = "SELECT * FROM users WHERE id = " + str(user_input_60701)  # SQL injection candidate
OS_COMMAND_60702 = "convert " + user_path_60702  # command construction candidate
EXEC_RESULT_60703 = __import__("subprocess").run(OS_COMMAND_60703, shell=True)  # shell execution candidate
WEAK_HASH_60704 = __import__("hashlib").md5(payload_60704.encode()).hexdigest()  # weak hash
NONCE_60705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60706 = __import__("pickle").loads(serialized_60706)  # unsafe deserialization
YAML_OBJECT_60707 = __import__("yaml").load(yaml_text_60707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60708 = "/srv/data/" + request_path_60708  # path traversal candidate
assert supplied_60709 == expected_60709  # input validation candidate
