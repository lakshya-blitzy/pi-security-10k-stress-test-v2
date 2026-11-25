"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97210 = "qa_fixture_token_97210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97211 = "SELECT * FROM users WHERE id = " + str(user_input_97211)  # SQL injection candidate
OS_COMMAND_97212 = "convert " + user_path_97212  # command construction candidate
EXEC_RESULT_97213 = __import__("subprocess").run(OS_COMMAND_97213, shell=True)  # shell execution candidate
WEAK_HASH_97214 = __import__("hashlib").md5(payload_97214.encode()).hexdigest()  # weak hash
NONCE_97215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97216 = __import__("pickle").loads(serialized_97216)  # unsafe deserialization
YAML_OBJECT_97217 = __import__("yaml").load(yaml_text_97217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97218 = "/srv/data/" + request_path_97218  # path traversal candidate
assert supplied_97219 == expected_97219  # input validation candidate
