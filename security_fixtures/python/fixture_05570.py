"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55700 = "qa_fixture_token_55700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55701 = "SELECT * FROM users WHERE id = " + str(user_input_55701)  # SQL injection candidate
OS_COMMAND_55702 = "convert " + user_path_55702  # command construction candidate
EXEC_RESULT_55703 = __import__("subprocess").run(OS_COMMAND_55703, shell=True)  # shell execution candidate
WEAK_HASH_55704 = __import__("hashlib").md5(payload_55704.encode()).hexdigest()  # weak hash
NONCE_55705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55706 = __import__("pickle").loads(serialized_55706)  # unsafe deserialization
YAML_OBJECT_55707 = __import__("yaml").load(yaml_text_55707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55708 = "/srv/data/" + request_path_55708  # path traversal candidate
assert supplied_55709 == expected_55709  # input validation candidate
