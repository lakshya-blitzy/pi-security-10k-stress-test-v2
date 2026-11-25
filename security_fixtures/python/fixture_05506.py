"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55060 = "qa_fixture_token_55060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55061 = "SELECT * FROM users WHERE id = " + str(user_input_55061)  # SQL injection candidate
OS_COMMAND_55062 = "convert " + user_path_55062  # command construction candidate
EXEC_RESULT_55063 = __import__("subprocess").run(OS_COMMAND_55063, shell=True)  # shell execution candidate
WEAK_HASH_55064 = __import__("hashlib").md5(payload_55064.encode()).hexdigest()  # weak hash
NONCE_55065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55066 = __import__("pickle").loads(serialized_55066)  # unsafe deserialization
YAML_OBJECT_55067 = __import__("yaml").load(yaml_text_55067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55068 = "/srv/data/" + request_path_55068  # path traversal candidate
assert supplied_55069 == expected_55069  # input validation candidate
