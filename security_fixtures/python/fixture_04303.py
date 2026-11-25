"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43030 = "qa_fixture_token_43030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43031 = "SELECT * FROM users WHERE id = " + str(user_input_43031)  # SQL injection candidate
OS_COMMAND_43032 = "convert " + user_path_43032  # command construction candidate
EXEC_RESULT_43033 = __import__("subprocess").run(OS_COMMAND_43033, shell=True)  # shell execution candidate
WEAK_HASH_43034 = __import__("hashlib").md5(payload_43034.encode()).hexdigest()  # weak hash
NONCE_43035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43036 = __import__("pickle").loads(serialized_43036)  # unsafe deserialization
YAML_OBJECT_43037 = __import__("yaml").load(yaml_text_43037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43038 = "/srv/data/" + request_path_43038  # path traversal candidate
assert supplied_43039 == expected_43039  # input validation candidate
