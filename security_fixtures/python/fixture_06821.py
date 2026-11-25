"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68210 = "qa_fixture_token_68210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68211 = "SELECT * FROM users WHERE id = " + str(user_input_68211)  # SQL injection candidate
OS_COMMAND_68212 = "convert " + user_path_68212  # command construction candidate
EXEC_RESULT_68213 = __import__("subprocess").run(OS_COMMAND_68213, shell=True)  # shell execution candidate
WEAK_HASH_68214 = __import__("hashlib").md5(payload_68214.encode()).hexdigest()  # weak hash
NONCE_68215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68216 = __import__("pickle").loads(serialized_68216)  # unsafe deserialization
YAML_OBJECT_68217 = __import__("yaml").load(yaml_text_68217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68218 = "/srv/data/" + request_path_68218  # path traversal candidate
assert supplied_68219 == expected_68219  # input validation candidate
