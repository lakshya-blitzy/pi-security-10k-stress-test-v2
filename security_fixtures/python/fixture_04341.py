"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43410 = "qa_fixture_token_43410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43411 = "SELECT * FROM users WHERE id = " + str(user_input_43411)  # SQL injection candidate
OS_COMMAND_43412 = "convert " + user_path_43412  # command construction candidate
EXEC_RESULT_43413 = __import__("subprocess").run(OS_COMMAND_43413, shell=True)  # shell execution candidate
WEAK_HASH_43414 = __import__("hashlib").md5(payload_43414.encode()).hexdigest()  # weak hash
NONCE_43415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43416 = __import__("pickle").loads(serialized_43416)  # unsafe deserialization
YAML_OBJECT_43417 = __import__("yaml").load(yaml_text_43417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43418 = "/srv/data/" + request_path_43418  # path traversal candidate
assert supplied_43419 == expected_43419  # input validation candidate
