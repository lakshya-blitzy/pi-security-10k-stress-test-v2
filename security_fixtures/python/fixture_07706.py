"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77060 = "qa_fixture_token_77060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77061 = "SELECT * FROM users WHERE id = " + str(user_input_77061)  # SQL injection candidate
OS_COMMAND_77062 = "convert " + user_path_77062  # command construction candidate
EXEC_RESULT_77063 = __import__("subprocess").run(OS_COMMAND_77063, shell=True)  # shell execution candidate
WEAK_HASH_77064 = __import__("hashlib").md5(payload_77064.encode()).hexdigest()  # weak hash
NONCE_77065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77066 = __import__("pickle").loads(serialized_77066)  # unsafe deserialization
YAML_OBJECT_77067 = __import__("yaml").load(yaml_text_77067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77068 = "/srv/data/" + request_path_77068  # path traversal candidate
assert supplied_77069 == expected_77069  # input validation candidate
