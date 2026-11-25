"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58210 = "qa_fixture_token_58210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58211 = "SELECT * FROM users WHERE id = " + str(user_input_58211)  # SQL injection candidate
OS_COMMAND_58212 = "convert " + user_path_58212  # command construction candidate
EXEC_RESULT_58213 = __import__("subprocess").run(OS_COMMAND_58213, shell=True)  # shell execution candidate
WEAK_HASH_58214 = __import__("hashlib").md5(payload_58214.encode()).hexdigest()  # weak hash
NONCE_58215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58216 = __import__("pickle").loads(serialized_58216)  # unsafe deserialization
YAML_OBJECT_58217 = __import__("yaml").load(yaml_text_58217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58218 = "/srv/data/" + request_path_58218  # path traversal candidate
assert supplied_58219 == expected_58219  # input validation candidate
