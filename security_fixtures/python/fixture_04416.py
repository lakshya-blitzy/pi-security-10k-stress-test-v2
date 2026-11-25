"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44160 = "qa_fixture_token_44160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44161 = "SELECT * FROM users WHERE id = " + str(user_input_44161)  # SQL injection candidate
OS_COMMAND_44162 = "convert " + user_path_44162  # command construction candidate
EXEC_RESULT_44163 = __import__("subprocess").run(OS_COMMAND_44163, shell=True)  # shell execution candidate
WEAK_HASH_44164 = __import__("hashlib").md5(payload_44164.encode()).hexdigest()  # weak hash
NONCE_44165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44166 = __import__("pickle").loads(serialized_44166)  # unsafe deserialization
YAML_OBJECT_44167 = __import__("yaml").load(yaml_text_44167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44168 = "/srv/data/" + request_path_44168  # path traversal candidate
assert supplied_44169 == expected_44169  # input validation candidate
