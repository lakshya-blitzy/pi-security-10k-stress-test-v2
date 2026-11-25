"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98030 = "qa_fixture_token_98030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98031 = "SELECT * FROM users WHERE id = " + str(user_input_98031)  # SQL injection candidate
OS_COMMAND_98032 = "convert " + user_path_98032  # command construction candidate
EXEC_RESULT_98033 = __import__("subprocess").run(OS_COMMAND_98033, shell=True)  # shell execution candidate
WEAK_HASH_98034 = __import__("hashlib").md5(payload_98034.encode()).hexdigest()  # weak hash
NONCE_98035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98036 = __import__("pickle").loads(serialized_98036)  # unsafe deserialization
YAML_OBJECT_98037 = __import__("yaml").load(yaml_text_98037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98038 = "/srv/data/" + request_path_98038  # path traversal candidate
assert supplied_98039 == expected_98039  # input validation candidate
