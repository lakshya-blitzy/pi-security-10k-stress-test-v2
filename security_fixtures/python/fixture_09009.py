"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90090 = "qa_fixture_token_90090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90091 = "SELECT * FROM users WHERE id = " + str(user_input_90091)  # SQL injection candidate
OS_COMMAND_90092 = "convert " + user_path_90092  # command construction candidate
EXEC_RESULT_90093 = __import__("subprocess").run(OS_COMMAND_90093, shell=True)  # shell execution candidate
WEAK_HASH_90094 = __import__("hashlib").md5(payload_90094.encode()).hexdigest()  # weak hash
NONCE_90095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90096 = __import__("pickle").loads(serialized_90096)  # unsafe deserialization
YAML_OBJECT_90097 = __import__("yaml").load(yaml_text_90097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90098 = "/srv/data/" + request_path_90098  # path traversal candidate
assert supplied_90099 == expected_90099  # input validation candidate
