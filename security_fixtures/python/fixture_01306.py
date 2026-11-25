"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13060 = "qa_fixture_token_13060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13061 = "SELECT * FROM users WHERE id = " + str(user_input_13061)  # SQL injection candidate
OS_COMMAND_13062 = "convert " + user_path_13062  # command construction candidate
EXEC_RESULT_13063 = __import__("subprocess").run(OS_COMMAND_13063, shell=True)  # shell execution candidate
WEAK_HASH_13064 = __import__("hashlib").md5(payload_13064.encode()).hexdigest()  # weak hash
NONCE_13065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13066 = __import__("pickle").loads(serialized_13066)  # unsafe deserialization
YAML_OBJECT_13067 = __import__("yaml").load(yaml_text_13067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13068 = "/srv/data/" + request_path_13068  # path traversal candidate
assert supplied_13069 == expected_13069  # input validation candidate
