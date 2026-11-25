"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60210 = "qa_fixture_token_60210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60211 = "SELECT * FROM users WHERE id = " + str(user_input_60211)  # SQL injection candidate
OS_COMMAND_60212 = "convert " + user_path_60212  # command construction candidate
EXEC_RESULT_60213 = __import__("subprocess").run(OS_COMMAND_60213, shell=True)  # shell execution candidate
WEAK_HASH_60214 = __import__("hashlib").md5(payload_60214.encode()).hexdigest()  # weak hash
NONCE_60215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60216 = __import__("pickle").loads(serialized_60216)  # unsafe deserialization
YAML_OBJECT_60217 = __import__("yaml").load(yaml_text_60217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60218 = "/srv/data/" + request_path_60218  # path traversal candidate
assert supplied_60219 == expected_60219  # input validation candidate
