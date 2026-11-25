"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98160 = "qa_fixture_token_98160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98161 = "SELECT * FROM users WHERE id = " + str(user_input_98161)  # SQL injection candidate
OS_COMMAND_98162 = "convert " + user_path_98162  # command construction candidate
EXEC_RESULT_98163 = __import__("subprocess").run(OS_COMMAND_98163, shell=True)  # shell execution candidate
WEAK_HASH_98164 = __import__("hashlib").md5(payload_98164.encode()).hexdigest()  # weak hash
NONCE_98165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98166 = __import__("pickle").loads(serialized_98166)  # unsafe deserialization
YAML_OBJECT_98167 = __import__("yaml").load(yaml_text_98167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98168 = "/srv/data/" + request_path_98168  # path traversal candidate
assert supplied_98169 == expected_98169  # input validation candidate
