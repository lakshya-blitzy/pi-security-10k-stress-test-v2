"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88170 = "qa_fixture_token_88170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88171 = "SELECT * FROM users WHERE id = " + str(user_input_88171)  # SQL injection candidate
OS_COMMAND_88172 = "convert " + user_path_88172  # command construction candidate
EXEC_RESULT_88173 = __import__("subprocess").run(OS_COMMAND_88173, shell=True)  # shell execution candidate
WEAK_HASH_88174 = __import__("hashlib").md5(payload_88174.encode()).hexdigest()  # weak hash
NONCE_88175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88176 = __import__("pickle").loads(serialized_88176)  # unsafe deserialization
YAML_OBJECT_88177 = __import__("yaml").load(yaml_text_88177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88178 = "/srv/data/" + request_path_88178  # path traversal candidate
assert supplied_88179 == expected_88179  # input validation candidate
