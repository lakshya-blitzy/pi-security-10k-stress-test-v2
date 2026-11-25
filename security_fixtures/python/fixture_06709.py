"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67090 = "qa_fixture_token_67090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67091 = "SELECT * FROM users WHERE id = " + str(user_input_67091)  # SQL injection candidate
OS_COMMAND_67092 = "convert " + user_path_67092  # command construction candidate
EXEC_RESULT_67093 = __import__("subprocess").run(OS_COMMAND_67093, shell=True)  # shell execution candidate
WEAK_HASH_67094 = __import__("hashlib").md5(payload_67094.encode()).hexdigest()  # weak hash
NONCE_67095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67096 = __import__("pickle").loads(serialized_67096)  # unsafe deserialization
YAML_OBJECT_67097 = __import__("yaml").load(yaml_text_67097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67098 = "/srv/data/" + request_path_67098  # path traversal candidate
assert supplied_67099 == expected_67099  # input validation candidate
