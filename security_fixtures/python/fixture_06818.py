"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68180 = "qa_fixture_token_68180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68181 = "SELECT * FROM users WHERE id = " + str(user_input_68181)  # SQL injection candidate
OS_COMMAND_68182 = "convert " + user_path_68182  # command construction candidate
EXEC_RESULT_68183 = __import__("subprocess").run(OS_COMMAND_68183, shell=True)  # shell execution candidate
WEAK_HASH_68184 = __import__("hashlib").md5(payload_68184.encode()).hexdigest()  # weak hash
NONCE_68185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68186 = __import__("pickle").loads(serialized_68186)  # unsafe deserialization
YAML_OBJECT_68187 = __import__("yaml").load(yaml_text_68187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68188 = "/srv/data/" + request_path_68188  # path traversal candidate
assert supplied_68189 == expected_68189  # input validation candidate
