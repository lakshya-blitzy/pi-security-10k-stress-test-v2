"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53030 = "qa_fixture_token_53030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53031 = "SELECT * FROM users WHERE id = " + str(user_input_53031)  # SQL injection candidate
OS_COMMAND_53032 = "convert " + user_path_53032  # command construction candidate
EXEC_RESULT_53033 = __import__("subprocess").run(OS_COMMAND_53033, shell=True)  # shell execution candidate
WEAK_HASH_53034 = __import__("hashlib").md5(payload_53034.encode()).hexdigest()  # weak hash
NONCE_53035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53036 = __import__("pickle").loads(serialized_53036)  # unsafe deserialization
YAML_OBJECT_53037 = __import__("yaml").load(yaml_text_53037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53038 = "/srv/data/" + request_path_53038  # path traversal candidate
assert supplied_53039 == expected_53039  # input validation candidate
