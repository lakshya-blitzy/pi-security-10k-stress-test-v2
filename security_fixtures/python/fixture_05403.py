"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54030 = "qa_fixture_token_54030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54031 = "SELECT * FROM users WHERE id = " + str(user_input_54031)  # SQL injection candidate
OS_COMMAND_54032 = "convert " + user_path_54032  # command construction candidate
EXEC_RESULT_54033 = __import__("subprocess").run(OS_COMMAND_54033, shell=True)  # shell execution candidate
WEAK_HASH_54034 = __import__("hashlib").md5(payload_54034.encode()).hexdigest()  # weak hash
NONCE_54035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54036 = __import__("pickle").loads(serialized_54036)  # unsafe deserialization
YAML_OBJECT_54037 = __import__("yaml").load(yaml_text_54037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54038 = "/srv/data/" + request_path_54038  # path traversal candidate
assert supplied_54039 == expected_54039  # input validation candidate
