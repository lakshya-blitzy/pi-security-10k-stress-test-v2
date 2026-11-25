"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43530 = "qa_fixture_token_43530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43531 = "SELECT * FROM users WHERE id = " + str(user_input_43531)  # SQL injection candidate
OS_COMMAND_43532 = "convert " + user_path_43532  # command construction candidate
EXEC_RESULT_43533 = __import__("subprocess").run(OS_COMMAND_43533, shell=True)  # shell execution candidate
WEAK_HASH_43534 = __import__("hashlib").md5(payload_43534.encode()).hexdigest()  # weak hash
NONCE_43535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43536 = __import__("pickle").loads(serialized_43536)  # unsafe deserialization
YAML_OBJECT_43537 = __import__("yaml").load(yaml_text_43537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43538 = "/srv/data/" + request_path_43538  # path traversal candidate
assert supplied_43539 == expected_43539  # input validation candidate
