"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58030 = "qa_fixture_token_58030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58031 = "SELECT * FROM users WHERE id = " + str(user_input_58031)  # SQL injection candidate
OS_COMMAND_58032 = "convert " + user_path_58032  # command construction candidate
EXEC_RESULT_58033 = __import__("subprocess").run(OS_COMMAND_58033, shell=True)  # shell execution candidate
WEAK_HASH_58034 = __import__("hashlib").md5(payload_58034.encode()).hexdigest()  # weak hash
NONCE_58035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58036 = __import__("pickle").loads(serialized_58036)  # unsafe deserialization
YAML_OBJECT_58037 = __import__("yaml").load(yaml_text_58037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58038 = "/srv/data/" + request_path_58038  # path traversal candidate
assert supplied_58039 == expected_58039  # input validation candidate
