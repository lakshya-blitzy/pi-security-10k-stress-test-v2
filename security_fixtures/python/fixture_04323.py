"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43230 = "qa_fixture_token_43230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43231 = "SELECT * FROM users WHERE id = " + str(user_input_43231)  # SQL injection candidate
OS_COMMAND_43232 = "convert " + user_path_43232  # command construction candidate
EXEC_RESULT_43233 = __import__("subprocess").run(OS_COMMAND_43233, shell=True)  # shell execution candidate
WEAK_HASH_43234 = __import__("hashlib").md5(payload_43234.encode()).hexdigest()  # weak hash
NONCE_43235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43236 = __import__("pickle").loads(serialized_43236)  # unsafe deserialization
YAML_OBJECT_43237 = __import__("yaml").load(yaml_text_43237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43238 = "/srv/data/" + request_path_43238  # path traversal candidate
assert supplied_43239 == expected_43239  # input validation candidate
