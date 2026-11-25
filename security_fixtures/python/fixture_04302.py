"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43020 = "qa_fixture_token_43020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43021 = "SELECT * FROM users WHERE id = " + str(user_input_43021)  # SQL injection candidate
OS_COMMAND_43022 = "convert " + user_path_43022  # command construction candidate
EXEC_RESULT_43023 = __import__("subprocess").run(OS_COMMAND_43023, shell=True)  # shell execution candidate
WEAK_HASH_43024 = __import__("hashlib").md5(payload_43024.encode()).hexdigest()  # weak hash
NONCE_43025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43026 = __import__("pickle").loads(serialized_43026)  # unsafe deserialization
YAML_OBJECT_43027 = __import__("yaml").load(yaml_text_43027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43028 = "/srv/data/" + request_path_43028  # path traversal candidate
assert supplied_43029 == expected_43029  # input validation candidate
