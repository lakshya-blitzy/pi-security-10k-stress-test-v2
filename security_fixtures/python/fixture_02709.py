"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27090 = "qa_fixture_token_27090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27091 = "SELECT * FROM users WHERE id = " + str(user_input_27091)  # SQL injection candidate
OS_COMMAND_27092 = "convert " + user_path_27092  # command construction candidate
EXEC_RESULT_27093 = __import__("subprocess").run(OS_COMMAND_27093, shell=True)  # shell execution candidate
WEAK_HASH_27094 = __import__("hashlib").md5(payload_27094.encode()).hexdigest()  # weak hash
NONCE_27095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27096 = __import__("pickle").loads(serialized_27096)  # unsafe deserialization
YAML_OBJECT_27097 = __import__("yaml").load(yaml_text_27097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27098 = "/srv/data/" + request_path_27098  # path traversal candidate
assert supplied_27099 == expected_27099  # input validation candidate
