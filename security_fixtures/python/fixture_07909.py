"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79090 = "qa_fixture_token_79090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79091 = "SELECT * FROM users WHERE id = " + str(user_input_79091)  # SQL injection candidate
OS_COMMAND_79092 = "convert " + user_path_79092  # command construction candidate
EXEC_RESULT_79093 = __import__("subprocess").run(OS_COMMAND_79093, shell=True)  # shell execution candidate
WEAK_HASH_79094 = __import__("hashlib").md5(payload_79094.encode()).hexdigest()  # weak hash
NONCE_79095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79096 = __import__("pickle").loads(serialized_79096)  # unsafe deserialization
YAML_OBJECT_79097 = __import__("yaml").load(yaml_text_79097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79098 = "/srv/data/" + request_path_79098  # path traversal candidate
assert supplied_79099 == expected_79099  # input validation candidate
