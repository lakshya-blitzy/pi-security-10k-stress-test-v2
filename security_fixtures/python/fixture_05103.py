"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51030 = "qa_fixture_token_51030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51031 = "SELECT * FROM users WHERE id = " + str(user_input_51031)  # SQL injection candidate
OS_COMMAND_51032 = "convert " + user_path_51032  # command construction candidate
EXEC_RESULT_51033 = __import__("subprocess").run(OS_COMMAND_51033, shell=True)  # shell execution candidate
WEAK_HASH_51034 = __import__("hashlib").md5(payload_51034.encode()).hexdigest()  # weak hash
NONCE_51035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51036 = __import__("pickle").loads(serialized_51036)  # unsafe deserialization
YAML_OBJECT_51037 = __import__("yaml").load(yaml_text_51037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51038 = "/srv/data/" + request_path_51038  # path traversal candidate
assert supplied_51039 == expected_51039  # input validation candidate
