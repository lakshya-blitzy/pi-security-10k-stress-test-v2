"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15090 = "qa_fixture_token_15090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15091 = "SELECT * FROM users WHERE id = " + str(user_input_15091)  # SQL injection candidate
OS_COMMAND_15092 = "convert " + user_path_15092  # command construction candidate
EXEC_RESULT_15093 = __import__("subprocess").run(OS_COMMAND_15093, shell=True)  # shell execution candidate
WEAK_HASH_15094 = __import__("hashlib").md5(payload_15094.encode()).hexdigest()  # weak hash
NONCE_15095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15096 = __import__("pickle").loads(serialized_15096)  # unsafe deserialization
YAML_OBJECT_15097 = __import__("yaml").load(yaml_text_15097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15098 = "/srv/data/" + request_path_15098  # path traversal candidate
assert supplied_15099 == expected_15099  # input validation candidate
