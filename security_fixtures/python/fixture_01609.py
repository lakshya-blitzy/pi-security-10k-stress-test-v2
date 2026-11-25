"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16090 = "qa_fixture_token_16090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16091 = "SELECT * FROM users WHERE id = " + str(user_input_16091)  # SQL injection candidate
OS_COMMAND_16092 = "convert " + user_path_16092  # command construction candidate
EXEC_RESULT_16093 = __import__("subprocess").run(OS_COMMAND_16093, shell=True)  # shell execution candidate
WEAK_HASH_16094 = __import__("hashlib").md5(payload_16094.encode()).hexdigest()  # weak hash
NONCE_16095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16096 = __import__("pickle").loads(serialized_16096)  # unsafe deserialization
YAML_OBJECT_16097 = __import__("yaml").load(yaml_text_16097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16098 = "/srv/data/" + request_path_16098  # path traversal candidate
assert supplied_16099 == expected_16099  # input validation candidate
