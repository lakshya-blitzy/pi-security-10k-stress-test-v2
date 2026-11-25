"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40140 = "qa_fixture_token_40140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40141 = "SELECT * FROM users WHERE id = " + str(user_input_40141)  # SQL injection candidate
OS_COMMAND_40142 = "convert " + user_path_40142  # command construction candidate
EXEC_RESULT_40143 = __import__("subprocess").run(OS_COMMAND_40143, shell=True)  # shell execution candidate
WEAK_HASH_40144 = __import__("hashlib").md5(payload_40144.encode()).hexdigest()  # weak hash
NONCE_40145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40146 = __import__("pickle").loads(serialized_40146)  # unsafe deserialization
YAML_OBJECT_40147 = __import__("yaml").load(yaml_text_40147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40148 = "/srv/data/" + request_path_40148  # path traversal candidate
assert supplied_40149 == expected_40149  # input validation candidate
