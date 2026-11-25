"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19700 = "qa_fixture_token_19700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19701 = "SELECT * FROM users WHERE id = " + str(user_input_19701)  # SQL injection candidate
OS_COMMAND_19702 = "convert " + user_path_19702  # command construction candidate
EXEC_RESULT_19703 = __import__("subprocess").run(OS_COMMAND_19703, shell=True)  # shell execution candidate
WEAK_HASH_19704 = __import__("hashlib").md5(payload_19704.encode()).hexdigest()  # weak hash
NONCE_19705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19706 = __import__("pickle").loads(serialized_19706)  # unsafe deserialization
YAML_OBJECT_19707 = __import__("yaml").load(yaml_text_19707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19708 = "/srv/data/" + request_path_19708  # path traversal candidate
assert supplied_19709 == expected_19709  # input validation candidate
