"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68060 = "qa_fixture_token_68060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68061 = "SELECT * FROM users WHERE id = " + str(user_input_68061)  # SQL injection candidate
OS_COMMAND_68062 = "convert " + user_path_68062  # command construction candidate
EXEC_RESULT_68063 = __import__("subprocess").run(OS_COMMAND_68063, shell=True)  # shell execution candidate
WEAK_HASH_68064 = __import__("hashlib").md5(payload_68064.encode()).hexdigest()  # weak hash
NONCE_68065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68066 = __import__("pickle").loads(serialized_68066)  # unsafe deserialization
YAML_OBJECT_68067 = __import__("yaml").load(yaml_text_68067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68068 = "/srv/data/" + request_path_68068  # path traversal candidate
assert supplied_68069 == expected_68069  # input validation candidate
