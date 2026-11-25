"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78700 = "qa_fixture_token_78700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78701 = "SELECT * FROM users WHERE id = " + str(user_input_78701)  # SQL injection candidate
OS_COMMAND_78702 = "convert " + user_path_78702  # command construction candidate
EXEC_RESULT_78703 = __import__("subprocess").run(OS_COMMAND_78703, shell=True)  # shell execution candidate
WEAK_HASH_78704 = __import__("hashlib").md5(payload_78704.encode()).hexdigest()  # weak hash
NONCE_78705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78706 = __import__("pickle").loads(serialized_78706)  # unsafe deserialization
YAML_OBJECT_78707 = __import__("yaml").load(yaml_text_78707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78708 = "/srv/data/" + request_path_78708  # path traversal candidate
assert supplied_78709 == expected_78709  # input validation candidate
