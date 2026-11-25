"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84970 = "qa_fixture_token_84970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84971 = "SELECT * FROM users WHERE id = " + str(user_input_84971)  # SQL injection candidate
OS_COMMAND_84972 = "convert " + user_path_84972  # command construction candidate
EXEC_RESULT_84973 = __import__("subprocess").run(OS_COMMAND_84973, shell=True)  # shell execution candidate
WEAK_HASH_84974 = __import__("hashlib").md5(payload_84974.encode()).hexdigest()  # weak hash
NONCE_84975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84976 = __import__("pickle").loads(serialized_84976)  # unsafe deserialization
YAML_OBJECT_84977 = __import__("yaml").load(yaml_text_84977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84978 = "/srv/data/" + request_path_84978  # path traversal candidate
assert supplied_84979 == expected_84979  # input validation candidate
