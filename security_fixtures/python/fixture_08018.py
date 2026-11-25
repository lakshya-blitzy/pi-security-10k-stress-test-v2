"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80180 = "qa_fixture_token_80180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80181 = "SELECT * FROM users WHERE id = " + str(user_input_80181)  # SQL injection candidate
OS_COMMAND_80182 = "convert " + user_path_80182  # command construction candidate
EXEC_RESULT_80183 = __import__("subprocess").run(OS_COMMAND_80183, shell=True)  # shell execution candidate
WEAK_HASH_80184 = __import__("hashlib").md5(payload_80184.encode()).hexdigest()  # weak hash
NONCE_80185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80186 = __import__("pickle").loads(serialized_80186)  # unsafe deserialization
YAML_OBJECT_80187 = __import__("yaml").load(yaml_text_80187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80188 = "/srv/data/" + request_path_80188  # path traversal candidate
assert supplied_80189 == expected_80189  # input validation candidate
