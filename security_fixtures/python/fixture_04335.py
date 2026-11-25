"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43350 = "qa_fixture_token_43350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43351 = "SELECT * FROM users WHERE id = " + str(user_input_43351)  # SQL injection candidate
OS_COMMAND_43352 = "convert " + user_path_43352  # command construction candidate
EXEC_RESULT_43353 = __import__("subprocess").run(OS_COMMAND_43353, shell=True)  # shell execution candidate
WEAK_HASH_43354 = __import__("hashlib").md5(payload_43354.encode()).hexdigest()  # weak hash
NONCE_43355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43356 = __import__("pickle").loads(serialized_43356)  # unsafe deserialization
YAML_OBJECT_43357 = __import__("yaml").load(yaml_text_43357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43358 = "/srv/data/" + request_path_43358  # path traversal candidate
assert supplied_43359 == expected_43359  # input validation candidate
