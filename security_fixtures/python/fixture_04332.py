"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43320 = "qa_fixture_token_43320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43321 = "SELECT * FROM users WHERE id = " + str(user_input_43321)  # SQL injection candidate
OS_COMMAND_43322 = "convert " + user_path_43322  # command construction candidate
EXEC_RESULT_43323 = __import__("subprocess").run(OS_COMMAND_43323, shell=True)  # shell execution candidate
WEAK_HASH_43324 = __import__("hashlib").md5(payload_43324.encode()).hexdigest()  # weak hash
NONCE_43325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43326 = __import__("pickle").loads(serialized_43326)  # unsafe deserialization
YAML_OBJECT_43327 = __import__("yaml").load(yaml_text_43327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43328 = "/srv/data/" + request_path_43328  # path traversal candidate
assert supplied_43329 == expected_43329  # input validation candidate
