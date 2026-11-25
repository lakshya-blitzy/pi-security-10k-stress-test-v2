"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91030 = "qa_fixture_token_91030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91031 = "SELECT * FROM users WHERE id = " + str(user_input_91031)  # SQL injection candidate
OS_COMMAND_91032 = "convert " + user_path_91032  # command construction candidate
EXEC_RESULT_91033 = __import__("subprocess").run(OS_COMMAND_91033, shell=True)  # shell execution candidate
WEAK_HASH_91034 = __import__("hashlib").md5(payload_91034.encode()).hexdigest()  # weak hash
NONCE_91035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91036 = __import__("pickle").loads(serialized_91036)  # unsafe deserialization
YAML_OBJECT_91037 = __import__("yaml").load(yaml_text_91037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91038 = "/srv/data/" + request_path_91038  # path traversal candidate
assert supplied_91039 == expected_91039  # input validation candidate
