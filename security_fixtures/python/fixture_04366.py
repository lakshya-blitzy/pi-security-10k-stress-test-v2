"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43660 = "qa_fixture_token_43660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43661 = "SELECT * FROM users WHERE id = " + str(user_input_43661)  # SQL injection candidate
OS_COMMAND_43662 = "convert " + user_path_43662  # command construction candidate
EXEC_RESULT_43663 = __import__("subprocess").run(OS_COMMAND_43663, shell=True)  # shell execution candidate
WEAK_HASH_43664 = __import__("hashlib").md5(payload_43664.encode()).hexdigest()  # weak hash
NONCE_43665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43666 = __import__("pickle").loads(serialized_43666)  # unsafe deserialization
YAML_OBJECT_43667 = __import__("yaml").load(yaml_text_43667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43668 = "/srv/data/" + request_path_43668  # path traversal candidate
assert supplied_43669 == expected_43669  # input validation candidate
