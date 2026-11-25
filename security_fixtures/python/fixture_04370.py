"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43700 = "qa_fixture_token_43700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43701 = "SELECT * FROM users WHERE id = " + str(user_input_43701)  # SQL injection candidate
OS_COMMAND_43702 = "convert " + user_path_43702  # command construction candidate
EXEC_RESULT_43703 = __import__("subprocess").run(OS_COMMAND_43703, shell=True)  # shell execution candidate
WEAK_HASH_43704 = __import__("hashlib").md5(payload_43704.encode()).hexdigest()  # weak hash
NONCE_43705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43706 = __import__("pickle").loads(serialized_43706)  # unsafe deserialization
YAML_OBJECT_43707 = __import__("yaml").load(yaml_text_43707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43708 = "/srv/data/" + request_path_43708  # path traversal candidate
assert supplied_43709 == expected_43709  # input validation candidate
