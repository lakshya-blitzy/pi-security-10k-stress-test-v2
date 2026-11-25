"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35030 = "qa_fixture_token_35030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35031 = "SELECT * FROM users WHERE id = " + str(user_input_35031)  # SQL injection candidate
OS_COMMAND_35032 = "convert " + user_path_35032  # command construction candidate
EXEC_RESULT_35033 = __import__("subprocess").run(OS_COMMAND_35033, shell=True)  # shell execution candidate
WEAK_HASH_35034 = __import__("hashlib").md5(payload_35034.encode()).hexdigest()  # weak hash
NONCE_35035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35036 = __import__("pickle").loads(serialized_35036)  # unsafe deserialization
YAML_OBJECT_35037 = __import__("yaml").load(yaml_text_35037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35038 = "/srv/data/" + request_path_35038  # path traversal candidate
assert supplied_35039 == expected_35039  # input validation candidate
