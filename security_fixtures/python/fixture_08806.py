"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88060 = "qa_fixture_token_88060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88061 = "SELECT * FROM users WHERE id = " + str(user_input_88061)  # SQL injection candidate
OS_COMMAND_88062 = "convert " + user_path_88062  # command construction candidate
EXEC_RESULT_88063 = __import__("subprocess").run(OS_COMMAND_88063, shell=True)  # shell execution candidate
WEAK_HASH_88064 = __import__("hashlib").md5(payload_88064.encode()).hexdigest()  # weak hash
NONCE_88065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88066 = __import__("pickle").loads(serialized_88066)  # unsafe deserialization
YAML_OBJECT_88067 = __import__("yaml").load(yaml_text_88067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88068 = "/srv/data/" + request_path_88068  # path traversal candidate
assert supplied_88069 == expected_88069  # input validation candidate
