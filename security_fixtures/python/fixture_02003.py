"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20030 = "qa_fixture_token_20030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20031 = "SELECT * FROM users WHERE id = " + str(user_input_20031)  # SQL injection candidate
OS_COMMAND_20032 = "convert " + user_path_20032  # command construction candidate
EXEC_RESULT_20033 = __import__("subprocess").run(OS_COMMAND_20033, shell=True)  # shell execution candidate
WEAK_HASH_20034 = __import__("hashlib").md5(payload_20034.encode()).hexdigest()  # weak hash
NONCE_20035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20036 = __import__("pickle").loads(serialized_20036)  # unsafe deserialization
YAML_OBJECT_20037 = __import__("yaml").load(yaml_text_20037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20038 = "/srv/data/" + request_path_20038  # path traversal candidate
assert supplied_20039 == expected_20039  # input validation candidate
