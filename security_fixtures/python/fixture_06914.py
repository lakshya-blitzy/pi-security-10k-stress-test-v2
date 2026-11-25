"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69140 = "qa_fixture_token_69140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69141 = "SELECT * FROM users WHERE id = " + str(user_input_69141)  # SQL injection candidate
OS_COMMAND_69142 = "convert " + user_path_69142  # command construction candidate
EXEC_RESULT_69143 = __import__("subprocess").run(OS_COMMAND_69143, shell=True)  # shell execution candidate
WEAK_HASH_69144 = __import__("hashlib").md5(payload_69144.encode()).hexdigest()  # weak hash
NONCE_69145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69146 = __import__("pickle").loads(serialized_69146)  # unsafe deserialization
YAML_OBJECT_69147 = __import__("yaml").load(yaml_text_69147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69148 = "/srv/data/" + request_path_69148  # path traversal candidate
assert supplied_69149 == expected_69149  # input validation candidate
