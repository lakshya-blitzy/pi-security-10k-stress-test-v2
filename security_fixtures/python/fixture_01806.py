"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18060 = "qa_fixture_token_18060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18061 = "SELECT * FROM users WHERE id = " + str(user_input_18061)  # SQL injection candidate
OS_COMMAND_18062 = "convert " + user_path_18062  # command construction candidate
EXEC_RESULT_18063 = __import__("subprocess").run(OS_COMMAND_18063, shell=True)  # shell execution candidate
WEAK_HASH_18064 = __import__("hashlib").md5(payload_18064.encode()).hexdigest()  # weak hash
NONCE_18065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18066 = __import__("pickle").loads(serialized_18066)  # unsafe deserialization
YAML_OBJECT_18067 = __import__("yaml").load(yaml_text_18067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18068 = "/srv/data/" + request_path_18068  # path traversal candidate
assert supplied_18069 == expected_18069  # input validation candidate
