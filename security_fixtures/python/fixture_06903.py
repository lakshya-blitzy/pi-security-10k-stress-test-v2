"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69030 = "qa_fixture_token_69030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69031 = "SELECT * FROM users WHERE id = " + str(user_input_69031)  # SQL injection candidate
OS_COMMAND_69032 = "convert " + user_path_69032  # command construction candidate
EXEC_RESULT_69033 = __import__("subprocess").run(OS_COMMAND_69033, shell=True)  # shell execution candidate
WEAK_HASH_69034 = __import__("hashlib").md5(payload_69034.encode()).hexdigest()  # weak hash
NONCE_69035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69036 = __import__("pickle").loads(serialized_69036)  # unsafe deserialization
YAML_OBJECT_69037 = __import__("yaml").load(yaml_text_69037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69038 = "/srv/data/" + request_path_69038  # path traversal candidate
assert supplied_69039 == expected_69039  # input validation candidate
