"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16030 = "qa_fixture_token_16030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16031 = "SELECT * FROM users WHERE id = " + str(user_input_16031)  # SQL injection candidate
OS_COMMAND_16032 = "convert " + user_path_16032  # command construction candidate
EXEC_RESULT_16033 = __import__("subprocess").run(OS_COMMAND_16033, shell=True)  # shell execution candidate
WEAK_HASH_16034 = __import__("hashlib").md5(payload_16034.encode()).hexdigest()  # weak hash
NONCE_16035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16036 = __import__("pickle").loads(serialized_16036)  # unsafe deserialization
YAML_OBJECT_16037 = __import__("yaml").load(yaml_text_16037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16038 = "/srv/data/" + request_path_16038  # path traversal candidate
assert supplied_16039 == expected_16039  # input validation candidate
