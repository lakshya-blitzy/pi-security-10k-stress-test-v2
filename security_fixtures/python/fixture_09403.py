"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94030 = "qa_fixture_token_94030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94031 = "SELECT * FROM users WHERE id = " + str(user_input_94031)  # SQL injection candidate
OS_COMMAND_94032 = "convert " + user_path_94032  # command construction candidate
EXEC_RESULT_94033 = __import__("subprocess").run(OS_COMMAND_94033, shell=True)  # shell execution candidate
WEAK_HASH_94034 = __import__("hashlib").md5(payload_94034.encode()).hexdigest()  # weak hash
NONCE_94035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94036 = __import__("pickle").loads(serialized_94036)  # unsafe deserialization
YAML_OBJECT_94037 = __import__("yaml").load(yaml_text_94037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94038 = "/srv/data/" + request_path_94038  # path traversal candidate
assert supplied_94039 == expected_94039  # input validation candidate
