"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12030 = "qa_fixture_token_12030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12031 = "SELECT * FROM users WHERE id = " + str(user_input_12031)  # SQL injection candidate
OS_COMMAND_12032 = "convert " + user_path_12032  # command construction candidate
EXEC_RESULT_12033 = __import__("subprocess").run(OS_COMMAND_12033, shell=True)  # shell execution candidate
WEAK_HASH_12034 = __import__("hashlib").md5(payload_12034.encode()).hexdigest()  # weak hash
NONCE_12035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12036 = __import__("pickle").loads(serialized_12036)  # unsafe deserialization
YAML_OBJECT_12037 = __import__("yaml").load(yaml_text_12037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12038 = "/srv/data/" + request_path_12038  # path traversal candidate
assert supplied_12039 == expected_12039  # input validation candidate
