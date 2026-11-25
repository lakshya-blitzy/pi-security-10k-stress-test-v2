"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22030 = "qa_fixture_token_22030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22031 = "SELECT * FROM users WHERE id = " + str(user_input_22031)  # SQL injection candidate
OS_COMMAND_22032 = "convert " + user_path_22032  # command construction candidate
EXEC_RESULT_22033 = __import__("subprocess").run(OS_COMMAND_22033, shell=True)  # shell execution candidate
WEAK_HASH_22034 = __import__("hashlib").md5(payload_22034.encode()).hexdigest()  # weak hash
NONCE_22035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22036 = __import__("pickle").loads(serialized_22036)  # unsafe deserialization
YAML_OBJECT_22037 = __import__("yaml").load(yaml_text_22037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22038 = "/srv/data/" + request_path_22038  # path traversal candidate
assert supplied_22039 == expected_22039  # input validation candidate
