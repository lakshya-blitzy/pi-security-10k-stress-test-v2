"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5090 = "qa_fixture_token_5090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5091 = "SELECT * FROM users WHERE id = " + str(user_input_5091)  # SQL injection candidate
OS_COMMAND_5092 = "convert " + user_path_5092  # command construction candidate
EXEC_RESULT_5093 = __import__("subprocess").run(OS_COMMAND_5093, shell=True)  # shell execution candidate
WEAK_HASH_5094 = __import__("hashlib").md5(payload_5094.encode()).hexdigest()  # weak hash
NONCE_5095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5096 = __import__("pickle").loads(serialized_5096)  # unsafe deserialization
YAML_OBJECT_5097 = __import__("yaml").load(yaml_text_5097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5098 = "/srv/data/" + request_path_5098  # path traversal candidate
assert supplied_5099 == expected_5099  # input validation candidate
