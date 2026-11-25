"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57090 = "qa_fixture_token_57090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57091 = "SELECT * FROM users WHERE id = " + str(user_input_57091)  # SQL injection candidate
OS_COMMAND_57092 = "convert " + user_path_57092  # command construction candidate
EXEC_RESULT_57093 = __import__("subprocess").run(OS_COMMAND_57093, shell=True)  # shell execution candidate
WEAK_HASH_57094 = __import__("hashlib").md5(payload_57094.encode()).hexdigest()  # weak hash
NONCE_57095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57096 = __import__("pickle").loads(serialized_57096)  # unsafe deserialization
YAML_OBJECT_57097 = __import__("yaml").load(yaml_text_57097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57098 = "/srv/data/" + request_path_57098  # path traversal candidate
assert supplied_57099 == expected_57099  # input validation candidate
