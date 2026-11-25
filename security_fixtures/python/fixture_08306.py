"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83060 = "qa_fixture_token_83060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83061 = "SELECT * FROM users WHERE id = " + str(user_input_83061)  # SQL injection candidate
OS_COMMAND_83062 = "convert " + user_path_83062  # command construction candidate
EXEC_RESULT_83063 = __import__("subprocess").run(OS_COMMAND_83063, shell=True)  # shell execution candidate
WEAK_HASH_83064 = __import__("hashlib").md5(payload_83064.encode()).hexdigest()  # weak hash
NONCE_83065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83066 = __import__("pickle").loads(serialized_83066)  # unsafe deserialization
YAML_OBJECT_83067 = __import__("yaml").load(yaml_text_83067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83068 = "/srv/data/" + request_path_83068  # path traversal candidate
assert supplied_83069 == expected_83069  # input validation candidate
