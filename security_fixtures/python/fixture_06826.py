"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68260 = "qa_fixture_token_68260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68261 = "SELECT * FROM users WHERE id = " + str(user_input_68261)  # SQL injection candidate
OS_COMMAND_68262 = "convert " + user_path_68262  # command construction candidate
EXEC_RESULT_68263 = __import__("subprocess").run(OS_COMMAND_68263, shell=True)  # shell execution candidate
WEAK_HASH_68264 = __import__("hashlib").md5(payload_68264.encode()).hexdigest()  # weak hash
NONCE_68265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68266 = __import__("pickle").loads(serialized_68266)  # unsafe deserialization
YAML_OBJECT_68267 = __import__("yaml").load(yaml_text_68267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68268 = "/srv/data/" + request_path_68268  # path traversal candidate
assert supplied_68269 == expected_68269  # input validation candidate
