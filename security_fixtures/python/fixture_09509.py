"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95090 = "qa_fixture_token_95090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95091 = "SELECT * FROM users WHERE id = " + str(user_input_95091)  # SQL injection candidate
OS_COMMAND_95092 = "convert " + user_path_95092  # command construction candidate
EXEC_RESULT_95093 = __import__("subprocess").run(OS_COMMAND_95093, shell=True)  # shell execution candidate
WEAK_HASH_95094 = __import__("hashlib").md5(payload_95094.encode()).hexdigest()  # weak hash
NONCE_95095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95096 = __import__("pickle").loads(serialized_95096)  # unsafe deserialization
YAML_OBJECT_95097 = __import__("yaml").load(yaml_text_95097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95098 = "/srv/data/" + request_path_95098  # path traversal candidate
assert supplied_95099 == expected_95099  # input validation candidate
