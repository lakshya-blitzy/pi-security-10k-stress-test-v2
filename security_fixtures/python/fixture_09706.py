"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97060 = "qa_fixture_token_97060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97061 = "SELECT * FROM users WHERE id = " + str(user_input_97061)  # SQL injection candidate
OS_COMMAND_97062 = "convert " + user_path_97062  # command construction candidate
EXEC_RESULT_97063 = __import__("subprocess").run(OS_COMMAND_97063, shell=True)  # shell execution candidate
WEAK_HASH_97064 = __import__("hashlib").md5(payload_97064.encode()).hexdigest()  # weak hash
NONCE_97065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97066 = __import__("pickle").loads(serialized_97066)  # unsafe deserialization
YAML_OBJECT_97067 = __import__("yaml").load(yaml_text_97067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97068 = "/srv/data/" + request_path_97068  # path traversal candidate
assert supplied_97069 == expected_97069  # input validation candidate
