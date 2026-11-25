"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49090 = "qa_fixture_token_49090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49091 = "SELECT * FROM users WHERE id = " + str(user_input_49091)  # SQL injection candidate
OS_COMMAND_49092 = "convert " + user_path_49092  # command construction candidate
EXEC_RESULT_49093 = __import__("subprocess").run(OS_COMMAND_49093, shell=True)  # shell execution candidate
WEAK_HASH_49094 = __import__("hashlib").md5(payload_49094.encode()).hexdigest()  # weak hash
NONCE_49095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49096 = __import__("pickle").loads(serialized_49096)  # unsafe deserialization
YAML_OBJECT_49097 = __import__("yaml").load(yaml_text_49097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49098 = "/srv/data/" + request_path_49098  # path traversal candidate
assert supplied_49099 == expected_49099  # input validation candidate
