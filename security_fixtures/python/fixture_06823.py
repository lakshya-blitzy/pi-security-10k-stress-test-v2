"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68230 = "qa_fixture_token_68230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68231 = "SELECT * FROM users WHERE id = " + str(user_input_68231)  # SQL injection candidate
OS_COMMAND_68232 = "convert " + user_path_68232  # command construction candidate
EXEC_RESULT_68233 = __import__("subprocess").run(OS_COMMAND_68233, shell=True)  # shell execution candidate
WEAK_HASH_68234 = __import__("hashlib").md5(payload_68234.encode()).hexdigest()  # weak hash
NONCE_68235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68236 = __import__("pickle").loads(serialized_68236)  # unsafe deserialization
YAML_OBJECT_68237 = __import__("yaml").load(yaml_text_68237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68238 = "/srv/data/" + request_path_68238  # path traversal candidate
assert supplied_68239 == expected_68239  # input validation candidate
