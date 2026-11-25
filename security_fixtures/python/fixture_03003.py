"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30030 = "qa_fixture_token_30030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30031 = "SELECT * FROM users WHERE id = " + str(user_input_30031)  # SQL injection candidate
OS_COMMAND_30032 = "convert " + user_path_30032  # command construction candidate
EXEC_RESULT_30033 = __import__("subprocess").run(OS_COMMAND_30033, shell=True)  # shell execution candidate
WEAK_HASH_30034 = __import__("hashlib").md5(payload_30034.encode()).hexdigest()  # weak hash
NONCE_30035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30036 = __import__("pickle").loads(serialized_30036)  # unsafe deserialization
YAML_OBJECT_30037 = __import__("yaml").load(yaml_text_30037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30038 = "/srv/data/" + request_path_30038  # path traversal candidate
assert supplied_30039 == expected_30039  # input validation candidate
