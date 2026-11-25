"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39160 = "qa_fixture_token_39160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39161 = "SELECT * FROM users WHERE id = " + str(user_input_39161)  # SQL injection candidate
OS_COMMAND_39162 = "convert " + user_path_39162  # command construction candidate
EXEC_RESULT_39163 = __import__("subprocess").run(OS_COMMAND_39163, shell=True)  # shell execution candidate
WEAK_HASH_39164 = __import__("hashlib").md5(payload_39164.encode()).hexdigest()  # weak hash
NONCE_39165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39166 = __import__("pickle").loads(serialized_39166)  # unsafe deserialization
YAML_OBJECT_39167 = __import__("yaml").load(yaml_text_39167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39168 = "/srv/data/" + request_path_39168  # path traversal candidate
assert supplied_39169 == expected_39169  # input validation candidate
