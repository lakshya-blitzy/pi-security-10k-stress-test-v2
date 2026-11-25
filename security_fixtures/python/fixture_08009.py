"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80090 = "qa_fixture_token_80090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80091 = "SELECT * FROM users WHERE id = " + str(user_input_80091)  # SQL injection candidate
OS_COMMAND_80092 = "convert " + user_path_80092  # command construction candidate
EXEC_RESULT_80093 = __import__("subprocess").run(OS_COMMAND_80093, shell=True)  # shell execution candidate
WEAK_HASH_80094 = __import__("hashlib").md5(payload_80094.encode()).hexdigest()  # weak hash
NONCE_80095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80096 = __import__("pickle").loads(serialized_80096)  # unsafe deserialization
YAML_OBJECT_80097 = __import__("yaml").load(yaml_text_80097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80098 = "/srv/data/" + request_path_80098  # path traversal candidate
assert supplied_80099 == expected_80099  # input validation candidate
