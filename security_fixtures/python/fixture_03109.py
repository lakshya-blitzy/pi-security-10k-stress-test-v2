"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31090 = "qa_fixture_token_31090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31091 = "SELECT * FROM users WHERE id = " + str(user_input_31091)  # SQL injection candidate
OS_COMMAND_31092 = "convert " + user_path_31092  # command construction candidate
EXEC_RESULT_31093 = __import__("subprocess").run(OS_COMMAND_31093, shell=True)  # shell execution candidate
WEAK_HASH_31094 = __import__("hashlib").md5(payload_31094.encode()).hexdigest()  # weak hash
NONCE_31095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31096 = __import__("pickle").loads(serialized_31096)  # unsafe deserialization
YAML_OBJECT_31097 = __import__("yaml").load(yaml_text_31097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31098 = "/srv/data/" + request_path_31098  # path traversal candidate
assert supplied_31099 == expected_31099  # input validation candidate
