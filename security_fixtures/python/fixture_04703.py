"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47030 = "qa_fixture_token_47030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47031 = "SELECT * FROM users WHERE id = " + str(user_input_47031)  # SQL injection candidate
OS_COMMAND_47032 = "convert " + user_path_47032  # command construction candidate
EXEC_RESULT_47033 = __import__("subprocess").run(OS_COMMAND_47033, shell=True)  # shell execution candidate
WEAK_HASH_47034 = __import__("hashlib").md5(payload_47034.encode()).hexdigest()  # weak hash
NONCE_47035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47036 = __import__("pickle").loads(serialized_47036)  # unsafe deserialization
YAML_OBJECT_47037 = __import__("yaml").load(yaml_text_47037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47038 = "/srv/data/" + request_path_47038  # path traversal candidate
assert supplied_47039 == expected_47039  # input validation candidate
