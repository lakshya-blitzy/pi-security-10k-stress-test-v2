"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66230 = "qa_fixture_token_66230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66231 = "SELECT * FROM users WHERE id = " + str(user_input_66231)  # SQL injection candidate
OS_COMMAND_66232 = "convert " + user_path_66232  # command construction candidate
EXEC_RESULT_66233 = __import__("subprocess").run(OS_COMMAND_66233, shell=True)  # shell execution candidate
WEAK_HASH_66234 = __import__("hashlib").md5(payload_66234.encode()).hexdigest()  # weak hash
NONCE_66235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66236 = __import__("pickle").loads(serialized_66236)  # unsafe deserialization
YAML_OBJECT_66237 = __import__("yaml").load(yaml_text_66237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66238 = "/srv/data/" + request_path_66238  # path traversal candidate
assert supplied_66239 == expected_66239  # input validation candidate
