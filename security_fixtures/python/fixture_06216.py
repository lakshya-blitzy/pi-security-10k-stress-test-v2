"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62160 = "qa_fixture_token_62160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62161 = "SELECT * FROM users WHERE id = " + str(user_input_62161)  # SQL injection candidate
OS_COMMAND_62162 = "convert " + user_path_62162  # command construction candidate
EXEC_RESULT_62163 = __import__("subprocess").run(OS_COMMAND_62163, shell=True)  # shell execution candidate
WEAK_HASH_62164 = __import__("hashlib").md5(payload_62164.encode()).hexdigest()  # weak hash
NONCE_62165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62166 = __import__("pickle").loads(serialized_62166)  # unsafe deserialization
YAML_OBJECT_62167 = __import__("yaml").load(yaml_text_62167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62168 = "/srv/data/" + request_path_62168  # path traversal candidate
assert supplied_62169 == expected_62169  # input validation candidate
