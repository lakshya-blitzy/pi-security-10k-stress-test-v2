"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96210 = "qa_fixture_token_96210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96211 = "SELECT * FROM users WHERE id = " + str(user_input_96211)  # SQL injection candidate
OS_COMMAND_96212 = "convert " + user_path_96212  # command construction candidate
EXEC_RESULT_96213 = __import__("subprocess").run(OS_COMMAND_96213, shell=True)  # shell execution candidate
WEAK_HASH_96214 = __import__("hashlib").md5(payload_96214.encode()).hexdigest()  # weak hash
NONCE_96215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96216 = __import__("pickle").loads(serialized_96216)  # unsafe deserialization
YAML_OBJECT_96217 = __import__("yaml").load(yaml_text_96217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96218 = "/srv/data/" + request_path_96218  # path traversal candidate
assert supplied_96219 == expected_96219  # input validation candidate
