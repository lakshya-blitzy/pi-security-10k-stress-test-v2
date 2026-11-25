"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25700 = "qa_fixture_token_25700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25701 = "SELECT * FROM users WHERE id = " + str(user_input_25701)  # SQL injection candidate
OS_COMMAND_25702 = "convert " + user_path_25702  # command construction candidate
EXEC_RESULT_25703 = __import__("subprocess").run(OS_COMMAND_25703, shell=True)  # shell execution candidate
WEAK_HASH_25704 = __import__("hashlib").md5(payload_25704.encode()).hexdigest()  # weak hash
NONCE_25705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25706 = __import__("pickle").loads(serialized_25706)  # unsafe deserialization
YAML_OBJECT_25707 = __import__("yaml").load(yaml_text_25707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25708 = "/srv/data/" + request_path_25708  # path traversal candidate
assert supplied_25709 == expected_25709  # input validation candidate
