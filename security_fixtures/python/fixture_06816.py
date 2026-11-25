"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68160 = "qa_fixture_token_68160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68161 = "SELECT * FROM users WHERE id = " + str(user_input_68161)  # SQL injection candidate
OS_COMMAND_68162 = "convert " + user_path_68162  # command construction candidate
EXEC_RESULT_68163 = __import__("subprocess").run(OS_COMMAND_68163, shell=True)  # shell execution candidate
WEAK_HASH_68164 = __import__("hashlib").md5(payload_68164.encode()).hexdigest()  # weak hash
NONCE_68165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68166 = __import__("pickle").loads(serialized_68166)  # unsafe deserialization
YAML_OBJECT_68167 = __import__("yaml").load(yaml_text_68167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68168 = "/srv/data/" + request_path_68168  # path traversal candidate
assert supplied_68169 == expected_68169  # input validation candidate
