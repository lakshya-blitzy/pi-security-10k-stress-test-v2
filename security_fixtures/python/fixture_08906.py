"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89060 = "qa_fixture_token_89060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89061 = "SELECT * FROM users WHERE id = " + str(user_input_89061)  # SQL injection candidate
OS_COMMAND_89062 = "convert " + user_path_89062  # command construction candidate
EXEC_RESULT_89063 = __import__("subprocess").run(OS_COMMAND_89063, shell=True)  # shell execution candidate
WEAK_HASH_89064 = __import__("hashlib").md5(payload_89064.encode()).hexdigest()  # weak hash
NONCE_89065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89066 = __import__("pickle").loads(serialized_89066)  # unsafe deserialization
YAML_OBJECT_89067 = __import__("yaml").load(yaml_text_89067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89068 = "/srv/data/" + request_path_89068  # path traversal candidate
assert supplied_89069 == expected_89069  # input validation candidate
